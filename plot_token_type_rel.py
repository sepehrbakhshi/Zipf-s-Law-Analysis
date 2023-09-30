# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 16:01:04 2023

@author: 3pehr
"""


import numpy as np
import pickle
import matplotlib.pyplot as plt
#for generating plot for the authors(all three books in one part) uncomment this section

with open('Dickens'+'/dickens_all_books'+'_type_token_rel_before.pkl', 'rb') as f:
    dickens_all_books_wf = pickle.load(f)
    
with open('Dostoyevsky'+'/dostoyevsky_all_books'+'_type_token_rel_before.pkl', 'rb') as f:
    dostoyevsky_all_books_wf = pickle.load(f)
    
with open('Tolstoy'+'/tolstoy_all_books'+'_type_token_rel_before.pkl', 'rb') as f:
    tolstoy_all_books_wf = pickle.load(f)


"""
with open('Dickens'+'/black_house'+'_type_token_rel.pkl', 'rb') as f:
    dickens_black_house_wf = pickle.load(f)
with open('Dickens'+'/david_caperfield'+'_type_token_rel.pkl', 'rb') as f:
    dickens_david_caperfield_wf = pickle.load(f)
with open('Dickens'+'/our_mutual_friend'+'_type_token_rel.pkl', 'rb') as f:
    dickens_our_mutual_friend_wf = pickle.load(f)
    
with open('Dostoyevsky'+'/crime_and_punishment'+'_type_token_rel.pkl', 'rb') as f:
    dostoyevsky_crime_and_punishment_wf = pickle.load(f)
with open('Dostoyevsky'+'/the_brothers_karamazov'+'_type_token_rel.pkl', 'rb') as f:
    dostoyevsky_the_brothers_karamazov_wf = pickle.load(f)
with open('Dostoyevsky'+'/the_devils'+'_type_token_rel.pkl', 'rb') as f:
    dostoyevsky_the_devils_wf = pickle.load(f)
    
with open('Tolstoy'+'/anna_karenina'+'_type_token_rel.pkl', 'rb') as f:
    tolstoy_anna_karenina_wf = pickle.load(f)
with open('Tolstoy'+'/resurrection'+'_type_token_rel.pkl', 'rb') as f:
    tolstoy_resurrection_wf = pickle.load(f)
with open('Tolstoy'+'/war_and_peace'+'_type_token_rel.pkl', 'rb') as f:
    tolstoy_war_and_peace_wf = pickle.load(f)

"""
vocab_counter_dickens = np.arange(1,len(dickens_all_books_wf) +1)
vocab_counter_dickens= vocab_counter_dickens * 1

vocab_counter_dostoyevsky = np.arange(1,len(dostoyevsky_all_books_wf) +1)
vocab_counter_dostoyevsky = vocab_counter_dostoyevsky * 1

vocab_counter_tolstoy = np.arange(1,len(tolstoy_all_books_wf) +1)
vocab_counter_tolstoy = vocab_counter_tolstoy * 1


"""
vocab_counter_dickens_black_house = np.arange(1,len(dickens_black_house_wf) +1)
vocab_counter_dickens_black_house = vocab_counter_dickens_black_house * 5000

vocab_counter_dickens_david_caperfield = np.arange(1,len(dickens_david_caperfield_wf) +1)
vocab_counter_dickens_david_caperfield = vocab_counter_dickens_david_caperfield * 5000

vocab_counter_dickens_our_mutual_friend = np.arange(1,len(dickens_our_mutual_friend_wf) +1)
vocab_counter_dickens_our_mutual_friend = vocab_counter_dickens_our_mutual_friend * 5000


vocab_counter_dostoyevsky_crime_and_punishment = np.arange(1,len(dostoyevsky_crime_and_punishment_wf)+1)
vocab_counter_dostoyevsky_crime_and_punishment = vocab_counter_dostoyevsky_crime_and_punishment * 5000

vocab_counter_dostoyevsky_the_brothers_karamazov = np.arange(1,len(dostoyevsky_the_brothers_karamazov_wf)+1)
vocab_counter_dostoyevsky_the_brothers_karamazov = vocab_counter_dostoyevsky_the_brothers_karamazov * 5000

vocab_counter_dostoyevsky_the_devils = np.arange(1,len(dostoyevsky_the_devils_wf)+1)
vocab_counter_dostoyevsky_the_devils = vocab_counter_dostoyevsky_the_devils * 5000



vocab_counter_tolstoy_anna_karenina = np.arange(1,len(tolstoy_anna_karenina_wf)+1)
vocab_counter_tolstoy_anna_karenina = vocab_counter_tolstoy_anna_karenina * 5000

vocab_counter_tolstoy_resurrection = np.arange(1,len(tolstoy_resurrection_wf)+1)
vocab_counter_tolstoy_resurrection = vocab_counter_tolstoy_resurrection * 5000

vocab_counter_tolstoy_war_and_peace = np.arange(1,len(tolstoy_war_and_peace_wf)+1)
vocab_counter_tolstoy_war_and_peace = vocab_counter_tolstoy_war_and_peace * 5000
"""
"""
plt.loglog(vocab_counter_dickens, dickens_all_books_wf, 'Green', label='Dickens' ,linestyle=':', linewidth=5)
plt.loglog(vocab_counter_dostoyevsky, dostoyevsky_all_books_wf, 'Red', label='Dostoyevsky',linestyle='--', linewidth=7)
plt.loglog(vocab_counter_tolstoy, tolstoy_all_books_wf, 'Blue', label='Tolstoy',linestyle='-.',  linewidth=2)
"""
"""
plt.loglog(vocab_counter_dickens_black_house, dickens_black_house_wf, 'Green', label='Black House' ,linestyle=':', linewidth=1)

plt.loglog(vocab_counter_dickens_david_caperfield, dickens_david_caperfield_wf, 'Green', label='David Caperfield' ,linestyle=':', linewidth=1)
plt.loglog(vocab_counter_dickens_our_mutual_friend, dickens_our_mutual_friend_wf, 'Green', label='Our Mutual Friend' ,linestyle=':', linewidth=1)

plt.loglog(vocab_counter_dostoyevsky_crime_and_punishment, dostoyevsky_crime_and_punishment_wf, 'Red', label='Crime & Punishment',linestyle='--', linewidth=1)
plt.loglog(vocab_counter_dostoyevsky_the_brothers_karamazov, dostoyevsky_the_brothers_karamazov_wf, 'Red', label='The Brothers Karamazov',linestyle='--', linewidth=1)
plt.loglog(vocab_counter_dostoyevsky_the_devils, dostoyevsky_the_devils_wf, 'Red', label='The Devils',linestyle='--', linewidth=1)

plt.loglog(vocab_counter_tolstoy_anna_karenina, tolstoy_anna_karenina_wf, 'Blue', label='Anna Karenina',linestyle='-.',  linewidth=1)
plt.loglog(vocab_counter_tolstoy_resurrection, tolstoy_resurrection_wf, 'Blue', label='Resurrection',linestyle='-.',  linewidth=1)
plt.loglog(vocab_counter_tolstoy_war_and_peace, tolstoy_war_and_peace_wf, 'Blue', label='War & Peace',linestyle='-.',  linewidth=1)
"""


plt.plot(vocab_counter_dickens, dickens_all_books_wf, color='Green', label='Dickens' ,linestyle=':', linewidth=5)
plt.plot(vocab_counter_dostoyevsky, dostoyevsky_all_books_wf, 'Red', label='Dostoyevsky',linestyle='--', linewidth=7)
plt.plot(vocab_counter_tolstoy, tolstoy_all_books_wf, 'Blue', label='Tolstoy',linestyle='-.',  linewidth=2)



"""
a2 = np.log10(vocab_counter_tolstoy)
b2 = np.log10(tolstoy_all_books_wf)

a = np.log10(vocab_counter_dickens)
b = np.log10(dickens_all_books_wf)

a3 = np.log10(vocab_counter_dostoyevsky)
b3 = np.log10(dostoyevsky_all_books_wf)

slope, intercept = np.polyfit(a, b, 1)
slope2, intercept2 = np.polyfit(a2, b2, 1)
slope3, intercept3 = np.polyfit(a3, b3, 1)
plt.plot(vocab_counter_tolstoy, 10**(slope2*a2 + intercept2), color="Blue")

plt.plot(vocab_counter_dickens, 10**(slope*a + intercept),color ='Green')
plt.plot(vocab_counter_dostoyevsky, 10**(slope3*a3 + intercept3),color ='Red')
"""
plt.xlabel('Tokens')

plt.ylabel('Types')
#plt.xlim(1, 1000)
plt.grid()
plt.legend(loc="lower right")


plt.savefig("type_vocab_loglog_all_books_authors_before_2.eps" )
plt.show()

