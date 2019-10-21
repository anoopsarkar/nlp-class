Warning: the following solutions may contain error.

# 1. n-gram Language models

## Question 1

1.
$$Pr(s) = \\  Pr(<bs>|<bs>) \cdot \\  Pr('I'|<bs>) \cdot \\  Pr('would'|'I') \cdot \\  Pr('like'|'would') \cdot \\  Pr('to'|'like') \cdot \\  Pr('go'|'to') \cdot \\  Pr('West'|'go') \cdot \\  Pr('.'|'West') \cdot \\  Pr(<es>|'.') $$ 

2. 
$$  Pr(s) = \\  Pr('I'|<bs>,<bs>) \cdot \\  Pr('would'|<bs>,'I') \cdot \\  Pr('like'|'I', 'would') \cdot \\  Pr('to'|'would', 'like')\cdot \\  Pr('go'|'like', 'to')\cdot \\  Pr('West'|'to', 'go')\cdot \\  Pr('.' |'go', 'West')\cdot \\  Pr(<es>|'West', '.')  $$

## Question 2
$$
1/(3^{n-1})
$$

Because there are these many different $x_1 ... x_n$ strings (as $x_n$ is STOP always), so sum over all $x_1 ... x_n$ strings to be equal to $1$ means each string gets probability $\frac{0.5^n}{3^{n-1}}$.

## Question 3
1. Max value of perplexity is $\infty$ if any sentence gets zero probability.

2. Min value is 1 as it predicts each sentence perfectly.

3. The test corpus should have a bigram unobserved in training which gets zero.

4. The test corpus should have exactly the same bigram as in training and each bigram should be unique.

## Question 4

$\lambda_1 = \alpha$, $\lambda_2 = \beta(1 - \alpha)$, $\lambda_3 = (1-\alpha)(1-\beta)$, take in $\alpha=\beta=0.5$ then we have the answer.

## Question 5

$$
P('I' | <bs>) = 2/3\\
P('Sam' | <bs>) = 1/3\\
P(<es> | 'Sam') = 1/2\\
P('Sam' | 'am') = 1/2\\
P('am' | 'I') = 2/3\\
P('do' | 'I') = 1/3\\
$$

# 2. Log linear models

## Question 1
Yes. Recall the definition:

$$
Pr(y∣\bold{x};\bold{v})=\frac{\bold{v}⋅\bold{f}(\bold{x},y)}{\sum_{y'\in Y} \bold{v}⋅\bold{f}(\bold{x},y')}
$$

The denominator here is exactly the same for all $y \in Y$, so when determining which label should be the output, $\argmax_y Pr(y∣\bold{x};\bold{v}) = \argmax_y \bold{v}⋅\bold{f}(\bold{x},y)$ is enough.

## Question 2

2: $k = |V| \times |Y|$
6: |{\cal Y}| &=& \frac{k}{|{\cal V}|} \\

$f_k(x, y) \in \R^{|V| \times |Y|}$, each $y \in Y$ is associated with a one-hot vector of the input $x$.

## Question 3

It is incorrect. This algorithm exits upon seeing the first $y$, while it should return the $y$ which gives the smallest $−\log Pr(y∣\bold{x};\bold{v})$.

## Question 4

$f_1(u,v) = \log(0.9) \textrm{ if } u=v$
$f_1(u,v) = \log(\frac{0.1}{|V|-1}) \textrm{ if } u \neq v$
$v_1 = 1$

# 3. Linear Combinations

Answers are here: https://github.com/anoopsarkar/nlp-class/blob/gh-pages/assets/notes/linearb_solution.pdf

# 4. Word2Vec Practice

## Question 1

2. $-\log(0.01)$

$Pr(y)$ for all $y$ equals 0.01, and cross-entropy is just negative log.

## Question 2
No. Suppose the algorithm is Skip-gram with negative sample, the classifier here is trained to maximise $u_w \cdot v_w$ for all positive samples, and penalise $u_w \cdot v_w'$ for all negative samples, then it is possible that while $u^A_w⋅v^A_w=u^B_w⋅v^B_w$ since such values are all maximised, but the actual trained values of $v_w^A$ and $v_w^B$ are different. For instance, you can divide $u^A$ by $k$ and multiply $v^A$ by $k$ to still obtain the equality but the vectors $v^A$ and $v^B$ are different. 

## Question 3
1. |V|
2. 1
3. $u_w \in \R^k$ are weights for scoring how likely the is $w$ the target word under the current context $\hat{v}$ 
4. $U \in \R^{|V| \times k}$
5. Negative sampling uses a separate classifier to distinguish between positive samples and negative samples and makes an independence assumption over the context vectors. Without modification to the cross-entropy loss function, such classifier cannot be trained due to the average over the context vectors.

SideNote: one could use negative sampling in a modified cross-entropy based loss function for CBOW, but empirical results suggest that this might not work very well as cross-entropy tends to be fairly powerful on its own.

## Question 4

Very simple proof.

$P(Y=1∣x)=\sigma(\beta x)  = \frac{1}{1+\exp(-\beta x)} = \frac{1}{1+\exp(\beta_2 x-\beta_1 x)} = \frac{\exp(\beta_1 x)}{\exp(\beta_1 x)+\exp(\beta_2 x)}$
$P(Y=2∣x)=1-\sigma(\beta x)  = 1-\frac{1}{1+\exp(-\beta x)} = \frac{\exp(-\beta x)}{1+\exp(-\beta x)} = \frac{1}{1+\exp(\beta x)} = \frac{\exp(\beta_2 x)}{\exp(\beta_1 x)+\exp(\beta_2 x)}$

## Question 5

1. Example answer:
$L_E(Q_E) = \sum_{w_i\in V_E} \left[ \alpha( ||v_i^E-\hat{v_i^E}||^2 + ||u_i^E-\hat{u_i^E}||^2) + \sum_{(w_i, w_j)\in \textit{Trans}, w_j\in V_F} \beta(||v_i^E-v_j^F||^2  +||u_i^E-u_j^F||^2) \right]$

2. Example answer:
$Q_E = \hat{Q}_E$

3. Same as subq1 and subq2, except that E and F are swapped.
