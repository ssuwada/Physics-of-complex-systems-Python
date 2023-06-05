    
import numpy as np
import matplotlib.pyplot as plt
from time import time, sleep
import math
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import DBSCAN

T = np.arange(0.5, 3.55, 0.05).reshape(-1, 1)    

with open('Magnetization_Full_range_N_10x10.txt', 'r') as file:
    # Read all lines from the file
    lines = file.readlines()
    # Remove trailing newline characters and create a list
    values1 = [float(line.strip()) for line in lines]

# Normalize the magnetization values between 0 and 1
    scaler = MinMaxScaler()
    values1_normalized = scaler.fit_transform(np.array(values1).reshape(-1, 1))

# Create a scatter plot of the filtered data
plt.plot(T, values1_normalized, color='red', label='L10')
plt.scatter(T,values1_normalized, marker='o')
plt.xlabel('T - Reducet temperature')
plt.ylabel('Magnetization (m)')
plt.title("Magnetization as a function of temperature")
#plt.legend()
#plt.show()

with open('Magnetization_Full_range_N_20x20.txt', 'r') as file:
    # Read all lines from the file
    lines = file.readlines()
    # Remove trailing newline characters and create a list
    values2 = [float(line.strip()) for line in lines]


# Normalize the magnetization values between 0 and 1
    scaler = MinMaxScaler()
    values1_normalized = scaler.fit_transform(np.array(values2).reshape(-1, 1))


# Create a scatter plot of the filtered data
plt.plot(T,values1_normalized, color='blue', label='L20')
plt.scatter(T,values1_normalized, marker='s')
# plt.xlabel('T - Reducet temperature')
# plt.ylabel('Magnetization (m)')
# plt.title("Magnetization as a function of temperature")
# plt.legend()
#plt.show()

with open('Magnetization_Full_range_N_40x40.txt', 'r') as file:
    # Read all lines from the file
    lines = file.readlines()
    # Remove trailing newline characters and create a list
    values4 = [float(line.strip()) for line in lines]

# Normalize the magnetization values between 0 and 1
    scaler = MinMaxScaler()
    values1_normalized = scaler.fit_transform(np.array(values4).reshape(-1, 1))

# Create a scatter plot of the filtered data
plt.plot(T, values1_normalized, color='black', label='L40')
plt.scatter(T,values1_normalized, marker='v')
plt.xlabel('T - Reducet temperature')
plt.ylabel('Magnetization (m)')
plt.title("Magnetization as a function of temperature")
#plt.legend()
#plt.show()

with open('Magnetization_Full_range_N_80x80.txt', 'r') as file:
    # Read all lines from the file
    lines = file.readlines()
    # Remove trailing newline characters and create a list
    values3 = [float(line.strip()) for line in lines]

# Normalize the magnetization values between 0 and 1
    scaler = MinMaxScaler()
    values1_normalized = scaler.fit_transform(np.array(values3).reshape(-1, 1))

# Create a scatter plot of the filtered data
plt.plot(T,values1_normalized, color='green', label='L80')
plt.scatter(T,values1_normalized, marker='^')
plt.xlabel('T - Reducet temperature')
plt.ylabel('Magnetization (m)')
plt.title("Magnetization as a function of temperature")
plt.legend()
plt.show()