---
layout: default
img: escherbabel
img_link: http://en.wikipedia.org/wiki/Tower_of_Babel_(M._C._Escher)
caption: "1928 woodcut by M. C. Escher showing the Tower of Babel."
title: "Project"
active_tab: project
---

# Final Project

<span class="text-info">Start by {{ site.hwdates[5].startdate }} or earlier</span> |
<span class="text-warning">Due on {{ site.hwdates[5].deadline }}</span>

## Project Ideas

First start with a task that has a well-defined dataset that you
can use for your project. Pick something you are passionate about
or something you find interesting.

A list of shared task datasets are provided below. In many cases
you can extend your homework code to produce innovative project
ideas for these tasks.

### Shared Task Collections

* [Torchtext](https://torchtext.readthedocs.io/en/latest/)
* [Sebastian Ruder's curated collection](https://github.com/sebastianruder/NLP-progress)
* [Kaggle NLP Tasks](https://www.kaggle.com/datasets?sortBy=hottest&group=public&page=1&pageSize=20&size=sizeAll&filetype=fileTypeAll&license=licenseAll&tagids=13204%2C11208%2C2107)

#### CoNLL Shared Tasks

* [CoNLL Shared Tasks](http://www.conll.org/previous-tasks)
* [CoNLL 2003 Named Entity Recognition Task](https://www.clips.uantwerpen.be/conll2003/ner/)
* [CoNLL 2000 Chunking Task](https://www.clips.uantwerpen.be/conll2000/chunking/)
* [CoNLL 2018 Multilingual Parsing](http://universaldependencies.org/conll18/)

#### SemEval Shared Tasks

* [SemEval 2018](http://alt.qcri.org/semeval2018/index.php?id=tasks)
* [SemEval 2017](http://alt.qcri.org/semeval2017/index.php?id=tasks)
* [SemEval 2016](http://alt.qcri.org/semeval2016/index.php?id=tasks)
* [SemEval 2015](http://alt.qcri.org/semeval2015/index.php?id=tasks)
* [SemEval 2014](http://alt.qcri.org/semeval2014/index.php?id=tasks)

### Classification Tasks

* [Toxic Comment Classification](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge)
* [Fake News Challenge](https://github.com/FakeNewsChallenge/fnc-10)
* [Spam / Click-bait detection](https://www.kaggle.com/therohk/examine-the-examiner)

### Information Extraction

* [Drug-Drug Interaction Extraction](https://github.com/zha204/ddi-corpus-database)
* [Web named entities](http://nlp.uned.es/weps/weps-3/data)
* [Twitter sequence prediction tasks](http://www.cs.cmu.edu/~ark/TweetNLP/)
* [WNUT Emerging and Rare entity recognition shared task](http://noisy-text.github.io/2017/emerging-rare-entities.html)
* [Gun violence text data](http://gun-violence.org)

### Parsing

* [Universal Dependencies](http://universaldependencies.org)
* [WikiText](https://www.salesforce.com/products/einstein/ai-research/the-wikitext-dependency-language-modeling-dataset/)
* [Opinion mining](https://ikernels-portal.disi.unitn.it/projects/sentube/)

### Machine Translation

* [WMT 2018 Shared Task](http://www.statmt.org/wmt18/)
* [WMT 2017 Shared Task](http://www.statmt.org/wmt17/)
* [WMT 2016 Shared Task](http://www.statmt.org/wmt16/)
* [WMT 2015 Shared Task](http://www.statmt.org/wmt15/)
* [NMT 2018 Neural MT Shared Task](https://sites.google.com/site/wnmt18/shared-task)
* [Web Inventory of Transcribed and Translated Talks](https://wit3.fbk.eu/mt.php?release=2016-01)

### Unlabeled Data for Clustering, Language Models, etc.

* [Wikipedia XML data](http://www-connex.lip6.fr/%7Edenoyer/wikipediaXML/)
* [Web data](http://corpus.leeds.ac.uk/internet.html)
* [BootCat](http://bootcat.dipintra.it)

### Sentiment and Opinion Mining

* [Stanford Sentiment Treebank](https://nlp.stanford.edu/sentiment/treebank.html)
* [Movie reviews](http://ai.stanford.edu/~amaas/data/sentiment/)
* [Yelp Challenge](https://www.yelp.com/dataset/challenge)
* [Sentiment and opinion mining datasets](https://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html)

### Natural Language Understanding and Inference

* [GLUE Benchmark](https://gluebenchmark.com)
* [RepEval 2017](https://repeval2017.github.io/shared/)
* [The Stanford Natural Language Inference (SNLI) Corpus](https://nlp.stanford.edu/projects/snli/)
* [Multi-Genre NLI](https://www.nyu.edu/projects/bowman/multinli/)
* [MedNLI](https://physionet.org/physiotools/mimic-code/mednli/)
* [XNLI](https://www.nyu.edu/projects/bowman/xnli/)

### Question Answering

* [Qanta shared task](https://sites.google.com/view/qanta/home) 
* [Algebra Question Answering with Rationales](https://github.com/deepmind/AQuA/)
* [Quora Question Pairs](https://www.kaggle.com/c/quora-question-pairs).
* Reverse QA: Jeopardy style QA. [json](https://drive.google.com/file/d/0BwT5wj_P7BKXb2hfM3d2RHU1ckE/view) and [csv](https://drive.google.com/file/d/0BwT5wj_P7BKXUl9tOUJWYzVvUjA/view)

## Project Submission

### Project proposal (due on {{ site.hwdates[5].proposal }})

For your project proposal please submit a text file in Markdown
format that includes a Title and an Abstract. Your abstract should
be about 250 words (please definitely use less than 1000 words).
Make sure the following points are in your abstract.

* Motivation 
    * which NLP task do you plan to do; 
    * which aspect of the problem / task did your group plan to work on (accuracy, interpretability, etc.); 
    * provide some reasons for your choice
* Approach 
    * Describe the algorithms and machine learning models you plan to use in your project. 
    * Using equations is not necessary but if you do, use a clear mathematical style to explain your model(s).
* Data
    * Exactly which data set do you plan to use
    * What is the evaluation measure for the data set and what is the baseline

### Poster Session

* Final Project Poster Session:
    * Time: {{ site.hwdates[5].deadline }} {{ site.hwdates[5].time }}. 
    * Location: {{ site.hwdates[5].location }}

#### Poster size

The poster size should be as follows:

* Landscape orientation: 3ft by 3ft.
* Portrait orientation: A0 portrait (4ft vertical by 3ft horizontal)

If you use LaTeX then here are two sample poster styles (A0 portrait):

* [LaTeX Portrait Poster Template](https://www.overleaf.com/latex/examples/latex-portrait-poster-template/gybjbztdkvyg)
* [Medical University of Vienna (MUW) Poster Template](https://www.overleaf.com/latex/templates/medical-university-of-vienna-muw-poster-template/xdgtytckkwzf)

#### Poster grading

The poster will be graded using the following criteria (1-5):

1. Goal is clear?
1. Implementation is clear?
1. Model was clear?
1. Did provided example make things clear?
1. Experimental evaluation was clear?
1. Adequate comparison to previous work?
1. Poster layout and oral explanation.
1. Analysis of the output.
1. Overall quality.

Please read through this set of [tutorial slides on making effective posters](assets/cached/makeup_ijcnlp_2017.pdf).

Also, I have provided [two](assets/cached/EMNLP2017_poster.pdf) [examples](assets/cached/IWSLT2015_poster.pdf) of NLP posters (note that they are not in portrait layout).

### Project Write-up

Apart from the poster session you must also submit your project
write-up as a Python notebook `project.ipynb` and your source
code for your project in your GitLab repository:

    git@csil-git1.cs.surrey.sfu.ca:USER/nlpclass-1187-g-GROUP.git

Put all your project files into the directory `project` in your
GitLab repository.

Make sure you have a `requirements.txt` file for your project 
so that we can use a virtual environment to run your code.

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
    * If you used homework code, which homework code you used in your project. Provide exactly which code was used in your project not written by your group (e.g. use of an aligner from an open-source project).
* Experimental Setup
    * Describe what kind of evaluation you are doing and which methods you are comparing against each other.
* Results 
    * Include a detailed comparison of different methods.
* Analysis of the Results
    * Did you improve over the baseline. Why or why not?
* Future Work
    * What could be fixed in your approach. What you did not have time to finish, but you think would be a useful addition to your project.

Please read this [guide to presenting your work](assets/cached/cs224u/cs224u-2019-presenting.pdf). Also available is a [video tutorial covering the same material](https://www.youtube.com/watch?v=WXLb4h2A724).

### Submit your project on Coursys

Go to [Coursys]({{ site.coursys }}). Under the `Final Project`
activity submit the following zip files:

* `output.zip`: output of your project implementation on a dataset. please include the evaluation code and references to allow us to check the evaluation you present in your write-up. Note this should only be your output on the test data file of some dataset plus any evaluation code and clear instructions on how to run the evaluation script.
* `source.zip`: this zip file should contain your iPython notebook that serves as the write-up for your project and only the source code you have written (along with a requirements.txt for a virtualenv). Do not include any data files in this zipfile. Please also include a README.username file as you have done for all your homeworks in this zip file.

The instructions for submission and development are provided in more detail in [Homework 0](hw0.html).

There are **no grace days** for project submission! So submit early and often.

That's it. You are done with your Final Project!

## Grading of Final Project Work

The final projects for this course will be graded using the following criteria:

* Originality 
* Substance (amount of work done for the project)
* Well documented use of prior results from research papers
* Clarity of the writing
* Quality of experimental design
* Quality of evaluation and results
* Theoretical insights / Practical insights
* Group work (did the group work effectively together)
* Overall score (based on the above criteria, but can include other factors like overall polish or creativity)

## Project Grading Framework

The total marks are distributed as follows:

* Work. Work done in the project. Results obtained. 50 marks (see the section on _Grading of the Final Project Work_ for grading details)
* Docs. Documentation of the work done in the notebook. 25 marks (see the section on _Project Write-up_ for grading details)
* Poster. Performance at the poster session and poster quality. 25 marks (see the section on _Poster grading_ for grading details)

