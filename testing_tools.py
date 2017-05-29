import random as rnd
import time 
import math
from statistics import stdev, mean, median
import matplotlib.pyplot as plt

def print_test_results(returned_list,  all_energies = 0, all_timings = 0, messages = 0, repetitive = 0):
    print (returned_list[0][0])
    print ("Number of Tests: ", len(returned_list))
    calculated_energies = list(zip(*returned_list))
    
    min_energy = min(calculated_energies[1])
    min_energy_time = calculated_energies[2][calculated_energies[1].index(min_energy)]
    print ("Lowest energy: ", min_energy, " took ", min_energy_time)

    max_energy = max(calculated_energies[1])
    max_energy_time = calculated_energies[2][calculated_energies[1].index(max_energy)]
    print ("Highest energy: ", max_energy, "took", max_energy_time)

    average_energy = mean(calculated_energies[1])
    print ("Average energy: ", average_energy)
    median_energy = median(calculated_energies[1])
    print ("Median energy: ", median_energy)
    try:
        stddev = stdev(calculated_energies[1])
        print ("Standard deviation: ", stddev)
    except:
        print ("Standard deviation is not available for single run!")
    average_time = mean(calculated_energies[2])
    print ("Average time: ", average_time)
    if all_energies:
        print ("All energies: ", calculated_energies[1])
    if all_timings:
        print ("All timings: ", calculated_energies[2])
    if messages:
        print ("All messgaes: ", calculated_energies[3])
    if repetitive != 0:
        graph_runs(repetitive, calculated_energies[4])
    print ()
    return

def graph_runs(code, runs):
    """ Work in progress"""
    size = len(runs)
    if size > 9:
        ans = input("Are you sure you want to print ", size, " runs? 1 = yes")
        if int(ans) != 1:
            return
    window_size = math.ceil(math.sqrt(size))
    pre = str(window_size) + str(window_size)
    fig = plt.figure()
    for i, item in enumerate(runs, 1):
        ax1 = fig.add_subplot(int(pre + str(i)))
        plt.plot(item[1],item[0])
        plt.ylabel('System Energy')
        plt.xlabel("Step number")
    plt.show()

def repetitive_test(function_to_test, number_of_tests, states_mode, *args, init_state = None, repetitive = 0):
    """Test the class function_to_test  number_of_tests times using the argument_list provided.
       The states mode determines what initial state is used.
       init_state defines the initial state for mode 3
       repetive provides the period at which energy samples should be taken, 0 = dont take any samples.
      
       0 = Use all 0s
       1 = Use all 1s
       2 = Use random
       3 = Use the one from argument_list
   
       return [min, max, avg, median,  std]"""
    global array_size
    array_size = len(args[1])

    def restore_states(states_mode): 
        if states_mode == 0:
            return [0 for i in range(array_size)]
        elif states_mode  == 1:
            return [1 for i in range(array_size)]
        elif states_mode == 2:
            return [rnd.randint(0,1) for i in range(array_size)]
        elif states_mode == 3:
            return init_state[:]
        else:
            raise Exception("Invalid states_mode")
        return

    returned_values = []
    for i in range(number_of_tests):
        states_for_testing = restore_states(states_mode)
        inst = function_to_test(states_for_testing, *args)
        if not repetitive != 0:
            inst.run_simulation()
        else:
            inst.run_simulation_period(repetitive)
        returned_values.append(inst.items_to_return())
    return returned_values

