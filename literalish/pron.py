#!/usr/bin/env python

from nltk.corpus import cmudict
from phoneme import phonemes

d = cmudict.dict()

def literalish(word):
    lits = []
    try:
        cands = d[word.lower()]
        for cand in cands:
            lit = []
            for cmu in cand:
                cmu = "".join([i for i in cmu if not i.isdigit()])
                lit.append(phonemes[cmu][1])
            lits.append("".join(lit))
        return "/".join(lits)
    except Exception as e:
        return "***{}***".format(word)

def translate(phrase):
    words = phrase.split(" ")
    result = []
    for word in words:
        result.append(literalish(word))
    print(" ".join(result))
    
