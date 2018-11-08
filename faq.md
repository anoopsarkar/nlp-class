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

  | **Final Grade** | **Final marks** |
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
    
* Your group has to submit several deliverables for each homework:
    * Source code for your homework will be submitted electronically on [courses.cs.sfu.ca](https://courses.cs.sfu.ca/).
    * Python notebook documenting your work
    * README files for each member of the group
* All homeworks are due by 11:59PM on the homework due date.
* Each homework comes with 2 grace days. However the grace days only apply to those who have a valid submission on the due date (a submission that scores -1 or -inf is invalid). For example, if your homework deadline is Tuesday 11:59PM and you submit a valid solution then you have until Thursday night 11:59PM to modify your homework submission.
* We will make every attempt to release grades for each homework the week it is due. However, this means that after we review the source code we might have to lower your official grade. If you cheated in some way, such as copying your submission or you have violated the ground rules for each homework, your grades will be decreased from the initial value.

### Groups
    
* The homework assignments will be solved in groups. Groups are typically 3 to 5 people. All groups must be formed before Homework 0 is due.
* You are allowed to leave a group and form a group of size one at the start of each homework but not at the end.
* Each group will create a single submission and upload it before the due date.
* Each group member will be graded on their self report and any commit logs that are submitted. If the TA or the instructor perceives there is a problem with collaboration in a group, certain group members can get zero marks. If you are pair programming, take turns in switching the user doing the commits to the repository.
* __Effective group collaboration__: We are looking to see effective collaboration to solve the homework assignment. People can play different roles and sometimes more than one role in the same homework:
    * Designer: creates a plan for implementation and coordinates activities of the group. Should create design docs (text files or markdown or equivalent only). Put these documents in the directory `docs` and mention the files in your `README.username` file (where `username` is your SFU login username).
    * Code reviews: write a critical view of the implementation by the group. Points out what is missing, inelegant code, etc. and produces a code review document (text files or markdown or equivalent only). Put these documents in the directory `docs` and mention the files in your `README.username` file.
    * Development: write the code. This can be done in collaboration. 
    * Testcases: write testcases to stress test the code. Provide the testcases in your submission.
* **Warning**: if you are missing a `README.username` file in your group source submission then that `username` might get zero marks.
* Use `git` for version control and effective collaboration. See the section below on setting up `git` for this course.

### CSIL
    
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

Just a heads up about the directory `$HOME/sfuhome` on CSIL machines. 
You should clone your repo inside your `$HOME` directory. You should not work inside your
`$HOME/sfuhome` directory.

### Exams
    
* If you must miss an exam because of a medical problem, you should make every attempt to contact me prior to the exam either by email or a message in my mailbox. 
* To request an extension of the due date due to a medical problem, you must submit the <a href="http://students.sfu.ca/forms.html">offical SFU Health Care Provider statement</a>. 
* If you miss an exam due to valid medical reasons you may have to take a make-up exam or you may be graded on your performance on the rest of the course. 
    
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
    * I will be kicked out of the university if I do not pass.
* This is a good reason:
    * There's a marking irregularity on my final or some other piece of work. 
*  The marking scheme is fixed.  If you did badly on a midterm, you can't weight the final mark more heavily. 
 
### Disclaimers about this web page
  
* All course information on this web page is tentative and could be in error. It can also change at any time. Confirm crucial dates or information with me in person during class. Double check with SFU calendar or schedule information for official class times and final exams time and location. 
* Students are expected to attend all classes: announcements about assigned readings, homeworks and exams will be made available at the start of each class. Such announcements may not be made on this web page, so don't rely on information here instead of attending class. 

