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
the context vectors for window size $m$: 

$$\hat{v} = \frac{1}{2k} (v_{i-m} + \ldots + v_{i-1} + v_{i+1} + \ldots + v_{i+m}) $$

Each $v_j$ is a word vector of dimension $k$. CBOW uses the following classifier to predict the "center" word:

$$ \hat{y} = \textrm{softmax}( U \cdot \hat{v} ) $$

1. Write down the dimension of the $\hat{y}$ vector.
2. Write down the value of $\sum_i \hat{y}_i$
3. Write down the definition of matrix $U$ in terms of the parameters $u_w$ for each $w \in V$.
4. Write down the dimensions of matrix $U$.
5. Briefly explain why we cannot use negative sampling (without modification) to train this model.

### Question 4

The sigmoid function maps input values into $[0,1]$. 

$$ \sigma(z) = \frac{1}{1 + exp(-z)} $$

We can define a two class classifier using the sigmoid:

$$P(Y=1 \mid x) = \sigma(\beta x)$$

$$P(Y=2 \mid x) = 1 - P(Y=1 \mid x)$$

Instead of two classes assume we have $k$ output labels, $Y = 1, \ldots k$
We can use the softmax function for this:

$$P(Y=i \mid x) = \frac{exp(\beta_i x)}{\sum_j exp(\beta_j x)}$$

Show that for $k=2$ these two definitions: the softmax and the sigmoid
are equivalent with $\beta$ in the sigmoid function being equal to $- (\beta_1 - \beta_2)$
in the softmax function over two classes $Y=1,2$.

### Acknowledgements

Some of these questions are modified versions of questions from the Stanford University course cs224n.

