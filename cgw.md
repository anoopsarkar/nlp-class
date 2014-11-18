---
layout: default
img: embedding
img_link: http://en.wikipedia.org/wiki/Center_embedding
caption: "The Embedding introduces a strange form of language whose grammar can be 'self-embedded' by computers."
title: "Competitive Grammar Writing"
active_tab: homework
---

Competitive Grammar Writing in Python
=====================================

Get started:

    git clone https://github.com/anoopsarkar/cgw.git

This task involves writing or creating weighted context-free grammars
in order to parse English sentences and utterances. The vocabulary
is fixed. 

## Notation

A context-free grammar (CFG) is defined using the following building blocks:

* $$N$$, a set of non-terminal symbols (these symbols do not appear in the input)
* $$S$$, one non-terminal from $$N$$ called the start symbol. All derivations in a CFG start from $$S$$
* $$V$$, a vocabulary of words called terminal symbols. $$N$$ and $$V$$ are disjoint
* Rules of the form: $$A \rightarrow \alpha$$ where $$A \in N$$ and $$\alpha \in (N \cup V)^\ast$$.
* Weights or frequencies or probabilities can be associated with each rule in a CFG.

A context-free grammar that is in extended Chomsky Normal Form
(eCNF) iff the right hand side of each CFG rule is either one
non-terminal, or two non-terminals, or one terminal symbol.

## The Data

Initial versions of the context-free grammar files are provided to you:

* `S1.gr`: the default grammar file contains a context-free grammar in eCNF.
* `S2.gr`: the default backoff grammar file.
* `Vocab.gr`: the vocabulary file contains rules of the type `A -> a` where `A` is a non-terminal that represents the part of speech and `a` is a word (also called a terminal symbol).

Here is a fragment of `S1.gr`. Each line is a weighted context-free
grammar rule. First column is the weight, second column is the
left-hand side non-terminal of the CFG rule and the rest of the
line is the right-hand side of the CFG rule:

    1   S1   NP VP
    1   S1   NP _VP
    1   _VP  VP Punc
    20  NP   Det Nbar
    1   NP   Proper

The non-terminal `VP` is used to keep the grammar in eCNF. The
probability of a particular rule is obtained by normalizing the
weights for each left-hand side non-terminal in the grammar. For
example, for rule `NP -> Det Nbar` the probability
is $$\frac{20}{20+1}$$.

The grammars in `S1.gr` and `S2.gr` are connected via the following rules in `S1.gr`:

    99 TOP  S1
    1  TOP  S2
    1  S2   Misc

## Other files

* `allowed_words.txt`: This file contains all the words that are allowed. You should make sure that your grammar generates sentences using exactly the words in this file. It does not specify the part of speech for each word, so you can choose to model the ambiguity of words in terms of part of speech in the `Vocab.gr` file.
* `example-sentences.txt`: This file contains example sentences that you can use as a starting point for your grammar development. Only the first two sentences of this file can be parsed using the default `S1.gr` grammar. The rest are parsed with the backoff `S2.gr` grammar. 
* `unseen.tags`: Used to deal with unknown words. You should not have to use this file during parsing, but the parser provided to you can optionally use this file in order to deal with unknown words in the input. 

## The Parser and Generator

You are given a parser that takes sentences as input and produces
parse trees and also a generator which generates a random sample
of sentences from the weighted grammar. Parsing and generating will
be useful steps in your grammar development strategy. You can learn
the various options for running the parser and generator using the
following command.

The parser has several options to speed up parsing, such as beam
size and pruning. Most likely you will not need to use those options
(unless your grammars are huge).

    python pcfg_parse_gen.py -h

### Parsing input

The parser provided to you reads in the grammar files and a set of
input sentences. It prints out the single most probable parse tree
for each sentence (using the weights assigned to each rule in the
input context-free grammar). The parser also reports the negative
cross-entropy score for the whole set of sentences. Assume the
parser gets a text of $$n$$ sentences to parse: $$s_1, s_2, \ldots,
s_n$$ and we write $$|s_i|$$ to denote the length of each sentence
$$s_i$$. The probability assigned to each sentence by the parser is
$$P(s_1), P(s_2), \ldots, P(s_n)$$. The negative cross entropy is the
average log probability score (bits per word) and is defined as
follows:

<p>$$\textrm{score}(s_1, \ldots, s_n) = \frac{ \log P(s_1) + \log P(s_2) + \ldots + \log P(s_n) }{ |s_1| + |s_2| + \ldots + |s_n| }$$</p> 

We keep the value as negative cross entropy so that higher scores
are better. 

    python pcfg_parse_gen.py -i -g "*.gr" < example_sentences.txt
    #loading grammar files: S1.gr, S2.gr, Vocab.gr
    #reading grammar file: S1.gr
    #reading grammar file: S2.gr
    #reading grammar file: Vocab.gr

    ... skipping the parse trees ...

    #-cross entropy (bits/word): -10.0502

### Generating output

In order to aid your grammar development you can also generate
sentences from the weighted grammar to test if your grammar is
producing grammatical sentences with high probability. The following
command samples 20 sentences from the `S1.gr,Vocab.gr` grammar
files. 

    python pcfg_parse_gen.py -o 20 -g S1.gr,Vocab.gr
    #loading grammar files: S1.gr, Vocab.gr
    #reading grammar file: S1.gr
    #reading grammar file: Vocab.gr
    every pound covers this swallow
    no quest covers a weight
    Uther Pendragon rides any quest
    the chalice carries no corner .
    any castle rides no weight
    Sir Lancelot carries the land .
    a castle is each land
    every quest has any fruit .
    no king carries the weight
    that corner has every coconut
    the castle is the sovereign
    the king has this sun
    that swallow has a king
    another story rides no story
    this defeater carries that sovereign
    each quest on no winter carries the sovereign .
    another king has no coconut through another husk .
    a king rides another winter
    that castle carries no castle
    every horse covers the husk .

## Acknowledgements

The idea for this task and the original data files are taken from the following paper: 

> Jason Eisner and Noah A. Smith. [Competitive Grammar Writing](http://aclweb.org/anthology/W/W08/W08-0212.pdf). In Proceedings of the ACL Workshop on Issues in Teaching Computational Linguistics, pages 97-105, Columbus, OH, June 2008.

