# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 15:03:32 2023

@author: 3pehr
"""
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
"""
X = [[0.6319504510812826,1.0724596397656732], [0.6422243414226743,0.9930892027849617],
     
     [0.6432004290963654,1.0251096976377478],
    [ 0.6098440793137121, 1.0806824184500923], [0.6042290808212255,1.0947708378344387], 
   [ 0.6205533067983187,1.0563547725995024],
     [0.6180007202677253, 1.0312547341161917], [0.6367034585142033,0.9672693842760898],
     [0.6572778363796197,0.8304661767221263]]
"""
"""
X = [0.6319504510812826, 0.6422243414226743, 0.6432004290963654,
     0.6098440793137121, 0.6042290808212255, 0.6205533067983187,
     0.6180007202677253, 0.6367034585142033, 0.6572778363796197
     
     ,0.7017302579705521, 0.6594414150173863, 0.6639550189239273,
     0.6812266062471255, 0.6681941199512377, 0.7160133394376292
     ]
"""
X = [0.5665783969813813, 0.5851444056910295, 0.5737468223164259,
 0.5406995996588327, 0.5312458905621041, 0.5520613682734488,
 0.5634700503456641, 0.5636171839124167, 0.5806290700005872]

#X = np.hstack((x.reshape(-1, 1), y.reshape(-1, 1), z.reshape(-1, 1)))
X = np.array(X)
X= X.reshape(-1,1)

n_clusters = 3

kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(X)

Y = np.zeros_like(X)
Y_1 = np.zeros_like(X)
#plt.scatter(X[:, 0], X[:, 1], c=labels)
labels = kmeans.labels_
print(labels)

dickens = np.where(labels == 0)
dostoyevsky = np.where(labels == 2)
tolstoy = np.where(labels == 1)
#hegel = np.where(labels == 4)
#bronte = np.where(labels == 0)

plt.scatter(X[dickens], Y[dickens],color ="green" , label = "C1")
plt.scatter(X[dostoyevsky], Y[dostoyevsky],color ="red", label = "C2")
plt.scatter(X[tolstoy], Y[tolstoy],color ="blue",label = "C3")
#plt.scatter(X[hegel], Y[hegel],color ="orange",label = "C4")
#plt.scatter(X[bronte], Y[bronte],color ="black",label = "C5")
"""

dickens = [0,1,2]
dostoyevsky = [3,4,5]
tolstoy = [6,7,8]
#hegel = [9,10,11]
#bronte = [12,13,14]
plt.scatter(X[dickens], Y_1[dickens],color ="green", label = "Dickens")
plt.scatter(X[dostoyevsky], Y_1[dostoyevsky],color ="red", label = "Dostoyevsky")
plt.scatter(X[tolstoy], Y_1[tolstoy],color ="blue",label = "Tolstoy")
#plt.scatter(X[hegel], Y[hegel],color ="orange",label = "Hegel")
#plt.scatter(X[bronte], Y[bronte],color ="black",label = "Bronte")
"""
plt.ylim(-1,1)
plt.grid()
plt.legend(loc="lower right",fontsize = 10)
plt.savefig("clustering_authors_before_removal_2.eps" )
plt.show()
#plt.scatter()
