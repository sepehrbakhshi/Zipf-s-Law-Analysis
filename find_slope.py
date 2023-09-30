# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 18:13:08 2023

@author: 3pehr
"""


import numpy as np
import pickle
import matplotlib.pyplot as plt
import time
#for generating plot for the authors(all three books in one part) uncomment this section

author_list = []
"""
author_list.append([])

author_list[0].append("hegels_philosophy_of_mind")
author_list[0].append("philosophy_of_fine_arts_vol1")
author_list[0].append("science_of_logic")
author_list.append([])
author_list[1].append("jane_eyre")
author_list[1].append("shirley")
author_list[1].append("vilette")

"""
author_list.append([])
author_list[0].append("black_house")
author_list[0].append("david_caperfield")
author_list[0].append("our_mutual_friend")
author_list.append([])
author_list[1].append("crime_and_punishment")
author_list[1].append("the_brothers_karamazov")
author_list[1].append("the_devils")
author_list.append([])
author_list[2].append("anna_karenina")
author_list[2].append("resurrection")
author_list[2].append("war_and_peace")

"""
author_list[0].append("dracula")
author_list[0].append("the_lady_of_shroud")
author_list[0].append("the_night_land")
author_list.append([])
author_list[1].append("lorna_doone")
author_list[1].append("the_light_of_scarthy")
author_list[1].append("the_man_in_the_iron_mask")
author_list.append([])
author_list[2].append("a_connecticut_yankee_in_king_arthurs_court")
author_list[2].append("the_mysterious_island")
author_list[2].append("twenty_thousand_leagues_under_the_seas")
"""
"""
author_list[0].append("crime_and_punishment")
author_list[0].append("the_brothers_karamazov")
author_list[0].append("the_devils")
author_list.append([])
author_list[1].append("black_house")
author_list[1].append("david_caperfield")
author_list[1].append("our_mutual_friend")
author_list.append([])
author_list[2].append("anna_karenina")
author_list[2].append("resurrection")
author_list[2].append("war_and_peace")
"""
type_token_rel=[]
for i in range(0, len(author_list)):
    type_token_rel.append([])
    
    if(i == 0):
        #author_name = "Horror"
        #author_name = "Hegel"
        author_name = "Dickens"
        
    elif(i == 1):
        #author_name = "Charlotte Bronte"
        #author_name = "Romance"
        author_name = "Dostoyevsky"
    elif(i == 2):
        #author_name = "Scifi"
        author_name = "Tolstoy"
        
    elif(i == 3):
        author_name = "Hegel"
        #author_name = "Scifi"
        
    elif(i == 4):
        #author_name = "Scifi"
        author_name = "Charlotte Bronte"
        
    
    for j in range(0, len(author_list[i])):
        print(author_list[i][j])
        with open(author_name+'/'+ author_list[i][j]+'_type_token_rel_before.pkl', 'rb') as f:
            type_token_rel[i].append(pickle.load(f))
type_token_rel = np.array(type_token_rel)

vocab_counter_list = []
for i in range(0 , len(author_list)):
    vocab_counter_list.append([])
    for j in range(0, len(author_list[i])):
        
        tmp_size = np.arange(1,len(type_token_rel[i][j]) +1)
        tmp_size = tmp_size * 1
        vocab_counter_list[i].append(tmp_size)
vocab_counter_list = np.array(vocab_counter_list)      

for i in range(0, len(vocab_counter_list)):
    if(i == 0):
        
        color = "green"
    if(i == 1):
        
        color = "red"
    if(i == 2):
        
        color = "blue"
    if(i == 3):
        color= 'orange'
    if(i ==4):
        color = 'yellow'
    for j in range(0, len(vocab_counter_list[i])):
        label = author_list[i][j]
        
        label = ""
        if(i == 0 and j == 0):
            label = "bleak_house"
        else:
            label = author_list[i][j]
        
        plt.loglog(vocab_counter_list[i][j], type_token_rel[i][j], color = color, label=label ,linestyle=':', linewidth=2)

plt.xlabel('Token')

plt.ylabel('Types')
plt.grid()
plt.legend(loc="lower right",fontsize = 7)

plt.savefig("type_token_loglog_separate_2.eps" )
plt.show()
asdas

slops = []
intercepts = []
log_vocabs = []
log_rels = []
for i in range(0, len(vocab_counter_list)):
    slops.append([])
    intercepts.append([])
    log_vocabs.append([])
    log_rels.append([])
    for j in range(0, len(vocab_counter_list[i])):
        print((vocab_counter_list[i][j]))
        
        tmplog = np.log10(vocab_counter_list[i][j])
        
        tmp_log_rel = np.log10(type_token_rel[i][j])
        log_vocabs[i].append(tmplog)
        log_rels[i].append(tmp_log_rel)
        slope, intercept = np.polyfit(tmplog, tmp_log_rel, 1)
        slops[i].append(slope)
        intercepts[i].append(intercept)

for i in range(0, len(intercepts)):
    if(i == 0):
        
        color = "green"
    if(i == 1):
        
        color = "red"
    if(i == 2):
        
        color = "blue"
    if(i == 3):
        color= 'orange'
    if(i ==4):
        color = 'yellow'
    for j in range(0, len(intercepts[i])):
        
        plt.loglog(vocab_counter_list[i][j], 10**(slops[i][j]*log_vocabs[i][j] + intercepts[i][j]), color=color, linestyle='-.', linewidth=2)


plt.xlabel('Token')

plt.ylabel('Types')
plt.grid()
plt.legend(loc="lower right",fontsize = 7)

plt.savefig("type_token_loglog_separate_2.eps" )
plt.show()

print(intercepts)
print(slops)
asdasd
#plt.savefig("slop_three_literature.eps" )
"""
plt.show()
x= [1,2,3]

plt.scatter(slops[0] , slops[0] , color= "red")
#plt.scatter(slops[1], slops[1], color= "green")
#plt.scatter(slops[2], slops[2], color= "blue")
#plt.scatter(slops[3], slops[3], color= "orange")
plt.scatter(slops[4], slops[4], color= "blue")
#plt.ylim((0,3))
plt.show()
"""

"""
plt.plot(vocab_counter_dickens_david_caperfield, 10**(slope_di2*di2 + intercept_di2), color="Green")
plt.plot(vocab_counter_dickens_our_mutual_friend, 10**(slope_di3*di3 + intercept_di3), color="Green")

plt.plot(vocab_counter_dostoyevsky_crime_and_punishment, 10**(slope_d1*d1 + intercept_d1), color="Red")
plt.plot(vocab_counter_dostoyevsky_the_brothers_karamazov, 10**(slope_d2*d2 + intercept_d2), color="Red")
plt.plot(vocab_counter_dostoyevsky_the_devils, 10**(slope_d3*d3 + intercept_d3), color="Red")


plt.plot(vocab_counter_tolstoy_anna_karenina, 10**(slope_t1*t1 + intercept_t1), color="Blue")
plt.plot(vocab_counter_tolstoy_resurrection, 10**(slope_t2*t2 + intercept_t2), color="Blue")
plt.plot(vocab_counter_tolstoy_war_and_peace, 10**(slope_t3*t3 + intercept_t3), color="Blue")


di1 = np.log10(vocab_counter_dickens_black_house)
di1_wf = np.log10(dickens_black_house_wf)
slope_di1, intercept_di1 = np.polyfit(di1, di1_wf, 1)

di2 = np.log10(vocab_counter_dickens_david_caperfield)
di2_wf = np.log10(dickens_david_caperfield_wf)
slope_di2, intercept_di2 = np.polyfit(di2, di2_wf, 1)

di3 = np.log10(vocab_counter_dickens_our_mutual_friend)
di3_wf = np.log10(dickens_our_mutual_friend_wf)
slope_di3, intercept_di3 = np.polyfit(di3, di3_wf, 1)

d1 = np.log10(vocab_counter_dostoyevsky_crime_and_punishment)
d1_wf = np.log10(dostoyevsky_crime_and_punishment_wf)
slope_d1, intercept_d1 = np.polyfit(d1, d1_wf, 1)

d2 = np.log10(vocab_counter_dostoyevsky_the_brothers_karamazov)
d2_wf = np.log10(dostoyevsky_the_brothers_karamazov_wf)
slope_d2, intercept_d2 = np.polyfit(d2, d2_wf, 1)

d3 = np.log10(vocab_counter_dostoyevsky_the_devils)
d3_wf = np.log10(dostoyevsky_the_devils_wf)
slope_d3, intercept_d3 = np.polyfit(d3, d3_wf, 1)

t1 = np.log10(vocab_counter_tolstoy_anna_karenina)
t1_wf = np.log10(tolstoy_anna_karenina_wf)
slope_t1, intercept_t1 = np.polyfit(t1,t1_wf, 1)

t2 = np.log10(vocab_counter_tolstoy_resurrection)
t2_wf = np.log10(tolstoy_resurrection_wf)
slope_t2, intercept_t2 = np.polyfit(t2,t2_wf, 1)

t3 = np.log10(vocab_counter_tolstoy_war_and_peace)
t3_wf = np.log10(tolstoy_war_and_peace_wf)
slope_t3, intercept_t3 = np.polyfit(t3,t3_wf, 1)

"""
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
"""
"""
plt.plot(vocab_counter_dickens_black_house, 10**(slope_di1*di1 + intercept_di1), color="Green")
plt.plot(vocab_counter_dickens_david_caperfield, 10**(slope_di2*di2 + intercept_di2), color="Green")
plt.plot(vocab_counter_dickens_our_mutual_friend, 10**(slope_di3*di3 + intercept_di3), color="Green")

plt.plot(vocab_counter_dostoyevsky_crime_and_punishment, 10**(slope_d1*d1 + intercept_d1), color="Red")
plt.plot(vocab_counter_dostoyevsky_the_brothers_karamazov, 10**(slope_d2*d2 + intercept_d2), color="Red")
plt.plot(vocab_counter_dostoyevsky_the_devils, 10**(slope_d3*d3 + intercept_d3), color="Red")


plt.plot(vocab_counter_tolstoy_anna_karenina, 10**(slope_t1*t1 + intercept_t1), color="Blue")
plt.plot(vocab_counter_tolstoy_resurrection, 10**(slope_t2*t2 + intercept_t2), color="Blue")
plt.plot(vocab_counter_tolstoy_war_and_peace, 10**(slope_t3*t3 + intercept_t3), color="Blue")
"""
"""
print(slope_t1)
print(slope_t2)
print(slope_t3)

print(slope_d1)
print(slope_d2)
print(slope_d3)

print("----")
print(slope_di1)
print(slope_di2)
print(slope_di3)
"""

