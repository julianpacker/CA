import random as rnd
import statistics
import time
from simulation import *
from generation import *

def input_data(weights, bias):
    sum = 0
    sum2 = 0
    for i in range(len(weights)):
        for j in range(len(weights)):
            sum += weights[i][j]
    for i in range (len(bias)):
        sum2 += bias[i]
    avg = sum/(len(weights)**2)
    avg2 = sum2/len(bias)
    print(avg, avg2)

# inputs and test
# from file
weights = matrix_from_file("w_5_1.txt")
bias = list_from_file("lf_5_1.txt")
for index, biasval in enumerate(bias):
    bias[index] = -biasval  # flip bias values as per behraz
symmetrize(weights)
arraysize = len(bias)
print("Array size: ", arraysize)
states = [1 for i in range(arraysize)]
local = generate_local_field(states, weights, bias)

"""
#from gaussian
array_size = 1024
weights = generate_gauss2(array_size)
##weights = [[1,0,6,7,4,6,0],[-3,7,0,-2,-1,0,-1],[0,4,-9,4,0,5,5],[5,4,0,-6,-3,1,2],[5,-2,-2,0,4,-1,0],[8,4,-1,-1,-1,1,7],[0,9,0,5,-3,-5,5]]
symmetrize(weights)
make_diagonal_zero(weights)
bias = random_bias(array_size)
states = [0 for i in range(array_size)]
local = generate_local_field(states,weights,bias)
print("here")
"""

counter = 50 #number of iterations
noise = .01 #higher value means less noise
times = 100 # number of times test is run
print("Ready to start")




'''
print("Basic test: ")
args = [states, weights, bias, counter, local, times]
start = time.time()
test_basic(args, run_simulation_basic)
diff = time.time() - start
print("Basic time: ", diff)
print()

'''
args = [states, weights, bias, counter, local, noise, times]
#input_data(weights,bias)
#in this case is about 1000
#0.0001,0.001 no good

print("Noise (Theirs) test: ")
start = time.time()
print("noise = ", noise)
test_multiple(args, run_simulation_theirs)

noise = .1
print("noise = ", noise)
test_multiple(args, run_simulation_theirs)

noise = 1
print("noise = ", noise)
test_multiple(args, run_simulation_theirs)

diff = time.time() - start
print("Noise (Theirs) time: ", diff)
print()

'''
print("New test: ")
start = time.time()
test_multiple(args, run_simulation_1_update)
diff = time.time() - start
print("New time: ", diff)
'''
'''

start = time.time()
print(run_simulation_flip(states, weights, bias, counter, local, 10, 150, 25))
diff = time.time() - start
print("Flip time: ", diff)
'''
# 4 states
# s = [0,0,0,0]
# w = [[0,2,3,-1],[2,0,6,3],[3,6,0,4],[-1,3,4,0]]
# b = [-1,2,-3,7]
# c = 10 #counter
# local_e_list = generate_local_field(s,w,b)
# print(calculate_system_energy(s,w,b))
# print(run_simulation_basic(s,w,b,c,local_e_list))
# print(run_simulation_theirs(s,w,b,c,local_e_list,1))