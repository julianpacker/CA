from simulation import *
from testing_tools import *
from generation import *

weights = matrix_from_file("w_5_1.txt")
bias = flip_bias(list_from_file("lf_5_1.txt"))

states = [0 for i in range(25)]
#ic = Simulation_Noise(states, weights, bias, 10000, 0.07))

#print_test_results(*repetitive_t_resultsest(Simulation_Basic, 50, 2, weights, bias, 100000))
# save_test_results_to_file(*repetitive_test(Simulation_Noise, 50, 2, weights, bias, 100000, 0.07))

# a = Test_Run(Simulation_1Update, 9,0, weights, bias, 7000, 0.03, 90, repetitive = 5)
# a.print_test_results()
# a.graph_runs()
a = Test_Runs(Simulation_1Update, 20, 0, weights, bias, [(7000, 7000, 1), (0.03,0.03,1), (50,100,5)])
a.searchmode_lowest()


#a = Test_Run(Simulation_Noise,5,0,weights, bias,*(10000,1))


