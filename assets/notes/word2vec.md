---
layout: default
title: word2vec
active_tab: syllabus
---

## Word2Vec Practice

### Question 1

Suppose a classifier predicts each possible class with equal
probability. If there are a 100 classes what will be the cross
entropy error on a single example?

| 1. | -log(100) |
| 2. | -log(0.01) | 
| 3. | -log(0.1) | 
| 4. | -0.01 log(1) |
| 5. | -100 log(0.01) |
{: .table}

### Question 2

Alice and Bob have each used the word2vec algorithm (either
skip-gram or CBOW) for the same vocabulary $V$.

Alice obtained "context" vectors $v_w^A$ and "center" or "target" vectors $u_w^A$ for each $w \in V$.
Similarly, Bob obtained "context" vectors $v_w^B$ and "center" vectors $u_w^B$ for each $w \in V$.

Suppose that for every pair of words $w, w' \in V$ the inner product or dot product is the 
same in both models:

$$ u_w^A \cdot v_w^A = u_w^B \cdot v_w^B $$

Does it follow that for every $w \in V$ that $v_w^A = v_w^B$? Why or why not?

### Question 3

For the continuous bag of words (CBOW) model of word2vec we use the average of
the context vectors: 

$$\frac{1}{2k} (v_{i-k} + \ldots + v_{i-1} + v_{i+1} + \ldots + v_{i+k}) $$

Briefly explain why we cannot use negative sampling to train this model.

### Question 4

For the continuous bag of words (CBOW) model of word2vec we use the following
classifier to predict the "center" word:

$$ \hat{y} = \textrm{softmax}( U \cdot \hat{v} ) $$

1. Write down the definition of matrix $U$ in terms of the parameters $u_w$ for each $w \in V$
2. Write down the dimensions of matrix $U$


### Acknowledgements

Some of these questions are modified versions of questions from the Stanford University course cs224n.

