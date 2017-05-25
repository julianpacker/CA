import random as rnd
import statistics
import time
from simulation import *
from generation import *

weights = matrix_from_file("w_5_1.txt")
bias = list_from_file("lf_5_1.txt")
for index, biasval in enumerate(bias):
    bias[index] = -biasval  # flip bias values as per behraz
symmetrize(weights)
arraysize = len(bias)


print(arraysize)

print("Flipper")

states = [0 for i in range(arraysize)]
local = generate_local_field(states, weights, bias)
print(run_simulation_flip(states, weights, bias, 100000000, local, 10, 25, 5))
print("\n\n")
states = [0 for i in range(arraysize)]

print("Array size: ", arraysize)
states = [1 for i in range(arraysize)]
>>>>>>> 87b8c5fc298a7722fe51ecd076fffa1b8f1c1d13
local = generate_local_field(states, weights, bias)
print(run_simulation_flip(states, weights, bias, 100000000, local, 10, 25, 5))


print("\n\n")
states = [0 for i in range(arraysize)]
local = generate_local_field(states, weights, bias)
print(run_simulation_flip(states, weights, bias, 10000000, local, 10, 25, 5))

print("\n\n")
states = [0 for i in range(arraysize)]
local = generate_local_field(states, weights, bias)
print(run_simulation_flip(states, weights, bias, 10000000, local, 10, 25, 5))

print("\n\n")
states = [0 for i in range(arraysize)]
local = generate_local_field(states, weights, bias)
print(run_simulation_flip(states, weights, bias, 10000000, local, 10, 25, 5))

print("\n\n")
states = [0 for i in range(arraysize)]
local = generate_local_field(states, weights, bias)
print(run_simulation_flip(states, weights, bias, 10000000, local, 10, 25, 5))

print("\n\n")
states = [0 for i in range(arraysize)]
local = generate_local_field(states, weights, bias)
print(run_simulation_flip(states, weights, bias, 10000000, local, 10, 25, 5))

print("\n\n")
print("Basic")

states = [0 for i in range(arraysize)]
local = generate_local_field(states, weights, bias)
print(run_simulation_basic(states,weights,bias,10000000, local))

print("\n\n")
states = [0 for i in range(arraysize)]
local = generate_local_field(states, weights, bias)
print(run_simulation_basic(states,weights,bias,10000000, local))

print("\n\n")
states = [0 for i in range(arraysize)]
local = generate_local_field(states, weights, bias)
print(run_simulation_basic(states,weights,bias,10000000, local))

print("\n\n")
states = [0 for i in range(arraysize)]
local = generate_local_field(states, weights, bias)
print(run_simulation_basic(states,weights,bias,10000000, local))

print("\n\n")
states = [0 for i in range(arraysize)]
local = generate_local_field(states, weights, bias)
print(run_simulation_basic(states,weights,bias,10000000, local))

print("\n\n")
states = [0 for i in range(arraysize)]
local = generate_local_field(states, weights, bias)
print(run_simulation_basic(states,weights,bias,10000000, local))

print("\n\n")
states = [0 for i in range(arraysize)]
local = generate_local_field(states, weights, bias)
print(run_simulation_basic(states,weights,bias,10000000, local))

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

counter = 100000 #number of iterations
noise = 0.5 #higher value means less noise
times = 100 # number of times test is run
print("Ready to start")





print("Basic test: ")
args = [states, weights, bias, counter, local, times]
start = time.time()
test_basic(args, run_simulation_basic)
diff = time.time() - start
print("Basic time: ", diff)
print()


args = [states, weights, bias, counter, local, noise, times]

print("Noise (Theirs) test: ")
start = time.time()
test_multiple(args, run_simulation_theirs)
diff = time.time() - start
print("Theirs time: ", diff)
print()

print("New test: ")
start = time.time()
test_multiple(args, run_simulation_1_update)
diff = time.time() - start
print("New time: ", diff)
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

