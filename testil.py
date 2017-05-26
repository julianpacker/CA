from simulation import *
from testing_tools import *
from generation import *

weights = matrix_from_file("w_5_1.txt")
bias = flip_bias(list_from_file("lf_5_1.txt"))


print_test_results(*repetitive_test(run_simulation_basic, 10, 2, weights, bias, 1000000))


print_test_results (*repetitive_test(run_simulation_theirs, 10, 2, weights, bias, 1000000, 0.01))

print_test_results (*repetitive_test(run_simulation_flip, 10, 2, weights, bias, 1000000, 10,7,2))

