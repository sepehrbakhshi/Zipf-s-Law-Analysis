# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 13:30:47 2023

@author: 3pehr
"""

import numpy as np
import pandas as pd
import string 
import re
import copy
import time
import pickle 

#my_stopwords = np.loadtxt('my_stopwords.txt',delimiter=',',dtype=str)
gist_file = open("my_stopword_2.txt", "r")
try:
    content = gist_file.read()
    my_stopwords = content.split(",")
finally:
    gist_file.close()

book_name = "new_corpus"
author_name = "new_book" #it can also be the name of the category
"""
data = open(author_name+'/'+book_name+'.txt',mode='r',encoding="utf8")
 
corpus = data.read().split()
"""
corpus = np.loadtxt("new_book/new_corpus.txt", dtype=str,delimiter=",")
print(len(corpus))
asdas
#data.close()
counter = 0  
#removing punctuations and changing all to lower cased from the stopword list
for i in my_stopwords:  
    
    my_stopwords[counter] = re.sub('[^0-9a-zA-Z]','', i)    
    my_stopwords[counter] = my_stopwords[counter].lower()
    counter += 1
    
#declare an empty dict for keeping the word types and their freqs
word_freq_before_sw = dict()

#removing punctuations and changing all to lower case
type_token_rel_before = []
for i in range(0, len(corpus)):
    
    corpus[i] = re.sub('[^0-9a-zA-Z]','', corpus[i])    
    corpus[i] = corpus[i].lower()
    
    
    if corpus[i] in word_freq_before_sw:
        word_freq_before_sw[corpus[i]] += 1
    else:
        
        word_freq_before_sw[corpus[i]] = 1
    if(i%1 == 0):
        type_token_rel_before.append(len(word_freq_before_sw))

with open(author_name+'/'+book_name+'_type_token_rel_before.pkl', 'wb') as f:
    pickle.dump(type_token_rel_before, f)

    
counter = 0  
corpus_removed = corpus.copy()
np.savetxt(author_name+'/'+book_name+"_corpus.txt", corpus, delimiter=',', fmt="%s")

#remove stop words
corpus_removed = [token for token in corpus_removed if token not in my_stopwords]
np.savetxt(author_name+'/'+book_name+"_corpus_sw_removed.txt", corpus_removed, delimiter=',', fmt="%s")

#my_stopwords = np.loadtxt('our_mutual_friend_corpus_sw_removed.txt',delimiter=',',dtype=str)

word_freq_after_sw = dict()
type_token_rel = []
for i in range(0, len(corpus_removed)):
   
    if corpus_removed[i] in word_freq_after_sw:
        word_freq_after_sw[corpus_removed[i]] += 1
    else:
        
        word_freq_after_sw[corpus_removed[i]] = 1
    # keep the word to types relationships for evey 5000 tokens
    if(i%1 == 0):
        type_token_rel.append(len(word_freq_after_sw))
     

with open(author_name+'/'+book_name+'_type_token_rel.pkl', 'wb') as f:
    pickle.dump(type_token_rel, f)

#sort the frequency dictionaries in reverse order
word_freq_after_sw_sorted = dict(sorted(word_freq_after_sw.items(), key=lambda x: x[1], reverse=True))
word_freq_before_sw_sorted = dict(sorted(word_freq_before_sw.items(), key=lambda x: x[1], reverse=True))

#(word_freq_after_sw_sorted)
"""
#a = list(word_freq_after_sw.items())
word_freq_after_sw_sorted.popitem()
first_key = next(iter(word_freq_after_sw_sorted))
del word_freq_after_sw_sorted[first_key]
"""
#print(word_freq_after_sw_sorted)

#word_freq_after_sw = dict(a)

#word_freq_after_sw_sorted = dict(sorted(word_freq_after_sw.items(), key=lambda x: x[1], reverse=True))

print(len(word_freq_before_sw_sorted))
print(len(word_freq_after_sw_sorted))
first_key = list(word_freq_before_sw_sorted.keys())[0]
first_value = word_freq_before_sw_sorted[first_key]

print(first_key)
print(first_value)

#print(word_freq_after_sw_sorted)


first_key = list(word_freq_after_sw_sorted.keys())[0]
first_value = word_freq_after_sw_sorted[first_key]



print(first_key)
print(first_value)
print(len(word_freq_after_sw_sorted))

with open(author_name+'/'+book_name+'_word_freq_before_sw_sorted.pkl', 'wb') as f:
    pickle.dump(word_freq_before_sw_sorted, f)

with open(author_name+'/'+book_name+'_word_freq_after_sw_sorted.pkl', 'wb') as f:
    pickle.dump(word_freq_after_sw_sorted, f)


