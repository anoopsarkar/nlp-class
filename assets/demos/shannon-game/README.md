## interactive demo

Run:

    python3.10 entropy_demo.py -w -p -l austen.lm.gz -f austen.txt

## offline LM generation

Sample 20 sentences.

    python3.10 gen_from_lm.py -p -l austen.lm.gz -n 20

Sample 20 sentences with their probabilities.

    python3.10 gen_from_lm.py -p -l austen.lm.gz -n 20
