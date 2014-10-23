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

<p class="text-muted">Due on Tuesday, November 4, 2014</p>

Decoding is process of taking input in French:

    honorables sénateurs , que se est - il passé ici , mardi dernier ?

...And finding its best English translation under your  model:

    honourable senators , what happened here last Tuesday ?

To decode, we need a model of English sentences conditioned on the
French sentence. You did most of the work of creating
such a model in [Homework 1](hw1.html). In this assignment,
we will give you some French sentences and a probabilistic model consisting of
a phrase-based translation model $$Pr_{\textrm{TM}}(\textbf{f},\textbf{a} \mid \textbf{e})$$
and an n-gram language model $$Pr_{\textrm{LM}}(\textbf{e})$$. __Your 
challenge is to find the most probable English translation under 
the model.__ We assume a noisy channel decomposition.

<center>
$$\begin{align*} \textbf{e}^* & = \arg \max_{\textbf{e}} \Pr(\textbf{e} \mid \textbf{f}) \\ 
& = \arg \max_{\textbf{e}} \frac{\Pr_{\textrm{TM}}(\textbf{f} \mid \textbf{e}) \times \Pr_{\textrm{LM}}(\textbf{e})}{p(\textbf{f})} \\ 
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
`data/input`.  You can compute $$p(\textbf{e} \mid \textbf{f})$$
using `score-decoder.py`.

    python score-decoder.py < output

### Scoring decoder output

The `score-decoder.py` command computes the total log probability
for the output file. If there are $$N$$ sentences in the output:
$$\textbf{f}^1, \ldots, \textbf{f}^N$$ then the output score is the sum of the
translation and language model log probability over all sentences:

<p>$$\textrm{score} = \sum_{i=1}^N \log \sum{\textbf{a}} \Pr_{\textrm{TM}}(\textbf{f}^i ,\textbf{a} \mid \textbf{e}^i) \times \Pr_{\textrm{LM}}(\textbf{e}^i) $$</p>

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

<center>$$\begin{align*} \textbf{e}^* &= \arg \max_{\textbf{e}} \sum_{\textbf{a}} Pr_{\textrm{TM}}(\textbf{f},\textbf{a} \mid \textbf{e}) \times Pr_{\textrm{LM}}(\textbf{e}) \\ 
&\approx \arg \max_{\textbf{e}} \max_{\textbf{a}} Pr_{\textrm{TM}}(\textbf{f},\textbf{a} \mid \textbf{e}) \times Pr_{\textrm{LM}}(\textbf{e}) \end{align*}$$</center>

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
    python decode -i example | python score-decoder.py -i example
    echo a selection committee was achievement . | python score-decoder.py -i example

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

    python decode | python score-decoder.py
    python decode -s 10000 | python score-decoder.py

The Challenge
-------------

Your task is to __find the most probable English translation__.
Our model assumes that any segmentation of the French sentence into
phrases followed by a one-for-one substitution and permutation of
those phrases is a valid translation. We make the simplifying
assumption that segmentation and ordering probabilities are uniform
across all sentences, hence constant.  This means that
$$p(\textbf{e},\textbf{a} \mid \textbf{f})$$ is proportional to the
product of the n-gram probabilities in $$Pr_{\textrm{LM}}(\textbf{e})$$
and the phrase translation probabilities in
$$Pr_{\textrm{TM}}(\textbf{f},\textbf{a} \mid \textbf{e})$$. To avoid
numerical underflow we work in logspace, seeking $$\arg \max_{\textbf{e}}
\max_{\textbf{a}} \log Pr_{\textrm{TM}}(\textbf{f},\textbf{a} \mid
\textbf{e}) + \log Pr_{\textrm{LM}}(\textbf{e})$$. The baseline
decoder works with log probabilities, so you can simply follow what
it does.

### The Leaderboard

In this homework, the score produced by `score-decoder.py` will be
the same as the score on the leaderboard. So you do not need to
upload your output nearly as often as you did in other homeworks.

To get on the leaderboard, produce your output file:

    python your-decoder.py > output

Then upload the file `output` to the leaderboard for Homework 4 on
[sfu-nlp-class.appspot.com](https://sfu-nlp-class.appspot.com)

### The Baseline

At minimum, you must implement a beam-search decoder like the one
we have given you that is also capable of _swapping adjacent phrases_.
To get full credit, you __must__ additionally experiment with another
decoding algorithm.  Any permutation of phrases is a valid translation,
so we strongly suggest searching over all or some part of this
larger space. This search is NP-Hard, so it will not be easy. 

### Extending the baseline

There are several approaches that tackle the decoding problem for
machine translation:

* [Implement a greedy decoder](http://www.iro.umontreal.ca/~felipe/bib2webV0.81/cv/papers/paper-tmi-2007.pdf).
* [Use chart parsing to search over many permutations in polynomial time](http://acl.ldc.upenn.edu/C/C04/C04-1030.pdf).
* [Use a traveling salesman problem (TSP) solver](http://aclweb.org/anthology-new/P/P09/P09-1038.pdf).
* [Use finite-state algorithms](http://mi.eng.cam.ac.uk/~wjb31/ppubs/ttmjnle.pdf).
* [Use Lagrangian relaxation](http://aclweb.org/anthology//D/D13/D13-1022.pdf).
* [Use integer linear programming](http://aclweb.org/anthology-new/N/N09/N09-2002.pdf).
* [Use A* search](http://aclweb.org/anthology-new/W/W01/W01-1408.pdf).

These methods all attempt to approximate or solve the Viterbi
approximation to decoding.  You can also try to approximate
$$p(\textbf{e} \mid \textbf{f})$$ directly.

* [Use variational algorithms](http://aclweb.org/anthology//P/P09/P09-1067.pdf).
* [Use Markov chain Monte Carlo algorithms](http://aclweb.org/anthology//W/W09/W09-1114.pdf).

But the sky's the limit! There are many ways to decode.  You can
try anything you want as long as you follow the ground rules:

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
$$\textbf{a} = (1,3,2)$$, that is, $$a_1 = 1$$, $$a_2 = 3$$, and
$$a_3 = 2$$ we can derive the probability of this sentence pair
alignment to be:

<p>$$\Pr(\mathbf{f}, \textbf{a} \mid \mathbf{e}) = t(f_1 \mid e_1)
\cdot t(f_2 \mid e_3) \cdot t(f_3 \mid e_2)$$</p>

In this simple model, we allow any alignment function that maps any
word in the source sentence to any word in the target sentence (no
matter how far apart they are). The alignments are not provided to
us, so we remove the alignments by summing over them[^2]:

<p>$$
\begin{eqnarray*}
\Pr(\mathbf{f} \mid \mathbf{e}, t) & = & \sum_{\textbf{a}} \Pr(\mathbf{f}, \textbf{a} \mid \mathbf{e}, t) \\
& = & \sum_{a_1=1}^J \cdots \sum_{a_I=1}^J  \prod_{i=1}^I t(f_i \mid e_{a_i}) \\
&& \textrm{(this computes all possible alignments)} \\
& = & \prod_{i=1}^I \sum_{j=1}^J t(f_i \mid e_j) \\
&& \textrm{(after conversion of $J^I$ terms into $I \cdot J$ terms)}
\end{eqnarray*}
$$</p>

[^2]: For each assignment of $$a_i$$ which is a sum over $$J$$ terms we have to do $$I$$ multiplications, so the total number of terms is $$J^I$$. However, if you allow assignment of $$a_i$$ to $$0$$ (alignment to *null*) then the number of terms is $$(J+1)^I$$.

We wish to learn the parameters $$t(\cdot \mid \cdot)$$ that maximize
the log-likelihood of the training data:

<p>$$ \arg\max_{t} L(t) = \arg\max_{t} \sum_s \log \Pr(\mathbf{f}^{(s)} \mid
\mathbf{e}^{(s)}, t) $$</p>

#### Training the model

In order to estimate the parameters $$t(\cdot \mid \cdot)$$
we start with an initial estimate $$t_0$$ and modify it iteratively
to get $$t_1, t_2, \ldots$$. The parameter updates are derived
for each French word $$f_i$$ and English word $$e_j$$ as follows:

<p>$$t_k(f_i \mid e_j) = \sum_{s=1}^N \sum_{(f_i, e_j) \in (\textbf{f}^{(s)}, \textbf{e}^{(s)})} \frac{ \textrm{count}(f_i, e_j, \textbf{f}^{(s)}, \textbf{e}^{(s)}) }{ \textrm{count}(e_j, \textbf{f}^{(s)}, \textbf{e}^{(s)}) }$$</p>

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
\textrm{count}(e_j, \textbf{f}, \textbf{e}) & = & \sum_{i=1}^I \textrm{count}(f_i, e_j, \textbf{f}, \textbf{e})
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
$$t_0(f \mid e) = \frac{1}{V_f}$$ where $$V_f$$ is the French
vocabulary size. This ensures that $$\sum_f t(f \mid e) = 1$$.

#### Convergence

The theory behind this algorithm states that the iterative updates
have the following property:

<p>$$L(t_k) \geq L(t_{k-1})$$</p>

We can check for convergence by checking if the value of $$L(t)$$
does not change much from the previous iteration (difference from
previous iteration is less than $$10^{-4}$$, for example).

The objective for the baseline method, $$L(t)$$, can be shown to
be an example of convex optimization, which means we are guaranteed
to find the value of $$t$$ that maximizes $$L(t)$$ *in the limit*.
However, this could mean hundreds or thousands of iterations for
any given data set.

Most practitioners simply iterate over the training data for 3 to
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
* [Add *null* words to the source sentence](http://aclweb.org/anthology/P/P04/P04-1066.pdf).
* There are [better ways to initialize the parameters](http://aclweb.org/anthology/P/P04/P04-1066.pdf) that lead to better alignments especially if you run only for 5 iterations.
* Implement a [HMM-based alignment model](http://aclweb.org/anthology/C/C96/C96-2141.pdf).
* Add part of speech tags to one language or both and use them, for example, to separate $$t( \textrm{usine} \mid \textrm{plant, N})$$ and $$t( \textrm{plante} \mid \textrm{plant, N})$$ from the alignment $$t( \textrm{planter} \mid \textrm{plant, V} )$$.
* Add phrasal chunks to one language or both and reward alignments within phrasal chunks and/or penalize alignments across phrasal chunks.
* Implement the more sophisticated alignment models from the [Statistical MT Tutorial Workbook](http://www.isi.edu/natural-language/mt/wkbk.pdf).

But the sky's the limit! You are welcome to design your own model,
as long as you follow the ground rules:

Ground Rules
------------

* Each group should submit using one person as the designated uploader.
* You must turn in three things:
  1. The alignment of the first 1000 lines of the German-English data set uploaded to the [leaderboard submission site](http://sfu-nlp-class.appspot.com) using the instructions given above. You can upload new output as often as you like, up until the assignment deadline. The Submit button for showing the test set scores will be unavailable until after the homework deadline and grace days have passed.  The German-English alignments will be evaluated for the leaderboard, but the `score-alignments.py` program on the French-English alignments will give you a good idea of how well you're doing.
  1. Your code. Each group should assign one member to upload the source code to [Coursys](https://courses.cs.sfu.ca) as the submission for Homework 3. The code should be self-contained, self-documenting, and easy to use. It should use the same input and output assumptions of `default.py`.
  1. A clear, mathematical description of your algorithm and its motivation written in scientific style. This needn't be long, but it should be clear enough that one of your fellow students could re-implement it exactly. Include the file for this writeup as part of the tarball or zip file you will upload to [Coursys](https://courses.cs.sfu.ca). Include also how your group divided up the work load and each group member's contribution to the homework solution.
* You cannot use data or code resources outside of what is provided to you. You can use NLTK but not the NLTK aligner implementation. You cannot use any public implemenation of word alignment such as `GIZA++`, `fast_align`, or any other open source aligner.
* For the written description of your algorithm, you can use plain ASCII but for math equations it is better to use either [latex](http://www.latex-project.org/) or [kramdown](https://github.com/gettalong/kramdown).  Do __not__ use any proprietary or binary file formats such as Microsoft Word.

If you have any questions or you're confused about anything, just ask.

#### Acknowledgements

This assignment is adapted from the word alignment homework developed
by [Matt Post](http://cs.jhu.edu/~post/) and [Adam
Lopez](http://cs.jhu.edu/~alopez/) based on an original homework
developed by [Philipp Koehn](http://homepages.inf.ed.ac.uk/pkoehn/)
and later modified by [John DeNero](http://www.denero.org/). It
incorporates some ideas from [Chris Dyer](http://www.cs.cmu.edu/~cdyer).

<!--
    le droit de permis passe donc de $ 25 à $ 500 .
    we see the licence fee going up from $ 25 to $ 500 .
-->

<!--
% 0 le 1 droit 2 de 3 permis 4 passe 5 donc 6 de 7 \$ 8 25 9 \`a 10 \$ 11 500 12 . \\
% 0 we 1 see 2 the 3 licence 4 fee 5 going 6 up 7 from 8 \$ 9 25 10 to 11 \$ 12 500 13 .
    0-2 1-4 3-3 4-5 4-6 5-7 7-8 8-9 9-10 10-11 11-12 12-13
-->

<!--
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
-->

