#   ---------SECOND CLASS EXERCISES -----------
#           Fleas jumping on two dogs
#           ---------------------
#              SEBASTIAN SUWADA 
#           ---------------------
#

import numpy as np 
import matplotlib.pyplot as plt
import random


#   Consider a population of N fleas jumping between two dogs, 
#   let us call these dogs ACE and REX. In each time step a 
#   single randomly selected flea jumps to the other dog with 
#   probability p. Initially all fleas live with REX. 
#   Can you predict what will be the situation in the long time limit?

#       1. Write a program, which simulates the model. 
#       The user enters the val- ues of three parameters: p ∈ [0, 1], N ∈ [0, 106], tsym ∈ [0, 106]. 
#       As a result two trajectories, showing the number of fleas on ACE NA and the number of fleas on REX NR 
#       in time t ∈ [0,tsym]. The results should be automatically saved in file named according to the 
#       following schema ”N”+N+”p”+p+”t”+tsym+”.txt”, for example file ”N100p0.3t1000.txt” 
#       consists of results for N = 100, p = 0.3, tsym = 1000. Each row in the file should contain of 
#       three numbers separated by double space: t NA NR.

#       2. Prepare a figure, which present NA and NR as a function of t; 
#       use leg- end for NA and NB. Repeat it for several values of N - what are your conclusions?


#   ------------- FUNC -------------

#   Checking if it is float or int number NOT str

def check_if_number_float(inp):
    try:
        number = float(inp)
        return (True, number)
    except: 
        return(False, inp)
    
def check_if_number_int(inp):
    try:
        number = int(inp)
        return (True, number)
    except: 
        return(False, inp)

#   Create conditions of input 

def user_input_init():

#   Initialize working variables as a Tuple.

    N_right = (False,-1000)
    p_right = (False, -0.9)
    Tsym_right = (False, -1000)

#   Initailize temp variables.

    temp = 0
    temp1 = 0
    temp2 = 0

#   While loop input user

    while N_right[0] != True or temp > 10000000 or temp < 0:
        N = input('Give amount of population flea..:  \n')
        N_right = check_if_number_int(N)
        temp = N_right[1]

    while p_right[0] != True or temp1 < 0 or temp1 > 1:
        print('Decide number from (0,1) \n') 
        p = input('Give probability of jumping to other dog..:  \n')
        p_right = check_if_number_float(p)
        temp1 = p_right[1]

    while Tsym_right[0] != True or temp2 < 0 or temp2 > 10000000:
        print('Type time in seconds \n')
        Tsym = input('Give time of the simulation..:  \n')
        Tsym_right = check_if_number_int(Tsym)
        temp2 = Tsym_right[1]
    return N_right[1], p_right[1], Tsym_right[1]

#   Initialization population of fleas

def fleas_rex_init(N):
    list_temp = []
    for i in range(N):
        list_temp.append(1)
    return list_temp

#   Algorithm of simulation

def simulation(rex_list, p, Tsym):
    one = []
    minus_one = []
    extra_data = []
    time_count = []
    for i in range(Tsym):
        rnd_place = random.randint(0,len(rex_list)-1)
        prob = random.random()
        if prob < p:
            if rex_list[rnd_place] == 1:    
                rex_list[rnd_place] = -1
            else:
                rex_list[rnd_place] = 1
        extra_data.append((i,rex_list.count(1),rex_list.count(-1))) #Append tuple of 3 elements to list extra data in each iteration.

        one.append(rex_list.count(1))
        minus_one.append(rex_list.count(-1))
    return one, minus_one, extra_data

#   Creating and showing plots that can describe situation with fleas on both dogs.

def show_simulation_plot(dog1,dog2):
    plt.plot(dog1, color="blue")
    plt.plot(dog2, color="red")

    plt.show()

def create_write_file(extra_data, N, p, T):
    f = open("N"+str(N)+"p"+str(p)+"t"+str(T)+".txt", "w")
    f.write("Tsym"+"  "+"NA"+"  "+"NR"+" \n")
    for i in range(T):
        f.write("  "+str(extra_data[i][0])+"  "+str(extra_data[i][1])+"  "+str(extra_data[i][2])+" \n")
    f.close()
    
#   ------------- MAIN -------------

#   Variables:
#   Tsym - Time simulation 
#   N - Number of population 
#   p - probability of jumping to other dog

N_right, p_right, Tsym_right = user_input_init()

#   Initialize fleas on one dog (Create list)

fleas = fleas_rex_init(N_right)

#   Run simulation

one, minus_one, extra_data = simulation(fleas, p_right, Tsym_right)

#   Show simulation
#   Plot to variables NA and NR in function of time

show_simulation_plot(one, minus_one)

#   Write to file

create_write_file(extra_data, N_right, p_right, Tsym_right)
