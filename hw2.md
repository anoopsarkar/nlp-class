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


Getting Started
---------------

You must have git and python (2.7) on your system to run the assignments.
Once you've confirmed this, run this command:

    git clone https://github.com/anoopsarkar/nlp-class-hw.git

The score reported is [F-measure](http://en.wikipedia.org/wiki/F1_score) which combines 
[precision and recall](http://en.wikipedia.org/wiki/Precision_and_recall) into a single score.

The Challenge
-------------

### The Baseline

#### Algorithm: Iterative segmenter

---
**## Data Structures ##**

`input`
: the input sequence of characters

---

### Your Task

Ground Rules
------------

* Each group should submit using one person as the designated uploader.
* You must turn in three things:
  1. Output of the test dataset which is in `chunker/data/input` uploaded to the [leaderboard submission site](http://sfu-nlp-class.appspot.com) according to [the Homework 0 instructions](hw0.html). You can upload new output as often
     as you like, up until the assignment deadline. The Submit button for showing the test set scores will be unavailable until after the homework deadline and grace days have passed.
The output will be evaluated using a secret metric, but the `score-segments.py` program will give you a good
     idea of how well you're doing.
  1. Your code. Each group should assign one member to upload the source code to [Coursys](https://courses.cs.sfu.ca) as the submission for Homework 1. The code should be self-contained, self-documenting, and easy to use. It should use the same input and output assumptions of `default.py`.
  1. A clear, mathematical description of your algorithm and its motivation
     written in scientific style. This needn't be long, but it should be
     clear enough that one of your fellow students could re-implement it 
     exactly. Include the file for this writeup as part of the tarball or zip file you
     will upload to [Coursys](https://courses.cs.sfu.ca).
* You cannot use data or code resources outside of what is provided
to you. You can use NLTK but not the NLTK tokenizer class. 
* For the written description of your algorithm, you can use plain ASCII but
for math equations it is better to use either
[latex](http://www.latex-project.org/) or
[kramdown](https://github.com/gettalong/kramdown).  Do __not__ use
any proprietary or binary file formats such as Microsoft Word.

If you have any questions or you're confused about anything, just ask.

