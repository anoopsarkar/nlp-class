---
layout: default
img: escherbabel
img_link: http://en.wikipedia.org/wiki/Tower_of_Babel_(M._C._Escher)
caption: "1928 woodcut by M. C. Escher showing the Tower of Babel."
title: "Project"
active_tab: project
---

Final Project
-------------

<span class="text-info">Start by {{ site.hwdates[5].startdate }} or earlier</span> |
<span class="text-warning">Due on {{ site.hwdates[5].deadline }}</span>

There will be a poster session in downtown Vancouver on {{
site.hwdates[5].deadline }}. Your group must present a poster at
this poster session providing details about your final course
project.

If you are enrolled in the Machine Learning course you must present
a different poster. You can share code between the projects but the
projects must be different from each other and have a distinct
contribution.

## Ideas

First start with a task that has a well-defined dataset that you
can use for your project. Pick something you are passionate about
or something you find interesting.

A list of shared task datasets are provided below. In many cases
you can extend your homework code to produce innovative project
ideas for these tasks.

### Information Extraction

* [Drug-Drug Interaction Extraction](http://labda.inf.uc3m.es/DrugDDI/DrugDDI.html)
* [Web named entities](http://nlp.uned.es/weps/weps-3/data)

### Noisy user-generated text

* [Twitter sequence prediction tasks](http://www.cs.cmu.edu/~ark/TweetNLP/)

### Unlabeled Data for Clustering, Language Models, etc.

* [Wikipedia XML data](http://www-connex.lip6.fr/%7Edenoyer/wikipediaXML/)

### SemEval Shared Tasks

* [SemEval 2018](http://alt.qcri.org/semeval2018/index.php?id=tasks)

### Sentiment

* [Stanford Sentiment Treebank](https://nlp.stanford.edu/sentiment/treebank.html)

### Natural Language Inference (Entailment Tasks)

* [RepEval 2017](https://repeval2017.github.io/shared/)
* [The Stanford Natural Language Inference (SNLI) Corpus](https://nlp.stanford.edu/projects/snli/)
* [Multi-Genre NLI](https://www.nyu.edu/projects/bowman/multinli/)
* [MedNLI](https://physionet.org/physiotools/mimic-code/mednli/)
* [XNLI](https://www.nyu.edu/projects/bowman/xnli/)

### Question Answering

* [Algebra Question Answering with Rationales](https://github.com/deepmind/AQuA/)

## Write-up

Your Python notebook must be called `project.ipynb`. In addition
to writing code for a good project submission, the description of
what you did for your project in your Python notebook is also a
very important part of your project submission. It **must** have
the following sections:

* Motivation 
    * Which aspect of the problem / task did your group choose to improve and reasons for your choice.
* Approach 
    * Describe the algorithms and machine learning models used in your project. Use a clear mathematical style to explain your model(s).
* Data 
    * Exactly which data files were used; also include here any external data that was not provided to you.
* Code
    * Describe which homework code you used in your project. Provide exactly which code was used in your project not written by your group (e.g. use of an aligner from an open-source project).
* Experimental Setup
    * Describe what kind of evaluation you are doing and which methods you are comparing against each other.
* Results 
    * Include a detailed comparison of different methods.
* Analysis of the Results
    * Did you improve over the baseline. Why or why not?
* Future Work
    * What could be fixed in your approach. What you did not have time to finish, but you think would be a useful addition to your project.

## Grading system for the project

The final projects will be graded using the following criteria:

* Originality 
* Substance (amount of work done for the project)
* Well documented use of prior results from research papers
* Clarity of the writing
* Quality of experimental design
* Quality of evaluation and results
* Theoretical insights / Practical insights
* Overall score (based on the above criteria, but can include other factors like polish of the project work)

