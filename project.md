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

<p class="text-muted">Due on Friday, December 8, 2017 (no grace days)</p>

Automatic evaluation is a key problem in machine translation. Suppose that we have two
machine translation systems. On one sentence, system A outputs:

*This type of zápisníku was very ceněn writers and cestovateli*.

And system B outputs:

*This type of notebook was very prized by writers and travellers*.

We suspect that system B is better, though we don’t necessarily know that its translations
of the words *zápisníku*, *ceněn*, and *cestovateli* are correct. But suppose that we also
have access to the following reference translation.

*This type of notebook is said to be highly prized by writers and travellers*.

We can easily judge that system B is better. **Your challenge is to write a program that
makes this judgement automatically**.
 
## Getting Started

You must have git and python (2.7) on your system.

If you have already cloned the `nlp-class-hw` repository,
then do the following to get the files for Homework 3:

    # go to the directory where you did a git clone before
    cd nlp-class-hw
    git pull origin master

Or you can create a new directory that does a fresh clone of the
repository:

    git clone https://github.com/anoopsarkar/nlp-class-hw.git

In the `evaluator` directory you will find several python programs
and data sets that you will use for this assignment.  

`default.py` contains the default method for evaluation:

    python default.py > output

This program uses a very simple evaluation method.
Given machine translations $$h_1$$ and $$h_2$$ and reference translation $$e$$,
it computes $$f(h_1,h_2,e)$$ as follows, where $$\ell(h,e)$$ is the count of words in $$h$$
that are also in $$e$$.

$$f(h_1,h_2,e)=\left\{\begin{array}{ll}
  1 & \mbox{if } \ell(h_1,e) > \ell(h_2,e)\\
  0 & \mbox{if } \ell(h_1,e) = \ell(h_2,e)\\
  -1 & \mbox{if } \ell(h_1,e) < \ell(h_2,e)  
\end{array}\right.$$

It is a good idea to check the output of your evaluation program using `check.py`.
This will avoid your upload hanging on the leaderboard and other nasty consequences.

    python check.py < output

It will report errors if your evaluation output is malformed.

Once you have checked the output of the evaluation program for
errors, we can compare the results of this function with those of
human annotator who rated the same translations.

    python score-evaluation.py < output

Or you can do it all at once:

    python default.py | python check.py | python score-evaluation.py 

              Pred. y=-1	y=0	y=1
    True y=-1	5245	2556	3161
    True y= 0	1412	1108	1413
    True y= 1	3090	2448	5135

    Accuracy = 0.449312

## The Challenge

Your task for this assignment is to **improve the accuracy of automatic evaluation as
much as possible**.  

### The Baseline

A good way to start improving the metric to use the simple
[METEOR](http://aclweb.org/anthology/W/W07/W07-0734.pdf)
([Wikipedia](http://en.wikipedia.org/wiki/METEOR) also has a nice description) metric with
the chunking penalty in place of $$\ell(h,e)$$.
METEOR computes the harmonic mean of precision and recall, penalized by the number of chunks. That is:

$$\ell(h,e) = \left(1 - \gamma \left(\frac{c}{m}\right)^\beta\right)\frac{P(h,e) \cdot R(h,e)}{(1-\alpha)R(h,e)+\alpha P(h,e)}$$

where $$P$$ and $$R$$ are precision and recall, defined as:

$$R(h,e) = \frac{|h\cap e|}{|e|} \qquad \mbox{and} \qquad P(h,e) = \frac{|h\cap e|}{|h|},$$

$$\beta,\gamma$$ are tunable parameters, $$c$$ is the number of chunks and $$m$$ is the number of
matched unigrams.

Be sure to tune the parameter $$\alpha$$ that balances precision and recall.
This is a very simple baseline to implement. However, evaluation is not solved,
and the goal of this assignment is for you to experiment with methods that yield
improved predictions of relative translation accuracy. 

### Extending the baseline

Some things that you might try:

* [Learn a classifier from the training data.](http://aclweb.org/anthology//W/W11/W11-2113.pdf)
* [Use WordNet to match synonyms.](http://wordnet.princeton.edu/)
* [Compute string similarity using string subsequence kernels.](http://jmlr.org/papers/volume2/lodhi02a/lodhi02a.pdf)
* Use an n-gram language model to better assess fluency.
* [Develop a single-sentence variant of BLEU.](http://aclweb.org/anthology//P/P02/P02-1040.pdf)
* [Use a dependency parser to assess syntactic well-formedness.](http://ssli.ee.washington.edu/people/jgk/dist/metaweb/mtjournal.pdf)
* Develop a method to automatically assess semantic similarity.
* [See what evaluation measures other people have implemented.](http://www.statmt.org/wmt10/pdf/wmt10-overview.pdf)

But the sky’s the limit! Automatic evaluation is far from solved,
and there are many different solutions you might invent. You can
try anything you want as long as you follow the ground rules (see
below).

You should feel free to use additional data resources such as
thesauruses, WordNet, or parallel data. You are also free to use
additional codebases and libraries <b>except for those expressly
intended to evaluate machine translation systems</b>. You must write
your own evaluation metric. However, if you want your evaluation
to depend on lemmatizers, stemmers, automatic parsers, or part-of-speech
taggers, or you would like to *learn* a metric using a general
machine learning toolkit, that is fine. But translation metrics
including (but not limited too) available implementations of BLEU,
METEOR, TER, NIST, and others are not permitted. You may of course
inspect these systems if you want to understand how they work,
although they tend to include other functionality that is not the
focus of this assignment.  It is possible to complete the assignment
with a very modest amount of python code. If you aren't sure whether
something is permitted, ask us.

You do not need any other data than what we provide. You are free
to use any code or software you like, __except for those expressly
intended to evaluate machine translation output__.  You must write
your own evaluation function. If you want to use part-of-speech
taggers, syntactic or semantic parsers, machine learning libraries,
thesauri, or any other off-the-shelf resources, go nuts. But
evaluation software like BLEU, TER, METEOR, or their many variants
are off-limits. You may of course inspect these systems if it helps
you understand how they work. If you aren't sure whether something
is permitted, ask us. If you want to do system combination, join
forces with your classmates (but only use the output from other
groups, not their source code!).

### The Leaderboard

In this homework, the score produced by `score-evaluation.py` will be
on the test set. Please do run your evaluation on the dev set many times
before uploading your results. 

To get on the leaderboard, produce your output file:

    python answer/evaluate.py > output

Then upload the file `output` to the leaderboard for the Project on
[sfu-nlp-class.appspot.com](https://sfu-nlp-class.appspot.com)


## Ground Rules

* Each group should submit using one person as the designated uploader. Ideally use the same person across all homeworks.
* Follow these step-by-step instructions to submit your homework solution:
  1. Your solution to this homework should be in the `answer` directory in a file called `evaluate.py`. The code should be self-contained, self-documenting, and easy to use. It should read the data exactly like `default.py` does. Your program should run like this:

            python answer/evaluate.py > output

  1. Upload this file `output` to the [leaderboard submission site](http://sfu-nlp-class.appspot.com) according to [the Homework 0 instructions](hw0.html).
  1. Run the program: `python zipsrc.py`. This will create a a zip file called `source.zip`. Each group should assign one member to upload `source.zip` to [Coursys]({{ site.coursys }}) as the submission for this homework.  It should use the same input and output assumptions of `default.py`. Only use `zipsrc.py` to prepare your zip file.
  1. Also in the `answer` directory include for each group member with a user name `username` a file in your submission called `README.username` which contains a description of your contribution to the homework solution along with the commit identifiers from either `svn` or `git`. If you have only one member in your group then create an empty file.
  1. A write-up of your course project as a PDF file and source for the write-up should be included in `source.zip`. More details about the course project write-up below.

If you have any questions or you're confused about anything, just ask.

## Write-up

In addition to performing well on the leaderboard, your write-up is also a very important parts of your project submission. It **must** have the following sections:

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

### Submission Format

For your write-up, you can use plain ASCII but for math equations
and tables it is better to use either
[latex](http://www.latex-project.org/) or
[kramdown](https://github.com/gettalong/kramdown).  Do __not__ use
any proprietary or binary file formats such as Microsoft Word unless you use
the template from the following page on Submission Formats. If you
do use Word or any other proprietary format then you must submit
the PDF file of your report as `report.pdf` in your `source.zip`
submission.

If you use latex then use the style files from the [Submission Format section of this page](https://transacl.org/ojs/index.php/tacl/about/submissions).

To get a PDF file you should run the following commands (which assume you have installed LaTeX on your system):

    pdflatex project
    bibtex project
    pdflatex project
    pdflatex project

You can then open `project.pdf` using any PDF viewer. Please submit
the LaTeX source and the PDF file along with your source code when
you submit your project to Coursys.

### Grading system for the write-up

The final projects will be graded using the following criteria:

* Originality 
* Substance (amount of work done for the project)
* Well documented use of prior results from research papers
* Clarity of the writing
* Quality of experimental design
* Quality of evaluation and results
* (Re)Use of existing homework code
* Overall score (based on the above criteria)

### Examples

Here is [one example of a good project submission](http://anoopsarkar.github.io/papers/pdf/sighan08.pdf). 
You can take inspiration for how to write a polished report from this
examples but make sure you have the sections required by the Write-up section above.

#### Acknowledgements

This assignment was designed by [Chris Dyer](http://www.cs.cmu.edu/~cdyer)
based on an original task by [Adam Lopez](http://alopez.github.io) which also inspired a 
[whole](http://aclweb.org/anthology//W/W12/W12-3101.pdf)
[series](http://aclweb.org/anthology//W/W12/W12-3102.pdf) 
[of](http://hltc.cs.ust.hk/iwslt/proceedings/paper_34.pdf) 
[papers](http://aclweb.org/anthology//P/P13/P13-1139.pdf).
It is based on the shared task for evaluation metrics that is run at the annual [Workshop on Statistical Machine Translation](http://statmt.org/wmt15). The task was introduced by [Chris Callison-Burch](http://www.cis.upenn.edu/~ccb/).
