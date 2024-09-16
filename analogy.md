# Homework 1: Word Vectors and the Analogy Task

<span class="text-info">Start on {{ site.hwdates[1].startdate }}</span> |
<span class="text-warning">Due on {{ site.hwdates[1].deadline }}</span>

## Getting Started

If you have already cloned my homework repository `nlp-class-hw` for
previous homeworks then go into that directory and update the directory:

    git pull origin/main
    cd nlp-class-hw/analogy

If you don't have that directory anymore then simply clone the
repository again:

    git clone https://github.com/anoopsarkar/nlp-class-hw.git

Clone your own repository from GitLab if you haven’t done it already:

    git clone git@github.sfu.ca:USER/nlpclass-{{ site.semcode }}-g-GROUP.git

Note that the `USER` above is the SFU username of the person in
your group that set up the GitLab repository.

Then copy over the contents of the `analogy` directory into your
`hw2` directory in your repository.

Set up the virtual environment:

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

Note that if you do not change the requirements then after you have
set up the virtual environment `venv` you can simply run the following
command to get started with your development for the homework:

    source venv/bin/activate

## Background

In this homework we will be exploring the use of word vectors to
solve simple analogy tasks.

A word vector is a distributed representation for a word that can
be trained via various methods on a word prediction task. A useful
word vector is a representation that can capture the usage of the
word in context. A properly trained set of word vectors for a
language can capture some interesting linguistic relations. These
relations can be tested using vector arithmetic to identify aspects
of the distributed representation.

![Vector offsets for three word pairs]({{ site.baseurl }}/assets/img/wvgender.png "Vector offsets for three word pairs illustrating the gender relation"){:height="50%" width="50%"}

![A different projection for king, queen]({{ site.baseurl }}/assets/img/wvplural.png "A different projection for the words king, queen showing the singular/plural relation"){:height="50%" width="50%"}

A common test for word vectors is the aritmetic analogy test.
Introducing this test, (Mikolov et al, 2013) proposed to measure
the presence of linguistic relations using vector arithmetic.

For two pairs of words that represent the same linguistic relation,
$$(a, a^\ast)$$ and $$(b, b^\ast)$$

![The analogy task for word vectors]({{ site.baseurl }}/assets/img/wvanalogy.png "Within pair similarity in the arithmetic analogy test. The vector arithmetic of `v(China) + (v(Paris) - v(France))` results in a vector that is close to the vector for the word `Beijing`."){:height="50%" width="50%"}

## The Data

The `dev` and `test` set for this homework is taken from the Google
word analogy dataset (Mikolov et al., 2013a) was collected for the
following paper on word vectors:

> Tomas Mikolov, Kai Chen, Greg Corrado, and Jeffrey Dean. 2013a. Efficient estimation of word representations in vector space. https://arxiv.org/abs/1301.3781

The dataset contains 19544 questions and covers 14 relation types,
7 of which are semantic in nature and 7 are morpho-syntactic (each
type is enumerated below). The dataset was created by manually
constructing example word-pairs of each relation, and providing all
the pairs of word-pairs (within each relation type) as analogy
questions.

## Default solution

The default solution is provided in `default.py`. To use the default
as your solution:

    cp default.py answer/analogy.py
    cp default.ipynb answer/analogy.ipynb
    python zipout.py
    python check.py

The default solution will look for the file `glove.6B.100d.magnitude`
in the data directory. 

You can either download the word vectors file from:

    http://magnitude.plasticity.ai/glove/medium/glove.6B.100d.magnitude

Or you can use the same file directly on CSIL from the following directory:

    /usr/shared/CMPT/courses/nlp-class/analogy/glove.6B.100d.magnitude

There is also a text file available that is compatible with
[gensim](https://radimrehurek.com/gensim/). 

    /usr/shared/CMPT/courses/nlp-class/analogy/glove.6B.100d.txt

Please do not copy over the file into your CSIL directory as it is
quite large and you can go over your disk quota. Instead modify
`default.py` to use the full path to the above file which is
accessible on the CSIL machines or use the command line option
for `default.py` to access the word vectors.

    python default.py -w /usr/shared/CMPT/courses/nlp-class/analogy/glove.6B.100d.magnitude > output.txt

And then you can check the score on the dev output file called `output.txt` by running:

    python analogy_check.py

Make sure that the command line options are kept as they are in
`default.py`. You can add to them but you must not delete any
command line options that exist in `default.py`.

Submitting the default solution without modification will get you
zero marks.

The default solution produces 10 candidates for each lexical
substitution and if any of them match the substitute words
preferred by a group of human annotators then that substitution
is marked as correct.

The overall score reported is the precision score over the entire
data set which is described in detail in the Accuracy section below.

Your solution should produce exactly 10 guesses for each lexical
substitution just like the default solution.

## The Challenge

Your task is to _improve the accuracy as much as possible_. The
score is explained in detail in the Accuracy section below. You can
only use the pre-trained word vectors file that has been provided
to you as described in the `Default solution` section above.
You cannot use any other word vectors or word embeddings.

## Data files

The data files provided are:

* `data/input` -- input files `dev.txt` and `test.txt`
* `data/reference/dev.out` -- the reference output for the `dev.txt` input file
* `data/lexicons` -- lexicon files that contain the word-word relations used for the Baseline method described below

In addition you must use the pre-trained word vectors from `glove.6B.100d.magnitude`.

`pymagnitude` is the Python library to use in order to access the
word vectors in `glove.6B.100d.magnitude`.  It is already in
`requirements.txt` so if you have set up your virtual environment
correctly you should be able to run:

    python
    >>> from pymagnitude import *
    >>> wv = Magnitude("data/glove.6B.100d.magnitude")
    >>> len(wv) # how many words in this word vector file
    400000
    >>> wv.dim # the dimensionality of each word vector
    100
    >>> wv.most_similar("cat", topn=5)
    [('dog', 0.87980753), ('rabbit', 0.7424427), ('cats', 0.7323004), ('monkey', 0.72887105), ('pet', 0.719014)]

The following code snippet prints out the first 5 components of the
word vector for 10 words out of the entire vocabulary:

    >>> for key, vector in wv[:10]:
    ...     print(key, vector[:5])
    ...
    the [-0.0065612 -0.0420655  0.1250817 -0.0686479  0.0142879]
    , [-0.0193882  0.0199032  0.1077039 -0.0978882  0.1213604]
    . [-0.0622309  0.0383524  0.0848841 -0.1186634 -0.0702856]
    of [-0.0242819 -0.0385573  0.1426693  0.0269912  0.0849883]
    to [-0.0294079  0.0077549  0.0295846 -0.0076247 -0.0139113]
    and [-0.012695   0.0408041  0.004187  -0.0893432  0.0598521]
    in [ 0.0140624 -0.0364279  0.0271868  0.0219427  0.0627435]
    a [-0.043387   0.007049  -0.0032453 -0.0278637  0.1032215]
    " [-0.0462585 -0.0359123  0.0266947 -0.1106516 -0.0430477]
    's [ 0.0883406 -0.0303955  0.1102929 -0.1025762 -0.0295324]

More information is available on the
[Magnitude](https://github.com/plasticityai/magnitude) GitHub page.

The lexicon files are as follows:

* `framenet.txt`: from the [Framenet](https://framenet.icsi.berkeley.edu/fndrupal/) project
* `ppdb-xl.txt`: from the [PPDB](http://paraphrase.org) project
* `wordnet-synonyms+.txt`: from [Wordnet](https://wordnet.princeton.edu/)
* `wordnet-synonyms.txt`: smaller set of synonyms from [Wordnet](https://wordnet.princeton.edu/) for use during development

Each file contains a list of words that are assumed to be semantically
related to each other. If you consider each ontology as a graph
then each line in the above files represents an edge between each
pair of words on that line.  For example, the line:

    faulty incorrect wrong defective

tells that that there is an undirected graph edge representing a
semantic relation between each pair of words on this line, e.g.
`faulty-incorrect`, `faulty-defective`, `incorrect-defective`, and
so on.

## Baseline 

The baseline method is what you should implement first before you
explore additional improvements to improve your score.

First, we will implement _retrofitting_ to combine the information
about word senses from Wordnet in order to modify the default word vectors.

### Retrofitting Word Vectors with Semantic Lexicons

Information about word senses can be found in many semantic lexicons.
The most widely used hand-curated semantic lexicon for the English
language is the [Wordnet](https://wordnet.princeton.edu) ontology.

For instance, if you search Wordnet for the word
[dry](http://wordnetweb.princeton.edu/perl/webwn?s=dry&sub=Search+WordNet&o2=&o0=1&o8=1&o1=1&o7=&o5=&o9=&o6=&o3=&o4=&h=)
you will see the various semantic relations of _dry_ with other
words captured in Wordnet.  

![Wordnet search for dry]({{ site.baseurl }}/assets/img/drywordnet.png "Synonym sets for dry on Wordnet"){:height="50%" width="50%"}

Of the many semantic relations in Wordnet
the most useful to us for this task is that we can identify various
groups of words with similar meanings. These groups of words are
called _synsets_ (short for synonym sets). However, how do we use
these semantic relations to augment the word representations we
have in our pre-trained word vectors?  This is where retrofitting
can be useful. The idea is to use the semantic relations from an
ontology like Wordnet and modify or retrofit the word vectors to
use that information. This can make the word vectors more useful
for tasks like lexical substitution which depend on knowledge of
various senses of the target word.

To explain how retrofitting works we need to work with some notation.
Let $w_i, w_j$ be words from the vocabulary $V$. Let ${\cal O}$ be
an ontology (for example, Wordnet) that encodes semantic relations
between words as described in the example above. We represent 
the ontology as an undirected graph $(V, E)$ with one vertex $v \in V$
for each word type and edges $(w_i, w_j) \in V \subseteq V \times V$
indicating some semantic relationship.

The word vectors for our vocabulary $V$ can be represented by a
matrix $\hat{Q}$ which has columns $(\hat{q}_1, \ldots, \hat{q}_n)$
where $|V| = n$ so $\hat{q}_i$ is the word vector for word $w_i$.
This matrix of word vectors $\hat{Q}$ has been provided to you as
a pre-trained model (the 100 dimensional GloVe word vectors provided
above).

The objective of retrofitting is to use the ontology graph ${\cal O}$
in order to learn a matrix $Q = (q_1, \ldots, q_n)$ such that the
columns of the matrix $Q$ are close (in vector space) to the word vectors in 
$\hat{Q} = (\hat{q}_1, \ldots, \hat{q}_n)$
(so $q_i$ is close to $\hat{q}_i$) and at the same time the columns
of the matrix $Q$ are close (in vector space) to the word vectors
of other words that are adjacent vertices in ${\cal O}$. So if $(w_i, w_j)$
are connected by an edge in the ontology then we want $q_i$ and $q_j$ to
be close in vector space. Retrofitting involves combining these two
criteria to modify the word vectors for the words in our vocabulary.

For example, the following figure shows how the semantic relations
in the ontology (the edges between the white nodes) can be used to
learn new retrofitted word vectors (the white nodes). For each word
the figures shows a link between the white node for that word (which
represents the retrofitted word vectors we wish to learn) and the
grey node for the same word (which comes from the pre-trained word
vectors).

![Word graph image]({{ site.baseurl }}/assets/img/retrofit.png "Word graph with edges between related words showing the observed (grey) and the inferred (white) word vector representations."){:height="50%" width="50%"}

The distance between two word vectors is represented by the Euclidean distance.
Our objective function $L$ for finding $Q$ can be written as: 

$$ L(Q) = \sum_{i=1}^n \left[ \alpha_i || q_i - \hat{q}_i ||^2 + \sum_{(i,j) \in E} \beta_{ij} || q_i - q_j ||^2 \right] $$

The algorithm to find $Q$ is as follows:

- Initialize $Q$ to be equal to the vectors in $\hat{Q}$
- For iterations $t = 1 \ldots T$
    - Take the derivative of $L(Q)$ wrt each $q_i$ word vector and assign it to zero to get an update:

        $$ q_i = \frac{\sum_{j:(i,j) \in E} \beta_{ij} q_j + \alpha_i \hat{q}_i}{\sum_{j:(i,j) \in E} \beta_{ij} + \alpha_i} $$

In practice set $T = 10$ which should correspond to changes in
Euclidean distance of adjacent vertices of roughly $10^{-2}$.  At
first, set $\alpha_i = 1$ for all $i$ and $\beta_{ij} = 1$ for all
$i,j$. You can try different weighting schemes to see if you get
an improvement.

See the `Data files` section above which explains how to iterate
through the vocabulary using `pymagnitude` functions.

Since `pymagnitude` only offers read-only access to word vectors
you will have to write your retrofitted word vectors to a file with
the word as first column followed by a space delimited list of 100
floating point numbers. For example, one line of this file will
look like this:

    the -0.038194 -0.24487 ...97 numbers here... 0.27062

Once you have written the retrofitted word vectors to this text file you can convert it into a `pymagnitude` format
using the pymagnitude convertor:

    $ python -m pymagnitude.converter -i data/glove.6B.100d.retrofit.txt -o data/glove.6B.100d.retrofit.magnitude
    Detected GloVe format! Converting to word2vec format first...(this may take some time)
    Loading vectors... (this may take some time)
    Found 400000 key(s)
    Each vector has 100 dimension(s)
    Creating magnitude format...
    Writing vectors... (this may take some time)
    0% completed
    1% completed
    ...
    99% completed
    Committing written vectors... (this may take some time)
    ...
    Successfully converted '/var/folders/.../...txt' to 'data/glove.6B.100d.retrofit.magnitude'!

If you are using `gensim` you can directly load up the retrofitted
text file or convert it into the `gensim` binary format.

You can use your retrofitted word vectors with the code in `default.py`
or an augmented version of `default.py` that uses a better method
to find the 10 substitute words for each target word (described
below in the `Incorporating Context Words` section).

### Background Reading

For more details read the original paper that introduced the
idea of retrofitting word vectors:

> [Retrofitting Word Vectors to Semantic Lexicons](https://www.aclweb.org/anthology/N15-1184/). Faruqui et. al. NAACL 2015.

You can also view the source code that implements retrofitting on
GitHub:

> [https://github.com/mfaruqui/retrofitting](https://github.com/mfaruqui/retrofitting)

You can view the implementation but you must implement the algorithm
yourself and apply it to the lexical substitution task.

You are welcome to design your own model, as long as you have
implemented the Baseline model first. One possible extension is
to use the context words around the target word to find a better
guess for the substitute word.

### Incorporating Context Words

You should also augment the default solution to incorporate the
context around the target word to find better substitute words. You
can use the approach in the following, but do not use their contextual
embeddings. You must still only use the GloVe embeddings provided
to you.

> [A Simple Word Embedding Model for Lexical Substitution](https://www.aclweb.org/anthology/W15-1501/). Oren Melamud, Omer Levy, Ido Dagan. 1st Workshop on Vector Space Modeling for NLP. 2015.


## Required files

You must create the following files:

* `answer/analogy.py` -- this is your solution to the homework. start by copying `default.py` as explained below.
* `answer/analogy.ipynb` -- this is the iPython notebook that will be your write-up for the homework.

## Run your solution on the data files

To create the `output.zip` file for upload to Coursys do:

    python zipout.py

For more options:

    python zipout.py -h

## Check your accuracy

To check your accuracy on the dev set:

    python check.py

The output score is a precision score where you get 10 guesses for
each example in the dataset but you are not penalized for getting
any guess wrong.  For each example $i$ in the dataset, let $H_i$
be the set of substitutes provided by the human annotators for the
given target word. There can be upto 5 different words (or phrases)
in the set $H_i$.  Your output for example $i$ consists of 10 guesses
which we represent as the set $O_i$. If the intersection of these
two sets $H_i \cap O_i$ is non empty we increment the count of true
positives $tp$. If the intersection is empty we increment the false
positives counter $fp$. The _score_ for this task is then defined as the
precision score $P$:

$$P = \frac{tp}{tp + fp}$$

For more options:

    python check.py -h

In particular use the log file to check your output evaluation:

    python check.py -l log

The accuracy on `data/input/test.txt` will not be shown.  We will
evaluate your output on the test input after the submission deadline.

The default solution gets a very poor F-score on the dev and test set:

    $ python check.py
    dev.out score: 27.8920
    test.out score: 36.0000

Implementing the Baseline method should give you an improved
accuracy on the dev set:

    $ python check.py
    dev.out score: 40.5167

## Submit your homework on Coursys

Once you are done with your homework submit all the relevant materials
to Coursys for evaluation.

### Create output.zip

Once you have a working solution in `answer/analogy.py` create
the `output.zip` for upload to Coursys using:

    python zipout.py

### Create source.zip

To create the `source.zip` file for upload to Coursys do:

    python zipsrc.py

You must have the following files or `zipsrc.py` will complain about it:

* `answer/analogy.py` -- this is your solution to the homework. start by copying `default.py` as explained below.
* `answer/analogy.ipynb` -- this is the iPython notebook that will be your write-up for the homework.

In addition, each group member should write down a short description of what they
did for this homework in `answer/README.username`.

### Upload to Coursys

Go to `Homework 2` on Coursys and do a group submission:

* Upload `output.zip` and `source.zip`
* Make sure your `source.zip` matches your Gitlab repository.
* Make sure you have documented your approach in `answer/analogy.ipynb`.
* Make sure each member of your group has documented their contribution to this homework in `answer/README.username` where `username` is your CSIL/GitLab username.

## Grading

The grading is split up into the following components:

* dev scores (see Table below)
* test scores (see Table below)
* iPython notebook write-up 
   * Make sure that you are not using any external data sources in your solution. You must only use the provided word vector file.
   * Make sure you have implemented retrofitting yourself.
   * Do **not** submit the retrofitted word vector file but you should provide a script that produces the retrofitted `.magnitude` word vectors used by your Baseline solution.
* Check if each group member has a `answer/README.username`.

Your F-score should be equal to or greater than the score listed for the corresponding marks.

| **Score(dev)** | **Score(test)** | **Marks** | **Grade** |
| 28 | 36   | 0   | F  |
| 30 | 37   | 55  | D  |
| 32 | 37.5 | 60  | C- |
| 33 | 38   | 65  | C  |
| 35 | 38.5 | 70  | C+ |
| 37 | 39   | 75  | B- |
| 38 | 39.5 | 80  | B  |
| 40 | 40   | 85  | B+ |
| 42 | 40.5 | 90  | A- |
| 48 | 41   | 95  | A  |
| 60 | 42   | 100 | A+ |
{: .table}

The score will be normalized to the marks on Coursys for the dev and test scores.

