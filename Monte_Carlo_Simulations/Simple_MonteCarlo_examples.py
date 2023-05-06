#   --------THIRD CLASS EXERCISES-----------
#          Monte Carlo simulations
#           ---------------------
#              SEBASTIAN SUWADA 
#           ---------------------
#

#   ------------- IMPORT -------------

import numpy as np 
import matplotlib.pyplot as plt
import random

#   ------------- FUNC -------------

def N_log(k):
    N = 10**k
    return N

def rand_xy():
    r = 1

    rnd1 = random.random()  # X value
    rnd2 = random.random()  # Y value

    return rnd1, rnd2
         
def calculate_pi(c_ount0, c_ount1):
     Pi = np.pi

     pi = 4*(c_ount0/c_ount1)
     e = abs(Pi - pi)
     return pi, e

#       Simulation variables numbers - simulation_pi()
#       For this we use square, and generate numbers random which are 
#       between zero and 1 and then we check if this value is in circle!
#       Count the numbers that hit into the circle - > c_ount0, hit into square -> c_ount1
#       Thats gives us value of estimated pi, and erorr which is 'e'

def simulation_pi(k):

    c_ount1 = 0
    c_ount0 = 0
    r = 1

    N = N_log(k)
    for i in range(N):
            rnd1, rnd2 = rand_xy()
            if rnd1**2 + rnd2**2 <= r:
                c_ount0 = c_ount0 + 1
            c_ount1 = c_ount1 + 1
    #print(c_ount0,c_ount1)
    pi, e = calculate_pi(c_ount0,c_ount1)
    #print(pi,e,N)
    return pi,e

#   Main simulation -> creating list of PI values and errors 

def simulation_ex1(N,k):
    temp_list_err = []
    temp_list_pi = []
    temp_pi = 0
    temp_err = 0
    for i in range(N):
        temp_pi, temp_err = simulation_pi(k)
        temp_list_err.append(temp_err)
        temp_list_pi.append(temp_pi)
    return temp_list_err, temp_list_pi

#   Calculating average value of numbers from list

def Average(list1):
     su = sum(list1)
     l = len(list1)
     avg = su/l
     return avg

#   LogLog PLOT

def plot_logLog(N,k,avg_err):
    x = np.linspace(1,N,k)
    plt.loglog(x,avg_err)
    plt.show()


#   Create simulation that will make list of average error in range of k value (for each k value)
#   And makes plot -> logxlog plot

def simulation_err_avg(N,k):
    temp1 = []
    temp2 = []
    avg_err = []
    temp3 = 0

    for i in range(k):
        temp1, temp2 = simulation_ex1(N,i)
        temp3 = Average(temp1)
        avg_err.append(temp3)

    plot_logLog(N,k,avg_err)

#   Toss coin func - dete -> Heads - 1, down - 0

def toss_coin():
    dete = 0
    coin = random.random()
    if coin >= 0.5:
        dete = 1
    else:
        dete = 0
    return dete

#   Simple toss simulation of N iterations

def simulation_tossRange(N):
    toss_list = []
    for i in range(N):
        toss_list.append(toss_coin())
    return toss_list
    #print(toss_list)

#   Create toss simulation of three tosses in row. 

def tossThree(N_three):
    toss_list = []
    for i in range(N_three):
        toss_list.append([toss_coin(),toss_coin(),toss_coin()])
    #print(toss_list)
    return toss_list

#   Toss theory check - created tuple in list which shows exacly number of heads and down of coin toss.

def checkToss_theory(N_three):
    count1 = []
    toss_list = []
    temp = 0
    it = 0              #   Number of odd value of toss for heads
    heads = 0           #   Number of heads toss in row

    toss_list = tossThree(N_three)

    for i in range(N_three):
        temp = toss_list[i]
        count1.append((temp.count(1),temp.count(0)))
        if count1[i][0] % 2 != 0:
            it = it + 1
        if count1[i][0]  == 3:
            heads = heads + 1

    #print(heads)
    #print(count1)
    #print(it)

    return it, heads

def siumlation_ex2(N2,iterations):
    it_list = []
    heads_prob_list = []

    for i in range(iterations):
        it, heads = checkToss_theory(N2)
        it_list.append(it)
        heads_prob_list.append(heads)

    avg = Average(it_list)
    prob = (avg/N2)*100
    avg2 = Average(heads_prob_list)
    prob2 = (avg2/N2)*100


    print('--------------------------- Ex 2 Results -----------------------'+'\n')

    print('Toss number = '+str(N2)+'\n')
    print('Iterations of simulation = '+str(iterations)+'\n')
    print('AVG1 - Average number of how many odd numbers are in all iteration of sim = '+str(avg)+'\n')
    print('Probablity of three coin toss and getting odd number of heads is equal to prob = '+str(prob)+'%'+'\n')
    print('AVG2 - Average number of 3 heads show up in row AVG2 = '+str(avg2)+'\n')
    print('Probablity that 3 heads showed up in row = '+str(prob2)+'%'+'\n')

    print('------------------------------  End  -----------------------'+'\n')

#   Create list of cards from one to 100 and create shuffle

def numered_cards():
    cards = []

    for i in range(100):
        cards.append(i)
    random.shuffle(cards)

    #print(cards)
    return cards

def check_if_cards_hit():
    cards = numered_cards()
    hit_counter = 0
    for i in range(100):
        if cards[i] == i:
            hit_counter = hit_counter + 1
    #print(hit_counter)

    return hit_counter

def cards_simulation(iterations):
    hit_counter_list = []
    for i in range(iterations):
        hit_counter_list.append(check_if_cards_hit())

    counter_2 = hit_counter_list.count(2)
    avg = Average(hit_counter_list)
    prob = (counter_2/iterations)*100
    
    #print(hit_counter_list)
    #print(counter_2, avg)

    print('--------------------------- Ex 3 Results -----------------------'+'\n')

    print('Iterations of simulation = '+str(iterations)+'\n')
    print('AVG - Average number of hits = '+str(avg)+'\n')
    print('AVG - Average number of hits (rounded) = '+str(round(avg))+'\n')
    print('Probablity of having exactly two hits = '+str(prob)+'%'+'\n')

    print('------------------------------  End  -----------------------'+'\n')

#   Dice roll where we can get numbers from 1-5 and 0 means no number

def dice_roll_times():
    dice_5 = []
    dice_10 = []
    i = 0

    for i in range(5):
        dice_5.append(random.randrange(0,6,1))
        dice_10.append(random.randrange(0,10,1))
    
    #print(dice_5)

    return dice_5, dice_10

#   Simulation of exercise number 4

def simulation_ex4(iterations):
    count_zeros5 = 0
    count_zeros10 = 0

    for i in range(iterations):
        dice_5, dice_10 = dice_roll_times()
        zeros5 = dice_5.count(0)
        zeros10 = dice_10.count(0)
        if zeros5 == 2:
            count_zeros5 = count_zeros5 + 1
        if zeros10 == 2:
            count_zeros10 = count_zeros10 + 1
        
    #print(count_zeros5)
    #print(count_zeros10)

    prob5 = (count_zeros5/iterations)*100
    prob10 = (count_zeros10/iterations)*100

    print('--------------------------- Ex 4 Results -----------------------'+'\n')

    print('Iterations of simulation = '+str(iterations)+'\n')

    print('Probablity of no number appears twice [FOR DICE ROLL 5 TIMES] = '+str(prob5)+'%'+'\n')
    print('Probablity of no number appears twice [FOR DICE ROLL 10 TIMES] = '+str(prob10)+'%'+'\n')

    print('------------------------------  End  -----------------------'+'\n')


#                         ------------- MAIN -------------

#   Ex. 1

#       Relying on the geometrical interpretation of probability, 
#       write a program to estimate value of π. Run a simulation for N = 10k, 
#       k = 1, 2, ..., 7 random numbers. Observe how the accuracy of the result 
#       increases with the increasing sample size by plotting the absolute error |π − π'| 
#       as a function of N in double-logarithmic scale. Try to fit the straight line to the obtained graph. 
#       Why such a slope is obtained? In order to get better statistics, for each N, 
#       average the obtained result 100 times.

#   k - number of tries to hits into square/circle, k determines log value of N hits - > N = 10**k
#   iterations - number of iteration of whole run of simulation

#   Variables:

k = 7
iterations = 10

simulation_err_avg(iterations,k)

#       Ex. 2

#       The coin was tossed three times, and an odd number of heads appeared. 
#       Use the simulation to determine the probability that 3 heads showed up. 
#       Check if the result agrees with the theory.

#   N2 - number of toss in simulation
#   iterations2 - number of iterations in simulation

N2 = 3
iterations2 = 100

siumlation_ex2(N2,iterations2)

#       Ex. 3

#       We shuffle 100 numbered cards. Next, we turn them over one by one. 
#       If the i-th card shows up in the i-th step, we consider it a hit. 
#       Write a program to estimate the average number of hits. 
#       What is the probability of having exactly two hits?

#   iterations3 - number of iterations of whole simulation 

iterations3 = 1000
cards_simulation(iterations3)

#       Ex. 4

#       We roll a fair dice 5 times. Write a program to estimate the probability that no number appears twice. 
#       Estimate the probability also for 10 rolls. Compare the estimates with the analytical results.

#   iterations4 - number of iterations for rolling dice 5 times 

iterations4 = 1000

simulation_ex4(iterations4)
