
import numpy as np
import matplotlib.pyplot as plt
from time import time, sleep
import math
from sklearn.preprocessing import MinMaxScaler

E = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

for i in E:
    # Open the file in read mode
    with open('Trajectories_T_1_N_10x10_Prob_' + str(i) + '.txt', 'r') as file:
        # Read all lines from the file
        lines = file.readlines()

    # Remove trailing newline characters and create a list
    values1 = [float(line.strip()) for line in lines]



    plt.plot(values1, label='Initial prob =' + str(i))

    # plt.plot(values1_normalized, label='Initial prob =' + str(i))

plt.xlabel('t - [MCS]')
plt.ylabel('Normalized Magnetization (m)')
plt.title("Trajectories for T = 1 and N = 10, MCS = 2000")
plt.legend()
plt.show()

for i in E:
# Open the file in read mode
    with open('Trajectories_T_1_N_20x20_Prob_'+str(i)+'.txt', 'r') as file:
    # Read all lines from the file
        lines = file.readlines()

    # Remove trailing newline characters and create a list
    values2 = [float(line.strip()) for line in lines]

    plt.plot(values2, label = 'Initial prob ='+str(i))

plt.xlabel('t - [MCS]')
plt.ylabel('Magnetization (m)')
plt.title("Trajectories for T = 1 and N = 20")
plt.legend()
plt.show()


for i in E:
# Open the file in read mode
    with open('Trajectories_T_1_N_40x40_Prob_'+str(i)+'.txt', 'r') as file:
    # Read all lines from the file
        lines = file.readlines()

    # Remove trailing newline characters and create a list
    values3 = [float(line.strip()) for line in lines]

    plt.plot(values3, label = 'Initial prob ='+str(i))

plt.xlabel('t - [MCS]')
plt.ylabel('Magnetization (m)')
plt.title("Trajectories for T = 1 and N = 40")
plt.legend()
plt.show()

for i in E:
# Open the file in read mode
    with open('Trajectories_T_1_N_80x80_Prob_'+str(i)+'.txt', 'r') as file:
    # Read all lines from the file
        lines = file.readlines()

    # Remove trailing newline characters and create a list
    values4 = [float(line.strip()) for line in lines]

    plt.plot(values4, label = 'Initial prob ='+str(i))

plt.xlabel('t - [MCS]')
plt.ylabel('Magnetization (m)')
plt.title("Trajectories for T = 1 and N = 80")
plt.legend()
plt.show()