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


#   Write a program to solve the site percolation problem on the square lattice L timesL. 
#       As a reminder, in the site percolation problem, each site of a lattice is independently occupied with 
#       probability p. Therefore, a single Monte Carlo run consists of starting a lattice: 
#       for each site, you choose a random number r ∼ U(0,1), and if r < p then you put A[i,j] = 1 at a given site, 
#       otherwise you put A[i,j] = 0. After this step, you are ready to check if the path connecting the first and 
#       the last row exists (using The Burning Method, see e.g. pages 24-25 in ICP). Using Monte Carlo simulations, 
#       which should consist of T trials, generate the output file for the probability Pflow that the path connecting 
#       the firstandlastrowexistsasafunctionofp,wherep=p0 :dp:pk.
#       The output data should be stored in a single file for each set of input param- eters with an automatically 
#       generated name according to the following scheme: ′Ave−L′ + L +′ T ′ + T +′ .txt′. 
#       To collect output data, you need to introduce input data:

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

def dynamics_with_percolation(arr,p,pos1,pos2,L):
    # Initialize pos and disease to given position
    arr[pos1][pos2] = 2
    rnd = 0
    prob = 1 - p
    t = 0

    i = pos1    # x
    j = pos2    # y
    
    # Possible jumps: (i-1,j) ; (i+1,j) ; (i,j-1) ; (i,j+1)
    possib_jump = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
    possib_jump_corr_border = []
    possib_jump_corr = []
    positions_per = []

        #   Initialization of variables 
    possib_jump_corr.clear()
    possib_jump_corr_border.clear()
    positions_per.clear()

    #possib_jump = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
    random.shuffle(possib_jump)

    for a in range(len(possib_jump)):
        #   Check if there are any borders in grid:
        #   Given positions -> i,j array2d size [m][n] [rows][columns]
        if possib_jump[a][0] >= 0 and possib_jump[a][0] < L and possib_jump[a][1] >= 0 and possib_jump[a][1] < L:
        #           position (i,j) exists in the array
            possib_jump_corr_border.append(possib_jump[a])
        #       Now we have possible positions to jump.
    #print(possib_jump_corr_border)

    #   Check if there is any dog next to our position.
    #   If 1 is on position that means there is a potential dog to be infected :D

    for b in range(len(possib_jump_corr_border)):
        if arr[possib_jump_corr_border[b][0]][possib_jump_corr_border[b][1]] == 1:
            possib_jump_corr.append(possib_jump_corr_border[b])
        
    if len(possib_jump_corr) == 0:
        break_flag = True

    #print(possib_jump_corr)

    for c in range(len(possib_jump_corr)):
        rnd = rand_func()
        if rnd > prob:
            arr[possib_jump_corr[c][0]][possib_jump_corr[c][1]] = 2
            i = possib_jump_corr[c][0]
            j = possib_jump_corr[c][1]
            positions_per.append((i,j))
    
    return positions_per,arr
    
def percolation(arr,p,pos1,pos2,L):
    
    pos_x = pos1
    pos_y = pos2
    positions = []
    positions1 = []
    extended_pos = []
    temp = []
    break_flag = False

    positions1, arr = dynamics_with_percolation(arr,p,pos_x,pos_y,L)
    extended_pos.extend(positions1)

    while break_flag == False:

        temp.extend(extended_pos)
        extended_pos.clear()
        
        for i in range(len(temp)):
            positions, arr = dynamics_with_percolation(arr,p,temp[i][0],temp[i][1],L)
            extended_pos.extend(positions)
            positions.clear()
            #print(temp[i][0])
        if len(extended_pos) == 0:
            break_flag = True

        temp.clear()

        # Define the color map for the grid
    cmap = plt.cm.get_cmap('Greys', 3)
    cmap.set_under('white') #dog
    cmap.set_over('black')  #flea on dog
    plt.imshow(arr, cmap=cmap, vmin=0, vmax=2)

    # Add a color bar to the plot
    cbar = plt.colorbar()
    cbar.set_ticks([0.5, 1.5])
    cbar.set_ticklabels(['no dog', 'flea'])

    plt.title("Flea spread on dogs with percolation")

    plt.show()

def scatter_plot(L,T,plow,pmax,step):

    prob_step,Pflow_list = percolation_MC(L,T,plow,pmax,step)
    plt.scatter(prob_step,Pflow_list, c='black', label='Plot 1')
    plt.plot(prob_step, Pflow_list, '--')
    prob_step1,Pflow_list1, = percolation_MC(L+40,T,plow,pmax,step)
    plt.scatter(prob_step1,Pflow_list1, c='green', label='Plot 3')
    plt.plot(prob_step1, Pflow_list1, '--')
    prob_step2,Pflow_list2, = percolation_MC(L+90,T,plow,pmax,step)
    plt.scatter(prob_step2,Pflow_list2, c='blue', label='Plot 2')
    plt.plot(prob_step2, Pflow_list2, '--')


    plt.xlim([0,1])
    plt.ylim([0,1])
    plt.xlabel('Occupation probability')
    plt.ylabel('Pflow')
    plt.title("MonteCarlo Simulation")
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
#show_dogs_pos(arr)

#   ---------------------- (b) -----------------------

#       Ex. 1 (b)
#       0 - no dog 
#       1 - there is dog
#       2 - infected dog


#   Simulation Ex. 1 (b)

# arr2 = create_array(L)
# arr2 = fill_array(L,p2,arr2)
# dynamics_of_flea(arr2,p,pos1_x,pos2_y,L)

#   ---------------------- Ex. Percolation -----------------------

#   Simulation Ex. 2 - percolation example

L1 = 0
T = 0
pmax = 0
pmin = 0
step = 0
L1,T,pmax,pmin,step = load_fromTXT2()

print(L1,T,pmax,pmin,step)
#percolation_MC(L1,T,pmin,pmax,step)
#scatter_plot(L1,T,pmin,pmax,step)

find_nearest_path(arr,L)
#percolation(arr,p,pos1_x,pos2_y,L)



#   Execution time of program:

end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time)




#   ---------------------- BRUDNOPIS -----------------------

#       plt.scatter(5, 5, marker='x', color='red', s=10) - > dodaj marker w kszatlcie x

#   matplotpib inport animation
#   anim = FUNCANIMATION(FIG,animate,interval=1)
#   rng.random(9).reshape((3,3)) -> reshape of arr
#   plt.imshow()