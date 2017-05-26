from simulation import *
from testing_tools import *
from generation import *

weights = matrix_from_file("w_5_1.txt")
bias = flip_bias(list_from_file("lf_5_1.txt"))

states = [0 for i in range(25)]
#ic = Simulation_Noise(states, weights, bias, 10000, 0.07))
print_test_results(*repetitive_test(Simulation_Basic, 5, 2, weights, bias, 1000000))


print_test_results (*repetitive_test(Simulation_Noise, 5, 2, weights, bias, 1000000, 0.01))

#print_test_results (*repetitive_test(run_simulation_flip, 10, 2, weights, bias, 1000000, 10,7,2))

