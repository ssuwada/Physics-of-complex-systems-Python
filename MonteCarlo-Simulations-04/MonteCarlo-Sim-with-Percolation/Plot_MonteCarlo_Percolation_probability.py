
import matplotlib.pyplot as plt
import numpy as np

Pflow1 = np.loadtxt('F2_L10T100Step0.01.txt', delimiter=',')
Step1 = np.loadtxt('F3_L10T100Step0.01.txt', delimiter=',')
Pflow2 = np.loadtxt('F2_L50T100Step0.01.txt', delimiter=',')
Step2 = np.loadtxt('F3_L50T100Step0.01.txt', delimiter=',')
Pflow3 = np.loadtxt('F2_L100T100Step0.01.txt', delimiter=',')
Step3 = np.loadtxt('F3_L100T100Step0.01.txt', delimiter=',')

plt.plot(Pflow1, Step1,c='black', label='L = 10')
plt.plot(Pflow2, Step2,c='green', label='L = 50')
plt.plot(Pflow3, Step3,c='blue', label='L = 100')

plt.xlim([-0.01,1.01])
plt.ylim([-0.01,1.01])
plt.xlabel('Occupation probability')
plt.ylabel('Pflow')
plt.title("MonteCarlo Simulation")
plt.legend()


plt.show()