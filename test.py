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
