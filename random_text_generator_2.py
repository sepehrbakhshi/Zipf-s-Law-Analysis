# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 19:49:07 2023

@author: 3pehr
"""
import numpy as np

dickens_corpus = np.loadtxt("Dickens/dickens_all_books_corpus_sw_removed.txt", dtype=str,delimiter=",")
dostoyevsky_corpus = np.loadtxt("Dostoyevsky/dostoyevsky_all_books_corpus_sw_removed.txt", dtype=str,delimiter=",")
tolstoy_corpus = np.loadtxt("Tolstoy/tolstoy_all_books_corpus_sw_removed.txt", dtype=str,delimiter=",")

dickens_corpus = np.array(dickens_corpus)
dostoyevsky_corpus = np.array(dostoyevsky_corpus)
tolstoy_corpus = np.array(tolstoy_corpus)

dickens_corpus = dickens_corpus.reshape((dickens_corpus.shape[0],1))
dostoyevsky_corpus = dostoyevsky_corpus.reshape((dostoyevsky_corpus.shape[0],1))
tolstoy_corpus = tolstoy_corpus.reshape((tolstoy_corpus.shape[0],1))

tmp = np.concatenate((dickens_corpus,dostoyevsky_corpus), axis= 0)
concatenated_corpus = np.concatenate((tmp,tolstoy_corpus), axis= 0)

new_corpus_length = len(concatenated_corpus)*2/9
new_corpus = []

for k in range(0, int(new_corpus_length)):
    random_number = np.random.randint(0, int(new_corpus_length))
    tmp = concatenated_corpus[random_number]
    new_corpus.append(tmp[0])

np.savetxt("new_book"+'/'+"new"+"_corpus.txt", new_corpus, delimiter=',', fmt="%s")





