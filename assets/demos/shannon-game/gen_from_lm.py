import sys
import string
import time
import random
import math
import getopt
import gzip

class LM:

    def __init__(self):
        self.start = {}  # dictionary that holds trigram logprobs for valid starts
        # for a sentence
        self.lm = {}  # dictionary that holds the rest of the trigram logprobs

        # Warning: the language model created by SRILM should not delete low
        # count ngrams, otherwise this generator will not work. Use a command
        # like:
        #
        # ngram-count -order 3 -gtmax 0 -gt3min 1 -text austen.txt -lm
        # austen.lm

        # for trigram probability, prob = p(w3 | w1, w2) we create a
        # dictionary where the key is the tuple (w1,w2) and the value is a
        # list: [ (w3-1, prob-1) , (w3-2, prob-2), ... ]
        #
        # we have two such dictionaries, one for cases where w1 = <s> so that
        # we can use this dictionary to start the sentence, and the rest of
        # the ngrams are stored in the dictionary lm


    def load_lm(self, filename):
        """load_lm loads a file in the ARPA LM format used by SRILM"""
        if filename[-3:] == '.gz':
            lmfile = gzip.open(filename, 'rt')
        else:
            lmfile = open(filename, 'r')
        begin = False
        for line in lmfile:
            line = line.rstrip()
            if line[:5] == '\\end\\':
                break
            if line == "":
                continue
            if begin:
                fields = line.split()
                if fields[1] == "<s>":
                    startkey = (fields[1], fields[2])
                    startvalue = (fields[3], float(fields[0]))
                    if startkey in self.start: self.start[startkey].append(startvalue)
                    else: self.start[startkey] = [startvalue]
                else:
                    key = (fields[1], fields[2])
                    value = (fields[3], float(fields[0]))
                    if key in self.lm: self.lm[key].append(value)
                    else: self.lm[key] = [value]
            if line[:9] == '\\3-grams:':
                begin = True
        lmfile.close()


    def generate(self, numsents, printprob):
        """generates numsents sentences by random sampling from a language model"""
        start_opt_list = list(self.start.keys())
        print(start_opt_list)
        while numsents > 0:
            random.seed()

            # generate the start of the sentence by starting with a random
            # <s>, w1, w2 trigram
            (w1, w2) = random.choice(start_opt_list)
            next_word_list = self.start[(w1, w2)]
            (w3, prob) = random.choice(next_word_list)

            # the sentence and probability of each word is stored in gen_sent
            # and gen_logprob
            gen_sent = [w1, w2]  # the sentence starts with w1, w2
            gen_logprob = []

            # loop until end of sentence </s> is generated
            while 1:
                gen_sent.append(w3)
                gen_logprob.append(prob)  # prob = p(w3 | w1, w2)

                if w3 == "</s>": break

                prob_out = random.random()
                accumulate = 0.0
                key = (w2, w3)
                w2 = w3

                if key not in self.lm:
                    print("missing key", key, file=sys.stderr)
                    break

                # main loop: sample from the events { w3-1, w3-2, ... } using
                # the prob = p(w3-i | w1, w2)
                for (lm_w, lm_logprob) in self.lm[key]:

                    if lm_logprob > -98:
                        lm_prob = math.exp(lm_logprob)
                    else:
                        lm_prob = 0.0

                    w3 = lm_w
                    prob = lm_logprob

                    if (prob_out < (lm_prob + accumulate)):
                        break
                    else:
                        accumulate += lm_prob

            print(" ".join(gen_sent))
            if (printprob):
                print(" ".join(["%f" % i for i in gen_logprob]))
            numsents -= 1


def usage():
    print(
        "usage: python gen-from-lm.py [-p|--printprob] -l|--lmfile file -n|--numsents num",
        file=sys.stderr)


if __name__ == '__main__':
    try:
        (printprob, lmfile, numsents) = (0, None, 1)
        opts, args = getopt.getopt(sys.argv[1:], "pl:n:",
                                   ["printprob", "lmfile=", "numsents="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for o, a in opts:
        if o in ("-p", "--printprob"):
            printprob = 1
        if o in ("-l", "--lmfile"):
            lmfile = a
        if o in ("-n", "--numsents"):
            numsents = int(a)

    if (lmfile == None):
        usage()
        sys.exit(2)

    lm = LM()
    lm.load_lm(lmfile)
    lm.generate(numsents, printprob)
