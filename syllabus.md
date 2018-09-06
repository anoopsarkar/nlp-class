---
layout: default
img: artsrouni
img_link: http://www.hutchinsweb.me.uk/IJT-2004.pdf
caption: "Georges Artsrouni's mechanical brain, a translation device patented in 1933 in France."
title: Syllabus
active_tab: syllabus
---

## Syllabus

The syllabus is preliminary and subject to change.

<style type="text/css">
    .bs-example{
        margin: 20px;
    }
</style>

<div class="bs-example">
    <div class="panel-group" id="accordion">
        {% for week in site.data.syllabus %}
            {% if week.include %}
            <div class="panel panel-default">
                <div class="panel-heading">
                    <h4 class="panel-title">
                        <a data-toggle="collapse" data-parent="#accordion" href="#{{ week.tag }}">{{ week.title }}</a>
                    </h4>
                </div>
                {% if week.current %}
                <div id="{{ week.tag }}" class="panel-collapse collapse in">
                {% else %}
                <div id="{{ week.tag }}" class="panel-collapse collapse">
                {% endif %}
                <div class="panel panel-default">
                  {% if week.notes %}
                      <div class="panel-heading">
                        <h3 class="panel-title">Lecture notes</h3>
                      </div>
                      <ul class="list-group">
                      {% for notes in week.notes %}
                        <li class="list-group-item"> <a href="{{ notes.url }}">{{ notes.title }}</a>
                            {%if notes.video %}
                                <a href="{{ notes.video }}"><span class="glyphicon glyphicon-film"></span></a>
                            {% endif %}
                            {% if notes.download %} 
                                <a href="{{ notes.download }}"><span class="glyphicon glyphicon-save"> </span></a> 
                            {% endif %}
                            {% if notes.author %} 
                                ({{ notes.author }}) 
                            {% endif %}
                        </li>
                      {% endfor %}
                      </ul>
                  {% endif %}
                  {%if week.links %}
                      <div class="panel-heading">
                        <h3 class="panel-title">Links (<i class="fa fa-star"></i>=optional)</h3>
                      </div>
                      <ul class="list-group">
                      {% for link in week.links %}
                        <li class="list-group-item"> 
                        {% if link.optional %}
                            <i class="fa fa-star"> </i>
                        {% else %}
                            <i class="fa"> </i> 
                        {% endif %}
                        <a href="{{ link.url }}">{{ link.title }}</a>.
                            {%if link.author %}
                                {{ link.author }}.
                            {% endif %}
                            {%if link.citation %}
                                {{ link.citation }}.
                            {% endif %}
                            {%if link.video %}
                                <a href="{{ link.video }}"><span class="glyphicon glyphicon-film"></span></a>
                            {% endif %}
                            {% if link.download %} 
                                <a href="{{ link.download }}"><span class="glyphicon glyphicon-save"> </span></a> 
                            {% endif %}
                        </li>
                      {% endfor %}
                      </ul>
                  {% endif %}
                </div>
                </div>
            </div>
            {% endif %}
        {% endfor %}
    </div>
</div>

