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

The final project is to translate from Chinese to English using the
machine translation system you have built over the course of the
semester. You should use the code you have written for your homework
assignments to build the translation system.

### Data Files

**Warning: do not redistribute this data. SFU has a license to use this data from the Linguistic Data Consortium (LDC) but we cannot take this data and give it to others.**

The data files are available on CSIL Linux machines in the following directory:

    /usr/shared/CMPT/nlp-class/project

Important information about the license is given in the file `LICENSE`.

#### Training data

The training data is taken from the following sources:

* [Hong Kong Parliament parallel corpus](https://catalog.ldc.upenn.edu/LDC2004T08) 
* [GALE Phase-1 Chinese newsgroup data](https://catalog.ldc.upenn.edu/LDC2009T15).

Training data comes in different sizes. The data files in each of the
large, medium, and small folders are:

* `train.cn`: segmented Chinese corpus
* `train.cn.unseg`: un-segmented Chinese corpus
* `train.en`: lower-cased English corpus
* `phrase-table/moses/phrase-table.gz`: phrase-table in the usual format
  compatible with the [Moses SMT system](http://statmt.org/moses/)

##### Toy

First 2k sentences from the full training data.

##### Small

First 20k sentences from the full training data.

##### Medium

First 100k sentences from the full training data.

##### Large:

The entire training data (2.3M sentences).

In the `large` directory, there are a few additional files:

* `phrase-table/dev-filtered/rules_cnt.final.out`: phrase table
  filtered for the data in `dev`, so that only the phrases useful
  for tuning your SMT system are in this phrase table.
* `phrase-table/test-filtered/rules_cnt.final.out`: phrase table
  filtered for the data in `test`.
* `lex.e2f` and `lex.f2e`: lexical probabilities

#### Tuning set

The files for tuning your SMT system are in the `dev` directory. This data
is meant to be used for tuning the weights of your machine translation
log-linear model. There are four references for each source sentence.

The data comes from the following sources:

* [Multiple-Translation Chinese (MTC) part 1](https://catalog.ldc.upenn.edu/LDC2002T01)
* [Multiple-Translation Chinese (MTC) part 3](https://catalog.ldc.upenn.edu/LDC2004T07)

#### Test set

The files that are used as test data to report your performance are in
the `test` directory. There are four references for each source sentence.

The data comes from the following source:

* [Multiple-Translation Chinese (MTC) part 4](https://catalog.ldc.upenn.edu/LDC2006T04)

#### Language Model

The language model files are in the `lm` directory.

* `en.gigaword.3g.arpa.gz`: large LM estimated using
  Kneser-Ney smoothing from the [English Gigaword corpus](https://catalog.ldc.upenn.edu/LDC2011T07)
* `en.gigaword.3g.filtered.dev_test.arpa.gz`: small-sized LM filtered from the
  large LM for the dev and test files (52MB compressed)
* `en.gigaword.3g.filtered.train_dev_test.arpa.gz`: medium-sized LM filtered from the
  large LM for the target side of the large phrase table and the dev and test files (93MB compressed)
* `en.tiny.3g.arpa`: tiny LM from the decoding homework

#### Chinese word segmentation data

The training data for training a Chinese word segmenter is in the
`seg` directory.  

The data comes from the [Chinese Word Segmentation Bakeoff](http://www.sighan.org/bakeoff2005/).

The data has been processed into a column format similar to the
chunking format used in the chunker homework. If you wish to convert
this into a frequency dictionary you will have to parse these column
files into words using the `B` (begin word) and `I` (inside word)
and `O` (single character word) tags.

There are three files:

* `cityu_train.utf8`: from the City University of Hong Kong
* `msr_train.utf8`: from Microsoft Research (Beijing)
* `upenn_train.utf8`: from the University of Pennsylvania Chinese Treebank

They can be converted into a single frequency dictionary for your
homework segmenter, or you can use your chunker to train a context-aware
model of Chinese word segmentation.

You may want to check if your segmentation actually improves alignment
scores before you proceed through the entire translation pipeline.
A simple way to check this is to compare the IBM Model 1 scores
with the provided segmented Chinese aligned to the given parallel
English data with your own segmentation of the Chinese data also
aligned to the same parallel English data.

### Scripts

The following are scripts that can be used to create a phrase table with
feature values from source, target and alignment data.

* `pp_xtrct_sc.sh`: shell script to run phrase extractor on the toy
  data set.
* `pp_xtrct.sh`: shell script to run phrase extractor. It splits the
  data into shards of 20K sentences each and then runs phrase extraction
  in parallel. It then filters each phrase file for `dev` or `test`
  and finally merges the phrases for each shard.

The scripts above call the following Python programs in the right
sequence.

* `PPXtractor_ph1.py`: python program for extracting phrase-pairs from
  a source, target, and alignment files.
* `PPXtractor_ph2n3.py`: python program for identifying the source
  phrases in the given dev/test set and filter the phrase file for the
  source phrases.
* `PPXtractor_ph2.py`: python program for computing forward and reverse
  lexical scores.
* `PPXtractor_ph3.py`: python program for estimating the forward
  $$P(s|t)$$ and reverse $$P(t|s)$$ probabilities using relative frequency
  estimation.


### System Description

Your system description is the most important part of your project.
Your write-up must have the following sections:

* Motivation 
    * Which aspect of the translation system did your group choose to improve and reasons for your choice.
* Approach 
    * Describe the algorithms and machine learning models used in your project.
* Data 
    * Exactly which data files were used; also include here any external data that was not provided to you.
* Experimental Setup
    * Describe what kind of evaluation you are doing and which methods you are comparing against each other.
* Results 
    * Include a detailed comparison of different methods.
* Analysis of the Results
    * Did you improve over the baseline. Why or why not?
* Future Work

### Project Ideas

Here are some ideas for your project work. You should take inspiration from these ideas and try to come with your own ideas.

### Submission Format

Your submission is a write-up of what you did for your final project.
The submission must be a text document in one of the following formats:

* Plain ASCII
* Kramdown (with LaTeX markup)
* LaTeX source (along with all the supplementary files such as figures if used)

### Grading system

The final projects will be graded using the following criteria:

* Originality
* Clarity of the writing
* Experimental Details
* Results
* Use of existing homework code

*Warning*: this page is still being updated.

