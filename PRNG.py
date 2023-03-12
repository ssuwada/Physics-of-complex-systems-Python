#---------  FIRST CLASS EXERCISES -----------
#   PRNG - PSEUDO RANDOM NUMBER GENERATOR
#   IMPLEMENTATION, FUNCIONALITY AND PLOTS 
#   WITH SAVING TO FILE GENERATED NUMBERS
#           ---------------------
#              SEBASTIAN SUWADA 
#           ---------------------

import numpy as np 
import matplotlib.pyplot as plt


#--------- FUNC -------------
#Functions - PRNG, ListplusOne


def prgn(a,c,N,seed):
    list1 = []
    seed = 0.023
    list1.append(seed)
    for i in range(N):
        xn = (a*list1[i]+c)%m
        list1.append(xn)
    return list1    

def list_plus_one(list1):
    list_temp = []
    [list_temp.append(list1[i+1]) for i in range (len(list1)-1)]
    list1.pop()
    return list_temp, list1


#---------------- MAIN -----------------
#   Main implementation of functions

#   STATIC NUM
a = 23
c = 0
m = pow(10,8) + 1
seed = 0.023

#   PRNG
N = int(input('Number of elements: '))
list1 = prgn(a,c,N,seed)

#   Ex. 1 (b-i)
#   PLOT
plt.plot(list1)
plt.show()


#   Ex. 1 (b-ii)
#   PLOT
list_temp = list_plus_one(list1)
plt.scatter(list_temp[0], list_temp[1])
plt.show()


#   Ex. 1 (b-iii)
#   PLOT
list_temp2 = list_plus_one(list_temp[0])
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(list_temp2[0], list_temp[0], list_temp2[1]) 
plt.show()

#   Ex. 1 (a) - writting to .txt files

f = open("LCG1-N"+str(N)+"U"+str(seed)+".txt", "w")
f.writelines(str(list1))
f.close()



#------------ EXERCISE 2 ------------
#   Ex. 2
#   DEF IBM - RANDU -> LCG WITH DIFFERENT a,c,m.

a = pow(2,16) + 3
c = 0
m = pow(2,31) + 1


#   PRNG
N2 = int(input('Number of elements: '))
list1 = prgn(a,c,N,seed)

#   Ex. 2 (b-i)
#PLOT
plt.plot(list1)
plt.show()


#   Ex. 2 (b-ii)
#   PLOT
list_temp = list_plus_one(list1)
plt.scatter(list_temp[0], list_temp[1])
plt.show()


#   Ex. 2 (b-iii)
#   PLOT
list_temp2 = list_plus_one(list_temp[0])
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(list_temp2[0], list_temp[0], list_temp2[1]) 
plt.show()

#   FILE OPEN AND WRITE
f = open("LCG2-N"+str(N2)+"U"+str(seed)+".txt", "w")
f.writelines(str(list1))
f.close()
