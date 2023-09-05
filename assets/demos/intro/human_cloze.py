import nltk
import random
#word_choice = 'violin'
#word_choice = 'butter'
#word_choice = 'sauce'
#word_choice = 'sandwich'
#word_choice = 'probabilities'
#word_choice = 'joke'
word_choice = 'rice'

def replace_with_blanks(sent, word):
    return map(lambda x: '_______' if x == word else x, sent)

def mask_random(sent):
    rand_word = random.choice(sent)
    return replace_with_blanks(sent, rand_word)

for sent in nltk.corpus.brown.sents():
    if word_choice in sent:
        print('-' * 72)
        print(' '.join(mask_random(random.choice(nltk.corpus.brown.sents()))))
        print(' '.join(replace_with_blanks(sent, word_choice)))
        print(' '.join(mask_random(random.choice(nltk.corpus.brown.sents()))))

