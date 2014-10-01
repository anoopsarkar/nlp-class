---
layout: default
img: bratconll2k
img_link: "http://weaver.nlplab.org/~brat/demo/latest/#/not-editable/CoNLL-00-Chunking/train.txt-doc-1"
caption: Explore phrasal chunking interactively using Brat
title: Homework 2 | Chunking
active_tab: homework
---

Phrasal Chunking <span class="text-muted">Homework 2</span>
=============================================================

<p class="text-muted">Due on Tuesday, October 7, 2014</p>

The syntax of a natural language, similar to the syntax of a programming language involves
the arrangement of tokens into meaningful groups. Phrasal chunking is the task of finding 
non-recursive syntactic groups of words. For example, the sentence:

> He reckons the current account deficit will narrow to only # 1.8 billion in September .

can be divided into phrasal chunks as follows[^1]:

> [NP <span style="color: DarkBlue">He</span>] 
[VP <span style="color: BlueViolet">reckons</span>] 
[NP <span style="color: DarkBlue">the current account deficit</span>] 
[VP <span style="color: BlueViolet">will narrow</span>] 
[PP <span style="color: red">to</span>] 
[NP <span style="color: DarkBlue">only # 1.8 billion</span>] 
[PP <span style="color: red">in</span>] 
[NP <span style="color: DarkBlue">September</span>] .

[^1]: *Caveat*: If you have a linguistic background, you might find the verb phrases `VP` and prepositional phrases `PP` are different from what you might be used to. In this task, the `VP` is a verb and verb modifiers like auxiliaries (`were`) or modals (`might`), and the `PP` simply contains the preposition. This difference is because of the fact that the chunks are non-recursive (cannot contain other phrases) -- we need trees for full syntax.

Data set
--------

The train and test data consist of three columns separated by spaces.
Each word has been put on a separate line and there is an empty
line after each sentence.

The first column contains the current word, the second column is
the part-of-speech tag for that word, and the third column is
the chunk tag.

Here is an example of the file format:

    He        PRP  B-NP
    reckons   VBZ  B-VP
    the       DT   B-NP
    current   JJ   I-NP
    account   NN   I-NP
    deficit   NN   I-NP
    will      MD   B-VP
    narrow    VB   I-VP
    to        TO   B-PP
    only      RB   B-NP
    #         #    I-NP
    1.8       CD   I-NP
    billion   CD   I-NP
    in        IN   B-PP
    September NNP  B-NP
    .         .    O

The chunk tags contain the name of the chunk type, for example I-NP
for noun phrase words and I-VP for verb phrase words.  Most chunk
types have two types of chunk tags, B-CHUNK for the first word of
the chunk and I-CHUNK for each other word in the chunk. See the
Appendix below for a detailed description of the part-of-speech
tags and the chunk tags in this data set. The full set of tags
for this task is in the file `data/tagset.txt`.

The sequence of labels, `B-NP`, ..., `I-NP` represents a single
phrasal chunk. For instance, the following sequence of labels:

    the       DT   B-NP
    current   JJ   I-NP
    account   NN   I-NP
    deficit   NN   I-NP

gives us the NP phrase:

> [NP <span style="color: DarkBlue">the current account deficit</span>] 

The O chunk tag is used for tokens which are not part of any chunk.

The data set comes from the Conference on Natural Language Learning:
[CoNLL 2000 shared task](http://www.cnts.ua.ac.be/conll2000/chunking/)[^2].

[^2]: [Introduction to the CoNLL-2000 Shared Task: Chunking](http://www.cnts.ua.ac.be/conll2000/pdf/12732tjo.pdf)

Getting Started 
---------------

You must have git and python (2.7) on your system to run the assignments.

If you have already cloned the `nlp-class-hw` repository for Homework 1,
then do the following to get the files for Homework 2:

    # go to the directory where you did a git clone for HW1
    cd nlp-class-hw 
    git pull

Or you can create a new directory that does a fresh clone of the repository:

    git clone https://github.com/anoopsarkar/nlp-class-hw.git

In the `chunker` directory you will find several python programs that you will
use for this assignment.

To count the number of labeled examples in the file format shown above, use `count-sentences.py`:

    python count-sentences.py -i data/train.txt.gz 
    8936

`default.py` contains the default training algorithm for the chunking task.

    python default.py -m default.model

`perc.py` contains the implementation of the $$\arg\max$$ search
that computes the best sequence of chunk tags given an input sentence
that has words and the part-of-speech tags for each word.

    python perc.py -m default.model > output

`score-chunks.py` evaluates the output chunking for the input file, `data/input.txt.gz`

    python score-chunks.py -t output

You can also do the $$\arg\max$$ search for the best sequence of
chunk tags and the evaluation in one line:

    python perc.py -m default.model | python score-chunks.py

This prints out the evaluation scores for `default.py`:

    processed 250 sentences with 5460 tokens and 2997 phrases; found phrases: 6002; correct phrases: 477
         ADJP: precision:   0.00%; recall:   0.00%; F1:   0.00; found:      0; correct:     53
         ADVP: precision:   0.00%; recall:   0.00%; F1:   0.00; found:      0; correct:     96
        CONJP: precision:   0.00%; recall:   0.00%; F1:   0.00; found:      0; correct:      2
           NP: precision:   7.95%; recall:  30.13%; F1:  12.58; found:   6002; correct:   1583
           PP: precision:   0.00%; recall:   0.00%; F1:   0.00; found:      0; correct:    626
          PRT: precision:   0.00%; recall:   0.00%; F1:   0.00; found:      0; correct:     10
         SBAR: precision:   0.00%; recall:   0.00%; F1:   0.00; found:      0; correct:     50
           VP: precision:   0.00%; recall:   0.00%; F1:   0.00; found:      0; correct:    577
    accuracy:  25.57%; precision:   7.95%; recall:  15.92%; F1:  10.60
    Score: 10.60

The overall score reported is the cumulative
[F-measure](http://en.wikipedia.org/wiki/F1_score) which combines
[precision and recall](http://en.wikipedia.org/wiki/Precision_and_recall)
into a single score. The evaluation program also shows the precision, recall
and F-measure for each phrase type in the list of chunking tags. 

For instance, the precision score for NP chunks is the number of
correct NP chunks out of the number of NP chunks produced in the
output, and the recall score for NP chunks is the number of correct
NP chunks out of the number of NP chunks in the reference.

The Challenge
-------------

The main goal of this homework is to train a [structured prediction
model](http://en.wikipedia.org/wiki/Structured_prediction) for the
phrasal chunking task. The search algorithm that provides the
$$\arg\max$$ sequence of output phrasal chunk labels is provided
to you (in `perc.py`). Your job is to implement the training algorithm
that provides weights for each feature used in the prediction by
the model.

    python your-trainer.py -m model
    python perc.py -m model > output
    python score-chunks.py -t output

You will upload the file `output` to the leaderboard submission
site at [sfu-nlp-class.appspot.com](http://sfu-nlp-class.appspot.com/).

By default, the training data is loaded from the following files:

    data/train.txt.gz
    data/train.feats.gz

By default, the test data is loaded from the following files:

    data/input.txt.gz
    data/input.feats.gz

The `*.feats.gz` files are explained below in the description of
the Baseline method. 

### The Baseline

The goal is to provide the best sequence of chunk tags for each input
sentence. We will represent this task as a Hidden Markov Model and
find the best sequence of output labels using the Viterbi algorithm.
The Viterbi algorithm for HMMs has been provided to you in `perc.py`
and this Viterbi implementation is used to find the $$\arg\max$$ 
sequence of output chunk tags.

In the training data we are provided with a set of sentences, and
each sentence has the reference output chunk labels. Each sentence
is a sequence of words and other useful information such as
part-of-speech tags which we refer to as $$w_{[1:n]}$$.  Each
sequence of words is associated with a sequence of output labels
$$t_{[1:n]}$$. 

This problem of assigning $$t_{[1:n]}$$ to the input $$w_{[1:n]}$$
is decomposed into a sequence of decisions in a left-to-right
fashion. At each point there is a *history* which is the context
in which the output label is assigned to a particular word $$w_i$$.
A history is a three-tuple: $$h = (t_{-1}, w_{[1:n]}, i)$$, where
$$t_{-1}$$ is the output label for $$w_{i-1}$$. For each output
label $$t$$, we can write a feature vector representation
of history-tag pairs. Each component of the feature vector
is called a feature function: $$\phi_s(h, t)$$ where there 
are $$d$$ feature functions, $$s = 1, \ldots, d$$. 
For instance, one such feature function might be:

> If $$w_i$$ is the word `the` and $$t$$ is `B-NP` return 1
> else return 0

Another feature function might look at the previous output label:

> If $$t_{-1}$$ is the label `B-NP` and $$t$$ is `I-NP` return 1
> else return 0

For this homework the feature functions have been provided to you
and their values have been pre-computed in the `data/*.feats.gz`
files. Details of the feature vector representation for this chunking
task is provided in the Appendix below.

From these local feature vectors we can create a feature vector
for the entire sentence:

<p>$$ \Phi_s(w_{[1:n]}, t_{[1:n]}) = \sum_{i=1}^n \phi_s(h_i, t_i) $$</p>

The feature vector for the sentence $$\Phi$$ has the same dimensionality
as the feature vector for each tagging decision, $$\phi$$.

#### Algorithm: Perceptron algorithm for HMMs

---
**## Data Structures ##**

`train`
: sentences with output labels: $$(w_{[1:n_j]}^{(j)}, t_{[1:n_j]}^{(j)})$$ 

`T`
: number of iterations over the training set. `opts.n` in `default.py`

$$\phi$$
: function that maps history/output-label pairs to $$d$$-dimensional feature vectors. $$\phi$$ for each history is provided in `data/train.feats.gz`

$$\Phi$$
: global feature vector defined as above by summing over all local feature vectors $$\phi$$

**w**
: $$d$$ dimensional weight vector. one weight for each feature in the feature vector.
{: .dl-horizontal}

**## Initialization ##**

* Set weight vector **w** to zeroes.
{: .list-unstyled}

**## Main Loop ##**

* for t = 1, ..., T, for j = 1, ..., n
    * Use the Viterbi algorithm to find the output of the model on the $$i$$-th training sentence (the function `perc_test` in `perc.py` implements the Viterbi algorithm) where $${\cal T}^{n_j}$$ is the set of all tag sequences of length $$n_j$$.
    <p>$$ z_{[1:n]} = \arg\max_{u_{[1:n]} \in {\cal T}^{n_j}} \sum_s w_s \Phi_s(w_{[1:n_j]}^{(j)}, u_{[1:n_j]}) $$</p>
    * If $$z_{[1:n]} \neq t_{[1:n]}^{(j)}$$ then update the weight vector:
        <p>$$w_s = w_s + \Phi_s(w_{[1:n_j]}^{(j)}, t_{[1:n_j]}^{(j)}) - \Phi_s(w_{[1:n_j]}^{(j)}, z_{[1:n_j]})$$</p>
* return **w**
{: .list-unstyled}
---

The weight vector update step rewards the features that occur in
the reference and penalizes any features that appear in the
$$\arg\max$$ that do not appear in the reference. Features that
lead to incorrect output labels, e.g. $$w_i$$ is the word `the` and
the output label is `B-VP`, will tend to get negative weights, and
features that are observed in the reference will tend to get positive
weights.

Try to write the following difference:

<p>$$\Phi_s(w_{[1:n_j]}^{(j)}, t_{[1:n_j]}^{(j)}) - \Phi_s(w_{[1:n_j]}^{(j)}, z_{[1:n_j]})$$</p>

in terms of the sum over $$\sum_{i=1}^{n_j} \phi_s(h_i, t_i)$$ and notice that
depending on the differences in output labels between $$t_{[1:n_j]}^{(j)}$$ and $$z_{[1:n_j]}$$
different $$s$$ dimensions in the weight vector will updated for the $$\arg\max$$ labels 
versus the truth labels.

An [example feature vector update](https://gist.github.com/anoopsarkar/0b8d0d6ab2f9e257afb8)
might be helpful to check how the update happens for each sentence in the training data set.

In the above pseudo-code, when $$z_{[1:n]} \neq t_{[1:n]}^{(j)}$$
this is counted as a mistake made by the perceptron. The theory
behind the algorithm states that the number of mistakes is 
bounded by a factor called the *margin* of the dataset. In practice,
you should check that the number of mistakes in for an epoch t is smaller
than epoch t-1. We stop before the number of mistakes is zero
because there might be examples in the training data that can
never be correctly predicted.

The $$\arg\max$$ computation above explores all $$S^{n_j}$$ output
label sequences in the set $${\cal T}^{n_j}$$, where $$S$$ is the
total number of output labels (provided in `data/tagset.txt`).  If
this $$\arg\max$$ search is done naively it will take exponential
time. However, the Viterbi algorithm, which is given to you as the
function `perc_test` in `perc.py`, is a dynamic programming algorithm
that computes the $$\arg\max$$ in $${\cal O}(S^2 n_j)$$ time (for
bigram features on output labels).

The algorithm and the theory behind it is described in much greater
detail in the following paper:

> Michael Collins. [Discriminative Training Methods for Hidden
> Markov Models: Theory and Experiments with Perceptron
> Algorithms](http://www.aclweb.org/anthology/W/W02/W02-1001.pdf). EMNLP
> 2002.

You will find that training using the perceptron can be very
compute intensive and time consuming. To help with speedier
development, you can reduce the value of `T` to 1. Also,
the following files contain the sentences and features
for a small training data set:

    data/train.dev
    data/train.feats.dev

Also, when testing your model you can run on a smaller
subset of the input test data:

    data/small.test
    data/small.test.feats

---

### Your Task

Developing a chunker using the Perceptron algorithm (described in
the above pseudo-code) is good enough to get an F-measure that is
close to the performance of the baseline system on the leaderboard.
But getting closer to the best known accuracy on this task, which
is hovering around 94.12 F-measure is a more interesting
challenge. To get full credit you **must** experiment with at least
one additional model of your choice and document your work. Here
are some ideas:

* Use the averaged perceptron algorithm. 
    * First read [Collins 2002](http://www.aclweb.org/anthology/W/W02/W02-1001.pdf).
    * For more detailed pseudo-code see [Sarkar 2011](http://www.cs.sfu.ca/~anoop/papers/pdf/syntax-parsing-survey-2011.pdf) (page 36 and the more efficient version in page 38).
* Use [different data representations](http://www.cs.sfu.ca/~anoop/papers/pdf/ai05.pdf) for chunking and combine them with voting or other means.
* Use [a Margin Infused perceptron algorithm](http://jmlr.csail.mit.edu/papers/v7/crammer06a.html).
* Use a [Conditional Random Field](http://aclweb.org/anthology/N/N03/N03-1028.pdf) aka CRF for batch learning. The baseline above is an example of [online learning](http://en.wikipedia.org/wiki/Online_machine_learning).
* Use [stochastic gradient descent](http://leon.bottou.org/projects/sgd) which uses online learning to train the CRF.
* Use [trigram features over output labels](http://www.aclweb.org/anthology/W05-0611) instead of bigram features.
* Use [clusters over output label sequences and word-by-word independent classifiers](http://aclweb.org/anthology/N/N12/N12-1015.pdf) instead of Viterbi search and a structured perceptron.
* Use [violation fixing and beam search](http://aclweb.org/anthology/N/N12/N12-1015.pdf) instead of argmax search.
* Use [bidirectional search](http://aclweb.org/anthology/P/P07/P07-1096.pdf) which jumps around in the input sentence instead of a strict left-to-right search.

But the sky's the limit! You are welcome to design your own model, as long 
as you follow the ground rules:

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

Appendix
--------

### Part-of-speech tags

| Part-of-speech tag | Description |
|--------------------------------------
| CC | Coordinating conjunction | 
| CD | Cardinal number |
| DT | Determiner |
| EX | Existential there |
| FW | Foreign word |
| IN | Preposition or subordinating conjunction |
| JJ | Adjective |
| JJR| Adjective, comparative |
| JJS| Adjective, superlative |
| LS | List item marker |
| MD | Modal |
| NN | Noun, singular or mass |
| NNS| Noun, plural |
| NNP| Proper noun, singular |
| NNPS   | Proper noun, plural |
| PDT| Predeterminer |
| POS| Possessive ending |
| PRP| Personal pronoun |
| PRP$|   Possessive pronoun |
| RB | Adverb |
| RBR| Adverb, comparative |
| RBS| Adverb, superlative |
| RP | Particle |
| SYM| Symbol |
| TO | to |
| UH | Interjection |
| VB | Verb, base form |
| VBD| Verb, past tense |
| VBG| Verb, gerund or present participle |
| VBN| Verb, past participle |
| VBP| Verb, non-3rd person singular present |
| VBZ| Verb, 3rd person singular present |
| WDT| Wh-determiner |
| WP | Wh-pronoun |
| WP$ | Possessive wh-pronoun |
| WRB | Wh-adverb  |
|--------------------------------------
{: .table}

### Chunk tags

| Chunk tag | Description | Examples | Comment |
|-------------------------------------------------------
| NP | noun phrase | `[NP Eastern Airlines]` | The most common phrase in the data set. |
| VP | verb phrase | `[VP have to be]` ; `[VP have got]` `[VP is]` ; `[VP could very well show]` | Does *not* include the object of the verb |
| ADVP | adverb phrase | `[NP a year] [ADVP earlier]` | Modifies a verb phrase or noun phrase. |
| ADJP | adjective phrase | `[NP 68 years] [ADJP old]` | Modifies a noun phrase. |
| PP | prepositional phrase | `[PP in]` ; `[PP such as]` ; `[PP particularly among]` | Contains only the preposition *not* the complement NP phrase after the preposition. |
| SBAR | complementizer phrase | `[SBAR that]` ; `[SBAR even though]` | Marks the start of a sentence |
| CONJP | conjunction phrase | `[CONJP and]` ; `[CONJP as well as]` | |
| PRT | verb particle phrase | `[PRT up]` ; `[PRT on and off]` | Verb particles in English: `call up`; `up` is the particle. |
| INTJ | interjection phrase | `[INTJ alas]` ; `[INTJ good grief !]` | Very rare |
| LST | list phrase | `[LST 1.]` ; `[LST first]` ; `[LST a]` | Very rare |
| UCP | unlike coordinated phrase | `[UCP and]` | Similar to the CONJP phrase but for conjunction of two different phrase types. Extremely rare. |
| O | outside any phrase | `[O .]` ; `[SBAR that]` `[NP there]` `[VP were]` `[O n't]` `[NP any major problems]` | Mostly punctuations, but some corner cases as well. |
|--------------------------------------
{: .table}

### Feature Schema

This section explains the format of data in the `*.feats.gz` files. 

Consider a fragment of the example sentence from the introduction:

    He PRP B-NP
    reckons VBZ B-VP
    the DT B-NP
    current JJ I-NP
    account NN I-NP

Let us consider generating features for the 3rd word in this sentence, `the DT B-NP`.
This word is assigned an index of `0`. The word before, `reckons` is assigned a relative 
row position of `-1` and `He` has a row position `-2`. Similarly, the next word
`current` is row position `1`, and so on. We can also look at the different values
in each row position. For example, for row position `-1` the column position `0`
represents the word `reckons` and column position `1` is the part-of-speech tag, `VBZ`.

We can now define a feature schema that generates features for each row position
using the notation `%x[i,j]` where `%x` represents the input, `i` is the relative
row position, and `j` is the value at the column for that row position.

Similarly, `%y[i]` represents a feature schema for the output labels, where
`i` is the relative row position. 

We can create n-gram feature schema by combining multiple row positions separated
by a slash `/`. For instance, `%x[i,j]/%x[i,j]` is a bigram feature schema.

| Feature name | Schema | Example for `the` |
|----------------------------------
| U00 | %x[-2,0] | `FEAT U00:He` |
| U01 | %x[-1,0] | `FEAT U01:reckons` |
| U02 | %x[0,0] | `FEAT U02:the` |
| U03 | %x[1,0] | `FEAT U03:current` |
| U04 | %x[2,0] | `FEAT U04:account` |
| U05 | %x[-1,0]/%x[0,0] | `FEAT U05:reckons/the` |
| U06 | %x[0,0]/%x[1,0] | `FEAT U06:the/current` |
| U10 | %x[-2,1] | `FEAT U10:PRP` |
| U11 | %x[-1,1] | `FEAT U11:VBZ` |
| U12 | %x[0,1]q | `FEAT U12:DTq` |
| U13 | %x[1,1] | `FEAT U13:JJ` |
| U14 | %x[2,1] | `FEAT U14:NN` |
| U15 | %x[-2,1]/%x[-1,1] | `FEAT U15:PRP/VBZ` |
| U16 | %x[-1,1]/%x[0,1] | `FEAT U16:VBZ/DT` |
| U17 | %x[0,1]/%x[1,1] | `FEAT U17:DT/JJ` |
| U18 | %x[1,1]/%x[2,1] | `FEAT U18:JJ/NN` |
| U20 | %x[-2,1]/%x[-1,1]/%x[0,1] | `FEAT U20:PRP/VBZ/DT` |
| U21 | %x[-1,1]/%x[0,1]/%x[1,1] | `FEAT U21:VBZ/DT/JJ` |
| U22 | %x[0,1]/%x[1,1]/%x[2,1] | `FEAT U22:DT/JJ/NN` |
| B | %y[-1]/%y[0] | `FEAT B` |
{: .table}

The last feature `B` which stands for the bigram feature over output
labels is not spelled out in the `.feats.gz` files because this
feature has all pairs of output labels and the computation of the
$$\arg\max$$ is needed to tell us which `B` feature obtained the
highest score and if it was different from the pair of output labels
in the reference chunks.

For example, the Viterbi algorithm in `perc.py` could produce the
output label `I-NP` for the word `the` and the output label `B-NP`
for the previous word `reckons`. Thus, the decoder has produced a
bigram `B` feature: `B-NP/I-NP` which is a feature that the trainer
should penalize because it is incorrect.  The trainer should also
reward the correct bigram feature `B-VP/B-NP`.


