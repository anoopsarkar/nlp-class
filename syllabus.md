---
layout: default
img: artsrouni
img_link: http://www.hutchinsweb.me.uk/IJT-2004.pdf
caption: "Georges Artsrouni's mechanical brain, a translation device patented in 1933 in France."
title: Syllabus
active_tab: syllabus
---

<table class="table table-striped"> 
  <tbody>
    <tr>
      <th>Date</th>
      <th>Topic</th>
      <th>Readings/Videos (<i class="fa fa-star"></i>=optional)</th>
    </tr>
    {% for lecture in site.data.syllabus.past %}
    <tr>
      <td>{{ lecture.date | date: "%b %d" }}</td>
      <td>
        {% if lecture.slides %}<a href="{{ lecture.slides }}">{{ lecture.title }}</a>
        {% else %}{{ lecture.title }}{% endif %}
      {% if lecture.links %}
        {% for link in lecture.links %}
          <p><a href="{{ link.url }}">{{ link.text }}</a></p>
        {% endfor %}
      {% endif %}
        {% if lecture.language %}
        <br/><a href="lin10.html">Language in 10</a>: <a href="{{ lecture.language_slides }}">{{ lecture.language }}</a>
        {% endif %}
      </td>
      <td>
        {% if lecture.reading %}
          <ul class="fa-ul">
          {% for reading in lecture.reading %}
            <li>
            {% if reading.optional %}<i class="fa-li fa fa-star"> </i>
            {% else %}<i class="fa-li fa"> </i> {% endif %}
            {% if reading.author %} {{ reading.author }}, {% endif %}
            {% if reading.url %}
            <a href="{{ reading.url }}">{{ reading.title }}</a>
            {% else %}
            {{ reading.title }} 
            {% endif %}
            </li>
          {% endfor %}
          </ul>
        {% endif %}
      </td>
    </tr>
    {% endfor %}

  </tbody>
</table>

