from simulation import *
from testing_tools import *
from generation import *

# setup from file - all parameters
weights = matrix_from_file("w_5_1.txt")
bias = flip_bias(list_from_file("lf_5_1.txt"))
counter = 1000
states_mode = 2
number_of_tests = 5
noise = 0.07
wait_period = 10
init_flip = 7
dec_flip = 2
# Values tested for noise for lf_5_1 and w_5_1 input values:
# 0.01, 0.05, 0.06, 0.065, 0.0675, 0.07, 0.0725, 0.075, 0.08 ,0.09, 0.1, 0.2, 0.3, 0.5, 0.7, 1, 1.1, 10, 100
# 0.07 was selected as final value, but 0.065-0.075 all about the same

"""    The states mode determines what initial state is used.
       0 = Use all 0s
       1 = Use all 1s
       2 = Use random
       3 = Use the one from argument_list (optional init_state variable)
"""

# repetitive_test(function_to_test, number_of_tests, states_mode, *args, init_state = None):
print_test_results(*repetitive_test(Simulation_1Update, number_of_tests, states_mode, weights, bias, counter, noise))

#print_test_results(*repetitive_test(Simulation_Basic, number_of_tests, states_mode, weights, bias, counter))

print_test_results(*repetitive_test(Simulation_Noise, number_of_tests, states_mode, weights, bias, counter, noise))

# print_test_results(*repetitive_test(run_simulation_flip, number_of_tests, states_mode, weights, bias, counter,
#                                      wait_period, init_flip, dec_flip))

#old data and old test styles

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

print("Basic test: ")
args = [states, weights, bias, counter, local, times]
start = time.time()
test_basic(args, run_simulation_basic)
diff = time.time() - start
print("Basic time: ", diff)
print()

args = [states, weights, bias, counter, local, noise, times]
#input_data(weights,bias)
#in this case is about 1000
#0.0001,0.001 no good

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
    return
"""