# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 14:32:45 2017

@author: DELL1
Gensim based Text Summarizer  
Based on Text rank algorithm 
discussed in this paper https://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf
"""
from gensim.summarization import summarize

def summary(tex):
    return(summarize(tex,ratio=0.5))

text=""
text=input("Input here :")
print(summary(text))
