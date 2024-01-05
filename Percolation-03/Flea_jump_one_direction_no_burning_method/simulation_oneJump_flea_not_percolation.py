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

def show_dogs_pos(arr):

    # Define the color map for the grid
    colors = ["white", "grey"]
    cmap = matplotlib.colors.ListedColormap(colors)
    plt.imshow(arr, cmap=cmap, vmin=0, vmax=2)

    # Add a color bar to the plot
    cbar = plt.colorbar()
    cbar.set_ticks([0.5, 1.5])
    cbar.set_ticklabels(['no dog', 'dog'])

    #Title 
    plt.title("Dog spread")

    plt.show()

#   2. Using the array from the previous exercise, place a flea on the leftmost dog in 
#       the first row of the grid – you can set a cell visited by the flea to ’2’. The flea will start 
#       jumping randomly from dog to dog, but it can only jump a distance of 1, i.e. to one of the four 
#       adjacent cells occupied by dogs. Each cell visited by the flea is marked ’2’ and remains ’2’ forever.
#       Introduce a parameter t denoting time – one unit of time denotes one jump. After time t, 
#       save it to file and then draw - mark dogs with gray color, 
#       empty cells with white color and flea with black color. The parameters p, L should be loaded 
#       from the initialization file ini.txt.

#   a) The above description of the jump is not exact, and it can be imple- mented in at least two ways. 
#       Do you see it? Think about it, discuss it, and choose one option to implement.
#   (b) Play around with different values for the parameters. 
#       You can even implement a simple animation to see how the flea jumps. 
#       Can you draw any conclusions from this exercise?

def initialize_pos(arr,pos1,pos2):
    arr[pos1][pos2] = 2

def dynamics_of_flea(arr,p,pos1,pos2,L):
    # Initialize pos and disease to given position
    arr[pos1][pos2] = 2
    actual_pos = [pos1,pos2]    #(x,y) 
    rnd = 0
    p = 1 - p
    t = 0

    i = pos1    # x
    j = pos2    # y
    
    # Possible jumps: (i-1,j) ; (i+1,j) ; (i,j-1) ; (i,j+1)
    break_flag = False
    possib_jump = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
    possib_jump_corr_border = []
    possib_jump_corr = []

    #   While there is no break flag do:
    while break_flag == False:

        #   Initialization of variables 
        possib_jump_corr.clear()
        possib_jump_corr_border.clear()
        break_flag = False
        count = 0

        possib_jump = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
        random.shuffle(possib_jump)

        for a in range(len(possib_jump)):
            #   Check if there are any borders in grid:
            #   Given positions -> i,j array2d size [m][n] [rows][columns]
            if possib_jump[a][0] >= 0 and possib_jump[a][0] < L and possib_jump[a][1] >= 0 and possib_jump[a][1] < L:
        #           position (i,j) exists in the array
                possib_jump_corr_border.append(possib_jump[a])
        #       Now we have possible positions to jump.
        print(possib_jump_corr_border)

    #   Check if there is any dog next to our position.
    #   If 1 is on position that means there is a potential dog to be infected :D

        for b in range(len(possib_jump_corr_border)):
            if arr[possib_jump_corr_border[b][0]][possib_jump_corr_border[b][1]] == 1:
                possib_jump_corr.append(possib_jump_corr_border[b])
        
        if len(possib_jump_corr) == 0:
            break_flag = True

        print(possib_jump_corr)

        for c in range(len(possib_jump_corr)):
            rnd = rand_func()
            if rnd > p:
                arr[possib_jump_corr[c][0]][possib_jump_corr[c][1]] = 2
                i = possib_jump_corr[c][0]
                #print([possib_jump_corr[c][0]])
                #print([possib_jump_corr[c][1]])
                j = possib_jump_corr[c][1]
                t = t + 1
                break
            else:
                count = count + 1

            # End of spreading disease:

            if count == len(possib_jump_corr):
                break_flag = True

        # End of while
    
    print(t)

    # Define the color map for the grid
    cmap = plt.cm.get_cmap('Greys', 3)
    cmap.set_under('white') #dog
    cmap.set_over('black')  #flea on dog
    plt.imshow(arr, cmap=cmap, vmin=0, vmax=2)

    # Add a color bar to the plot
    cbar = plt.colorbar()
    cbar.set_ticks([0.5, 1.5])
    cbar.set_ticklabels(['no dog', 'flea'])

    plt.title("Flea spread on dogs - only one jump")

    plt.show()


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
show_dogs_pos(arr)

#   ---------------------- (b) -----------------------

#       Ex. 1 (b)
#       0 - no dog 
#       1 - there is dog
#       2 - infected dog


#   Simulation Ex. 1 (b)

arr2 = create_array(L)
arr2 = fill_array(L,p2,arr2)
dynamics_of_flea(arr2,p,pos1_x,pos2_y,L)


end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time)
