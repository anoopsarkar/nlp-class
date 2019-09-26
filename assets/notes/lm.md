---
layout: default
title: n-gram language models
active_tab: syllabus
---

## n-gram Language models

### Question 1

Consider the following sentence $s$ where `<bs>` and `<es>` are padding tokens:

    <bs> <bs> I would like to go West . <es>

1. Write down $P(s)$ using a bigram language model.
1. Write down $P(s)$ using a trigram language model.

### Question 2

Using a vocabulary $${\cal V} = \{$$ crazy, killer, clown $$\}$$ define a language model which has a particular constraint: $$p(x_1, \ldots, x_n) = \gamma \times 0.5^n$$ for any $$x_1, \ldots, x_n$$ such that $$x_i \in {\cal V}$$ for $$i = 1, \ldots, n-1$$ and $$x_n =$$ STOP.

$$\gamma$$ is some expression that can be a function of $$n$$.

Choose one of the following definitions of $$\gamma$$ so that $$p(x_1, \ldots, x_n)$$ is a valid language model.

| 1. | $$3^{n-1}$$ |
| 2. | $$3^n$$ |
| 3. | $$1$$ |
| 4. | $$\frac{1}{3^n}$$ |
| 5. | $$\frac{1}{3^{n-1}}$$ |
{: .table}

Hint: $$\sum_{n=1}^\infty 0.5^n = 1$$.

### Question 3

The perplexity of a language model on a test corpus is defined as 

$$2^{-\ell}$$

where

$$\ell = \frac{1}{M} \sum_{i=1}^m \log_2 p(x^{(i)})$$

where $$m$$ is the number of sentences in the corpus, $$M$$ is the total number of words in the corpus,
$$\log_2$$ is log base 2, $$x^{(i)}$$ is the $$i$$'th sentence in the corpus. 

1. What is the maximum value for perplexity $$2^{-\ell}$$.
1. What is the minimum value for perplexity $$2^{-\ell}$$.
1. Assume we have a bigram language model where

   $$p(w_1, \ldots, w_n) = \prod_{i=1}^n q(w_i \mid w_{i-1})$$

   and $$w_0 = \ast$$ and $$w_n =$$ STOP. Each parameter $$q(w \mid v)$$ is calculated as follows:

   $$q(w \mid v) = \frac{C(v,w)}{C(v)}$$

   C($$\cdot$$) is the count of that item in training data.
   Write down a training corpus and a test corpus such that the
   perplexity of the model trained on the training corpus takes the
   maximum possible value on the test corpus.
1. Write down a training corpus and a test corpus such that the perplexity of the model trained on 
   the training corpus takes the minimum possible value on the test corpus. (Assume that we use a 
   bigram language model as in the previous question).

### Question 4

We define a trigram language model as follows. Take $$C(w),
C(v, w)$$ and $$C(u, v, w)$$ to be unigram, bigram and trigram
counts taken from a training corpus (here $$w$$ is a single word, $$v, w$$
is a bigram, and $$u, v, w$$ is a trigram). Take $$N$$ to be the total
number of words seen in the corpus. Then the unigram, bigram and
trigram maximum-likelihood estimates are:

$$q(w) = \frac{C(w)}{N}$$

$$q(w \mid v) = \frac{C(v,w)}{C(v)}$$

$$q(w \mid u, v) = \frac{C(u,v,w)}{C(u,v)}$$

The final estimate of the trigram probability is:

$$p(w \mid u, v) = \alpha \times q(w \mid u, v) + (1 - \alpha) \times \left( \beta \times q(w \mid v) + (1 - \beta) \times q(w) \right)$$

Assume that $$\alpha = \beta = 0.5$$. Show that the above model is equivalent to the following model by providing 
values for $$\lambda_1, \lambda_2, \lambda_3$$.

$$p(w \mid u, v) = \lambda_1 \times q(w \mid u, v) + \lambda_2 \times q(w \mid v) + \lambda_3 \times q(w)$$

### Question 5

Consider the following corpus of sentences where `<bs>` and `<es>` are padding tokens:

    <bs> I am Sam <es>
    <bs> Sam I am <es>
    <bs> I do not like green eggs and ham <es>

Fill in the following table:

| P(`I` \| `<bs>`) = |  | P(`Sam` \| `<bs>`) = |  | P(`am` \| `I`) = | |
| P(`<es>` \| `Sam`) = |  | P(`Sam` \| `am`) = |  | P(`do` \| `I`) = | |
{: .table}

### Acknowledgements

Some of these questions are modified versions of questions from the Columbia University course COMS 4705 by Michael Collins.

