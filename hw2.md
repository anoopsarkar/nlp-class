---
layout: default
img: voynich
img_link: "http://en.wikipedia.org/wiki/Voynich_manuscript"
caption: "The Voynich manuscript"
title: Homework 2 | Decipherment
active_tab: homework
---

# Homework 2: Decipherment

<span class="text-info">Start by {{ site.hwdates[2].startdate }} or earlier</span> |
<span class="text-warning">Due on {{ site.hwdates[2].deadline }}</span>

Get started:

    git clone https://github.com/anoopsarkar/nlp-class-hw.git
    cd nlp-class-hw/decipher

Clone your repository if you haven’t done it already:

    git clone git@csil-git1.cs.surrey.sfu.ca:USER/nlpclass-1187-g-GROUP.git

Then copy over the contents of the `decipher` directory above as `hw2` in your repository.

Set up the virtual environment:

    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt

Note that if you do not change the requirements then after you have
set up the virtual environment `venv` you can simply run the following
command to get started with your development for the homework:

    source venv/bin/activate

## Background

## The Data

## The Challenge

### Default Submission

### The Baseline

### Your Task

You have to document your development of your grammars in your
Python notebook called `decipher.ipynb` in your submission.

Before you submit your homework add a file `doc/README.username`
that documents the work done by each `username` in your group. Group
members can get zero marks if they do not have this file that shows
that they worked on the homework equally with other group members.
Put any instructions to the TA and instructor in `doc/README.txt`
or `doc/README.md`.

### Submit your homework on Coursys

When you are ready to submit go to GitLab and select `New tag` to
create a new tag. For `Tag name` use `hw2` and optionally write a
`Message`. Then select `Create tag` to create this tag.

Go to [Coursys]({{ site.coursys }}). Under the `Homework 1`
activity submit your git repository URL. It will look like
this for some `USER` in your group called `g-GROUP`:

    git@csil-git1.cs.surrey.sfu.ca:USER/nlpclass-1187-g-GROUP.git

The instructions are provided in more detail in [Homework 0](hw0.html).

That's it. You are done with Homework 1!

### Grading

Your submission will be graded using the following
grading scheme:

## Acknowledgements

Thanks to Nishant Kambhatla for curating some of the data and the
source code for this homework.
