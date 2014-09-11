---
layout: default
img: embedding
img_link: http://en.wikipedia.org/wiki/Center_embedding
caption: "The Embedding introduces a strange form of language whose grammar can be 'self-embedded' by computers."
title: Leaderboard
active_tab: leaderboard
jquery: true
---

Submit your assignments [here](http://sfu-nlp-class.appspot.com). Results will be updated in a few minutes.

<script type="text/javascript" src="//sfu-nlp-class.appspot.com/leaderboard.js"></script>

<table class="table table-hover table-condensed">
  <thead>
    <tr>
      <th>
        Rank
      </th>
      <th>
        Handle
      </th>
      <th class="text-right">
        <a href="hw0.html">#0</a><br/><span class="small text-muted">Setup</span>
      </th>
      <th class="text-right">
        <a href="hw1.html">#1</a><br/><span class="small text-muted">Segment</span>
      </th>
<!---
      <th class="text-right">
        <a href="hw2.html">#2</a><br/><span class="small text-muted">Model score</span>
      </th>
      <th class="text-right">
        <a href="hw3.html">#3</a><br/><span class="small text-muted">Accuracy</span>
      </th>
      <th class="text-right">
        <a href="hw4.html">#4</a><br/><span class="small text-muted">BLEU</span>
      </th>
      <th class="text-right">
        <a href="hw5.html">#5</a><br/><span class="small text-muted">Accuracy</span>
      </th>
-->
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>

<script type="text/javascript" src="leaderboard-code.js"></script>

<div class="panel panel-default"> 
<div class="panel-heading">Legend</div> 

<div class="panel-body"> 

<p>A value of -1 indicates that the assignment file was found but
contained invalid content.</p>

<p>The highlighted lines are <span class="text-success">oracle (best possible)</span>,
<span class="text-danger">default (performance of code provided to you; no marks)</span> and <span class="text-warning">baseline (minimum performance for 74 marks out of 100)</span>. In between <span class="text-danger">default</span> and <span class="text-warning">baseline</span> you can earn upto 54 marks out of 100.</p>

</div>

</div>

### Acknowledgements

The original leaderboard code for Google App Engine was developed by [Matt Post](https://github.com/mjpost) and [Adam Lopez](https://github.com/alopez).

