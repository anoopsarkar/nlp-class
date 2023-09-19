#  scp oak.fas.sfu.ca:/cs/natlang-data/austen/austen.lm .
#  scp oak.fas.sfu.ca:/cs/natlang-data/austen/austen.txt .

import sys
import string
import time
import random
import math
import getopt

import tty
import termios

from gen_from_lm import LM

log_two_base_ten = math.log10(2)

def log_base_2(base_ten_logprob):
    return base_ten_logprob / log_two_base_ten


def entropy_and_word_prob(events, word, uniform):
    word_prob = 0.0
    entropy = 0.0
    unif = 1.0 / len(events)
    for (w3, prob) in events:
        if uniform:
            entropy += unif * math.log(unif, 2)
        else:
            entropy += math.pow(10.0, prob) * log_base_2(prob)
        if (w3 == word):
            word_prob = math.pow(10.0, prob)
    if len(events) == 1:
        entropy = 0.0
    return (-1 * entropy, word_prob)


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setcbreak(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    except KeyboardInterrupt:
        print("Control-C pressed", file=sys.stderr)
        sys.exit(0)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def compute_entropy(lm, filename, numsents, numskip, printprob, wait, uniform):
    """prints entropy of each word position based on probability from a language model"""

    try:
        f = open(filename, 'r')
    except:
        usage()
        sys.exit(2)

    i = 0
    n = 0
    for line in f:
        i += 1
        if (i <= numskip): continue

        if (n >= numsents): break
        n += 1

        line = line.strip()
        words = line.split()

        if len(words) <= 1: continue

        w1 = '<s>'
        w2 = words[0]
        w3 = words[1]
        (entropy, word_prob) = entropy_and_word_prob(lm.start[(w1, w2)], w3, uniform)
        print(w1, w2)
        if printprob: print("{}\t\t\t[entropy={:.2f} n_gram_prob={:.2f}]".format(w3, entropy, word_prob))
        else: print("{}\t\t\t[entropy={:.2f}]".format(w3, entropy))

        w1 = w2
        w2 = w3
        for w3 in words[2:]:
            if wait: getch()
            (entropy, word_prob) = entropy_and_word_prob(lm.lm[(w1, w2)], w3, uniform)
            if printprob:
                print("{}\t\t\t[entropy={:.2f} n_gram_prob={:.2f}]".format(w3, entropy, word_prob))
            else:
                print("{}\t\t\t[entropy={:.2f}]".format(w3, entropy))
            w1 = w2
            w2 = w3
        print()

def usage():
    print(
        "usage: python entropy_demo.py -w|--wait -p|--printprob -u|--uniform -l|--lmfile file -f|--corpusfile file -n|--numsents num -s|--skip num",
        file=sys.stderr)


if __name__ == '__main__':
    try:
        (lmfile, corpusfile, numsents, numskip, printprob, wait,
         uniform) = (None, None, 1, 0, 0, 0, 0)
        opts, args = getopt.getopt(sys.argv[1:], "wpul:f:n:s:", [
            "wait", "printprob", "uniform", "lmfile=", "corpusfile=",
            "numsents=", "skip="
        ])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for o, a in opts:
        if o in ("-w", "--wait"):
            wait = 1
        if o in ("-p", "--printprob"):
            printprob = 1
        if o in ("-u", "--uniform"):
            uniform = 1
        if o in ("-l", "--lmfile"):
            lmfile = a
        if o in ("-f", "--corpusfile"):
            corpusfile = a
        if o in ("-n", "--numsents"):
            numsents = int(a)
        if o in ("-s", "--skip"):
            numskip = int(a)

    if (corpusfile == None):
        usage()
        sys.exit(2)

    lm = LM()
    try:
        lm.load_lm(lmfile)
    except:
        print(sys.stderr, f"could not load {lmfile}")
        sys.exit(1)
    compute_entropy(lm, corpusfile, numsents, numskip, printprob, wait, uniform)
