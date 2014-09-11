---
layout: default
img: mayhem
img_url: http://en.wikipedia.org/wiki/Text_segmentation
caption: Segmentation is harder than it seems.
title: Homework 1 | Segmentation
active_tab: homework
---

Word Segmentation <span class="text-muted">Homework 1</span>
=============================================================

Word segmentation is the task of restoring missing word
boundaries. For example, in some cases word boundaries
are lost as in web page URLs like _choosespain.com_ which
could be either _chooses pain_ or _choose spain_ and you 
might visit such an URL looking for one or the other.

This homework is on Chinese word segmentation, a language
in which word boundaries are not usually provided. For
instance here is an example Chinese sentence without word
boundaries:

    北京大学生比赛

This can be segmented a few different ways and one segmentation
leads to a particular meaning (indicated by the English translation below):

    北京 大学生 比赛
    Beijing student competition

A different segmentation leads to a different meaning:

    北京大学 生 比赛
    Peking University Health Competition

We will be using _training data_ collected from Chinese
sentences that have been segmented by human experts.
We will run the word segmentation program that you
will write for this homework on _test data_ that will
be automatically evaluated against a reference
segmentation.

Getting Started
---------------

You must have git and python (2.7) on your system to run the assignments.
Once you've confirmed this, run this command:

    git clone https://github.com/anoopsarkar/nlp-class-hw.git

In the `segmenter` directory you will find a python program called
`baseline.py`, which contains a complete but very simple segmentation algorithm.
It simply inserts word boundaries between each Chinese character in the
input. It is a terrible segmenter but it does read the input and produce
a valid output that can be scored.

You can see how well `baseline.py` does by running the following:

    python baseline.py | python score-segments.py

Alternatively, you can run:

    python baseline.py > output
    python score-segments.py -t output

The score reported is [F-measure](http://en.wikipedia.org/wiki/F1_score) which combines 
[precision and recall](http://en.wikipedia.org/wiki/Precision_and_recall) into a single score.

The Challenge
-------------

Your task is to _improve the F-measure as much as possible_. To help you do
this the `data` directory in `segmenter` contains two files:

    count_1w.txt : unigram counts of Chinese words
    count_2w.txt : bigram counts of Chinese word pairs

Developing a simple segmenter that uses unigram probabilities is
enough to beat the baseline system. But getting closer to the oracle
score will be an interesting challenge. To get full credit you
**must** experiment with at least one additional model of your
choice and document your work. Here are some ideas:

* Use the bigram model to score word segmentation candidates.
* Do better _smoothing_ of the unigram and bigram probability models.

But the sky's the limit! You are welcome to design your own model, as long 
as you follow the ground rules:

Ground Rules
------------

* Each group should submit using one person as the designated uploader.
* You must turn in three things:
  1. A segmentation of the entire dataset which is in `segmenter/input` uploaded to the [leaderboard submission site](http://sfu-nlp-class.appspot.com) according to <a href="hw0.html">the Homework 0 instructions</a>. You can upload new output as often
     as you like, up until the assignment deadline. Do _not_ press Submit unless you are finished with your development. 
The output will be evaluated using a secret metric, but the `score-segments.py` program will give you a good
     idea of how well you're doing.
  1. Your code. Each group should assign one member to upload the source code to [Coursys](https://courses.cs.sfu.ca) as the submission for Homework 1. The code should be self-contained, self-documenting, and easy to use. It should use the same input and output assumptions of `baseline.py`.
  1. A clear, mathematical description of your algorithm and its motivation
     written in scientific style. This needn't be long, but it should be
     clear enough that one of your fellow students could re-implement it 
     exactly. 
* You cannot use data or code resources outside of what is provided
to you. You can use NLTK but not the NLTK tokenizer class. You can
use plain ASCII but for math equations it is better to use either
[latex](http://www.latex-project.org/) or [kramdown](https://github.com/gettalong/kramdown).
Do __not__ use any proprietary or binary file formats such as Microsoft Word.

If you have any questions or you're confused about anything, just ask.

