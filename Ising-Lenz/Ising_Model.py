#   --------FOURTH CLASS EXERCISES-----------
#            Metropolis algorithm
#           ---------------------
#              SEBASTIAN SUWADA 
#           ---------------------
#

#   ------------- IMPORT -------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from time import time, sleep
import math
import matplotlib.colors
import multiprocessing as mp


# SETUP

def initialize(N, E):
    agents_positive = int(N**2*E)                         # positive spin amount
    agents_negative = int(N**2 - agents_positive)         # negative spin amount 

    a = (N,N)
    list_temp = []

    for i in range(agents_positive):
        list_temp.append(1)
    for i in range(agents_negative):
        list_temp.append(-1)

    np.random.shuffle(list_temp)

    arr_temp = np.reshape(list_temp,a)

    return arr_temp

def chose_rnd(N):
    i = np.random.randint(0, N-1)
    j = np.random.randint(0, N-1)
    return i,j

def calculate_dE(N,arr):
    i,j = chose_rnd(N)
    dE = 2*arr[i][j]*(arr[i-1][j]+arr[i+1][j]+arr[i][j-1]+arr[i][j+1])
    return dE, i, j

def chose_rnd_uniform():
    return np.random.uniform(0,1)

def calculate_e_pow(dE,T):
    return (math.e)**(-dE/T)

def calculate_M(N,Sij):
    return (1/(N**2))*(np.sum(Sij))

def oneMCS(N, arr, T):

    Sij = []
    random_list = []
    random_list = [np.random.uniform(0,1) for _ in range(N**2)]

    for i in range(N**2):
        dE, i, j = calculate_dE(N,arr)
        if dE <= 0:
            arr[i][j] *= -1
        else:
            U = random_list[i] # (zamienic na np.random.random(N,N)<P).ASTYPE(INT) zeby byl jeden matrix
            if U < calculate_e_pow(dE,T):
                arr[i][j] *= -1
        Sij.append(arr[i][j])
    
    m = calculate_M(N,Sij)

    return m, arr

def imshow_init(arr,T,N):

    # Define the color map for the grid
    colors = ["grey", "white"]
    cmap = matplotlib.colors.ListedColormap(colors)
    plt.imshow(arr, cmap=cmap, vmin=0, vmax=2)

    # Add a color bar to the plot
    cbar = plt.colorbar()
    cbar.set_ticks([0.5, 1.5])
    cbar.set_ticklabels(['Negative Spin', 'Positive Spin'])

    #Title 
    plt.title("Initial configuration of spins for T = "+str(T)+" and "+str(N)+"x"+str(N))
    plt.show()

def imshow_final(arr,T,N):

    # Define the color map for the grid
    colors = ["grey", "white"]
    cmap = matplotlib.colors.ListedColormap(colors)
    plt.imshow(arr, cmap=cmap, vmin=0, vmax=2)

    # Add a color bar to the plot
    cbar = plt.colorbar()
    cbar.set_ticks([0.5, 1.5])
    cbar.set_ticklabels(['Negative Spin', 'Positive Spin'])

    #Title 
    plt.title("Final configuration of spins for T = "+str(T)+" and "+str(N)+"x"+str(N))
    plt.show()

def simulation_1(N, arr, dE, T, n):

    empty_array = np.zeros((N, N))

    #   SHOW BEFORE LATTICE
    # Create files of values
    f2 = open("Initial_T_"+str(T)+"_N_"+str(N)+".txt", "w")
    f3 = open("Final_T_"+str(T)+"_N_"+str(N)+".txt", "w")

    #   Write initial values from array into file

    for i in range(N):
        for j in range(N):
            f2.write(str(arr[i][j]) + '\n')

    imshow_init(arr,T,N)

    #   Perform MCS

    for f in range(n):
        m, empty_array = oneMCS(N, arr, dE, T)
    
    #   Write final values from array into file

    for i in range(N):
        for j in range(N):
            f3.write(str(empty_array[i][j]) + '\n')

    imshow_final(arr,T,N)

    f2.close()
    f3.close()

def simulation_2(N, T, n):
    E = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

    magnetization = []

    for i in E:
        print(f'Fraction of spins: {i}  for Monte Carlo simulation started..')
        magnetization.clear()
        arr = initialize(N,i)
        #dE = calculate_dE(N,arr)
        empty_array = np.zeros((N, N))

#   Perform MCS
        for f in range(n):
            m, empty_array = oneMCS(N, arr, T)
            magnetization.append(m)

    # Create file of values for magnetizaion
        f = open("Trajectories_T_"+str(T)+"_N_"+str(N)+"x"+str(N)+"_Prob_"+str(i)+".txt", "w")
        for item in magnetization:
            f.write(str(item) + '\n')
        f.close()

# powtorzyc symulacje jeszcze z 100 raz 

def simulation_3(N, n):
    T = np.arange(0.5, 3.55, 0.05)    
    magnetization = []
    magnetization_full = []

    for i in T:
        magnetization.clear()
        arr = initialize(N,0.5)
        dE = calculate_dE(N,arr)
        empty_array = np.zeros((N, N))

#   Perform MCS
        for f in range(n):
            m, empty_array = oneMCS(N, arr, dE, i)
            magnetization.append(m)
        magnetization_full.append(abs(np.sum(magnetization)/len(magnetization)))

    return magnetization_full

def simulation_3_2(N,n):
    T = np.arange(0.5, 3.55, 0.05)
    magnetization_full = np.zeros(T.shape)

    for idx, i in enumerate(T):
        print(f'Iteration: {idx} running..')
        arr = initialize(N, 1)
        dE = calculate_dE(N, arr)
        empty_array = np.zeros((N, N))

        # Perform MCS
        magnetization = np.zeros(n)
        for f in range(n):
            m, empty_array = oneMCS(N, arr, i)
            magnetization[f] = m

        magnetization_full[idx] = np.abs(np.mean(magnetization))

    filename = "Magnetization_Full_range_N_" + str(N) + "x" + str(N) + ".txt"
    with open(filename, "w") as f:
        for item in magnetization_full:
            f.write(str(item) + '\n')

    return magnetization_full

def sim_more(N,n,iter):
    magnetization_full = []
    T = np.arange(0.5, 3.55, 0.05)    
    list_temp = []
    result = []
    magnetization_full = [0] * len(T)

    for i in range(iter):
        print(f'Iteration: {i}  running..')
        list_temp = simulation_3_2(N,n)
        for j in range(len(T)-1):
            magnetization_full[j] = magnetization_full[j] + list_temp[j]

    for value in magnetization_full:
        result.append(value / len(T))

    #   Create file of values for magnetizaion
    f = open("Magnetization_Full_range_N_"+str(N)+"x"+str(N)+".txt", "w")
    for item in result:
        f.write(str(item) + '\n')
    f.close()

def sim_more_2(N, n, iter):
    T = np.arange(0.5, 3.55, 0.05)
    magnetization_full = np.zeros(len(T))

    for i in range(iter):
        print(f'Iteration: {i} running..')
        list_temp = simulation_3_2(N, n)
        magnetization_full += np.array(list_temp)

    magnetization_full /= iter

    # Create file of values for magnetization
    filename = "Magnetization_Full_range_N_" + str(N) + "x" + str(N) + ".txt"
    with open(filename, "w") as f:
        for item in magnetization_full:
            f.write(str(item) + '\n')

# ----------- MAIN -----------

N = 100     # Square lattice size
E = 0.5     # Initial status define percent of positive spins
T = 4       # Temperature
n = 100     # performance of MCS(monte carlo sim)

#  ------- FIRST TASK -------

#   1. Configuration of spins after 100 MC steps 
#       for a lattice of 10 × 10 and 80 × 80 
#       for three temperatures: T1 = 1, T2 = 2.26, T3 = 4.

# ts = time()

#   Initial values for first task:
#   LATTICE 10x10

E = 0.5     # Initial status define percent of positive spins
n = 100     # Performance of MCS(monte carlo sim)


#   Square lattice 10 x 10 

# N = 10

# T = 1
# arr = initialize(N,E)
# dE = calculate_dE(N,arr)
# simulation_1(N,arr,dE, T, n)

# T = 2.26
# arr = initialize(N,E)
# dE = calculate_dE(N,arr)
# simulation_1(N,arr,dE, T, n)

# T = 4
# arr = initialize(N,E)
# dE = calculate_dE(N,arr)
# simulation_1(N,arr,dE, T, n)

#   Square lattice 80 x 80 

# N = 80

# T = 1
# arr = initialize(N,E)
# dE = calculate_dE(N,arr)
# simulation_1(N,arr,dE, T, n)

# T = 2.26
# arr = initialize(N,E)
# dE = calculate_dE(N,arr)
# simulation_1(N,arr,dE, T, n)

# T = 4
# arr = initialize(N,E)
# dE = calculate_dE(N,arr)
# simulation_1(N,arr,dE, T, n)

# time_taken = time() - ts
# print(f'First task done in {time_taken} seconds')

#  ------- SECOND TASK -------

N = [10, 20, 40, 80]     # Square lattice size
E = 0.5     # Initial status define percent of positive spins
T = 1       # Temperature
n = 200     # performance of MCS(monte carlo sim)

ts = time()

#simulation_2(N[0], T, n)
#simulation_2(N[1], T, n)
#simulation_2(N[2], T, n)
#simulation_2(N[3], T, n)

time_taken = time() - ts
print(f'First task done in {time_taken} seconds')

#  ------- THIRD TASK -------

N = 80
T = 1.85

ts = time()
#simulation_2(N, T, n)
#T = 2.26
#simulation_2(N, T, n)
# T = 3.25
# simulation_2(N, T, n)

time_taken = time() - ts
print(f'First task done in {time_taken} seconds')

#  ------- 4th TASK -------

n = 1000

ts = time()

# N = 10
# simulation_3_2(N,n)
# N = 20
# simulation_3_2(N,n)
# N = 40
# simulation_3_2(N,n)
# N = 80
# simulation_3_2(N,n)

time_taken = time() - ts
print(f'First task done in {time_taken} seconds')


