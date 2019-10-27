---
layout: default
img: bratconll2k
img_link: "http://weaver.nlplab.org/~brat/demo/latest/#/not-editable/CoNLL-00-Chunking/train.txt-doc-1"
caption: Explore phrasal chunking interactively using Brat
title: Homework 3 | Robust Phrasal Chunking
active_tab: homework
---

# Homework 3: Robust Phrasal Chunking

<span class="text-info">Start on {{ site.hwdates[3].startdate }}</span> |
<span class="text-warning">Due on {{ site.hwdates[3].deadline }}</span>

## Getting Started

If you have already cloned my homework repository `nlp-class-hw` for
previous homeworks then go into that directory and update the directory:

    git pull origin/master
    cd nlp-class-hw/chunker

If you don't have that directory anymore then simply clone the
repository again:

    git clone https://github.com/anoopsarkar/nlp-class-hw.git

Clone your own repository from GitLab if you haven’t done it already:

    git clone git@csil-git1.cs.surrey.sfu.ca:USER/nlpclass-{{ site.semcode }}-g-GROUP.git

Note that the `USER` above is the SFU username of the person in
your group that set up the GitLab repository.

Then copy over the contents of the `chunker` directory into your
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

## Data set

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

There is a helpful program `count_sentences.py` which allows you
to count how many sentences are in a CoNLL formatted file.

For this homework the training data has been preprocessed and singleton
tokens have been replaced with the `[UNK]` token (which stands for unknown
word). In the dev and test data any unseen words will be replaced with
the `[UNK]` token.

This homework is not just about phrasal chunking but **robust**
phrasal chunking. The input data in dev and test files have been
infected with noise so the input to your chunker will look like
this:

    Rqckwell NNP
    , ,
    based VBN
    in IN
    El NNP
    Segundo NNP
    , ,
    Calief. NNP
    , ,
    is VBZ
    an DT
    aerospace NN
    , ,
    electronics NNS
    , ,
    automotive JJ
    and CC
    graphics NNS
    concern VBP
    . .

As you see the words have been infected with noise so
that it contains several spelling mistakes, e.g. `Rockwell` 
is now `Rqckwell`. The training data is clean and any
model trained on the training data will treat these 
noisy words as unknown words.

The input files do not have the output chunk labels
which appear in `data/reference/dev.out` for input `data/input/dev.txt`.

## Data files

The data files provided are:

* `data/train.txt.gz` -- the training data used to train the `default.py` model
* `data/input` -- input files `dev.txt` and `test.txt` infected with noise
* `data/reference/dev.out` -- the reference output for the `dev.txt` input file

## Default solution

The default solution is provided in `default.py`. To use the default
as your solution:

    cp default.py answer/chunker.py
    cp default.ipynb answer/chunker.ipynb
    python3 zipout.py
    python3 check.py

The default solution will look for the file `chunker.tar`
in the data directory. If it does not find this file it
will start training on the `data/train.txt.gz` file. This
will take about 15-20 minutes.

You can either download the `chunker.tar` model file from:

    https://drive.google.com/drive/folders/1LaY1cczbLD1laiJqce7-htM6JCqph61e?usp=sharing

Or you can use the same file directly on CSIL from the following directory:

    /usr/shared/CMPT/courses/nlp-class/chunker/chunker.tar

Please do not copy over the file into your CSIL directory as it is
moderately large and you can go over your disk quota. Instead modify
`default.py` to use the full path to the above file which is
accessible on the CSIL machines or use the command line option
for `default.py` to access the word vectors.

    python3 default.py -m /usr/shared/CMPT/courses/nlp-class/chunker/chunker > output.txt

Note that the suffix `.tar` should **not** be added to the model file.

If you have a `chunker.tar` in the `data` directory then you can simply run:

    python3 default.py > output.txt

And then you can check the score on the dev output file called `output.txt` by running:

    python3 conlleval.py -o output.txt

which produces the following detailed evaluation:

    processed 23663 tokens with 11896 phrases; found: 11672 phrases; correct: 8568.
    accuracy:  84.35%; (non-O)
    accuracy:  85.65%; precision:  73.41%; recall:  72.02%; FB1:  72.71
                 ADJP: precision:  36.49%; recall:  11.95%; FB1:  18.00  74
                 ADVP: precision:  71.36%; recall:  39.45%; FB1:  50.81  220
                CONJP: precision:   0.00%; recall:   0.00%; FB1:   0.00  0
                 INTJ: precision:   0.00%; recall:   0.00%; FB1:   0.00  0
                   NP: precision:  70.33%; recall:  76.80%; FB1:  73.42  6811
                   PP: precision:  92.40%; recall:  87.14%; FB1:  89.69  2302
                  PRT: precision:  65.00%; recall:  57.78%; FB1:  61.18  40
                 SBAR: precision:  84.62%; recall:  41.77%; FB1:  55.93  117
                   VP: precision:  63.66%; recall:  58.25%; FB1:  60.83  2108
    (73.40644276901988, 72.02420981842637, 72.70875763747455)

For this homework we will be scoring your solution based on the FB1 score
which is described in detail in the Accuracy section below.

Make sure that the command line options are kept as they are in
`default.py`. You can add to them but you must not delete any
command line options that exist in `default.py`.

Submitting the default solution without modification will get you
zero marks.

### The default model

The model used in `default.py` is a very simple recurrent neural
network used to predict the phrasal chunking tags. The model
structure can be examined using the following code, assuming
that you are in the `nlp-class-hw/chunker` directory or if
you have the `data` directory in your current directory
with the training data and the model file:

    from default import *
    import os
    chunker = LSTMTagger(os.path.join('data', 'train.txt.gz'), os.path.join('data', 'chunker'), '.tar')
    print(chunker.model)

This prints out the model:

    LSTMTaggerModel(
      (word_embeddings): Embedding(9675, 128)
      (lstm): LSTM(128, 64)
      (hidden2tag): Linear(in_features=64, out_features=22, bias=True)
    )

The input is a learned word embeddings of dimension 128 for the
vocabulary of size 9675 extracted from the training data. Note that
the model learns these embeddings to minimize the loss on the phrasal
chunking task rather than using pre-trained embeddings. The 128
dimensional vector is provided as input to a recurrent neural network
(an LSTM in this case) which has 64 neurons as the representation
at each index of the input sentence. At each time step this vector
of size 64 is given to a linear classifier which produces one of
22 output phrasal chunking tags.

Optimizing the above parameters to find the minimum loss on the
training data by gradient descent is done automatically using Pytorch
API calls.

### Hyperparameters

For this homework we will enforce that all the hyperparameters
used in the default solution (such as embedding dimension, hidden layer dimension, training epochs)
must be kept fixed. You should not change them in your solution.

## The Challenge

Your task is to _improve the accuracy as much as possible while
keeping the hyperparameters used in the default solution for the
phrasal chunker_. The score is explained in detail in the Accuracy
section below.

## Baseline 

The baseline method is what you should implement first before you
explore additional improvements to improve your score.

First, we will implement a semi-character RNN to deal with noisy
input. 

> [Robsut Wrod Reocginiton via semi-Character Recurrent Neural Network](https://arxiv.org/abs/1608.02214). Keisuke Sakaguchi, Kevin Duh, Matt Post, Benjamin Van Durme. AAAI 2017

and also see:

> [Combating Adversarial Misspellings with Robust Word Recognition](https://www.aclweb.org/anthology/P19-1561/). Danish Pruthi, Bhuwan Dhingra, Zachary C. Lipton. ACL 2019.


## Required files

You must create the following files:

* `answer/chunker.py` -- this is your solution to the homework. start by copying `default.py` as explained below.
* `answer/chunker.ipynb` -- this is the iPython notebook that will be your write-up for the homework.

## Run your solution on the data files

To create the `output.zip` file for upload to Coursys do:

    python3 zipout.py

For more options:

    python3 zipout.py -h

## Check your accuracy

To check your accuracy on the dev set:

    python3 check.py

The output score is the $F_{\beta=1}$ score or [FB1 score](https://en.wikipedia.org/wiki/F1_score)
which is the harmonic mean of the precision and recall
computed over all the output phrasal chunks.

    python3 check.py -h

In particular use the log file to check your output evaluation:

    python3 check.py -l log

The accuracy on `data/input/test.txt` will not be shown.  We will
evaluate your output on the test input after the submission deadline.

## Submit your homework on Coursys

Once you are done with your homework submit all the relevant materials
to Coursys for evaluation.

### Create output.zip

Once you have a working solution in `answer/chunker.py` create
the `output.zip` for upload to Coursys using:

    python3 zipout.py

### Create source.zip

To create the `source.zip` file for upload to Coursys do:

    python3 zipsrc.py

You must have the following files or `zipsrc.py` will complain about it:

* `answer/chunker.py` -- this is your solution to the homework. start by copying `default.py` as explained below.
* `answer/chunker.ipynb` -- this is the iPython notebook that will be your write-up for the homework.

In addition, each group member should write down a short description of what they
did for this homework in `answer/README.username`.

### Upload to Coursys

Go to `Homework 3` on Coursys and do a group submission:

* Upload `output.zip` and `source.zip`
* Make sure your `source.zip` matches your Gitlab repository.
* Make sure you have documented your approach in `answer/chunker.ipynb`.
* Make sure each member of your group has documented their contribution to this homework in `answer/README.username` where `username` is your CSIL/GitLab username.

## Grading

The grading is split up into the following components:

* dev scores (see Table below)
* test scores (see Table below)
* iPython notebook write-up 
   * Make sure that you are not using any external data sources in your solution. You must only use the provided word vector file.
   * Make sure you have implemented the semi-character RNN model yourself.
   * Do **not** change the hyperparameters for the phrasal chunker in `default.py` in the solution to the robust chunking problem.
* Check if each group member has a `answer/README.username`.

Your F-score should be equal to or greater than the score listed for the corresponding marks.

| **Score(dev)** | **Score(test)** | **Marks** | **Grade** |
| 72   | 65   | 0   | F  |
| 72.7 | 65.2 | 55  | D  |
| 73   | 65.5 | 60  | C- |
| 73.2 | 66   | 65  | C  |
| 73.5 | 66.5 | 70  | C+ |
| 73.7 | 67   | 75  | B- |
| 74   | 67.2 | 80  | B  |
| 74.5 | 67.5 | 85  | B+ |
| 75   | 67.7 | 90  | A- |
| 75.5 | 68   | 95  | A  |
| 75.7 | 70   | 100 | A+ |
{: .table}

The score will be normalized to the marks on Coursys for the dev and test scores.
