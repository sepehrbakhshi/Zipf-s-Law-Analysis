# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 13:22:46 2023

@author: 3pehr
"""

import numpy as np
import pickle
import matplotlib.pyplot as plt

author = 'Tolstoy'

if(author == 'Dostoyevsky'):
    book1 = "crime_and_punishment"
    book2 = "the_brothers_karamazov"
    book3 = "the_devils"
    label_1 = 'Crime & Punishment'
    label_2 = 'The Brothers Karamazov'
    label_3 = 'The Devils'

elif(author == 'Tolstoy'):
    book1 = "anna_karenina"
    book2 = "resurrection"
    book3 = "war_and_peace"
    label_1 = 'Anna Karenina'
    label_2 = 'Resurrection'
    label_3 = 'War & Peace'

elif(author == 'Dickens'):
    book1 = "black_house"
    book2 = "david_caperfield"
    book3 = "our_mutual_friend"
    label_1 = 'Black House'
    label_2 = 'David Caperfield'
    label_3 = 'Our Mutual Friend'


with open(author+'/'+book1+'_word_freq_before_sw_sorted.pkl', 'rb') as f:
    first_book_wf = pickle.load(f)
    
with open(author+'/'+ book2 +'_word_freq_before_sw_sorted.pkl', 'rb') as f:
    second_book_wf = pickle.load(f)
    
with open(author+'/'+ book3 +'_word_freq_before_sw_sorted.pkl', 'rb') as f:
    third_book_wf = pickle.load(f)
    
ranks_first = np.arange(1, len(first_book_wf)+1)
ranks_first = np.array(ranks_first)

ranks_second = np.arange(1, len(second_book_wf)+1)
ranks_second = np.array(ranks_second)

ranks_third = np.arange(1, len(third_book_wf)+1)
ranks_third = np.array(ranks_third)

freqs_first = list(first_book_wf.values())
freqs_second = list(second_book_wf.values())
freqs_third = list(third_book_wf.values())

#maximum_rank = max(len(dickens_all_books_wf),len(dostoyevsky_all_books_wf),len(tolstoy_all_books_wf))
#ranks = np.arange(1,maximum_rank)

plt.loglog(ranks_first, freqs_first, 'Green', label= label_1 ,linestyle=':', linewidth=3)
plt.loglog(ranks_second, freqs_second, 'Red', label= label_2  ,linestyle='--', linewidth=3)
plt.loglog(ranks_third, freqs_third, 'Blue', label= label_3 ,linestyle='-.',  linewidth=3)

plt.xlabel('Ranks (log)')

plt.ylabel('Frequency (log)')
plt.grid()
plt.legend(loc="upper right")
plt.savefig("Tolstoy_zipfs_loglog_before.eps" )
plt.show()
