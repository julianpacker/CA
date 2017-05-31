from simulation import *
from testing_tools import *
from generation import *

weights = matrix_from_file("w_15_1.txt")
bias = flip_bias(list_from_file("lf_15_1.txt"))

states = [0 for i in range(25)]
#ic = Simulation_Noise(states, weights, bias, 10000, 0.07))

#print_test_results(*repetitive_t_resultsest(Simulation_Basic, 50, 2, weights, bias, 100000))
#print_test_results(*repetitive_test(Simulation_Noise, 50, 2, weights, bias, 100000, 0.07))


b = Test_Runs(Simulation_MergeNoise,5, 0, weights, bias,((5,8,1),(15,15,1),(3,5,1),(50000,50000,1)))
b.searchmode_median()

while True:
    input_a = input("Type a command: ")
    try:
        exec(input_a)
    except:
        print("Invalid Command")

#b = Test_Run(Simulation_MergeNoise, 25, 0, weights, bias, 7, 15, 4, 50000, repetitive = 1)
#b.print_test_results()

#a = Test_Run(Simulation_Noise, 25,0, weights, bias, 50000,0.07, repetitive = 100)
#a.print_test_results()

#b.graph_runs()
#a.graph_runs()


#a = Test_Runs(Simulation_Noise, 50, 0, weights, bias, [(50000, 50000, 1),(0.01,0.15,20)])
#a.searchmode_median()


#a = Test_Run(Simulation_Noise,5,0,weights, bias,*(10000,1))


