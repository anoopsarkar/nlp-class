import argparse, bz2
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--tagfile", help="tag sequences one per line", default="train.0-18.tag.txt.bz2")
parser.add_argument("-w", "--wordfile", help="word sequences (aka sentences) one per line", default="train.0-18.word.txt.bz2")
parser.add_argument("-p", "--pattern", help="tag pattern to look for", default="$ CD JJ NN")
args = parser.parse_args()

def subfinder(mylist, pattern):
    matches = []
    for i in range(len(mylist)):
        if mylist[i] == pattern[0] and mylist[i:i+len(pattern)] == pattern:
            matches.append((i,i+len(pattern)))
    return matches

sents = []
with bz2.open(args.wordfile) as wf:
    for line in wf:
        sents.append(str(line).strip())
with bz2.open(args.tagfile) as tf:
    for i, line in enumerate(tf):
        line = str(line).strip()
        if args.pattern in line:
            #print(line)
            #print(sents[i])
            matches = subfinder(line.split(), args.pattern.split())
            for (k,j) in matches:
                #print(line.split()[k:j])
                print(" ".join(sents[i].split()[k:j]))
