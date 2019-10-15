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

### Question 5

Let us assume we have an English dataset of sentences:


    We have all seen how President Obama has made research and development a key plank of his stimulus package. 
    If you're a pirate fan, it's time to make those pitiful black-clad landlubbers walk the plank. 
    ...

And a French dataset of sentences:

    Nous avons tous vu comment le président Obama a fait de la recherche et du développement un des piliers de ses mesures de relance.
    Si vous avez l'âme d'un pirate, vous vous ferez un plaisir de pousser ces gars en pyjama noir sur la planche.  
    ...

The English and French sentences are not necessarily translations of each other. Also assume we have
a bilingual dictionary that provides pairs of words in English and French which are translations 
of each other:

    plank, piliers
    plank, planche

Assume you have been given a word2vec model for English $\hat{Q}^E$ with
parameters $v_i^E$ and $u_i^E$ for each English word $w_i \in {\cal
V}_E$ where ${\cal V}_E$ is the English vocabulary. Similarly we
have a word2vec model for French $\hat{Q}^F$ with parameters $v_j^F$ and $u_j^F$
for each French word $w_j \in {\cal V}_F$ where ${\cal V}_F$ is the
French vocabulary.

The retrofitting objective for matrix $Q$ and $\hat{Q}$ is
given by the following objective function $L(Q)$ where there is some semantic
relation edge ${\cal E}$ between words $w_i$ and $w_j$. We wish to find a matrix
$Q = (q_1, \ldots, q_n)$ such that the
columns of the matrix $Q$ are close (in vector space) to the word vectors in $\hat{Q} = (\hat{q}_1, \ldots, \hat{q}_n)$
(so $q_i$ is close to $\hat{q}_i$) and at the same time the columns
of the matrix $Q$ are close (in vector space) to the word vectors
of other words connected via an edge ${\cal E}$. So if $(w_i, w_j)$
are connected by an edge then we want $q_i$ and $q_j$ to be close in vector space. 

$$ L(Q) = \sum_{i=1}^n \left[ \alpha_i || q_i - \hat{q}_i ||^2 + \sum_{(i,j) \in {\cal E}} \beta_{ij} || q_i - q_j ||^2 \right] $$

1. Provide a new retrofitting objective function $L_E(Q_E)$ by using the word2vec models for English and French. The objective function $L_E(Q_E)$ should ensure that 
English words that were close in vector space in $Q_E$ remain close but are also close in vector space to their translation pairs in the bilingual dictionary. For example,
if English words `plank` and `deal` were close in vector space in $\hat{Q}_E$ they should remain close in $Q_E$, and at the same time
if `plank` was listed as a translation pair with `piliers` then their respective word vectors should be close in vector space as well.
2. Provide the initialization step for $Q_E$.
3. Provide a similar retrofitting objective function and initialization step for French $L_F(Q_F)$.


### Acknowledgements

The first few questions here are modified versions of questions from the Stanford University course cs224n.

