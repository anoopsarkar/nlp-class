---
layout: default
img: loch_fyne
img_link: "https://aclanthology.org/W17-5525.pdf"
caption: Pictorial representation of the meaning representation for the E2E table to text generation task
title: Homework 4 | Prompt Tuning for Text Generation
active_tab: homework
---

# Homework 4: Prompt Tuning for Text Generation

<span class="text-info">Start on {{ site.hwdates[4].startdate }}</span> |
<span class="text-warning">Due on {{ site.hwdates[4].deadline }}</span>

## Getting Started

If you have already cloned my homework repository `nlp-class-hw` for
previous homeworks then go into that directory and update the directory:

    git pull origin/master
    cd nlp-class-hw/prefixtune

If you don't have that directory anymore then simply clone the
repository again:

    git clone https://github.com/anoopsarkar/nlp-class-hw.git

Clone your own repository from GitLab if you haven’t done it already:

    git clone git@github.sfu.ca:USER/nlpclass-{{ site.semcode }}-g-GROUP.git

Note that the `USER` above is the SFU username of the person in
your group that set up the GitLab repository.

Then copy over the contents of the `prefixtune` directory into your
`hw3` directory in your repository.

Set up the virtual environment:

    python3.10 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt

You must use Python 3.10 (or later) for this homework.

Note that if you do not change the requirements then after you have
set up the virtual environment `venv` you can simply run the following
command to get started with your development for the homework:

    source venv/bin/activate

## Background

The goal for this homework is to learn to use an autoregressive
language model which processes the input from left to right and
predicts the next token based on the left context (also called a
causal language model when there is a distinct input and output but
is trained and decoded as if it was a left to right LM).

We will be using a text to table task, which takes structured data
in the form of a table and produces a text description of what is
in the data.

For example, if the input is:

| **name** | **area** | **family friendly** |
| Alimentum  | city centre  | no |
{: .table}

The table is linearized and stored as follows:

    name : Alimentum | area : city centre | family friendly : no

This linearized table is given as input to a language model
to produce a text description of the table:

    There is a place in the city centre , Alimentum , that is not family - friendly .

However, there can be many ways to produce a text description. Here are some of the
ways you can produced a text for the same table:

    There is a place in the city centre , Alimentum , that is not family - friendly .
    In the city centre there is a venue name Alimentum , this is not a family - friendly venue .
    Alimentum is not a family - friendly place , located in city centre .
    Alimentum is not a family - friendly arena and is located in the city centre .
    Alimentum is not a family - friendly place in the city centre .
    Alimentum in city centre is not a family - friendly place .

A large language model is trained on data from many diverse sources and there
might be a mix of structured and unstructured data in the training data helping it
to solve this task if you prompt the language model in the right way.

The goal of this assignment is to fine-tune a language model (one
that isn't exposed to the entire web) in a compute-efficient way
using prefix tuning. The end result is that the parameters for the
large language model are not even modified after fine-tuning and
we only learn an appropriate (continuous) prompt that can solve
this task using in-context learning.

## Data set

The data set is the E2E table to text task as described in detail
in the following publication:

> [The E2E Dataset: New Challenges For End-to-End Generation](https://arxiv.org/abs/1706.09254). Jekaterina Novikova, Ondřej Dušek, Verena Rieser. SIGDIAL 2017 short paper.

The [leaderboard](https://paperswithcode.com/sota/table-to-text-generation-on-e2e) for this task shows that there is still room for improvement on the state-of-the-art.

## Data files

The data files provided are:

* `data/train.txt.gz` -- the training data used to train the `answer/default.py` model (`default.py` uses the [huggingface dataset for E2E](https://huggingface.co/datasets/e2e_nlg) to load the data but a copy of the training data is provided just in case).
* `data/input` -- input files `dev.txt` and `test.txt` infected with noise. a subset of `dev.txt` is provided as `small.txt` for development of your solution.
* `data/reference/dev.out` -- the reference output for the `dev.txt` input file
* `data/reference/small.out` -- the reference output for the `dev.txt` input file

## Default solution

The default solution is provided in `answer/default.py`. To use the default
as your solution:

    cd answer
    cp default.py prefixtune.py
    cp default.ipynb prefixtune.ipynb
    cd ..
    python3 zipout.py
    python3 check.py

The default solution will use the language model directly using a
prompt to solve the task. `default.py` has additional code provided
that will look for a fine-tuned model as `data/peft.pt` and use
that for decoding if it exists. Otherwise, there is code in
`default.py` that loads up the dataset for fine-tuning. You will
need to copy and modify `default.py` to add your own fine-tuning
steps to train a better model for this task.

Please do not commit your model file or the language model file
into your git repository as it is moderately large and you can go
over your disk quota.

To run the default program as follows:

    python3 answer/default.py -i data/input/small.txt > output.txt

And then you can check the score on the dev output file called `output.txt` by running:

    python3 bleu.py -t data/reference/small.out -o output.txt

which produces the evaluation as a BLEU score:

    bleu score: 1.3688755959761818

For this homework we will be scoring your solution based on the BLEU score
which is described in detail in the Accuracy section below. However the BLEU
score is not the only focus. You can focus on efficiency, model size, 
experimental comparison with other approaches and many other choices.

Make sure that the command line options are kept as they are in
`answer/default.py`. You can add to them but you must not delete any
command line options that exist in `answer/default.py`.

Submitting the default solution without modification will get you
zero marks.

### Accuracy

The accuracy for this homework is calculated using the 
[BLEU score](https://en.wikipedia.org/wiki/BLEU)
which compares n-gram overlap between the candidate and the
reference. It then combines that with a brevity penalty to make
sure the candidate is approximately matching the length of the
reference.

- Reference: `The NASA Opportunity rover is battling a massive dust storm on Mars .`
- Candidate: `A NASA rover is fighting a massive storm on Mars .`

The candidate has 11 tokens (so 11 unigrams, 10 bigrams, 9 trigrams
and 8 fourgrams). The following n-gram matches can be found:

- **Unigram**: `A`, `NASA`, `rover`, `is`, `a`, `massive`, `storm`, `on`, `Mars` **Score** = 9/11
- **Bigram**: `rover is`, `a massive`, `storm on`, `on Mars`, `Mars .` **Score** = 5/10
- **Trigram**: `storm on Mars`, `on Mars .` **Score** = 2/9
- **Fourgram**: `storm on Mars .` **Score** = 1/8

In the BLEU score we actually use the minimum frequency of each n-gram based on
reference versus candidate, e.g. if an n-gram occurs twice in the candidate, but
only once in the reference then we take the numerator to be one.

The overall n-gram precision score is a equally weighted geometric mean
of each of the n-gram precision values.

- **Overall precision**: (9/11 * 5/10 * 2/9 * 1/8)^(1/4) = 0.32649

The brevity penalty is calculated as the minimum of 1 and exp(1 -
reference-length/output-length). For the above example, the reference
length is 13 and the candidate length is 11 so the brevity penalty
is 0.8337.

The BLEU score is the product of the overall precision score and
the brevity penalty. For the above example, the BLEU score would
be 0.27221.

### Pytorch

You will need to use some Pytorch API calls and possibly the
Huggingface Transformers package API to solve this homework. The
following links will help you get started on what you need to know
to get started. You can learn a lot of the Pytorch basics by
understanding `default.py`.

Some useful links if you feel lost at the beginning:

* [60 mins intro to Pytorch](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html)
* [Introduction to the transformers library](https://huggingface.co/docs/transformers/notebooks)

Read the source code in `default.py` in detail.

## Prefix Tuning

You will implement the approach presented in this paper to solve
the table to text fine-tuning challenge:

> [Prefix-Tuning: Optimizing Continuous Prompts for Generation](https://aclanthology.org/2021.acl-long.353). Xiang Lisa Li, Percy Liang. ACL 2021.

### Hyperparameters

`default.py` uses `distilgpt2` as the language model which is the
smallest of the GPT2 models. You can alternatively use `gpt2` but
you should not use `gpt2-large` or `gpt2-xl` or any of the massively
large language models since they can be very slow even on a GPU.

The other hyperparameters for prefix tuning are available by
running:

    python3 answer/default.py -h

You can experiment with different values for the number of virtual
tokens and the prefix projection boolean flag.  Although five virtual
tokens seems to work the best when compared to the increased training
time for more virtual tokens.

Setting the prefix projection boolean to `True` will improve results
but at the cost of more parameters (0.1 percent of original model
will go up to 10 percent).

You can experiment with different parameters to the `model.generate()`
function in `predict()` or even replace it altogether. Explore
[useful parameters for the generate
function](https://huggingface.co/blog/how-to-generate).

Do not change any of the other hyperparameters unless you post
on the discussion board and it is approved by the instructor.

## Required files

You must create the following files:

* `answer/prefixtune.py` -- this is your solution to the homework. start by copying `default.py` as explained below.
* `answer/prefixtune.ipynb` -- this is the iPython notebook that will be your write-up for the homework.

## Run your solution on the data files

To create the `output.zip` file for upload to Coursys do:

    python3 zipout.py

For more options:

    python3 zipout.py -h

## Check your accuracy

To check your accuracy on the dev set:

    python3 check.py

The output score is the BLEU score.

    python3 check.py -h

In particular use the log file to check your output evaluation:

    python3 check.py -l log

The accuracy on `data/input/test.txt` will not be shown.  We will
evaluate your output on the test input after the submission deadline.

## Submit your homework on Coursys

Once you are done with your homework submit all the relevant materials
to Coursys for evaluation.

### Create output.zip

Once you have a working solution in `answer/prefixtune.py` create
the `output.zip` for upload to Coursys using:

    python3 zipout.py

### Create source.zip

To create the `source.zip` file for upload to Coursys do:

    python3 zipsrc.py

You must have the following files or `zipsrc.py` will complain about it:

* `answer/prefixtune.py` -- this is your solution to the homework. start by copying `default.py` as explained below.
* `answer/prefixtune.ipynb` -- this is the iPython notebook that will be your write-up for the homework.

Each group member should write about what they did for this homework in the Python notebook.

### Upload to Coursys

Go to `Homework 4` on Coursys and do a group submission:

* Upload `output.zip` and `source.zip`
* Make sure you have documented your approach in `answer/prefixtune.ipynb`.
* Make sure each member of your group has documented their contribution to this homework in the Python notebook.

## Grading

The grading is split up into the following components:

* dev scores (see Table below)
* test scores (see Table below)
* iPython notebook write-up 
   * Make sure that you are not using any external data sources in your solution.
   * Make sure you have implemented the fine-tuning model improvements yourself without using external libraries.
* Check if each group member has written about what they did in the Python notebook.

Your BLEU score should be equal to or greater than the score listed for the corresponding marks.

| **Score(dev)** | **Score(test)** | **Marks** | **Grade** |
| 0.0  | 0.0  | 0   | F  |
| 1.3  | 1.2  | 55  | D  |
| 10   | 12   | 60  | C- |
| 15   | 17   | 65  | C  |
| 17   | 20   | 70  | C+ |
| 19   | 24   | 75  | B- |
| 20   | 26   | 80  | B  |
| 22   | 28   | 85  | B+ |
| 24   | 30   | 90  | A- |
| 26   | 32   | 95  | A  |
| 30   | 35   | 100 | A+ |
{: .table}

The score will be normalized to the marks on Coursys for the dev and test scores.

