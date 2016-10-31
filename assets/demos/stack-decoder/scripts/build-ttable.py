#!/usr/bin/python

# Takes the output of process-mail.py and builds a ttable file for use
# with my stack decoder

import os
import sys
import math
from itertools import *

sourcewords = sys.argv[1:]
targetwords = { "<s>": 1, "</s>": 1}

print 'var WORDS = ['
for i,sourceword in enumerate(sourcewords):
    cmd = "cat data/*." + `i` + ".txt > data/" + `i` + ".txt"
    os.system(cmd)

    data = ["'%s'" % (sourceword)]

    words = {}
    sum = 0
    for word in open('data/' + `i` + '.txt'):
        word = word.strip().replace("'", "\\'")
        targetwords[word] = 1
        words[word] = words.get(word,0) + 1
        sum += 1

    for word in words.keys():
        prob = 1.0 * words[word] / sum
        data.append("['%s', %.5f]" % (word, math.log(prob)))

    print "  [" + ", ".join(data) + "],"

print "];"
print

out = open('ngrams', 'w')
for word1 in targetwords.keys():
    for word2 in targetwords.keys():
        out.write('%s %s\n' % (word1, word2))
out.close()

cmd = "cat ngrams | /users/post/code/joshua/src/joshua/decoder/ff/lm/kenlm/ngram_query /users/post/expts/gigaword.kenlm null 2> /dev/null | awk '{print $6}' > ngrams.scores"
os.system(cmd)

print "var BIGRAM = {"
ngrams = {}
for bigram, score in izip(open('ngrams'), open('ngrams.scores')):
    word1, word2 = bigram.split()
    word1 = word1.replace('<', '&lt;').replace('>', '&gt;')
    word2 = word2.replace('<', '&lt;').replace('>', '&gt;')
    if not ngrams.has_key(word1):
        ngrams[word1] = {}
    ngrams[word1][word2] = score

for word1 in ngrams.keys():
    data = []
    for word2 in ngrams[word1].keys():
        data.append("'%s': %.5f" % (word2, float(ngrams[word1][word2])))
    print "  '%s': { %s }," % (word1, ", ".join(data))

print "};"
