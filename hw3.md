---
layoue: default
img: rosetta
img_link: "http://en.wikipedia.org/wiki/Rosetta_Stone"
caption: Jean-François Champollion used word alignment (starting with the word Ptolemy) to decipher Egyptian hierogyphics.
title: Homework 3 | Cross Attention
active_tab: homework
---

# Homework 3: Attention

<span class="text-info">Start on {{ site.hwdates[3].startdate }}</span> |
<span class="text-warning">Due on {{ site.hwdates[3].deadline }}</span>

## Getting Started

If you have already cloned my homework repository `nlp-class-hw` for
previous homeworks then go into that directory and update the directory:

    git pull origin/master
    cd nlp-class-hw/neuralmt

If you don't have that directory anymore then simply clone the
repository again:

    git clone https://github.com/anoopsarkar/nlp-class-hw.git

Clone your own repository from GitLab if you haven’t done it already:

    git clone git@csil-git1.cs.surrey.sfu.ca:USER/nlpclass-{{ site.semcode }}-g-GROUP.git

Note that the `USER` above is the SFU username of the person in
your group that set up the GitLab repository.

Then copy over the contents of the `neuralmt` directory into your
`hw3` directory in your repository.

Set up the virtual environment:

    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt

Note that if you do not change the requirements then after you have
set up the virtual environment `venv` you can simply run the following
command to get started with your development for the homework:

    source venv/bin/activate

## Data files

The data files provided are:

* `data/input` -- input files `dev.txt` and `test.txt`
* `data/reference/dev.out` -- the reference output for the `dev.txt` input file

## Default solution

The default solution is provided in `default.py`. To use the default
as your solution:

    cp default.py answer/neuralmt.py
    cp default.ipynb answer/neuralmt.ipynb
    python3 zipout.py # Warning: can take >10mins to translate dev and test input files
    python3 check.py

The default solution will look for the file `seq2seq_E049.pt`
pre-trained model file in the data directory. You do **not** 
need to train a model for this homework.

You can either download the `seq2seq_E049.pt` model file from:

    https://drive.google.com/open?id=1SCT1K8gxDmhxW7ZmEeOPqlLzPJk_qLyL

Or you can use the same file directly on CSIL from the following directory:

    /usr/shared/CMPT/courses/nlp-class/neuralmt/seq2seq_E049.pt

After you implement the baseline approach if you wish to tackle
ensemble decoding then you will need additional model files to
create the ensemble. The extra model files are as follows:

* `seq2seq_E048.pt`
* `seq2seq_E047.pt`
* `seq2seq_E046.pt`
* `seq2seq_E045.pt`

These model files are available from:

    https://drive.google.com/drive/folders/1Gct8Jbb7bPLl9EhI5p1YvD2Bs5wzLxvJ?usp=sharing

and on CSIL in the following directory:

    /usr/shared/CMPT/courses/nlp-class/neuralmt/*.pt

Please do not copy over the file into your CSIL directory as it is
moderately large and you can go over your disk quota. Instead modify
`default.py` to use the full path to the above file which is
accessible on the CSIL machines or use the command line option
for `default.py`.

    python3 default.py -m /usr/shared/CMPT/courses/nlp-class/neuralmt/seq2seq_E049.pt > output.txt

If you have a copy or soft link to `seq2seq_E049.pt` in the `data` directory then you can simply run:

    python3 default.py > output.txt

Note that this will take 5-10 minutes depending on your machine.

And then you can check the score on the dev output file called `output.txt` by running:

    python3 bleu_check.py -o output.txt

which produces the following evaluation:

    BLEU = 3.35 34.4/7.6/2.1/0.6 (BP = 0.771 ratio = 0.794 hyp_len = 19766 ref_len = 24902)

For this homework we will be scoring your solution based on the BLEU score
which is described in detail in the Accuracy section below.

Make sure that the command line options are kept as they are in
`default.py`. You can add to them but you must not delete any
command line options that exist in `default.py`.

Submitting the default solution without modification will get you
zero marks.

## The Challenge

You are given a pre-trained sequence to sequence (seq2seq) model
for neural machine translation (NMT). Also provided to you is a
basic NMT implementation that loads the encoder and decoder parameters
from the pre-trained model and produces a translation for input
documents. Your task is to augment the NMT implementation with the
correct attention module to improve the translation performance.

### Baseline 

Attention for this homework and for the trained model(s) provided
to you is defined as follows:

$$\mathrm{score}_i = W_{enc}( h^{enc}_i ) + W_{dec}( h^{dec} )$$

Define the $\alpha$ vector as follows:

$$\alpha = \mathrm{softmax}(V_{att} \mathrm{tanh} (\mathrm{score}))$$

The we define the context vector using the $\alpha$ weights for each source side index $i$:

$$c = \sum_i \alpha_i \times h^{enc}_i$$

The context vector $c$ is combined with the current decoder hidden
state $h^{dec}$ and this representation is used to compute the
softmax over the target language vocabulary at the current decoder
time step. We then move to the next time step and repeat this process
until we produce an end of sentence marker.

Implementing the attention model described above will improve
your output translations as can be seen by the BLEU score:

    $ python3 zipout.py    # using baseline implementation
    $ python3 check.py
    dev.out score: 17.1139

### Extensions to Baseline

We fixed the interface in a specific way that allows you to implement at least:

1. [Unknown word replacement](http://www.aclweb.org/anthology/P15-1002).
2. Beam search decoding.
3. Ensemble decoding.

Original training data is also provided (tokenised). You may use it whichever
way you want to augment the provided Seq2Seq model.

### Useful Tools

For visualisation, one could easily use the included functions in `utils.py`:

    from utils import alphaPlot

    # Since alpha is batched, alpha[0] refers to the first item in the batch
    alpha_plot = alphaPlot(alpha[0], output, source)

This converts the alpha values into a nice attention graph.
Example code in combination with `tensorboard` is provided in `validator.py`.
This can help you visualise an entire `test_iter`.

In addition, `default.py` has an additional parameter `-n`.
If your inference is taking too long and you'd like to test your implementation
with a subset of dev (say first 100 samples), you can do that.

## Required files

You must create the following files:

* `answer/neuralmt.py` -- this is your solution to the homework. start by copying `default.py` as explained below.
* `answer/neuralmt.ipynb` -- this is the iPython notebook that will be your write-up for the homework.

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

Once you have a working solution in `answer/neuralmt.py` create
the `output.zip` for upload to Coursys using:

    python3 zipout.py

### Create source.zip

To create the `source.zip` file for upload to Coursys do:

    python3 zipsrc.py

You must have the following files or `zipsrc.py` will complain about it:

* `answer/neuralmt.py` -- this is your solution to the homework. start by copying `default.py` as explained below.
* `answer/neuralmt.ipynb` -- this is the iPython notebook that will be your write-up for the homework.

In addition, each group member should write down a short description of what they
did for this homework in `answer/README.username`.

### Upload to Coursys

Go to `Homework 3` on Coursys and do a group submission:

* Upload `output.zip` and `source.zip`
* Make sure your `source.zip` matches your Gitlab repository.
* Make sure you have documented your approach in `answer/neuralmt.ipynb`.
* Make sure each member of your group has documented their contribution to this homework in `answer/README.username` where `username` is your CSIL/GitLab username.

## Grading

The grading is split up into the following components:

* dev scores (see Table below)
* test scores (see Table below)
* iPython notebook write-up 
* Check if each group member has a `answer/README.username`.

Your F-score should be equal to or greater than the score listed for the corresponding marks.

| **BLEU(dev)** | **BLEU(test)** | **Marks** | **Grade** |
| 2.5  | 2.0  | 0   | F  |
| 3.0  | 2.5  | 55  | D  |
| 4.0  | 3.0  | 60  | C- |
| 5.0  | 4.0  | 65  | C  |
| 6.0  | 5.0  | 70  | C+ |
| 8.0  | 7.0  | 75  | B- |
| 10.0 | 9.0  | 80  | B  |
| 14.0 | 14.0 | 85  | B+ |
| 17.0 | 16.0 | 90  | A- |
| 18.0 | 17.0 | 95  | A  |
| 20.0 | 19.0 | 100 | A+ |
{: .table}

The score will be normalized to the marks on Coursys for the dev and test scores.
