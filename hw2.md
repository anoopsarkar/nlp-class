---
layout: default
img: word_vectors_small
img_link: https://nlp.stanford.edu/projects/glove/
caption: "Banded structures are visible in this visualization of word vectors"
title: "Homework | Lexical Substitution"
active_tab: homework
---

# Homework 2: Lexical Substitution

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
substitution for a target word in a sentence. For example, in the
following set of sentences the word **dry** can be replaced with
different words provided in the second column. Either `dull` or
`teetotal` or `parched` can be suitable replacements for the word
**dry** depending on the context.

| 16  | the problem is , aari seems to have no memory of their love other than a **dry** recitation as if he is reading a script of who he is supposed to be . | dull boring soulless uninteresting flat |
| 29  | she proved that in two years in illinois they had voted ninety-six towns **dry** , and that at that rate we would soon get over montana and have it dry . | alcohol_free teetotal | 
| 5   | if the mixture is too **dry** , add some water ; if it is too soft, add some flour . |  parched unmoistened desiccated stodgy |
{: .table}

The first column is the index of the target word (also shown in
bold-face in the examples above) which we need to substitute with
another word/phrase that is a suitable replacement in the context
of this sentence. In some cases the substitute provided by human
annotators for this dataset might be a phrase, e.g. `alcohol_free`
is a substitute for `dry` in the second example above.

This task is closely related to the task of identifying the different
_word senses_ of the target word. 

The dataset we will be using in this homework was collected by
asking humans to provide words (and sometimes phrases) as substitutes
for particular target words.  They were provided with the full
sentence so that they can choose the substitute word based on the
context.

The data we will be using for this homework is taken from the
following shared task data:

> [SemEval-2007 Task 10: English Lexical Substitution Task](https://www.aclweb.org/anthology/S07-1009/). Diana McCarthy, Roberto Navigli. 

The data and the evaluation have been modified to make it a simpler
task specifically for this homework. Your task will be to provide
10 guesses as to the appropriate substitute word and if any of the
10 guesses match the substitute word preferred by the human annotator
it will be considered correct. We will be using a simplified form
of the various evaluation scores provided in the above paper. Your
program  will be allowed 10 guesses and we check if any of them
match the set of words provided by the human annotators.

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

The default solution will look for the file `glove.6B.100d.magnitude`
in the data directory. 

You can either download the word vectors file from:

    http://magnitude.plasticity.ai/glove/medium/glove.6B.100d.magnitude

Or you can use the same file directly on CSIL from the following directory:

    /usr/shared/CMPT/classes/nlp-class/lexsub/glove.6B.100d.magnitude

Please do not copy over the file into your CSIL directory as it is
quite large and you can go over your disk quota. Instead modify
`default.py` to use the full path to the above file which is
accessible on the CSIL machines or use the command line option
for `default.py` to access the word vectors.

    python3 default.py -w /usr/shared/CMPT/classes/nlp-class/lexsub/glove.6B.100d.magnitude > output.txt

And then you can check the score on the dev output file called `output.txt` by running:

    python3 lexsub_check.py

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
    dev.out score: 27.8920
    test.out score: 36.0000

Implementing the Baseline method should give you an improved
accuracy on the dev set:

    $ python3 check.py
    dev.out score: 40.5167

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

Go to `Homework 2` on Coursys and do a group submission:

* Upload `output.zip` and `source.zip`
* Make sure you have documented your approach in `answer/lexsub.ipynb`.
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

| **Accuracy(dev)** | **Accuracy(test)** | **Marks** | **Grade** |
| 28 | 36 | 0   | F  |
| 30 | 37 | 55  | D  |
| 32 | 37.5 | 60  | C- |
| 33 | 38 | 65  | C  |
| 35 | 38.5 | 70  | C+ |
| 37 | 39 | 75  | B- |
| 38 | 39.5 | 80  | B  |
| 39 | 40 | 85  | B+ |
| 40 | 41 | 90  | A- |
| 45 | 43 | 95  | A  |
| 50 | 46 | 100 | A+ |
{: .table}

The score will be normalized to the marks on Coursys for the dev and test scores.

