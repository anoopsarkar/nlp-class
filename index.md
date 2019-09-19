---
layout: default
img: C-3PO
img_link: "http://en.wikipedia.org/wiki/Languages_in_Star_Wars"
caption: "In Star Wars, C-3PO is fluent in over six million forms of communication."
title: Course Information
active_tab: main_page 
---

## Natural Language Processing <span class="text-muted">Fall 2019</span>

Imagine a world where you can pick up a phone and talk in English,
while at the other end of the line your words are [spoken in
Chinese](https://www.youtube.com/watch?v=Nu-nlQqFCKg).  Imagine a
[computer animated representation of
yourself](http://mitpress.mit.edu/books/embodied-conversational-agents)
speaking fluently what you have written in an email. Imagine
automatically uncovering protein/drug interactions in [petabytes
of medical abstracts](http://fable.chop.edu/). Imagine feeding a
computer an ancient script that no living person can read, then
listening as [the computer reads aloud in this dead
language](https://isi.edu/natural-language/mt/decipher.html).
Imagine a computer that can [do better than humans at answering
questions](https://www.youtube.com/watch?v=lI-M7O_bRNg).  

Natural Language Processing is the automatic analysis of human
languages such as English, Korean, and thousands of others analyzed
by computer algorithms. Unlike artificially created programming
languages where the structure and meaning of programs is easy to
encode, human languages provide an interesting challenge, both in
terms of its analysis and the learning of language from observations.

#### Instructor
* [Anoop Sarkar](http://www.cs.sfu.ca/~anoop/) 

#### Teaching Assistants
<ul>
{% for ta in site.tas %}
<li>{{ ta.name }}, <code>{{ ta.email }}</code>, Office hour: {{ ta.officehour }}.</li>
{% endfor %}
</ul>

#### Asking for help
* Ask for help on [the discussion board]({{ site.coursys }}/discussion)
* Instructor office hours: Thu 9:30-10:30am TASC1 9427
* TA office hours: TBD
* <b>No emails</b> to the TAs and strictly emails about personal matters to the instructor
* Use only SFU email address and use `cmpt413:` or `cmpt825:` (for ugrad and grad respectively) as subject prefix

#### Time and place
* Tue 4:30-5:20 [BLU 9660](http://www.sfu.ca/campuses/maps-and-directions/burnaby-map.html) 
* Thu 3:30-5:20 [BLU 9660](http://www.sfu.ca/campuses/maps-and-directions/burnaby-map.html)
* Last day of classes: {{ site.lastday }}

#### Calendar
* [Subscribe]({{ site.calendar }})

#### Textbook
* No required textbook. Online readings provided in Syllabus.

#### Grading
* Submit homework source code and check your grades on [Coursys]({{ site.coursys }})
* Programming setup homework: HW0 due on {{ site.hwdates[0].deadline }} (2%)
* Four programming homeworks. Due dates: HW1 on {{ site.hwdates[1].deadline }}, HW2 on {{ site.hwdates[2].deadline }}, HW3 on {{ site.hwdates[3].deadline }}, HW4 on {{ site.hwdates[4].deadline }} (10% each)
* In class midterm: {{ site.midterm }} (25%)
* Participation: Helping other students on the discussion board in a positive way (5%)
* Final Project Proposal: Due on {{ site.hwdates[5].proposal }} (5%)
* Final Project: Due on {{ site.hwdates[5].deadline }} (23%)
* Final Project Poster Session:
    * Time: {{ site.hwdates[5].deadline }} {{ site.hwdates[5].time }}. 
    * Location: {{ site.hwdates[5].location }}

