---
layout: default
img: voynich
img_link: http://en.wikipedia.org/wiki/Voynich_manuscript 
caption: The Voynich manuscript
title: Homework 4 | Decoding
active_tab: homework
---

Translation Decoding <span class="text-muted">Homework 4</span>
============================================================

<p class="text-muted">Due on Tuesday, November 15, 2016</p>

Decoding is process of taking input in French:

    honorables sénateurs , que se est - il passé ici , mardi dernier ?

...And finding its best English translation under your  model:

    honourable senators , what happened here last Tuesday ?

To decode, we need a model of English sentences conditioned on the
French sentence. You did most of the work of creating
such a model in [Homework 1](hw1.html). In this assignment,
we will give you some French sentences and a probabilistic model consisting of
a phrase-based translation model $$\Pr_{\textrm{TM}}(\textbf{f},\textbf{a} \mid \textbf{e})$$
and an n-gram language model $$\Pr_{\textrm{LM}}(\textbf{e})$$. __Your 
challenge is to find the most probable English translation under 
the model.__ We assume a noisy channel decomposition.

<center>
$$\begin{align*} \textbf{e}^* & = \arg \max_{\textbf{e}} \Pr(\textbf{e} \mid \textbf{f}) \\ 
& = \arg \max_{\textbf{e}} \frac{\Pr_{\textrm{TM}}(\textbf{f} \mid \textbf{e}) \times \Pr_{\textrm{LM}}(\textbf{e})}{\Pr(\textbf{f})} \\ 
&= \arg \max_{\textbf{e}} \Pr_{\textrm{TM}}(\textbf{f} \mid \textbf{e}) \times \Pr_{\textrm{LM}}(\textbf{e}) \\ 
&= \arg \max_{\textbf{e}} \sum_{\textbf{a}} \Pr_{\textrm{TM}}(\textbf{f},\textbf{a} \mid \textbf{e}) \times \Pr_{\textrm{LM}}(\textbf{e}) \end{align*}$$
</center>

Getting Started 
---------------

You must have git and python (2.7) on your system to run the
assignments.

If you have already cloned the `nlp-class-hw` repository,
then do the following to get the files for Homework 3:

    # go to the directory where you did a git clone before
    cd nlp-class-hw
    git pull origin master

Or you can create a new directory that does a fresh clone of the
repository:

    git clone https://github.com/anoopsarkar/nlp-class-hw.git

In the `decoder` directory you will find several python programs
and data sets that you will use for this assignment.  

`default.py` contains the default decoder:

    python default.py > output

`default.py` implements a complete but very simple decoder. The
above command creates the file `output` with translations of
`data/input`.  You can compute $$\Pr(\textbf{e} \mid \textbf{f})$$
using `score-decoder.py`.

    python score-decoder.py < output

Or you can do it all at once:

    python default.py | python score-decoder.py

### Scoring decoder output

The `score-decoder.py` command computes the total log probability
for the output file. If there are $$N$$ sentences in the output:
$$\textbf{f}^1, \ldots, \textbf{f}^N$$ then the output score is the sum of the
translation and language model log probability over all sentences:

<p>$$\textrm{score} = \sum_{i=1}^N \log \sum_{\textbf{a}} \Pr_{\textrm{TM}}(\textbf{f}^i ,\textbf{a} \mid \textbf{e}^i) \times \Pr_{\textrm{LM}}(\textbf{e}^i) $$</p>

It sums over all possible ways that the model could have generated
the English from the French, including translations that permute
the phrases. This sum is exponential (and hence intractable) in
general, but the phrase dictionary is fixed and sparse (and small
for this homework), so we can compute it in a few minutes. It is
still easier to do this than it is to find the optimal translation
but if you look at the implementation of `score-decoder.py` you may
get some hints about how to do the assignment!

The most important thing to understand about the scoring of your
decoder is that we are not scoring accuracy of the output translation,
but rather we are scoring a decoder based on whether the $$\arg\max$$
output produced by a decoder has a *model score* that approaches
the *best possible* model score. Note that the translation with the
best score may not still be a good translation in the target language.

### Understanding the default decoder

The decoder generates the most probable translations that it can
find, using three common approximations.

First, it seeks the _Viterbi approximation_ to the most probable
translation. Instead of computing the intractable sum over all
alignments for each sentence, we simply find the best single alignment
and use its translation.

<center>$$\begin{align*} \textbf{e}^* &= \arg \max_{\textbf{e}} \sum_{\textbf{a}} \Pr_{\textrm{TM}}(\textbf{f},\textbf{a} \mid \textbf{e}) \times \Pr_{\textrm{LM}}(\textbf{e}) \\ 
&\approx \arg \max_{\textbf{e}} \max_{\textbf{a}} \Pr_{\textrm{TM}}(\textbf{f},\textbf{a} \mid \textbf{e}) \times \Pr_{\textrm{LM}}(\textbf{e}) \end{align*}$$</center>

Second, it translates French phrases into English without changing
their order. So, it only reorders words  if the reordering has been
memorized as a phrase pair.  For example, in the first sentence,
we see that _<span class="text text-primary">mardi</span> <span
class="text text-danger">dernier</span>_ is correctly translated
as _<span class="text text-danger">last</span> <span class="text
text-primary">Tuesday</span>_.  If we consult `data/tm`, we will
find that the model has memorized the phrase pair `mardi dernier
||| last Tuesday`. But in the second sentence, we see that _<span
class="text text-danger">Comité</span> <span class="text text-primary">de
sélection</span>_ is translated as _<span class="text
text-danger">committee</span> <span class="text
text-primary">selection</span>_, rather than the more correct _<span
class="text text-primary">selection</span> <span class="text
text-danger">committee</span>_.  To show that this is a search
problem rather than a modeling problem, we can generate the latter
output by hand and check that the model really prefers it.

    head -2 data/input | tail -1 > example
    python default.py -i example | python score-decoder.py -i example
    echo "a selection committee was achievement ." | python score-decoder.py -i example

Recall that the scores are reported as log-probabilities, and higher
scores (with lower absolute value) are better. We see that the model
prefers _<span class="text text-primary">selection</span> <span
class="text text-danger">committee</span>_, but the decoder does
not consider this word order.

Finally, our decoder uses strict pruning. As it consumes the input
sentence from left to right, it keeps only the highest-scoring
output up to that point. You can vary the number of number of outputs
kept at each point in the translation using the `-s` parameter. See
how this affects the resulting model score.

    python default.py | python score-decoder.py
    python default.py -s 10000 | python score-decoder.py

The Challenge
-------------

Your task is to __find the most probable English translation__.
Our model assumes that any segmentation of the French sentence into
phrases followed by a one-for-one substitution and permutation of
those phrases is a valid translation. We make the simplifying
assumption that segmentation and ordering probabilities are uniform
across all sentences, hence constant.  This means that
$$\Pr(\textbf{e},\textbf{a} \mid \textbf{f})$$ is proportional to the
product of the n-gram probabilities in $$\Pr_{\textrm{LM}}(\textbf{e})$$
and the phrase translation probabilities in
$$\Pr_{\textrm{TM}}(\textbf{f},\textbf{a} \mid \textbf{e})$$. To avoid
numerical underflow we work in logspace, seeking $$\arg \max_{\textbf{e}}
\max_{\textbf{a}} \log \Pr_{\textrm{TM}}(\textbf{f},\textbf{a} \mid
\textbf{e}) + \log \Pr_{\textrm{LM}}(\textbf{e})$$. The baseline
decoder works with log probabilities, so you can simply follow what
it does.

### The Leaderboard

In this homework, the score produced by `score-decoder.py` will be
the same as the score on the leaderboard. So you do not need to
upload your output nearly as often as you did in other homeworks.

To get on the leaderboard, produce your output file:

    python answer/decode.py > output

Then upload the file `output` to the leaderboard for Homework 4 on
[sfu-nlp-class.appspot.com](https://sfu-nlp-class.appspot.com)

### The Baseline

At minimum, you must implement a beam-search decoder like the one
we have given you that is also capable of _swapping adjacent phrases_.
To get full credit, you __must__ additionally experiment with another
decoding algorithm.  Any permutation of phrases is a valid translation,
so we strongly suggest searching over all or some part of this
larger space. This search is NP-Hard, so it will not be easy. 

A detailed description of the standard algorithm for a beam-search
decoder is provided in the following lecture notes:

> [Phrase-based Translation Models](assets/mcollins-notes/pb.pdf). Michael Collins.

### Extending the baseline

There are several approaches that tackle the decoding problem for
machine translation:

* Use a beam width parameter instead of picking the top-k in each stack as described in page 12 of the [Collins lecture notes](assets/mcollins-notes/pb.pdf).
* Implement a pruning score separate from the model score:
    * Use a distortion penalty so that reordering is penalized by distance as described in page 11 of the [Collins lecture notes](assets/mcollins-notes/pb.pdf).
    * Use a weight for the language model and translation model and tune the weights (by hand) to minimize search error as described in page 17 of the [Koehn lecture notes on decoding](http://anoopsarkar.github.io/nlp-class/assets/slides/06-decoding.pdf). 
    * Use future cost as described in pages 25-29 of the [Koehn lecture notes on decoding](http://anoopsarkar.github.io/nlp-class/assets/slides/06-decoding.pdf).
* [Implement a greedy decoder](http://www.iro.umontreal.ca/~felipe/bib2webV0.81/cv/papers/paper-tmi-2007.pdf).
* [Use A\* search](http://aclweb.org/anthology-new/W/W01/W01-1408.pdf).
* [Use Lagrangian relaxation](http://aclweb.org/anthology//D/D13/D13-1022.pdf). Guaranteed to find the best score!
* [Use a traveling salesman problem (TSP) solver](http://aclweb.org/anthology-new/P/P09/P09-1038.pdf).
* [Use integer linear programming](http://aclweb.org/anthology-new/N/N09/N09-2002.pdf).
* [Use finite-state algorithms](http://mi.eng.cam.ac.uk/~wjb31/ppubs/ttmjnle.pdf).

These methods all attempt to approximate or solve the Viterbi
approximation to decoding.  You can also try to approximate
$$\Pr(\textbf{e} \mid \textbf{f})$$ directly. Here are some attempts
but they are quite advanced:

* [Use variational algorithms](http://aclweb.org/anthology//P/P09/P09-1067.pdf).
* [Use Markov chain Monte Carlo algorithms](http://aclweb.org/anthology//W/W09/W09-1114.pdf).

But the sky's the limit! There are many ways to decode.  You can
try anything you want as long as you follow the ground rules:

Ground Rules
------------

* Each group should submit using one person as the designated uploader. Ideally use the same person across all homeworks.
* Follow these step-by-step instructions to submit your homework solution:
  1. Your solution to this homework should be in the `answer` directory in a file called `decode.py`. The code should be self-contained, self-documenting, and easy to use. It should read the data exactly like `default.py` does. Your program should run like this:

            python answer/decode.py > output

  1. Upload this file `output` to the [leaderboard submission site](http://sfu-nlp-class.appspot.com) according to [the Homework 0 instructions](hw0.html).
  1. Run the program: `python zipsrc.py`. This will create a a zip file called `source.zip`. Each group should assign one member to upload `source.zip` to [Coursys]({{ site.coursys }}) as the submission for this homework. 
 It should use the same input and output assumptions of `default.py`. Only use `zipsrc.py` to prepare your zip file.
  1. A clear, mathematical description of your algorithm and its motivation written in scientific style. This needn't be long, but it should be clear enough that one of your fellow students could re-implement it exactly. You are given a dummy `README.md` file in the answer directory. Update this file with your description.
  1. Also in the `answer` directory include for each group member with a user name `username` a file in your submission called `README.username` which contains a description of your contribution to the homework solution along with the commit identifiers from either `svn` or `git`. If you have only one member in your group then create an empty file.
* You cannot use data or code resources outside of what is provided to you. You can use NLTK but not the NLTK tokenizer class. 
* For the written description of your algorithm, you can use plain ASCII but for math equations it is better to use either [latex](http://www.latex-project.org/) or [kramdown](https://github.com/gettalong/kramdown).  Do __not__ use any proprietary or binary file formats such as Microsoft Word.

If you have any questions or you're confused about anything, just ask.

#### Acknowledgements

This assignment is adapted from the decoding homework developed
by [Matt Post](http://cs.jhu.edu/~post/) and [Adam
Lopez](http://cs.jhu.edu/~alopez/).

