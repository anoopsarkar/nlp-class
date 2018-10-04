---
layout: default
img: voynich
img_link: "http://en.wikipedia.org/wiki/Voynich_manuscript"
caption: "The Voynich manuscript"
title: Homework 2 | Decipherment
active_tab: homework
---

# Homework 2: Decipherment

<span class="text-info">Start by {{ site.hwdates[2].startdate }} or earlier</span> |
<span class="text-warning">Due on {{ site.hwdates[2].deadline }}</span>

Get started:

    git clone https://github.com/anoopsarkar/nlp-class-hw.git
    cd nlp-class-hw/decipher

Clone your repository if you haven’t done it already:

    git clone git@csil-git1.cs.surrey.sfu.ca:USER/nlpclass-1187-g-GROUP.git

Then copy over the contents of the `decipher` directory above as `hw2` in your repository.

Set up the virtual environment:

    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt

Note that if you do not change the requirements then after you have
set up the virtual environment `venv` you can simply run the following
command to get started with your development for the homework:

    source venv/bin/activate

## Background

This homework uses a language model for the task of automatic
computational decipherment of a cipher text. The text is assumed
to be originally in English (although it might have many typos) and
then encrypted using symbols that are not the English alphabet.
For this homework, we will focus on substitution ciphers.  You will
be using character language models for English to solve this homework.

A simple example of a substitution cipher is the Caesar cipher which
is a 1:1 substitution cipher where each letter in English is replaced
with exactly the same but different letter.  An example of a Caesar
cipher is the `rot13` encoding:

    import codecs
    print(codecs.encode('hello world', 'rot_13'))

This will print `uryyb jbeyq` which is the encrypted version of the
plaintext `hello world`. Computational decipherment takes the
encrypted text and finds the plaintext in English.

A slightly more complex version of a cipher is the homophonic
substitution cipher where the mapping is not 1:1. Each English
letter can be mapped to multiple cipher text symbols. Consider
the following mapping of symbols:

| $$\alpha$$ | a |
| $$\beta$$ | b |
| $$\epsilon$$ | e |
| $$\gamma$$ | g |
| $$\Gamma$$ | g |
| $$\omicron$$ | o |
| $$\eta$$ | n |
| $$\rho$$ | r |
| $$\Sigma$$ | r |
| $$\psi$$ | r |
| $$\sigma$$ | s |
| $$\tau$$ | t |
| $$\upsilon$$ | u |
| $$\omega$$ | y |

Notice that `g` and `r` are mapped to multiple cipher symbols.
With the above key, you can easily decode the following cipher
text:

$$\tau \alpha \sigma \tau \omega \omicron \Sigma \gamma \alpha \eta \beta \upsilon \rho \Gamma \epsilon \psi \sigma$$

## The Challenge

In this homework, we have provided you with a cipher text of 408
symbol tokens in the file `data/cipher.txt`:

    º∫P/Z/uB∫ÀOR•–X•B
    WV+≈GyF∞ºHPπKÇ—y≈
    MJy^uIÀΩ—T‘NQyDµ£
    S¢/º∑BPORAu∫∆RÃ—E
    À^LMZJƒ“\–FHVW≈æy
    π+—GDºKI£∞—Xæµ§S¢
    RN‘IyEÃOæ—GBTQS∑B
    Lƒ/P∑BπX—EHMu^RRÀ
    √ZK—–I£W—ÇæµLM“º∑
    BPDR+j•∞\N¢≈EuHÀF
    Z√–OVWIµ+‘L£Ã^R∞H
    IºDR∏Ty“\ƒ≈/πXJQA
    PµMæRu‘∫L£NVEKH•G
    “IÇJÀµºæLMÃNA£Z¢P
    §u–ÀAº∑BVW\+VT‘OP
    ^•S“Ã∆u≈∞ΩD§G∫∫IM
    NÀ£S√E/º∫∫Z∆AP∑BV
    –≈X—W—∏F∑æ√+πºAºB
    ∫OTµRu√+∏ƒy—∏^S—W
    VZ≈GyKE∏TyAº∫∑L‘∏
    HÇFBXº§XADƒ\ΩLÇ•—
    ∏≈ƒ∑∑∞≈µPORXQF∫G√
    ZπJT‘—∏æJI+“BPQW∞
    VEX“ºWI∞—EHM£•uIÀ

There is no newline at the end of the file and the newlines in the
cipher text file are not part of the cipher.

The plaintext is in the English language. While the plaintext
language is English, the writer of this cipher text may have inserted
junk sequences and might have intentionally or unintentionally added
misspellings of English words before encrypting the message using
a homophonic cipher. Your challenge is to decode this message using
the character language models provided to you.

**Warning: The cipher in this homework is real. If you are able to
decipher the contents you will definitely find the deciphered message
very disturbing to read. This is because this homework uses a 
cipher that was used in a real-world criminal investigation in the late
1960s, early 1970s. Despite the fact that this letter was deciphered,
the criminal was never caught. My apologies if you find the plaintext
disturbing to read.**

### The Data

* The file `decipher.ipynb` contains the starter Python notebook. You can copy and modify this file for your submission.
* The ciphertext is given in the file `data/cipher.txt`. There is no newline at the end of the file. All characters in this file except the newline characters are cipher characters.
* An ngram language model is given in the file `data/6-gram-wiki-char.lm.bz2` which is a bzip2 file. The Python program `ngram.py` has a character language model implementation that can read this data file.

### Default Submission

The default submission for this homework is described in `decipher.ipynb`.

The default solution matches the frequency of symbols in the cipher text with frequency of letters in the plaintext language (in this case, English). Note that this is just some text in English used to compute letter frequencies. We do not have access to the real plaintext in this homework. 

In order to do compute plaintext frequencies, we use an English dataset has no punctuation or spaces and all characters are lowercase.

For the default solution to this homework we will use the data file `data/default.wiki.txt.bz2`. 
The default solution uses a simple frequency matching heuristic to map cipher symbols to English letters.
We match the frequencies using the function $f()$ of each cipher symbol $c$ with each English letter $e$:

$$h(c,e) = | \log(\frac{f(c)}{f(e)})) | $$

For each cipher text symbol c we then compute the most likely plain text symbol e by sorting based on the above score.
Using this scoring function we map each cipher symbol to the most likely English letter which provides a decipherment (although not a very good one) of the cipher text.

### The Baseline

The baseline method you will implement is a beam search algorithm for decipherment that uses
character language models.

The ciphertext is: $f_1^N = f_1, \ldots, f_i, \ldots, f_N, f_i \in V_f$

The plaintext candidates are: $e_1^N = e_1, \ldots, e_i, \ldots, e_N, e_i \in V_e$

Substitution of a cipher symbol with a plaintext symbol is represented by a function:
$\phi: V_f \rightarrow V_e$

Decipherment aims to find:
$\hat{\phi} = \underset{\phi}{\operatorname{argmax}} \Pr( \phi(f_1), \ldots, \phi(f_N) )$
where $\Pr$ is a language model. 

The following algorithm implements a beam search algorithm to 
find the argmax solution in the equation above.

![Beam Search Algorithm](assets/img/decipherbeam.png "Beam Search for Decipherment")

This algorithm does breadth first search of the tree of possible
cipher mappings to plaintext letters and prunes solutions that
receive bad language model scores.

To explain this algorithm in detail we will use a running example.
Let the ciphertext be `BURGER` and the plaintext decoded version
is `burger`. The ciphertext is assumed to be in uppercase and the
lowercase of each ciphertext letter is assumed to be the plaintext.
This is just to explain the algorithm using an example where it is
immediately clear what the mapping is from cipher symbol to plaintext
letter. $V_e$ is the set of plaintext letters and we assume in
this example that there are 26 English letters (lowercase, no
punctuation). $V_f$ is the cipher alphabet which for the input
cipher `BURGER` size of $V_f$ will be just 5.

In the algorithm we will use a scoring function `SCORE`
that is used to score each partial hypothesis. 

$$\texttt{SCORE}(\phi) = \Pr( g(f_1), \ldots, g(f_N) )$$

where $g()$ is a function that returns a mapping to plaintext using
$\phi$ if the mapping is defined in $\phi$ else it returns a dummy
symbol `_` that is not scored by the language model $\Pr$. For
example, we might want to score a partial decipherment $\phi = \{
(r, R), (b, B), (u, U) \}$ for the ciphertext `BURGER` which implies
a partial decipherment `bur___r` in which case only the substrings
`bur` and `r` will be scored using the language model $\Pr$.

`EXT_ORDER` is a list of cipher symbols sorted by their frequencies
in the ciphertext. e.g. In our running example `EXT_ORDER = [ R,
B, U, G, E ]`. The most frequent cipher symbol is at the head of
this list.

`EXT_LIMITS` provides a constraint for the maximum number of
cipher symbols that can map to each English letter. For a 1:1
substitution cipher `EXT_LIMITS` would be 1.  For a homophonic
cipher it should be greater than 1. It can never be more than
size of $V_f$. In our running example, let us assume that
`EXT_LIMITS` is set to 2.

We track all partial hypotheses in two sets $H_s$ and $H_t$.
$H_s$ is a set of decipherments $\phi$ which have already
been scored and pruned, and $H_t$ is used to store all
extensions of each hypothesis $\phi in H_s$ for scoring
and pruning in line 11 of the algorithm.

`CARDINALITY` is the number of cipher symbols already mapped to plaintext.
In our running example, let us assume that we are in the
middle of the decipherment process and we have $\phi = \{
(r, R), (b, B), (u, U) \}$ for the ciphertext `BURGER`.  So
the value of `CARDINALITY` in this example is 3 since we
have deciphered in this hypothesis `bur__r`. So in line 6
of the algorithm we are considering the cipher symbol
`G` and checking all possible decipherments for that
symbol. 

In each step of the while loop we increase the hypothesis
size:

$$\phi' = \phi \cup \{ (e,f) \}$$

where $e, f$ is a new hypothesized mapping from cipher symbol $f$
to plaintext $e$.

`HISTOGRAM_PRUNE` keeps the best scoring hypothesis and prunes
the rest.

In line 9, we consider extending $\phi$ to $\phi'$  
by adding every $e \in V_e$ one at a time and calculating
the `SCORE` of $\phi'$. In our example, in line 9 we would
create a score many $\phi'$ candidates:

$$
\begin{align*}
\phi' = \phi \cup \{ (a, G) \} & \texttt{SCORE} = 0.02 \\
\phi' = \phi \cup \{ (b, G) \} & \texttt{SCORE} = 0.01 \\
\ldots  \\
\phi' = \phi \cup \{ (g, G) \} & \texttt{SCORE} = 0.09 \\
\ldots  \\
\phi' = \phi \cup \{ (z, G) \} & \texttt{SCORE} = 0.00 
\end{align*}
$$

We add each $\phi'$ and its score to
$H_t$ and then prune away any hypotheses that have very
low scores using `HISTOGRAM_PRUNE` on line 12. In our
example, if we assume that only the highest scoring
hypothesis is kept then $\phi' = \phi \cup \{ (g, G) \}$
would be the only $\phi'$ to be kept in $H_t$.
Then we assign $H_t$ to be the new $H_s$ and continue on
with decipherment of the next symbol in `EXT_ORDER`.

### Your Task

Your solution to this homework should take a cipher text where the
plaintext is assumed to be in the English language (with typos,
etc.) and using a character language model it should decipher the
cipher text and provide the plaintext.  The output is assumed to
contain no spaces or punctuation and is in lower case. This matches
the character language models that have been provided to you. You
cannot use any external data sources for this homework. You can
only use the language models provided to you.

You have to document your development of your grammars in your
Python notebook called `decipher.ipynb` in your submission.
As usual you have been given a default `decipher.ipynb` which
is described above in the Default Submission section.

Before you submit your homework add a file `doc/README.username`
that documents the work done by each `username` in your group. Group
members can get zero marks if they do not have this file that shows
that they worked on the homework equally with other group members.
Put any instructions to the TA and instructor in `doc/README.txt`
or `doc/README.md`.

### Further Reading

You can improve upon the baseline in many ways. The following papers
describe some methods to get a better performance for the decipherment
task. Some papers focus on accuracy and some focus on speed. (example)

1. [An Exact A\* Method for Deciphering Letter-Substitution Ciphers](http://www.mt-archive.info/ACL-2010-Corlett.pdf)
1. [Beam Search for Solving Substitution Ciphers](https://pdfs.semanticscholar.org/690b/6a1e710e9b3569d536f428b2d0532d9bea08.pdf)
1. [Improved Decipherment of Homophonic Ciphers](http://emnlp2014.org/papers/pdf/EMNLP2014184.pdf)
1. [Solving Substitution Ciphers with Combined Language Models](http://www.aclweb.org/anthology/C14-1218)
1. [Decipherment of Substitution Ciphers with Neural Language Models](assets/cached/decipherment_neural_lm_emnlp2018.pdf)

### Submit your homework on Coursys

When you are ready to submit go to GitLab and select `New tag` to
create a new tag. For `Tag name` use `hw2` and optionally write a
`Message`. Then select `Create tag` to create this tag.

Go to [Coursys]({{ site.coursys }}). Under the `Homework 2`
activity submit your git repository URL. It will look like
this for some `USER` in your group called `g-GROUP`:

    git@csil-git1.cs.surrey.sfu.ca:USER/nlpclass-1187-g-GROUP.git

The instructions are provided in more detail in [Homework 0](hw0.html).

That's it. You are done with Homework 2!

### Grading

Your submission will be graded using the following
grading scheme:

1. Performance on the cipher text provided above.
1. Performance on a cipher text that is also an English cipher over the same plaintext alphabet. You should not make any assumptions about the ciphertext symbols. The ciphertext symbol alphabet could be very different from the cipher provided above.
1. 10 points for your documentation of work in the Python notebook assigned by the TAs. Include what was done, the different experiments you tried, and if you combined different approaches then how you did the combination. Remember to put a `doc/README.username` for each `username` in your group.

## Acknowledgements

Thanks to Nishant Kambhatla for curating some of the data and the
source code for this homework.
