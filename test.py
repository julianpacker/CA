import random as rnd
import statistics
import time
from simulation import *
from generation import *

# inputs and test
# from file
weights = matrix_from_file("w2.txt")
bias = list_from_file("f2.txt")
for index, biasval in enumerate(bias):
    bias[index] = -biasval  # flip bias values as per behraz
symmetrize(weights)
arraysize = len(bias)
print(arraysize)
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

counter = arraysize ** 2 #number of iterations
noise = 1 #higher value means less noise
times = 2 # number of times test is run
print("Ready to start")

start = time.time()
test_basic(states, weights, bias, counter, local, times)
diff = time.time() - start
print("Basic time: ", diff)

start = time.time()
test_theirs(states, weights, bias, counter, local, noise, times)
diff = time.time() - start
print("Theirs time: ", diff)

start = time.time()
print(run_simulation_flip(states, weights, bias, counter, local, 10, 150, 25))
diff = time.time() - start
print("Flip time: ", diff)

# 4 states
# s = [0,0,0,0]
# w = [[0,2,3,-1],[2,0,6,3],[3,6,0,4],[-1,3,4,0]]
# b = [-1,2,-3,7]
# c = 10 #counter
# local_e_list = generate_local_field(s,w,b)
# print(calculate_system_energy(s,w,b))
# print(run_simulation_basic(s,w,b,c,local_e_list))
# print(run_simulation_theirs(s,w,b,c,local_e_list,1))