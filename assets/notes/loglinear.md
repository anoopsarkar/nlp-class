---
layout: default
title: Log linear models
active_tab: syllabus
---

## Log linear models

### Question 1

Consider the computation of the conditional log probability $\log \Pr(y \mid \textbf{x}; \textbf{v})$ where $\textbf{x}$ is the input to the classifier and $y$ is the output label from this classifier. 

$$ \log \Pr(y \mid \textbf{x}; \textbf{v}) = \underbrace{\textbf{v} \cdot \textbf{f}(\textbf{x}, y)}_{\textrm{linear term}} - \underbrace{\log \sum_{y'} exp\left( \textbf{v} \cdot \textbf{f}(\textbf{x}, y') \right)}_{\textrm{normalization term}} $$

Assume you have been given a trained model $\textbf{v}$. Can we replace the classifier with the following version at test time:

$$ \log \Pr(y \mid \textbf{x}; \textbf{v}) = \textbf{v} \cdot \textbf{f}(\textbf{x}, y) $$

Explain why or why not.

### Question 2

In order to define a log-linear model for a task we need a vector of size $k$ which are the features $\textbf{f}_k (x, y)$ for each output label $y \in {\cal Y}$. 
Let $|{\cal Y}|$ be the number of output labels. Assume that the input $x$ is a single word from a vocabulary ${\cal V}$. 
Define the feature vector to be a one-hot vector of size $|{\cal V}|$ associated with each output label $y$. 
To create this one-hot vector each word is assigned an arbitrary number (assume the words are lexicographically sorted and assigned a number based on the sorted order). 
Which of the following statements is true:
$$
\begin{eqnarray}
k &=& |{\cal V}| + |{\cal Y}| \\
k &=& |{\cal V}| \times |{\cal Y}| \\
|{\cal V}| &=& k \times |{\cal Y}| \\
|{\cal V}| &=& k \times \log( |{\cal Y}| ) \\
|{\cal V}| &=& \frac{k}{|{\cal Y}|} \\
|{\cal Y}| &=& \frac{k}{|{\cal V}|} \\
|{\cal Y}| &=& \frac{|{\cal V}|}{k} \\
|{\cal Y}| &=& \frac{\log( |{\cal V}| )}{k} 
\end{eqnarray}
$$

### Question 3

Consider the following pseudo-code for finding $\textrm{argmax}_y$ from $\log \Pr(y \mid \textbf{x}; \textbf{v})$ where the input $\textbf{x}$, the parameters $\textbf{v}$ are given as input and the set of possible labels ${\cal Y}$ are given.

- define $\textrm{argmax}_y$($\textbf{x}$, $\textbf{v}$, ${\cal Y}$)
    - $m \leftarrow \infty$ (in Python: `float("inf")`)
    - for $y \in {\cal Y}$:
        - $s \leftarrow - \log \Pr(y \mid \textbf{x}; \textbf{v})$
        - if $s < m$ then:
            - $m \leftarrow s$
            - return $y$

Is the pseudo-code correct? If not, provide the correct pseudo-code.

### Question 4

Assume we have a bigram language model $\Pr(w_1, \ldots, w_n)$ that is defined using a log-linear model.

$$ \Pr(w_1, \ldots, w_n) = \prod_{i=1}^n p(w_i \mid w_{i-1}; \textbf{v}) $$

where the bigram probabilities $p(w_i \mid w_{i-1}; \textbf{v})$ is defined using a log-linear model.
The log-linear model uses a feature vector definition $f(u, v) \in \mathbb{R}^d$ that maps each bigram
$(u, v)$ to a $d$ dimensional feature vector and uses a parameter vector $\textbf{v} \in \mathbb{R}^d$.

$$ \log \Pr(w_i \mid w_{i-1}; \textbf{v}) = \textbf{v} \cdot \textbf{f}{(w_{i-1}, w_i)} - \log \sum_{w'} exp\left( \textbf{v} \cdot \textbf{f}(w_{i-1}, w') \right) $$

Let the vocabulary size be \|V\|. Show that it is possible to define a log-linear bigram language model with a single feature such that $d=1$ with the following properties:

$$ p(w_i \mid w_{i-1}; \textbf{v}) = 0.9 \textrm{ if } w_i=w_{i-1} $$
and
$$ p(w_i \mid w_{i-1}; \textbf{v}) = \frac{0.1}{|V|-1} \textrm{ if } w_i \neq w_{i-1} $$ 

Provide the definition of the single feature $f_1(u, v) \in \mathbb{R}$
and the value of the parameter $v_1 \in \mathbb{R}$ that gives the
above distribution.

### Question 5

In a log-linear model there are two output labels y = {+,-} and
four features f1, f2, f3, f4 defined over input string x over the
alphabet $\{a,b\}^2$ as follows with parameters v1, v2, v3, v4:

| f1(x,y) | = 1 if x[0]=='a' and y=+ 0 otherwise | parameter: v1 |
| f2(x,y) | = 1 if x[0]=='a' and y=- 0 otherwise | parameter: v2 |
| f3(x,y) | = 1 if x[1]=='b' and y=+ 0 otherwise | parameter: v3 |
| f4(x,y) | = 1 if x[1]=='b' and y=- 0 otherwise | parameter: v4 |
{: .table}

Provide the expression for the following input strings using the
value of the features (0 or 1) and use the parameters v1, v2, v3,
v4 in your answer since we do not know their values yet.:

1. P(y=+ | x=ab)
1. P(y=- | x=ab)
1. P(y=+ | x=bb)
1. P(y=- | x=bb)

### Acknowledgements

Some of these questions are modified versions of questions from the Columbia University course COMS 4705 by Michael Collins.

