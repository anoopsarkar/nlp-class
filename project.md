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

## Poster Session

There will be a poster session in downtown Vancouver on {{
site.hwdates[5].deadline }}. Your group must present a poster at
this poster session providing details about your final course
project.

If you are enrolled in the Machine Learning course you must present
a different poster. You can share code between the projects but the
projects must be different from each other and have a distinct
contribution.

Apart from the poster session you must also submit your project
write-up as a Python notebook `project.ipynb` and your source
code for your project in your GitLab repository:

    git@csil-git1.cs.surrey.sfu.ca:USER/nlpclass-1187-g-GROUP.git

Make sure you have a `requirements.txt` file for your project 
so that we can use a virtual environment to run your code.

## Project Ideas

First start with a task that has a well-defined dataset that you
can use for your project. Pick something you are passionate about
or something you find interesting.

A list of shared task datasets are provided below. In many cases
you can extend your homework code to produce innovative project
ideas for these tasks.

### Information Extraction

* [Drug-Drug Interaction Extraction](http://labda.inf.uc3m.es/DrugDDI/DrugDDI.html)
* [Web named entities](http://nlp.uned.es/weps/weps-3/data)
* [Twitter sequence prediction tasks](http://www.cs.cmu.edu/~ark/TweetNLP/)

### Parsing

* [Universal Dependencies](http://universaldependencies.org)
* [WikiText](https://www.salesforce.com/products/einstein/ai-research/the-wikitext-dependency-language-modeling-dataset/)

### Machine Translation

* [WMT 2018 Shared Task](http://www.statmt.org/wmt18/)
* [WMT 2017 Shared Task](http://www.statmt.org/wmt17/)
* [WMT 2016 Shared Task](http://www.statmt.org/wmt16/)
* [WMT 2015 Shared Task](http://www.statmt.org/wmt15/)
* [NMT 2018 Neural MT Shared Task](https://sites.google.com/site/wnmt18/shared-task)
* [Web Inventory of Transcribed and Translated Talks](https://wit3.fbk.eu/mt.php?release=2016-01)

### Unlabeled Data for Clustering, Language Models, etc.

* [Wikipedia XML data](http://www-connex.lip6.fr/%7Edenoyer/wikipediaXML/)

### Sentiment

* [Stanford Sentiment Treebank](https://nlp.stanford.edu/sentiment/treebank.html)
* [Movie reviews](http://ai.stanford.edu/~amaas/data/sentiment/)
* [Yelp Challenge](https://www.yelp.com/dataset/challenge)

### Natural Language Inference (Entailment Tasks)

* [RepEval 2017](https://repeval2017.github.io/shared/)
* [The Stanford Natural Language Inference (SNLI) Corpus](https://nlp.stanford.edu/projects/snli/)
* [Multi-Genre NLI](https://www.nyu.edu/projects/bowman/multinli/)
* [MedNLI](https://physionet.org/physiotools/mimic-code/mednli/)
* [XNLI](https://www.nyu.edu/projects/bowman/xnli/)
* [Fake News Challenge](https://github.com/FakeNewsChallenge/fnc-10)

### Question Answering

* [Algebra Question Answering with Rationales](https://github.com/deepmind/AQuA/)

### CoNLL Shared Tasks

* [CoNLL Shared Tasks](http://www.conll.org/previous-tasks)
* [CoNLL 2003 Named Entity Recognition Task](https://www.clips.uantwerpen.be/conll2003/ner/)
* [CoNLL 2000 Chunking Task](https://www.clips.uantwerpen.be/conll2000/chunking/)
* [CoNLL 2018 Multilingual Parsing](http://universaldependencies.org/conll18/)

### SemEval Shared Tasks

* [SemEval 2018](http://alt.qcri.org/semeval2018/index.php?id=tasks)
* [SemEval 2017](http://alt.qcri.org/semeval2017/index.php?id=tasks)
* [SemEval 2016](http://alt.qcri.org/semeval2016/index.php?id=tasks)
* [SemEval 2015](http://alt.qcri.org/semeval2015/index.php?id=tasks)
* [SemEval 2014](http://alt.qcri.org/semeval2014/index.php?id=tasks)

### Kaggle Tasks

* [Kaggle NLP Tasks](https://www.kaggle.com/datasets?sortBy=hottest&group=public&page=1&pageSize=20&size=sizeAll&filetype=fileTypeAll&license=licenseAll&tagids=13204%2C11208%2C2107)
* [Quora Question Pairs](https://www.kaggle.com/c/quora-question-pairs)
* [Toxic Comment Classification](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge)

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

