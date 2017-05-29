import random as rnd
import time 
from statistics import stdev, mean, median

def print_test_results(returned_list, timings_list, name,  all_energies = 0, all_timings = 0, messages = 0): 
    print (name)
    calculated_energies = list(zip(*returned_list))
    
    min_energy = min(calculated_energies[0])
    min_energy_time = timings_list[calculated_energies[0].index(min_energy)]
    print ("Lowest energy: ", min_energy, " took ", min_energy_time)

    max_energy = max(calculated_energies[0])
    max_energy_time = timings_list[calculated_energies[0].index(max_energy)]
    print ("Highest energy: ", max_energy, "took", max_energy_time)

    average_energy = mean(calculated_energies[0])
    print ("Average energy: ", average_energy)
    median_energy = median(calculated_energies[0])
    print ("Median energy: ", median_energy)
    stddev = stdev(calculated_energies[0])
    print ("Standard deviation: ", stddev)
    average_time = mean(timings_list)
    print ("Average time: ", average_time)
    print ("\n\n")
    return

def repetitive_test(function_to_test, number_of_tests, states_mode, *args, init_state = None):
    """Test the function_to_test number_of_tests times using the argument_list provided.
       The states mode determines what initial state is used.
      
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

    returned_values =  []
    timings_list = []
    for i in range(number_of_tests):
        states_for_testing = restore_states(states_mode)
        start_time = time.time()
        inst = function_to_test(states_for_testing, *args)
        returned_values.append([inst.run_simulation()])
        timings_list.append(time.time() - start_time)

    return (returned_values, timings_list, inst.name)
