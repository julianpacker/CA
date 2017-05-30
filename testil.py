from simulation import *
from testing_tools import *
from generation import *

weights = matrix_from_file("w_5_1.txt")
bias = flip_bias(list_from_file("lf_5_1.txt"))

states = [0 for i in range(25)]
#ic = Simulation_Noise(states, weights, bias, 10000, 0.07))

#print_test_results(*repetitive_t_resultsest(Simulation_Basic, 50, 2, weights, bias, 100000))
#print_test_results(*repetitive_test(Simulation_Noise, 50, 2, weights, bias, 100000, 0.07))

#a = Test_Run(Simulation_Flip, 9,0, weights, bias, 10000,5, 25, 3, repetitive = 5)
#a.print_test_results()
#a.graph_runs()
a = Test_Runs(Simulation_Noise, 50, 0, weights, bias, [(50000, 50000, 1),(0.01,0.15,20)])
a.searchmode_median()


#a = Test_Run(Simulation_Noise,5,0,weights, bias,*(10000,1))


