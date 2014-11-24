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

## Files

In order to complete the project, you are provided with data files
to build a Chinese-English machine translation system. This data
has already been processed into alignments, phrase tables, etc. You
can use the processed data as given to you or generate your own
alignments, phrase tables, etc.

You are also provided with some Python programs that generate a
phrase table with typical feature values: $$p(e|f), p(f|e), lex(e|f),
lex(f|e)$$ where $$e$$ and $$f$$ are phrases in the phrase table.

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

### Programs for phrase table generation

The following are scripts that can be used to create a phrase table
with feature values from source, target and alignment data.

* `pp_xtrct_sc.sh`: shell script to run phrase extractor on the toy
  data set. **You should use this script if you have produced your
  own alignments or if you have produced your own Chinese segmentation
  and alignments based on that segmentation**
* `pp_xtrct.sh`: shell script to run phrase extractor. It splits
  the data into shards of 20K sentences each and then runs phrase
  extraction in parallel. It then filters each phrase file for `dev`
  or `test` and finally merges the phrases for each shard. This
  script assumes you have access to a large cluster of multiple
  machines managed by grid management software such as Torque (using
  the `qsub` command).

The scripts above call the following Python programs in the appropriate
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

## The Challenge

The challenge is to use the code you have written for your homework
assignments in this course in order to build a Chinese-English
translation system and get a competitive BLEU score on the test
set.

You can choose to follow any route as long as you have a Chinese-English
machine translation system at the end. You should have a comparison
between at least two methods on the dataset, and compare their BLEU
scores.

Below I describe a few basic steps you can take in order to obtain
a performant Chinese-English SMT system using your homework code
from this course.

### Get decoder working on toy data

The absolute first step: get your decoder working with the `toy`
phrase table data and the tiny LM data from the `lm` directory.

Run your decoder on the test set and try to get a BLEU score.
It will have a terrible score but it will be a start.

### Use filtered phrase tables with your decoder

The most basic Chinese-English translator you can build is to use
the filtered phrase tables and language model with your decoder. I
recommend using the following data files:

* `large/phrase-table/test-filtered/rules_cnt.final.out`: phrase
  table filtered for the data in `test`.
* `en.gigaword.3g.filtered.train_dev_test.arpa.gz`: medium-sized
  LM filtered from the large LM for the target side of the large
  phrase table and the dev and test files (93MB compressed)
* The test files in the `test` directory.

You need to change a few things in your decoder: 

* Modify the code that loads up the language model to read a gzip
  file using the Python gzip module.
* Modify the decoder to use all the feature values in the phrase
  table file (earlier we just had one feature per phrase pair, now
  we have four). You can use uniform weights to combine the feature
  values and the language model feature.
* Optionally use multiple references in computing the BLEU score
  on the test set.

This will give you a basic Chinese-English SMT system and would be
a valid course project submission. However, you can do a little bit
more to improve your performance.

### Feedback loop between Decoder and Reranker

Once you have your decoder working and producing a BLEU score
on the test set, you can then learn a better weight vector
using your reranking code.

* Take the decoder from the previous section. 
* Use the phrase table filtered for the data in `dev`:
  `large/phrase-table/dev-filtered/rules_cnt.final.out` and produce
  a 100-best list from the last stack in your decoder (the last stack
  covers all input words).
* Use your reranking code to produce a weight vector that favors
  translations that match the `dev` references.
* Use this new weight vector with your decoder to produce
  a new 100-best list for the `dev` set. Iterate until improvement
  in the BLEU score on the `dev` set is minimal or a small number 
  of iterations (say 5) if it is taking too long to converge.
* Use the final weight vector with your decoder on the 
  test set using the phrase table filtered for the test set: 
  `phrase-table/test-filtered/rules_cnt.final.out`.

Compare your BLEU score on the test set with your previous
approach that used uniform weights.

There are many other ideas and you should come up with some
ideas on your own.

### Other ideas

* Add new features to the decoder.  You can experiment with 
  the features you added in your decoder and reranker homeworks.
* Improving Chinese segmentation using the `seg` data. However,
  this approach has a serious penalty of having to produce new
  alignments and subsequently a new phrase table. This is useful
  only if you are certain your segmentations are going to be
  better than we have provided. One approach is to produce 
  [segmentations that are guaranteed to improve the alignment score](ftp://ftp.cs.rochester.edu/pub/papers/ai/10.tr957.Bayesian_Learning_of_Tokenization_for_Machine_Translation.pdf).
* [Improve handling of unknown Chinese words](https://www.aclweb.org/anthology/I/I08/I08-1030.pdf)
* [Do not segment the Chinese sentence at all](http://www.phontron.com/paper/neubig12acl.pdf)

Ideas you should not try:

* Using your own aligner and creating a phrase table. The alignments
  we have provided to you are very high quality, for the particular
  Chinese segmentations given to you. Simply getting new alignments
  on the same data is unlikely to improve results.

But the sky's the limit! You can try anything you want, as long
as you follow the ground rules.

## Ground Rules

* Each group should submit using one person as the designated uploader.
* You must turn in two things:
  1. A write-up that explains what you accomplished in your course project. It should be written in a clear, scientific style and contain enough information for another student to replicate your results. More information about the write-up is given below.
  1. Your code. The code should be self-contained, self-documenting, and easy to use. Please include a detailed description of how to run your code.
* Each group should assign one member to upload the write-up and source code to [Coursys](https://courses.cs.sfu.ca) as a single tarball or zip files as the submission for Final Project. 
* You cannot use data or code resources outside of what is provided to you. You can use NLTK but not any NLTK reranking code directly. You cannot use any public implemenation of reranking such as the one included in `moses`, `Joshua`  or `cdec` or any other open source decoder.

### Write-up

Your write-up is the most important part of your project. It must have the following sections:

* Motivation 
    * Which aspect of the translation system did your group choose to improve and reasons for your choice.
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

For your write-up, you can use plain ASCII but for math equations
and tables it is better to use either
[latex](http://www.latex-project.org/) or
[kramdown](https://github.com/gettalong/kramdown).  Do __not__ use
any proprietary or binary file formats such as Microsoft Word.

## Grading system

The final projects will be graded using the following criteria:

* Originality 
* Substance (amount of work done for the project)
* Well documented use of prior results from research papers
* Clarity of the writing
* Quality of experimental design
* Quality of evaluation and results
* (Re)Use of existing homework code
* Overall score (based on the above criteria)

