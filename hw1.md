---
layout: default
img: embedding
img_link: http://en.wikipedia.org/wiki/Center_embedding
caption: "The Embedding introduces a strange form of language whose grammar can be 'self-embedded' by computers."
title: "Homework | Competitive Grammar Writing"
active_tab: homework
---

# Homework 1

<span class="text-info">Start on {{ site.hwdates[1].startdate }}</span> |
<span class="text-warning">Due on {{ site.hwdates[1].deadline }}</span>

## Getting Started

If you have already cloned my homework repository `nlp-class-hw` for
Homework 0 then go into that directory and update the directory:

    git pull origin/master
    cd nlp-class-hw/zhsegment

If you don't have that directory anymore then simply clone the
repository again:

    git clone https://github.com/anoopsarkar/nlp-class-hw.git

Clone your own repository from GitLab if you haven’t done it already:

    git clone git@csil-git1.cs.surrey.sfu.ca:USER/nlpclass-1187-g-GROUP.git

Note that the `USER` above is the SFU username of the person in
your group that set up the GitLab repository.

Then copy over the contents of the `zhsegment` directory into your
`hw1` directory in your repository.

Set up the virtual environment:

    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt

Note that if you do not change the requirements then after you have
set up the virtual environment `venv` you can simply run the following
command to get started with your development for the homework:

    source venv/bin/activate

## Background

Word segmentation is the task of restoring missing word boundaries.
This homework is on Chinese word segmentation, a language in which
word boundaries are not usually provided. For instance here is an
example Chinese sentence without word boundaries:

    北京大学生比赛

This can be segmented a few different ways and one segmentation
leads to a particular meaning (indicated by the English translation
below):

    北京 大学生 比赛
    Beijing student competition

A different segmentation leads to a different meaning (and translation):

    北京大学 生 比赛
    Peking University Health Competition

We will be using _training data_ collected from Chinese sentences
that have been segmented by human experts.  We will run the word
segmentation program that you will write for this homework on _test
data_ that will be automatically evaluated against a reference
segmentation.

## Default solution

The default solution is provided in `default.py`. To use the default
as your solution:

    cp default.py answer/zhsegment.py
    cp default.ipynb answer/zhsegment.ipynb
    python3 zipout.py
    python3 check.py

Make sure that the command line options are kept as they are in
`default.py`. You can add to them but you must not delete any
command line options that exist in `default.py`.

Submitting the default solution without modification will get you
zero marks.

The default solution simply identifies each Chinese character as a
word. So if the input is a sequence of characters (without word
boundaries): $$c_0, \ldots, c_n$$. Then the output is simply a
sequence of words $$w_0 w_1 \ldots w_n$$ where $$w_i == c_i$$.

The score reported is [F-score](http://en.wikipedia.org/wiki/F1_score) which combines
[precision and recall](http://en.wikipedia.org/wiki/Precision_and_recall) into a single score.
F-score is explained further below.

## The Challenge

Your task is to _improve the F-score as much as possible_ which is explained
in detail in the Accuracy section below. To help you do
this the `data` directory contains two files:

    count_1w.txt : unigram counts of Chinese words
    count_2w.txt : bigram counts of Chinese word pairs

You can also optionally use the data used to create the above count files which is in `train.txt.bz2` in the `data` directory.

You can also use a larger dataset provided to you via this link: [wseg_simplified_cn.txt.bz2](https://vault.sfu.ca/index.php/s/ghsaEeqtvV5IYLF) which contains 1M Chinese sentences with word segments (bzip2 compressed). This link is only available for SFU students. You must not give a copy of this data set to **anybody**. 

## Data files

The data files provided are:

* `data/count_1w.txt` -- unigram word counts (from segmented Chinese data)
* `data/count_2w.txt` -- bigram word counts (from segmented Chinese data)
* `data/input` -- input files `dev.txt` and `test.txt`
* `data/reference/dev.out` -- the reference output for the `dev.txt` input file

## Baseline 

The baseline method is what you should implement first before you
explore additional improvements to improve the F-score. You **must**
implement the iterative approach shown below to replace the recursive
approach with memoization.

A simple baseline uses a unigram language model over Chinese words.
The input is a sequence of Chinese characters (without word
boundaries): $$c_0, \ldots, c_n$$.

Let us define a word as a sequence of characters: $$w_i^j$$ is
a word that spans from character $$i$$ to character $$j$$. So
one possible word sequence is $$w_0^3 w_4^{10} w_{11}^n$$. We
can score this sequence using unigram probabilities.

<p>$$\arg\max_{w_0^i, w_{i+1}^j, \ldots, w_{n-k}^n} P_w(w_0^i) \times P_w(w_{i+1}^j) \times \ldots \times P_w(w_{n-k}^n)$$</p>

The unigram probability $$P_w$$ can be constructed using the data
in `count_1w.txt`. The model is simple, an unigram model, but the
search is over all possible ways to form word sequences for the
input sequence of characters. The argmax over all such sequences
will give you the baseline system. The $$\arg\max$$ above can be computed
using the following recursive search over $$segment(c_0, \ldots, c_n)$$:

<p>$$\begin{eqnarray}
segment(c_i, \ldots, c_j) &=& \arg\max_{\forall k <= L} P_w(w_i^k) \times segment(c_{k+1}, \ldots, c_j) \\
segment(\emptyset) &=& 1.0
\end{eqnarray}$$</p>

where $$L = min(maxlen, j)$$ in order to avoid considering segmentations
of very long words which are going to be very unlikely.
$$segment(\emptyset)$$ is the base case of the recursion: an input
of length zero, which results in a segmentation of length zero with
probability $$1.0$$.

One could [memoize](http://en.wikipedia.org/wiki/Memoization)
$$segment$$ in order to avoid the slow exploration of the exponentially
many segmentations.  However Chinese sentences (especially in the
newswire domain) are very long in terms of number of characters. A
recursive approach is not computationally efficient enough to tackle
real-world data.  An alternative is to do this iteratively. The
following pseudo-code illustrates how to find the argmax iteratively.

### Algorithm: Iterative segmenter

---
**## Data Structures ##**

`input`
: the input sequence of characters

`chart`
: the dynamic programming table to store the argmax for every prefix of `input`
: indexed by character position in `input`

`Entry`
: each entry in the `chart` has four components: Entry(`word`, `start-position`, `log-probability`, `back-pointer`)
: the `back-pointer` in each `entry` links it to a previous entry that it extends

`heap`
: a list or priority queue containing the entries to be expanded, sorted on `start-position` or `log-probability`
{: .dl-horizontal}

---
**## Initialize the `heap` ##**

* for each `word` that matches `input` at position 0    
    * insert Entry(`word`, 0, $$\log P_w$$(`word`), $$\emptyset$$) into `heap`
{: .list-unstyled}

**## Iteratively fill in `chart[i]` for all `i` ##**

* while `heap` is nonempty:
    * `entry` = top entry in the `heap`
    * get the `endindex` based on the length of the word in `entry`
    * if `chart`[`endindex`] has a previous entry, `preventry`
        * if `entry` has a higher probability than `preventry`:
            * `chart`[`endindex`] = `entry`
        * if `entry` has a lower or equal probability than `preventry`:
            * continue  **## we have already found a good segmentation until `endindex` ##**
    * else 
        * `chart`[`endindex`] = `entry`
    * for each `newword` that matches `input` starting at position `endindex`+1
        * `newentry` = Entry(`newword`, `endindex`+1, `entry`.`log-probability` + $$\log P_w$$(`newword`), `entry`)
        * if `newentry` does not exist in `heap`:
            * insert `newentry` into `heap`
{: .list-unstyled}

**## Get the best segmentation ##**

* `finalindex` is the length of `input`
* `finalentry` = `chart`[`finalindex`] 
* The best segmentation starts from `finalentry` and follows the `back-pointer` recursively until the first word
{: .list-unstyled}
---

It might help to examine [an example
run](https://gist.github.com/anoopsarkar/da67c6566a7268bb53b7) of
the above pseudo-code on a particular input. To keep the example
short, the segmenter in the example assumes that unknown words can
only be on length one. You will get a better F-score if you allow
unknown words of arbitrary length (with the appropriate smoothed
probability score).

## Your Task

Developing a segmenter using the above pseudo-code that uses unigram probabilities is
good enough to get close to the baseline system. But getting closer to the oracle
score will be a more interesting challenge. In addition to getting a good score
on the leaderboard you **must** experiment with at least one extension of the
baseline or an additional model of your
choice and document your work. Here are some ideas:

* Use the bigram model to score word segmentation candidates.
* Do better _smoothing_ of the unigram and bigram probability models.
* More advanced methods[^1]

[^1]: If you are ambitious, you can use more advanced machine learning methods such as [global linear models](http://anoopsarkar.github.io/papers/pdf/cnwseg-ai2009.pdf) or [neural networks](http://aclweb.org/anthology/P/P16/P16-1039.pdf) or [bidirectional RNNs](https://arxiv.org/abs/1808.06511) or [transition-based neural language models](http://aclweb.org/anthology/P/P16/P16-1040.pdf). In particular you might want to pay attention to the error analysis for out of vocabulary words in these papers. Even without fancy neural networks the same analysis might help you improve your accuracy.

But the sky's the limit! You are welcome to design your own model, as long 
as you have implemented the Baseline model first.

## Required files

You must create the following files:

* `answer/zhsegment.py` -- this is your solution to the homework. start by copying `default.py` as explained below.
* `answer/zhsegment.ipynb` -- this is the iPython notebook that will be your write-up for the homework.

## Run your solution on the data files

To create the `output.zip` file for upload to Coursys do:

    python3 zipout.py

For more options:

    python3 zipout.py -h

## Check your accuracy

To check your accuracy on the dev set:

    python3 check.py

The score reported is [F-score](http://en.wikipedia.org/wiki/F1_score) which combines
[precision and recall](http://en.wikipedia.org/wiki/Precision_and_recall) into a single score.

For this homework, _tp_ (true positives) is defined as the words that were found in the output that
exist in the reference. If a word occurs in the output but not in reference it is counted as a _fp_
(false positive) and vice versa is counted as a _fn_ (false negative).
Precision $$p$$ is defined as $$\frac{tp}{tp+fp}$$. Recall $$r$$ is defined as $$\frac{tp}{tp+fn}$$.

F-score is defined as $$2 \cdot \frac{p \cdot r}{p + r}$$.

For more options:

    python3 check.py -h

In particular use the log file to check your output evaluation:

    python3 check.py -l log

The accuracy on `data/input/test.txt` will not be shown.  We will
evaluate your output on the test input after the submission deadline.

The default solution gets a very poor F-score on the dev and test set:

    $ python3 check.py
    dev.out score: 0.27
    test.out score: 0.33

Implementing a greedy search gets an F-score of 0.66 on dev
while the Baseline method with unigram counts gets 0.89 on
the dev set.

Implementing the Baseline method augmented with bigram counts 
as a bigram model $$P(w_i \mid w_{i-1})$$ should give you an
improved F-score:

    $ python3 check.py
    dev.out score: 0.90
    test.out score: 0.77

By careful analysis of the output (even without any knowledge of
the Chinese language) should give you some further ideas to consolidate
certain types of characters into words based on regularity how they
combine into words in the training set.

## Submit your homework on Coursys

Once you are done with your homework submit all the relevant materials
to Coursys for evaluation.

### Create output.zip

Once you have a working solution in `answer/zhsegment.py` create
the `output.zip` for upload to Coursys using:

    python3 zipout.py

### Create source.zip

To create the `source.zip` file for upload to Coursys do:

    python3 zipsrc.py

You must have the following files or `zipsrc.py` will complain about it:

* `answer/zhsegment.py` -- this is your solution to the homework. start by copying `default.py` as explained below.
* `answer/zhsegment.ipynb` -- this is the iPython notebook that will be your write-up for the homework.

In addition, each group member should write down a short description of what they
did for this homework in `answer/README.username`.

### Upload to Coursys

Go to `Homework 1` on Coursys and do a group submission:

* Upload `output.zip` and `source.zip`
* Make sure you have documented your approach in `answer/zhsegment.ipynb`.
* Make sure each member of your group has documented their contribution to this homework in `answer/README.username` where `username` is your CSIL/GitLab username.

## Grading

The grading is split up into the following components:

* dev scores (see Table below)
* test scores (see Table below)
* iPython notebook write-up 
   * Make sure that iterative search algorithm is implemented as described in the Baseline section above
* Check if each group member has a `answer/README.username`.

Your F-score should be equal to or greater than the score listed for the corresponding marks.

| **F-score(dev)** | **F-score(test)** | **Marks** | **Grade** |
| 27 | 33 | 0   | F  |
| 50 | 45 | 55  | D  |
| 55 | 50 | 60  | C- |
| 60 | 55 | 65  | C  |
| 65 | 60 | 70  | C+ |
| 70 | 65 | 75  | B- |
| 75 | 70 | 80  | B  |
| 80 | 73 | 85  | B+ |
| 85 | 76 | 90  | A- |
| 90 | 78 | 95  | A  |
| 92 | 80 | 100 | A+ |
{: .table}


The score will be normalized to the marks on Coursys for the dev and test scores.

