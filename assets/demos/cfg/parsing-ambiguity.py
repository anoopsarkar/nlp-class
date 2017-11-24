import nltk
from nltk import CFG
import sys

grammar = CFG.fromstring("""
N -> N N | 'natural' | 'language' | 'processing' | 'course'
""")

if len(sys.argv) > 1:
    inp = 'natural language processing course'
else:
    for line in sys.stdin:
        inp = line.strip()
print grammar.start()
print grammar.productions()
parser = nltk.ChartParser(grammar)
for tree in parser.parse(inp.split()):
    print(tree)
