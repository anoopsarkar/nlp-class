---
layout: default
img: C-3PO
img_link: "http://en.wikipedia.org/wiki/Languages_in_Star_Wars"
caption: "In Star Wars, C-3PO is fluent in over six million forms of communication."
title: Course Information
active_tab: main_page
---

## Natural Language Processing <span class="text-muted">{{ site.semester }}</span>

Natural Language Processing (NLP) was traditionally a research field heavily reliant on partially supervised machine learning to tackle language tasks. However, the landscape shifted dramatically with the advent of large language models (LLMs), popularized by tools like ChatGPT. Unlike earlier models, LLMs are trained using self-supervised learning, exhibiting remarkable emergent behavior and tackling a wide range of tasks they were never explicitly trained on. This demonstrates that unsupervised learning is scalable and capable of achieving zero-shot performance, where models perform tasks with little to no task-specific examples.

This course delves into language models and representation learning for NLP. We will explore key components such as model architecture, effective training strategies, and inference techniques, highlighting their applications across diverse natural language processing tasks. As NLP rapidly evolves, LLMs have become a cornerstone of artificial intelligence research and development.

#### Instructor
* [Anoop Sarkar](http://www.cs.sfu.ca/~anoop/)

#### Teaching Assistants
<ul>
{% for ta in site.tas %}
<li>{{ ta.name }}, <code>{{ ta.email }}</code>, Office hour: {{ ta.officehour }}.</li>
{% endfor %}
</ul>

#### Asking for help
* Ask for help on [the discussion forum]({{ site.coursys }}/forum)
* Instructor office hours: Thu 8:30-9:30am (starts on Sept 21); Zoom link on Coursys discussion forum
* <b>No emails</b> to the TAs and strictly emails about personal matters to the instructor
* Always post to the [the discussion forum]({{ site.coursys }}/forum) instead of email. If you have to email use your SFU email address only.

#### Time and place
* Wed 9:30-10:20am Blusson Hall [BLU10011](http://www.sfu.ca/campuses/maps-and-directions/burnaby-map.html)
* Fri 8:30am-10:20am Blusson Hall [BLU10011](http://www.sfu.ca/campuses/maps-and-directions/burnaby-map.html)
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
