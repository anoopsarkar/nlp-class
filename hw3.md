---
layout: default
img: rosetta
img_link: "http://en.wikipedia.org/wiki/Rosetta_Stone"
caption: Jean-François Champollion used word alignment (starting with the word Ptolemy) to decipher Egyptian hierogyphics.
title: Homework 3 | Alignment
active_tab: homework
---

Word Alignment <span class="text-muted">Homework 3</span>
=============================================================

<p class="text-muted">Due on Tuesday, October 21, 2014</p>

Word alignment is a key task in building a machine translation system.
We start with a large corpus of aligned sentences called a parallel
corpus. For example, we might have the following sentence pair
from the Canadian Hansards (the published proceedings of the
Canadian parliament):

    le droit de permis passe donc de $ 25 à $ 500 .
    we see the licence fee going up from $ 25 to $ 500 .

Your task is to find the alignments between the words between
the two languages. For example, given the sentence pair
above, your program should output a word alignment in the
following format that uses the word indices from the two
languages:

<!--
% 0 le 1 droit 2 de 3 permis 4 passe 5 donc 6 de 7 \$ 8 25 9 \`a 10 \$ 11 500 12 . \\
% 0 we 1 see 2 the 3 licence 4 fee 5 going 6 up 7 from 8 \$ 9 25 10 to 11 \$ 12 500 13 .
-->

    0-2 1-4 3-3 4-5 4-6 5-7 7-8 8-9 9-10 10-11 11-12 12-13

This corresponds to an alignment of the words shown in the following table:

| 0 `le` | 2 `the` |
| 1 `droit` | 4 `fee` |
| 2 `de` | |
| 3 `permis` | 3 `license` |
| 4 `passe` | 5 `going` |
| 4 `passe` | 6 `up` |
| 5 `donc` | 7 `from` |
| 6 `de` | |
| 7 `$` | 8 `$` |
| 8 `25` | 9 `25` |
| 9 `à` | 10 `to` |
| 10 `$` | 11 `$` |
| 11 `500` | 12 `500` |
| 12 `.` | 13 `.` |
{: .table}

Getting Started 
---------------

You must have git and python (2.7) on your system to run the assignments.

If you have already cloned the `nlp-class-hw` repository,
then do the following to get the files for Homework 3:

    # go to the directory where you did a git clone before
    cd nlp-class-hw
    git pull

Or you can create a new directory that does a fresh clone of the repository:

    git clone https://github.com/anoopsarkar/nlp-class-hw.git

In the `aligner` directory you will find several python programs that you will
use for this assignment.

`default.py` contains a default training algorithm for the alignment task. 

    python default.py -m default.model

`default.py` implements a complete but very simple alignment
algorithm. For every word, it computes the set of sentences that
the word appears in. Intuititvely, word pairs that appear in similar
sets of sentences are likely to be translations. Our aligner first
computes the similarity of these sets with [Dice's
coefficient](http://goo.gl/XS9rps).  Given the co-occurence count
$$C(e,f)$$ of words $$e$$ and $$f$$ in the parallel corpus, Dice's
coefficient for each pair of words $$e_i, f_j$$ is:

<p>$$ \delta(i,j) = \frac{2 \times C(e_i, f_j)}{C(e_i) +C(f_j)} $$</p>

The default aligner will align any word pair $$e_i, f_j$$ with a coefficient $$\delta(i,j)$$ over 0.5. 
You can experiment with different thresholds using `-t`.

The Challenge
-------------

The goal of this homework is to train a word alignment model using
a given set of sentence pairs in two languages and then produce a
word alignment for the data sets given to you. 

You are only provided sentence pairs without any alignments, hence
this is an example of *unsupervised learning*.  The plan is to learn
a conditional probability model $$\Pr(\textbf{f} \mid \textbf{e})$$
of a French sentence $$\textbf{f}$$ given an English sentence
$$\textbf{e}$$.  You are given a dataset $${\cal D}$$ of $$1, \ldots,
N$$ sentence pairs that are known to be translation pairs:

<p>$${\cal D} = \{ (\textbf{f}^{(1)}, \textbf{e}^{(1)}), \ldots,
(\textbf{f}^{(N)}, \textbf{e}^{(N)}) \}$$</p>

Just like `default.py` your code should implement at least the following command line arguments:

    -p DIR/PREFIX   prefix for parallel data, Defaults: DIR=data PREFIX=hansards
    -f suffix       suffix of the source language data, Default: fr (French)
    -e suffix       suffix of the target language data, Default: en (English)
    -n NUMBER       number of training examples to use, Default: n = sys.maxint (use all training examples)

You will upload the file `output` to the leaderboard submission
site at [sfu-nlp-class.appspot.com](http://sfu-nlp-class.appspot.com/).

### The Baseline

#### The word alignment model

The baseline model is a simple model that uses a *word-to-word* or
*lexical* translation model. It has only one set of parameters: a
conditional probability $$t(f \mid e)$$ where $$f$$ is a French
word and $$e$$ is an English word. We will build the model
$$\Pr(\textbf{f} \mid \textbf{e})$$ using $$t(\cdot \mid \cdot)$$.

Pick one translation pair from the data $${\cal D}$$. Let the French
sentence be $$\mathbf{f} = (f_1, \ldots, f_I)$$ and the English
sentence $$\mathbf{e} = (e_1, \ldots, e_J)$$.  Now we make a big
assumption: that each French word can only map to exactly one English
word. This means that we can represent an alignment $$\textbf{a}$$
of the French words by: $$\textbf{a} = (a_1, \ldots, a_I)$$. There
is one $$a_i$$ for each French word $$f_i$$ which corresponds to
an English word $$e_{a_i}$$. If $$a_i$$ is allowed to be $$0$$ then
it means that a French word $$f_i$$ is not mapped to any English
word. Setting $$a_i$$ to $$0$$ is called aligning $$f_i$$ to *null*.

<p>$$ \Pr(\mathbf{f}, \textbf{a} \mid \mathbf{e}) = \prod_{i=1}^I
t(f_i \mid e_{a_i})$$</p>

Assume we have a three word French sentence ($$I = 3$$) sentence-aligned
to a three word English sentence ($$J = 3$$).  If the alignment
$$\textbf{a} = (1,3,2)$$, that is, $$a_0 = 0$$, $$a_1 = 3$$, and
$$a_3 = 2$$ we can derive the probability of this sentence pair
alignment to be:

<p>$$\Pr(\mathbf{f}, \textbf{a} \mid \mathbf{e}) = t(f_1 \mid e_1)
\cdot t(f_2 \mid e_3) \cdot t(f_3 \mid e_2)$$</p>

In this simple model, we allow any alignment function that maps any
word in the source sentence to any word in the target sentence (no
matter how far apart they are). The alignments are not provided to
us, so we remove the alignments by summing over them:

<p>$$
\begin{eqnarray*}
\Pr(\mathbf{f} \mid \mathbf{e}, t) & = & \sum_{\textbf{a}} \Pr(\mathbf{f}, \textbf{a} \mid \mathbf{e}, t) \\
& = & \sum_{a_0=1}^J \cdots \sum_{a_I=1}^J  \prod_{i=1}^I t(f_i \mid e_{a_i}) \\
&& \textrm{(this computes all possible alignments)} \\
& = & \prod_{j=1}^J \sum_{i=1}^I t(f_i \mid e_j) \\
&& \textrm{(after conversion of $I^J$ terms into $I \cdot J$ terms)}
\end{eqnarray*}
$$</p>

We wish to learn the parameters $$t(\cdot \mid \cdot)$$ that maximize
the log-likelihood of the training data:

<p>$$ L(t) = \arg\max_{t} \sum_s \log \Pr(\mathbf{f}^{(s)} \mid
\mathbf{e}^{(s)}, t) $$</p>

#### Training the model

In order to estimate the parameters $$t(\cdot \mid \cdot)$$
we start with an initial estimate $$t_0$$ and modify it iteratively
to get $$t_1, t_2, \ldots$$. The parameter updates are derived
for each French word $$f_i$$ and English word $$e_j$$ as follows:

<p>$$t_k(f_i \mid e_j) = \sum_{s=1}^N \sum_{(f_i, e_j) \in (\textbf{f}^{(s)}, \textbf{e}^{(s)})} \frac{ \textrm{count}(f_i, e_j, \textbf{f}^{(s)}, \textbf{e}^{(s)}) }{ \textrm{count}(e_j, \textbf{f}^{(s)}) }$$</p>

These counts are *expected counts* over all possible alignments,
and each alignment has a probability computed using $$t_{k-1}$$.
Using maximum likelihood, each alignment between $$f_i$$ and $$e_j$$
is the number of times we observe an alignment between $$f_i$$ and
$$e_j$$ times the probability of that alignment divided by the total
of all other alignments to other French words observed for $$e_j$$
times the probability of each of those alignments.

<p>$$
\begin{eqnarray*}
\textrm{count}(f_i, e_j, \textbf{f}, \textbf{e}) & = & \frac{ t_{k-1}(f_i \mid e_j) }{ \Pr(\textbf{f} \mid \textbf{e}, t_{k-1}) } \\
& = & \frac{ t_{k-1}(f_i \mid e_j) }{ \sum_{a_i=1}^J t_{k-1}(f_i \mid e_{a_i}) } \\
\textrm{count}(e_j, \textbf{f}) & = & \sum_{f \in \textbf{f}} \textrm{count}(f, e_j)
\end{eqnarray*}
$$</p>

The description of the training algorithm is very compressed here.
You will have to work through the background reading below in order
to fully understand the steps. Pseudo-code for the training algorithm
is given below.

##### Algorithm: Training a lexical word alignment model

---

* $$k$$ = 0
* Initialize $$t_0$$ **## Easy choice: initialize uniformly ##**
* repeat
    * $$k$$ += 1
    * Initialize all counts to zero
    * for each $$(\textbf{f}, \textbf{e})$$ in $${\cal D}$$
        * for each $$f_i$$ in $$\textbf{f}$$
            * $$Z$$ = 0 **## Z commonly denotes a normalization term ##**
            * for each $$e_j$$ in $$\textbf{e}$$
                * $$Z$$ += $$t_{k-1}(f_i \mid e_j)$$
            * for each $$e_j$$ in $$\textbf{e}$$
                * `c` = $$ t_{k-1}(f_i \mid e_j) / Z $$
                * count($$f_i$$, $$e_j$$) += `c`
                * count($$e_j$$) += `c`
    * for each ($$f$$, $$e$$) in count
        * Set new parameters: $$t_k(f \mid e)$$ =  count($$f,e$$) / count($$e$$)
* until convergence **## See below for convergence tests ##**
{: .list-unstyled}
---

#### Initialization

Initializing uniformly means that every French word is equally
likely for every English word: for all $${e,f}$$ we initialize
$$t_0(f \mid e) = \frac{1}{V_e}$$ where $$V_e$$ is the English
vocabulary size.

#### Convergence

The theory behind this algorithm states that the iterative updates
have the following property:

<p>$$L(t_k) \geq L(t_{k-1})$$</p>

We can check for convergence by checking if the value of $$L(t)$$
does not change much from the previous iteration (difference from
previous iteration is less than $$10^{-4}$$, for example). However,
most practitioners simply iterate over the training data for 3 to
5 iterations.

#### Decoding: compute the $$\arg\max$$ word alignment

We have trained an alignment model so far, but what we really need
is the $$\arg\max$$ alignment for a given translation pair.

<p>$$ 
\hat{\textbf{a}} = \arg\max_{\textbf{a}} \Pr(\textbf{a} \mid \textbf{e}, \textbf{f})
$$</p>

The best alignment to a target sentence in our simple baseline model
is obtained by simply finding the best alignment for each word in
the source sentence independently of the other words. For each
French word $$f_i$$ in the source sentence the best alignment is
given by:

<p>$$ 
\hat{a_i} = \arg\max_{a_i} t(f_i \mid e_{a_i}) 
$$</p>

Pseudo-code for this $$\arg\max$$ search is given below.

##### Algorithm: Decoding the best alignment

---

* for each $$(\textbf{f}, \textbf{e})$$ in $${\cal D}$$
    * for each $$f_i$$ in $$\textbf{f}$$
        * `bestp` = 0
        * `bestj` = 0
        * for each $$e_j$$ in $$\textbf{e}$$
            * if $$t(f_i \mid e_j)$$ > `bestp`
                * `bestp` = $$t(f_i \mid e_j)$$
                * `bestj` = $$j$$
        * align $$f_i$$ to $$e_{\texttt{bestj}}$$
{: .list-unstyled}
---

#### Background reading

The model and training and decoding algorithms and the theory behind
the algorithms is covered in the following basic tutorial (which
is easier to understand than the original research papers):

> Adam Lopez. [Word Alignment and the Expectation-Maximization
> Algorithm](http://www.cs.jhu.edu/~alopez/papers/model1-note.pdf).

Easier to understand, but considerably longer is the following
workbook:

> Kevin Knight. [A Statistical MT Tutorial
> Workbook](http://www.isi.edu/natural-language/mt/wkbk.pdf). 1999.

---

### Your Task

Developing an aligner using the simple alignment algorithms (described
in the above pseudo-code) is good enough to get an alignment error
rate (AER) that is close to the performance of the baseline system
on the leaderboard.  But getting closer to the best known accuracy
on this task[^1] is a more interesting challenge. To get full credit
you **must** experiment with at least one extension of the baseline
and document your work. Here are some ideas:

[^1]: The best known alignment error rate on this task using the data provided to you for French-English is around 19 and for German-English the best error rate is approximately 12.5 according to this [comparison of different alignment models](http://aclweb.org/anthology/P/P04/P04-1023.pdf).

* There are better ways to find the best alignment:
    * Align using $$\Pr(\textbf{f} \mid \textbf{e})$$ and also align using $$\Pr(\textbf{e} \mid \textbf{f})$$, then decode the best alignment using each model independently and then report the alignments that are the intersection of these two alignment sets.
    * [Use the posterior probability to decode](http://aclweb.org/anthology/N/N06/N06-1014.pdf): $$\hat{a_i} = \arg\max_{a_i} \Pr(a_i \mid \textbf{f}, \textbf{e})$$
* There are [better ways to initialize the parameters](http://aclweb.org/anthology/P/P04/P04-1066.pdf) that lead to better alignments especially if you run only for 5 iterations.

But the sky's the limit! You are welcome to design your own model,
as long as you follow the ground rules:

Ground Rules
------------

* Each group should submit using one person as the designated uploader.
* You must turn in three things:
  1. Chunking output of the test dataset which is in `chunker/data/input.txt.gz` (this is the default input to `perc.py`) uploaded to the [leaderboard submission site](http://sfu-nlp-class.appspot.com) according to [the Homework 0 instructions](hw0.html). You can upload new output as often as you like, up until the assignment deadline. The Submit button for showing the test set scores will be unavailable until after the homework deadline and grace days have passed.  The output will be evaluated using a secret metric, but the `score-chunks.py` program will give you a good idea of how well you're doing.
  1. Your code. Each group should assign one member to upload the source code to [Coursys](https://courses.cs.sfu.ca) as the submission for Homework 2. The code should be self-contained, self-documenting, and easy to use. It should use the same input and output assumptions of `default.py`.
  1. A clear, mathematical description of your algorithm and its motivation written in scientific style. This needn't be long, but it should be clear enough that one of your fellow students could re-implement it exactly. Include the file for this writeup as part of the tarball or zip file you will upload to [Coursys](https://courses.cs.sfu.ca). Include also how your group divided up the work load and each group member's contribution to the homework solution.
* You cannot use data or code resources outside of what is provided to you. You can use NLTK but not the NLTK chunker implementation. 
* For the written description of your algorithm, you can use plain ASCII but for math equations it is better to use either [latex](http://www.latex-project.org/) or [kramdown](https://github.com/gettalong/kramdown).  Do __not__ use any proprietary or binary file formats such as Microsoft Word.

If you have any questions or you're confused about anything, just ask.

#### Acknowledgements

This assignment is adapted from the word alignment homework developed
by [Matt Post](http://cs.jhu.edu/~post/) and [Adam
Lopez](http://cs.jhu.edu/~alopez/) based on an original homework
developed by [Philipp Koehn](http://homepages.inf.ed.ac.uk/pkoehn/)
and later modified by [John DeNero](http://www.denero.org/). It
incorporates some ideas from [Chris Dyer](http://www.cs.cmu.edu/~cdyer).

