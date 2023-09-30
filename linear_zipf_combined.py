# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 13:22:46 2023

@author: 3pehr
"""

import numpy as np
import pickle
import matplotlib.pyplot as plt

with open('new_book'+'/new_corpus'+'_word_freq_after_sw_sorted.pkl', 'rb') as f:
    random_all_books_wf = pickle.load(f)
    

with open('Dickens'+'/dickens_all_books'+'_word_freq_after_sw_sorted.pkl', 'rb') as f:
    dickens_all_books_wf = pickle.load(f)
    
with open('Dostoyevsky'+'/dostoyevsky_all_books'+'_word_freq_after_sw_sorted.pkl', 'rb') as f:
    dostoyevsky_all_books_wf = pickle.load(f)
    
with open('Tolstoy'+'/tolstoy_all_books'+'_word_freq_after_sw_sorted.pkl', 'rb') as f:
    tolstoy_all_books_wf = pickle.load(f)

ranks_random = np.arange(1, len(random_all_books_wf)+1)
ranks_random = np.array(ranks_random)

ranks_dicknes = np.arange(1, len(dickens_all_books_wf)+1)
ranks_dicknes = np.array(ranks_dicknes)

ranks_dostoyevsky = np.arange(1, len(dostoyevsky_all_books_wf)+1)
ranks_dostoyevsky = np.array(ranks_dostoyevsky)

ranks_tolstoy = np.arange(1, len(tolstoy_all_books_wf)+1)
ranks_tolstoy = np.array(ranks_tolstoy)

freqs_random = list(random_all_books_wf.values())
freqs_dickens = list(dickens_all_books_wf.values())
freqs_dostoyevsky = list(dostoyevsky_all_books_wf.values())
freqs_tolstoy = list(tolstoy_all_books_wf.values())

max_freq_dickens = dickens_all_books_wf[list(random_all_books_wf)[0]]
max_freq_dickens = dickens_all_books_wf[list(dickens_all_books_wf)[0]]
max_freq_dostoyevsky = dostoyevsky_all_books_wf[list(dickens_all_books_wf)[0]]
max_freq_tolstoy = tolstoy_all_books_wf[list(dickens_all_books_wf)[0]]

#maximum_rank = max(len(dickens_all_books_wf),len(dostoyevsky_all_books_wf),len(tolstoy_all_books_wf))
#ranks = np.arange(1,maximum_rank)
plt.loglog(ranks_random, freqs_random, 'red', label='Random Corpus' ,linestyle=':', linewidth=2)

"""
plt.plot(ranks_dicknes, freqs_dickens, 'Green', label='Dickens' ,linestyle=':', linewidth=2)
plt.plot(ranks_dostoyevsky, freqs_dostoyevsky, 'Red', label='Dostoyevsky',linestyle='--', linewidth=7)
plt.plot(ranks_tolstoy, freqs_tolstoy, 'Blue', label='Tolstoy',linestyle='-.',  linewidth=2)
"""
plt.xlabel('Ranks')

plt.ylabel('Frequency')
plt.grid()
plt.legend(loc="upper right")
plt.savefig("zipfs_random_loglog.eps" )
plt.show()
