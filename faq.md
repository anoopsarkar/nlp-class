---
layout: default
img: hal9k
img_link: http://en.wikipedia.org/wiki/HAL_9000
caption: "In 2001 A Space Odyssey, HAL 9000 speaks in a calm voice and conversational manner in constrast to the humans."
title: FAQ
active_tab: faq
---

## (in) Frequently Asked Questions

### Reference books

* There is no official textbook for the course, but if you would like to read further about NLP, here are some good reference books:
    * [Neural Network methods for Natural Language Processing](http://www.morganclaypool.com/doi/10.2200/S00762ED1V01Y201703HLT037) by Yoav Goldberg.
    * [Speech and Language Processing](http://www.cs.colorado.edu/~martin/slp.html) by [Daniel Jurafsky](http://www.stanford.edu/~jurafsky) and [James Martin](http://www.cs.colorado.edu/~martin).
    * [Foundations of Statistical Natural Language Processing](http://nlp.stanford.edu/fsnlp/) by [Chris Manning](http://nlp.stanford.edu/~manning/) and [Hinrich Schütze](http://www.cis.uni-muenchen.de/schuetze/).
    * [Statistical Machine Translation](http://www.statmt.org/book/) by [Philipp Koehn](http://www.cs.jhu.edu/faculty/philipp-koehn/).
    * [Natural Language Processing with Python](http://www.nltk.org/book_1ed/) by [Steven Bird](http://estive.net/) and [Ewan Klein](http://homepages.inf.ed.ac.uk/ewan/) and [Edward Loper](http://ed.loper.org/).

### Email policy
    
* We will be using [the discussion board on courses.cs.sfu.ca]({{ site.coursys }}/discussion) instead of email.
* Before starting a new topic please check if the topic is already under discussion and check to see if your question has already been answered.
* If you must email the instructor or TA directly then use your SFU email address to send the email (do not use any other provider), and use `cmpt413:` or `cmpt825:` (depending on if you are an undergrad or grad student) as the prefix in your subject line.

### Grading

* The grade for the course is computed using the final marks which are a weighted average of each activity as defined on the [main page](index.html).
* The grade cutoff are as follows:

  | A+ | >95 |
  | A  | >90 |
  | A- | >85 |
  | B+ | >80 |
  | B  | >75 |
  | B- | >70 |
  | C+ | >65 |
  | C  | >60 |
  | C- | >55 |
  | D  | >50 |
  | F  | &le;50 |
  {: .table}

### Homework Submission and Grace Days
    
* Your group has to submit two deliverables for each homework:
    * Source code for your homework will be submitted electronically on [courses.cs.sfu.ca](https://courses.cs.sfu.ca/).
    * The output on the provided data has to be uploaded to the leaderboard server on [Google App Engine](http://sfu-nlp-class.appspot.com/).
* Only one member of the group should upload to the leaderboard and use the valid group name.
* Check your scores on the leaderboard and check that your group appears only once in the leaderboard.
* All homeworks are due by 11:59PM on the homework due date.
* Each homework comes with 2 grace days. However the grace days only apply to those who have a valid submission on the due date (a submission that scores -1 or -inf is invalid). For example, if your homework deadline is Tuesday 11:59PM and you submit a valid solution then you have until Thursday night 11:59PM to modify your homework submission.
* We will make every attempt to release grades for each homework the day after it is due. However, this means that after we review the source code we might have to lower your official grade. If you cheated in some way, such as copying your submission or you have violated the ground rules for each homework, your grades will be decreased from the initial value.

### Groups
    
* The homework assignments will be solved in groups. Maximum group size is four. All groups must be formed before Homework 0 is due.
* You are allowed to leave a group and form a group of size one at the start of each homework but not at the end.
* Each group will create a single submission and upload it before the due date.
* Each group member will be graded on their self report and any commit logs that are submitted. If the TA or the instructor perceives there is a problem with collaboration in a group, certain group members can get zero marks. If you are pair programming, take turns in switching the user doing the commits to the svn repository.
* __Effective group collaboration__: We are looking to see effective collaboration to solve the homework assignment. People can play different roles and sometimes more than one role in the same homework:
    * Designer: creates a plan for implementation and coordinates activities of the group. Should create design docs (text files or markdown or equivalent only). Put these documents in the directory `answer/docs` and mention the files in your `README.username` file (where `username` is your SFU login username).
    * Code reviews: write a critical view of the implementation by the group. Points out what is missing, inelegant code, etc. and produces a code review document (text files or markdown or equivalent only). Put these documents in the directory `answer/docs` and mention the files in your `README.username` file.
    * Development: write the code. This can be done in collaboration. 
    * Testcases: write testcases to stress test the code. Provide the testcases in your submission.
* **Warning**: if you are missing a `README.username` file in your group source submission then that `username` might get zero marks.
* Use `git` for version control and effective collaboration. See the section below on setting up `git` for this course.

### Programming
    
* Setup a source code version control system. The most convenient version control system is `git` and setup instructions are given below.
* We will be using the Python-based <a href="http://nltk.org/">NLTK: Natural Language Toolkit</a> and Python 2.7.x for programming.
* The easiest way to install Python with NLTK on your machine is to download [Anaconda Python distribution](https://store.continuum.io/cshop/anaconda/)
* It is expected that your program will compile and run using the standard runtime environment on the Linux CSIL lab machines. If you are developing on a Linux, Apple or Microsoft operating system at home, you have to ensure that the code will run on the CSIL machines before you submit the assignment. Please either visit the CSIL lab machines or you can use `ssh` to login to the CSIL Linux machines and also use `scp` to copy over and test your programs on the CSIL Linux machines before you submit them. Check the [CSIL Layout Map](http://www.cs.sfu.ca/content/dam/sfu/computing/csil/csil_layout_burnaby.pdf) for the machine names.
* [Remote access to CSIL](http://www.sfu.ca/computing/about/support/csil/unix/how-to-use-csil-linux-cpu-server.html) is allowed.
* CSIL computers accept SSH connections on port 24 (rather than the usual port 22). They can only be accessed from within the SFU network. If you are outside it, you need to go through a directly accessable computer, most likely fraser.sfu.ca. Here are some examples using the usual command line `ssh` and `scp` (from OpenSSH). Below $ is the command line shell on your home computer running Linux/MacosX/Cygwin. What follows is a recipe that will connect you remotely to a CSIL Linux machine: <script src="https://gist.github.com/4486532.js"></script> 
* If your local machine (e.g your laptop) has a different username from your SFU username (your username can be found by examining your SFU email address: username`sfu.ca), then prefix the SFU username to the ssh or scp command. `ssh (username)@fraser.sfu.ca`.
* You may want to refer to a quick Unix tutorial. There are several on the web. The following one covers most of what you need to use the Linux shell effectively: [Quick Unix Tutorial](http://unlser1.unl.csi.cuny.edu/tutorials/QuickUnixTutorial.html).
*  On some CSIL Linux machines, in some rare cases, you might have to extend your CPU time limit for a process. If you are using tcsh then run the command "limit cputime 1800" to extend CPU time to 1800 secs or 30 mins. If you are using bash then use the command "ulimit -t 1800".

#### Using the computer from the command line shell

In the instructions that follow, you will operate the computer using
the text-based command-line interface, known as the "shell". Start
off by reading [the CSIL guide to Linux](http://www.sfu.ca/computing/about/support/csil/unix.html){:target="_blank"}

Are you confident you know how to use the shell? Do [the shell challenge](shell_fu.txt)
to prove to yourself that you really know how to use the command shell.

Stop! We know that students skip over links! If you are
new to Linux, you really need to read up on some basics.
Read [the CSIL guide to Linux](http://www.sfu.ca/computing/about/support/csil/unix.html){:target="_blank"} now!

### Setup your git repo

#### Git Basics

We never write code all at once, and entirely correctly the first
time. We usually write some code, save it somewhere safe, then come
back to it and modify it until we are done with our task.  More
importantly, we need to track our changes so that we can experiment
with what works and what doesn't. In order to help us do these steps
we use a source code version control system (or VCS, for short).
The source code are our programs and version control lets us manage
all the changes we have made to our code.

Throughout this course, your programs will be managed and archived
using [Git](https://git-scm.com). The basic idea is as follows:

* Every student gets a private storage area called a repository on the SFU server machines, or "repo" for short.
* Your code is stored in your repo. Every time you make a change to your code, you *commit* a new *revision* of your code to the repo for permanent storage. All revisions you ever commit are kept, and you can retrieve any committed revision any time. This means you have a combined backup and means to undo any changes you ever make. This is how software engineers manage their code projects.

#### Creating a repo

Go to [the SFU Gitlab server](http://gitlab.cs.sfu.ca){:target="_blank"} 
which is on the web at 
[gitlab.cs.sfu.ca](http://gitlab.cs.sfu.ca){:target="_blank"}.
Log in with your SFU username and password, the same one you use to check your
e-mail on SFU Connect.

Once logged in, you will see a list of your existing repos. You probably have none right
now, so let's create one for CMPT413 or CMPT825 by clicking the `New Project`
button at the top right of the page.

On the `New Project` page, give your repo a name to the right of
the `Project name` field. Name your repo either: `nlpclass-{{site.semcode}}-groupname`
or `nlpclass-{{site.semcode}}-groupname` where `groupname` is your group name.

It's important to name the repo exactly as you see here. Leave all
other settings as they are and click the `Create Project`
button at the bottom left of the page. 

Make sure you do not change the default setting of
`Private`. Your repo must be visible only to yourself.
In other words, no other student can access it by default.
**You must not give access to your repo to any other students - plagiarism is a serious
academic offense, which applies as much to code as it
does to essays and exams.** 

Your repo has now been created. You will be taken to a web page for
your newly created repo.

The course instructor needs access to your repo in order to test
and  grade your code. Add the instructor as a member of your
repo by clicking on the Settings menu which looks like a gear icon <i class="fa fa-gear"></i>
and selecting `Members` from the dropdown menu. On the page that loads up
type in `{{site.instructor}}` in the `Add new user` box and then change the role permissions from
`Guest` to `Developer` in the dropdown menu. Click on `Add to Project` to add
the instructor to your github repo.

We have to set up your repo to call the automatic grading software.
Follow these steps

1. Click on the Settings menu which looks like a gear icon <i class="fa fa-gear"></i>
    1. Select `Webhooks`.
    1. Click on the link `Add Webhook`:
        1. In the field `URL` enter: `http://unit.csil.sfu.ca:5000/`
        1. Click the `Add Webhook` button near the bottom of the page.

This tells the Gitlab server to send a message to that URL every
time you commit code to your repo. The grading robot will retrieve
your code, test it, and tell you the results.

Next we will set up the Secure Shell (ssh) keys so you can access
your repo without a password. First follow [the instructions on
setting up your SSH key pair](https://csil-git1.cs.surrey.sfu.ca/help/ssh/README)
available at [csil-git1.cs.surrey.sfu.ca/help/ssh/README](https://csil-git1.cs.surrey.sfu.ca/help/ssh/README)

Now we have to copy your public key to the GitLab server.

**The [instructions](https://csil-git1.cs.surrey.sfu.ca/help/ssh/README) ask
you to use `xclip` which may not be installed on the CSIL machines. If you cannot use `xclip` then use the
following steps to set up your ssh key.**

If you have set up your SSH key correctly then you will have a public key. View it

    cat ~/.ssh/id_rsa.pub

This will show you the public key. Use the `Terminal` copy command to **copy**
this into your clipboard. 

Then go to [this page](https://csil-git1.cs.surrey.sfu.ca/profile): [csil-git1.cs.surrey.sfu.ca/profile](https://csil-git1.cs.surrey.sfu.ca/profile)

Use the web browser to paste command to **paste** your public key into the `Key`
box and give it a `Title` (e.g. use the default name provided) and then `Add key`.

#### Logging in to CSIL

It's time to get yourself set up in the CSIL Lab.

CSIL is open starting the second week
of the semester, 24 hours a day, 7 days a week. All your CMPT 127
lab sessions are in CSIL. Log in to the **Linux** machines.  Use
the same username and password as before.

The machines in these rooms have Linux and Windows installed. If
you a machine running Windows, simply restart the machine and select
Linux when prompted.

Once logged into Linux, you should see a familiar desktop interface.
In order to manipulate most of your work, you will need a terminal
window which runs the "shell".

Click the launcher in the upper-left corner of the desktop interface
and start the "Terminal Emulator" application, or Terminal for short.
It should be under the Accessories submenu.  If you can't find it,
then try searching for `Terminal` in the search box.

The Terminal will allow you to type commands to manipulate, run and
test programs in your labs.  But there will be no programming in this lab.
In this lab you are going to use Git.

#### Git clone (command line)

It's time for you to download a copy of your repo to your CSIL
machine.  The action of making a local copy of your online repo is
known as a "clone".

In the terminal window, enter the commands

    git config --global user.name your-username 
    git config --global user.email your-username@sfu.ca
    cd $HOME
    git clone git@csil-git1.cs.surrey.sfu.ca:your-username/nlpclass-{{site.semcode}}-groupname.git

Substitute your SFU `username` and `groupname` above.

If you did skipped any of the above steps in setting up your GitLab repo this command will not work.
The system might prompt you for a username/password combo.  Supply the usual
answers. To avoid entering your username/password over and over again you can
set up [passwordless ssh](http://www.linuxproblem.org/art_9.html).

Your repo will be cloned into a new directory (also known as a folder).

If you enter the command 

    ls

it should give you a *directory listing*, a list of all
files and subdirectories.  If you see your repo directory
you've managed a successful clone. If not, ask for help from the TAs.

The clone command downloads a copy of the entire repo into
your local machone. It still exists on the server. Once you have a
local clone, you can modify it and then inform the Git server about
the changes you made. Let's do that next.

Just a heads up about the directory `$HOME/sfuhome` on CSIL machines. 
You can clone inside your `$HOME` directory. You should not work inside your
`$HOME/sfuhome` directory.
    
### Exams
    
*  If you must miss an exam because of a medical problem, you should make an attempt to contact me prior to the exam either by email or a message in my mailbox. 
* To request an extension of the due date due to a medical problem, you must submit the <a href="http://students.sfu.ca/forms.html">offical SFU Health Care Provider statement</a>. 
* If you miss an exam due to valid medical reasons you will be graded on your performance on the rest of the course. 
* Make up exams will not be given under any circumstances. 
    
### Academic Honesty 
 
* Some examples of unacceptable behaviour:
     *  Handing in assignments that are not 100% your own work (in design, implementation, wording, etc.), without proper citation. There must be a README file in your submission with citations to any external code used. 
     *  Using any unpermitted resources during an exam. 
     *  Looking at, or attempting to look at, another student's paper during an exam. 
     *  Submitting work that has been submitted before, for any course at any institution. 
* If you are unclear on what academic honesty is, see <abbr title="Simon Fraser University" class="obvious">SFU</abbr>'s [Policy S10-01](http://www.sfu.ca/policies/Students/index.html) and the [University code of academic honesty](http://www.sfu.ca/policies/teaching/index.htm).
* All instances of academic dishonesty will be dealt with very severely. 
* In general, minimum requested penalties will be as follows:
     * For assignments: a mark of -100% on the assignment.  So, academic dishonesty on an assignment worth 5% of your final mark will result in a zero on the assignment, and a penalty of 5% from your final grade. 
     * For exams: an F in the course. 
     * Please note that these are minimum penalties.  At the instructor's option, more severe penalties may be given/requested. __All__ instances of academic dishonesty will be noted on your University record. 
*  The instructor may use, or require students to submit assignments to, an automated service that will check for plagiarism. 
 
### Exams and Tests 
 
* Exams may be written in either pen or pencil.  Calculators or other aids are not allowed unless explicitly stated. 
* Midterm exams and other tests will not be returned to you. You can examine them during office hours for the TA or the instructor.
* Final exams are not returned to students by University policy; they are kept by the instructor. 
* If you miss a test or exam, you must present a note from a doctor to get a mark other than zero.  Arrangements to make up the lost marks will be made on a case-by-case basis by the instructor.  Make-up exams may be given as an oral examination. 
* You must get a pass on the weighted average of the exams and final course project (if this is applicable) to pass the course. 
 
### Mark Appeals 

Except for final grades, this is how you can go about getting your mark changed:

* Requests for a change in your mark must come to the course instructor.  TAs will not change your mark, except for errors in addition or data entry. 
* Requests should come in the same form as you received your marks: if you got marks by email, forward that email to the instructor; if you had paper handed back, return that. 
* You should give a brief explanation of why you want your mark reevaluated.
* The instructor will remark the entire assignment/test.  This will be your mark, whether it is higher or lower than the original. 
* Appeals may be made up to two weeks after the mark is returned or until the final exam date, whichever is _first_.  After that deadline, you must make a formal mark appeal for any changes. 
* For exams in particular, these are _not_ reasons to get more marks:
    * I knew what I was saying here, but didn't write it. 
    * This is the correct answer for some question other than the one asked, but I didn't get any marks for it. 
    * I didn't understand the question. 
    * [I worked really really hard but got the answers wrong](https://en.wikipedia.org/wiki/Dunning%E2%80%93Kruger_effect).
 
### Final Exam and Final Marks Appeals 

If you're concerned about your mark at the end of the course, you can see the instructor.  Here are some guidelines:
 
* You can come to the instructor's office at designated times to review your final exam. 
* Like assignments, you can ask the instructor to reevaluate your final exam marking. 
* The following are not good reasons to get a higher final mark:
    * I want it. 
    * I think I deserve it. 
    * I need it. 
    * I'm close to the next grade cutoff. 
* This is a good reason:
    * There's a marking irregularity on my final or some other piece of work. 
*  The marking scheme is fixed.  If you did badly on a midterm, you can't weight the final more heavily. 
 
### Disclaimers about this web page
  
* All course information on this web page is tentative and could be in error. It can also change at any time. Confirm crucial dates or information with me in person during class. Double check with SFU calendar or schedule information for official class times and final exams time and location. 
* Students are expected to attend all classes: announcements about assigned readings, homeworks and exams will be made available at the start of each class. Such announcements may not be made on this web page, so don't rely on information here instead of attending class. 

