---
layout: default
img: rosetta
img_link: "http://en.wikipedia.org/wiki/Rosetta_Stone"
caption: Jean-François Champollion used word alignment (starting with the word Ptolemy) to decipher Egyptian hierogyphics.
title: Homework 4 | Attention in Neural Machine Translation
active_tab: homework
---

# Homework 4: Attention in Neural Machine Translation

<span class="text-info">Start on {{ site.hwdates[4].startdate }}</span> |
<span class="text-warning">Due on {{ site.hwdates[4].deadline }}</span>

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
`hw4` directory in your repository.

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

* `data/input` -- input files `dev.txt` and `test.txt` infected with noise
* `data/reference/dev.out` -- the reference output for the `dev.txt` input file

## Default solution

The default solution is provided in `default.py`. To use the default
as your solution:

    cp default.py answer/chunker.py
    cp default.ipynb answer/chunker.ipynb
    python3 zipout.py
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

    BLEU = 2.49 28.3/5.4/1.3/0.4 (BP = 0.854 ratio = 0.864 hyp_len = 21503 ref_len = 24902)

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

Attention is defined as follows:

$$\mathrm{score}_i = W_{enc}( h^{enc}_i ) + W_{dec}( h^{dec} )$$

where $\alpha$ is defined as:

$$\alpha_i = \mathrm{softmax}(V_{att} \mathrm{tanh} (\mathrm{score}_i))$$

Context vector calculation:

$$c = \sum_i \alpha_i \times h^{enc}_i$$

The context vector $c$ is combined with the current decoder hidden
state $h^{dec}$ and this representation is used to compute the
softmax over the target language vocabulary at the current decoder
time step. We then move to the next time step and repeat this process
until we produce an end of sentence marker.

### Extensions to Baseline

We fixed the interface in a specific way that allows you to implement at least:

1.[Unknown word replacement](https://www.aclweb.org/anthology/P15-1002/) 
2. Beam search decoding
3. Ensemble decoding

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

