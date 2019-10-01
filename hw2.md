---
layout: default
img: word_vectors_small
img_link: https://nlp.stanford.edu/projects/glove/
caption: Banded structures are visible in this visualization of word vectors
title: "Homework | Lexical Substitution using Word Vectors"
active_tab: homework
---

# Homework 2: Lexical Substitution using Word Vectors

<span class="text-info">Start on {{ site.hwdates[2].startdate }}</span> |
<span class="text-warning">Due on {{ site.hwdates[2].deadline }}</span>

## Getting Started

If you have already cloned my homework repository `nlp-class-hw` for
Homework 0 then go into that directory and update the directory:

    git pull origin/master
    cd nlp-class-hw/lexsub

If you don't have that directory anymore then simply clone the
repository again:

    git clone https://github.com/anoopsarkar/nlp-class-hw.git

Clone your own repository from GitLab if you haven’t done it already:

    git clone git@csil-git1.cs.surrey.sfu.ca:USER/nlpclass-{{ site.semcode }}-g-GROUP.git

Note that the `USER` above is the SFU username of the person in
your group that set up the GitLab repository.

Then copy over the contents of the `lexsub` directory into your
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

In this homework we will be exploring the task of finding a suitable
substitution for a target word in a sentence. For example, in the following
set of sentences the word **dry** can be replaced with different words
provided in the second column. Either _evaporate_, or _arid_ or _dry_
can be suitable replacements for the word **dry** depending on the
sentential context. 

| clinical trials burn money fast , putting companies in a precarious position if they do n't get definitive results before their bank accounts run **dry** | evaporate |
| surprisingly in such a **dry** continent as australia , salt becomes a problem when there is too much water . | arid |
| for people who knew him , it was typical of his **dry** humor , but some in the audience thought he was tipsy . | wry |
{: .table}

In some cases a phrase might have to be replaced,
e.g. _run dry_ has to be replaced with _evaporate_ in the first
example above.

This task is closely related to the task of identifying the different
_word senses_ of the target word. 

The dataset we will be using in this homework was collected by asking
humans to provide words as substitutes for particular target words.
They were provided with the full sentence so that they can choose
the substitute word based on the context.

The data we will be using for this homework is taken from the
following shared task data:

> [SemEval-2007 Task 10: English Lexical Substitution Task](https://www.aclweb.org/anthology/S07-1009/). Diana McCarthy, Roberto Navigli. 

The data and the evaluation have been modified to make it a simpler
task specifically for this homework. Your task will be to provide
10 guesses as to the appropriate substitute word and if any of the
10 guesses match the substitute word preferred by the human annotator
it will be considered correct. We will be using a simplified form
of the `oot` modal evaluation score from the above paper where 10
guesses are allowed without any penalty and scored against the human
preferred lexical substitution.

This homework will explore the use of word vectors aka word
embeddings for this task. We will be using a pre-trained collection
of word vectors that has been trained on a large corpus of text
data.

## Default solution

The default solution is provided in `default.py`. To use the default
as your solution:

    cp default.py answer/lexsub.py
    cp default.ipynb answer/lexsub.ipynb
    python3 zipout.py
    python3 check.py

Make sure that the command line options are kept as they are in
`default.py`. You can add to them but you must not delete any
command line options that exist in `default.py`.

Submitting the default solution without modification will get you
zero marks.

The default solution produces 10 candidates for each lexical
substitution and if any of them match the substitute word
preferred by a group of human annotators then that substitution
is marked as correct.

The overall score reported is the Accuracy score over the
entire data set.

Your solution should also produce 10 guesses for each lexical
substitution.

## The Challenge

Your task is to _improve the Accuracy as much as possible_ which is explained
in detail in the Accuracy section below. You must use the pre-trained
word vector file that has been provided to you. You can either
download this file from:

    http://magnitude.plasticity.ai/glove/medium/glove.6B.100d.magnitude

Or you can use the same file directly on CSIL from the following directory:

    /usr/shared/CMPT/classes/nlp-class/lexsub/glove.6B.100d.magnitude

## Data files

The data files provided are:

* `data/input` -- input files `dev.txt` and `test.txt`
* `data/reference/dev.out` -- the reference output for the `dev.txt` input file

In addition you must use the pre-trained word vectors from `glove.6B.100d.magnitude`.

## Baseline 

The baseline method is what you should implement first before you
explore additional improvements to improve the Accuracy.

First, we will implement _retrofitting_ to combine the information
about word senses from Wordnet in order to modify the default word vectors.

But the sky's the limit! You are welcome to design your own model, as long 
as you have implemented the Baseline model first.

## Required files

You must create the following files:

* `answer/lexsub.py` -- this is your solution to the homework. start by copying `default.py` as explained below.
* `answer/lexsub.ipynb` -- this is the iPython notebook that will be your write-up for the homework.

## Run your solution on the data files

To create the `output.zip` file for upload to Coursys do:

    python3 zipout.py

For more options:

    python3 zipout.py -h

## Check your accuracy

To check your accuracy on the dev set:

    python3 check.py

The output score is the accuracy of picking the right substitute word
for each word in context as selected by a group of human annotators.
Your program is provided 10 guesses to get the right substitute word.
The guesses are not assumed to be ordered by any score. The
output is considered correct so long as the word chosen by the
annotators exists in the set of 10 guesses.

For more options:

    python3 check.py -h

In particular use the log file to check your output evaluation:

    python3 check.py -l log

The accuracy on `data/input/test.txt` will not be shown.  We will
evaluate your output on the test input after the submission deadline.

The default solution gets a very poor F-score on the dev and test set:

    $ python3 check.py
    dev.out score: 17.79
    test.out score: 24.00

Implementing a greedy search gets an F-score of 0.66 on dev
while the Baseline method with unigram counts gets 0.89 on
the dev set.

Implementing the Baseline method should give you an improved
accuracy on the dev set:

    $ python3 check.py
    dev.out score: 27.01
    test.out score: 33.00

By careful analysis of the output (even without any knowledge of
the Chinese language) should give you some further ideas to consolidate
certain types of characters into words based on regularity how they
combine into words in the training set.

## Submit your homework on Coursys

Once you are done with your homework submit all the relevant materials
to Coursys for evaluation.

### Create output.zip

Once you have a working solution in `answer/lexsub.py` create
the `output.zip` for upload to Coursys using:

    python3 zipout.py

### Create source.zip

To create the `source.zip` file for upload to Coursys do:

    python3 zipsrc.py

You must have the following files or `zipsrc.py` will complain about it:

* `answer/lexsub.py` -- this is your solution to the homework. start by copying `default.py` as explained below.
* `answer/lexsub.ipynb` -- this is the iPython notebook that will be your write-up for the homework.

In addition, each group member should write down a short description of what they
did for this homework in `answer/README.username`.

### Upload to Coursys

Go to `Homework 1` on Coursys and do a group submission:

* Upload `output.zip` and `source.zip`
* Make sure you have documented your approach in `answer/lexsub.ipynb`.
* Make sure each member of your group has documented their contribution to this homework in `answer/README.username` where `username` is your CSIL/GitLab username.

## Grading

The grading is split up into the following components:

* dev scores (see Table below)
* test scores (see Table below)
* iPython notebook write-up 
   * Make sure that iterative search algorithm is implemented as described in the Baseline section above
* Check if each group member has a `answer/README.username`.

Your F-score should be equal to or greater than the score listed for the corresponding marks.

| **Accuracy(dev)** | **Accuracy(test)** | **Marks** | **Grade** |
| 17.7 | 24 | 0   | F  |
| 18 | 25 | 55  | D  |
| 19 | 26 | 60  | C- |
| 20 | 27 | 65  | C  |
| 21 | 28 | 70  | C+ |
| 22 | 29 | 75  | B- |
| 23 | 30 | 80  | B  |
| 25 | 31 | 85  | B+ |
| 27 | 33 | 90  | A- |
| 30 | 35 | 95  | A  |
| 35 | 37 | 100 | A+ |
{: .table}


The score will be normalized to the marks on Coursys for the dev and test scores.

