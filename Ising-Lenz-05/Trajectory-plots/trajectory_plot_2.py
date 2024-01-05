
import numpy as np
import matplotlib.pyplot as plt
from time import time, sleep
import math
from sklearn.preprocessing import MinMaxScaler


E = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

for i in E:
# Open the file in read mode
    with open('Trajectories_T_1.85_N_80x80_Prob_'+str(i)+'.txt', 'r') as file:
    # Read all lines from the file
        lines = file.readlines()

    # Remove trailing newline characters and create a list
    values1 = [float(line.strip()) for line in lines]

    # # # Create an instance of MinMaxScaler
    # scaler = MinMaxScaler(feature_range=(-1, 1))
    # # # Normalize the data
    # normalized_y = scaler.fit_transform(np.array(values1).reshape(-1, 1)).flatten()

    plt.plot(values1, label = 'Initial prob ='+str(i))

plt.xlabel('t - [MCS]')
plt.ylabel('Magnetization (m)')
plt.title("Trajectories for T = 1.85 and N = 80")
plt.legend()
plt.show()


for i in E:
# Open the file in read mode
    with open('Trajectories_T_2.26_N_80x80_Prob_'+str(i)+'.txt', 'r') as file:
    # Read all lines from the file
        lines = file.readlines()

    # Remove trailing newline characters and create a list
    values2 = [float(line.strip()) for line in lines]

    plt.plot(values2, label = 'Initial prob ='+str(i))

plt.xlabel('t - [MCS]')
plt.ylabel('Magnetization (m)')
plt.title("Trajectories for T = 2.26 and N = 80")
plt.legend()
plt.show()


for i in E:
# Open the file in read mode
    with open('Trajectories_T_3.25_N_80x80_Prob_'+str(i)+'.txt', 'r') as file:
    # Read all lines from the file
        lines = file.readlines()

    # Remove trailing newline characters and create a list
    values3 = [float(line.strip()) for line in lines]

    # scaler = MinMaxScaler(feature_range=(-1, 1))
    # # # # Normalize the data

    # normalized_y = scaler.fit_transform(np.array(values1).reshape(-1, 1)).flatten()

    plt.plot(values3, label = 'Initial prob ='+str(i))

plt.xlabel('t - [MCS]')
plt.ylabel('Magnetization (m)')
plt.title("Trajectories for T = 3.25 and N = 80")
plt.legend()
plt.show()
