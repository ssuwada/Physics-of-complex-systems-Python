#   --------FOURTH CLASS EXERCISES-----------
#              Site percolation
#           ---------------------
#              SEBASTIAN SUWADA 
#           ---------------------
#

#   ------------- IMPORT -------------

import numpy as np 
import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation
import matplotlib.colors
import time

start_time = time.time()


#   ---------------------- FUNC -----------------------

#   1. Implement a square grid L × L – you can just represent it by an array 
#       A[i, j], i, j = 1, . . . , L, but you can also use other structures. 
#       Fill an array: ’1’ (dog) with probability p or ’0’ (empty) with probability 1 − p. 
#       Save it to a file and draw it - mark the dog with the gray color and the empty cell with 
#       the white color. The parameters p, L should be loaded from the initialization file ini.txt.

def load_fromTXT1():
    with open("init.txt", "r") as file:
        data = file.read().strip().split(",")
    L = int(data[0])
    p = float(data[1])
    p2 = float(data[2])
    return L,p,p2

def create_array(L):
    a_shape = (L, L) 
    return np.zeros(a_shape)

def rand_func():
    return random.random()  # X value

def fill_array(L,p,arr):
    probablity = 1 - p
    temp = 0
    for x in range(L):
        for y in range(L):
            rnd = rand_func()
            if rnd > probablity:
                arr[x][y] = 1   #there is a dog
            else:
                arr[x][y] = 0   #there is no dog
    return arr

def load_fromTXT2():
    with open("init_per.txt", "r") as file:
        data = file.read().strip().split(",")
    L = int(data[0])            #Lattice
    T = int(data[1])            #Number of trials
    pmax = float(data[2])       #max p value
    pmin = float(data[3])       #min p val
    step = float(data[4])       #step

    return L,T,pmax,pmin,step

def find_nearest_path(arr,L):

    i = 0
    j = 0

    i1 = 0 
    j1 = 0
    
    t = 3
    
    val_retur = 0

    iter_list = []
    iter_list_corr = []
    
    arr_temp = create_array(L)
    arr_temp = np.copy(arr)

    break_flag = False


    # Check if there is a dog and give it t = 1 - > init function

    for g in range(L):
        if arr[0][g] == 1:
            arr_temp[0][g] = t

    while break_flag == False:

    # Create iter_list which have positions of existing t

        #my_marker = t

        iter_list.clear()

        for b in range(len(arr_temp)):
            for b1 in range(len(arr_temp)):
                if arr_temp[b][b1] == t: 
                    iter_list.append([b,b1])
                    if b == L-1:
                        break_flag = True
                        #print('Last row reached..')
                        val_retur = 1
                    #plt.scatter(b1, b, marker='${}$'.format(my_marker), color='white', s=40) # for creating numbers on squares

    # Check for that possible next variants and check if there are not any borders or duplicates

        iter_list_corr.clear()

        for l in range(len(iter_list)):
            i = iter_list[l][0]
            j = iter_list[l][1]
            neighb = [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]
            for l2 in range(len(neighb)):
                if neighb[l2][0] >= 0 and neighb[l2][0] < L and neighb[l2][1] >= 0 and neighb[l2][1] < L and \
                    arr[neighb[l2][0]][neighb[l2][1]] == 1 and arr_temp[neighb[l2][0]][neighb[l2][1]] != t and \
                    arr_temp[neighb[l2][0]][neighb[l2][1]] != t-1:
                    iter_list_corr.append(neighb[l2])

        
        if len(iter_list_corr) == 0:
             break_flag = True
             val_retur = 0
             #print('Last row didnt reach..')

    # Remove duplicates:
        
        iter_list_corr = [list(x) for x in set(tuple(x) for x in iter_list_corr)] #Positions of array(arr) for next step

        t = t+1

        for h in range(len(iter_list_corr)):
            i1 = iter_list_corr[h][0]
            j1 = iter_list_corr[h][1]
            arr_temp[i1][j1] = t
        
    #print(t-3)

    #  # Define the color map for the grid
    # colors = ["white", "grey"]
    # cmap = matplotlib.colors.ListedColormap(colors)
    # plt.imshow(arr, cmap=cmap, vmin=0, vmax=2)

    # # # Add a color bar to the plot
    # cbar = plt.colorbar()
    # cbar.set_ticks([0.5, 1.5])
    # cbar.set_ticklabels(['no dog', 'dog'])

    # # # Title 
    # plt.title("Dog spread with ticks")
    # plt.show()

    return val_retur,t-3

def percolation_MC(L,T,plow,pmax,step):
    temp_out = 0
    t = 0 

    prob_step = []
    wrapp_prob = []
    Pflow_list = []

    #f = open("Ave-L"+str(L)+"T"+str(T)+".txt", "w")
    #   Pflow - F3 ; p - F2
    f2 = open("F2_L"+str(L)+"T"+str(T)+"Step"+str(step)+".txt", "w")
    f3 = open("F3_L"+str(L)+"T"+str(T)+"Step"+str(step)+".txt", "w")

    #f.write(""+str(L)+"%L"+"\n"+str(T)+"%T"+"\n"+str(plow)+"%p0"+"\n"+str(pmax)+"%pmax"+"\n"+str(step)+"'%'step"+"\n")
    arr_temp = create_array(L)

    for value in np.arange(plow, pmax, step):
        for i in range(T):
            arr_temp = fill_array(L,value,arr_temp)
            temp_out, t = find_nearest_path(arr_temp,L)
            wrapp_prob.append(temp_out)
   
        Pflow = float(sum(wrapp_prob)/T)
        #f.write("Step"+str(value)+"\n")
        #f.write("Pflow"+str(Pflow)+"\n")
        f2.write(str(round(value,2))+",")
        f3.write(str(Pflow)+",")

        print(Pflow)
        wrapp_prob.clear()
        Pflow_list.append(Pflow)
        prob_step.append(value)

    #f.close()
    f2.close()
    f3.close()
    return prob_step,Pflow_list

#   ---------------------- MAIN -----------------------

#   Input values of L - grid size and p - probablility (should be get from txt file)

L = 0     #Grid size
p = 0     #Probability of jumping into other dog
p2 = 0    #probability for Amount of dogs

L,p,p2 = load_fromTXT1()

#   Input position

pos1_x = 50
pos2_y = 50

#   ---------------------- (a) -----------------------
#       Ex. 1

#   Simulation Ex. 1

arr = create_array(L)
arr = fill_array(L,p2,arr)

#   Simulation Ex. 2 - percolation example

L1 = 0
T = 0
pmax = 0
pmin = 0
step = 0
L1,T,pmax,pmin,step = load_fromTXT2()

percolation_MC(L1,T,pmin,pmax,step)

#   Execution time of program:

end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time)