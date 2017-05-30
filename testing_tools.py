import random as rnd
import time 
import math
import itertools
from math import inf
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
        print ("All messages: ", calculated_energies[3])
    if repetitive != 0:
        graph_runs(repetitive, calculated_energies[4])
    print ()
    return

def save_test_results_to_file(returned_list,  all_energies = 0, all_timings = 0, messages = 0, repetitive = 0, file_name = "results.txt"):
    f = open(file_name, 'w')
    list_to_write = [returned_list[0][0], "\n", "Number of Tests: ", str(len(returned_list)), "\n"]
    f.writelines(list_to_write)
    calculated_energies = list(zip(*returned_list))

    min_energy = min(calculated_energies[1])
    min_energy_time = calculated_energies[2][calculated_energies[1].index(min_energy)]
    lowest_string = "Lowest energy: " + min_energy + " took " + min_energy_time + '\n'

    max_energy = max(calculated_energies[1])
    max_energy_time = calculated_energies[2][calculated_energies[1].index(max_energy)]
    highest_string = "Highest energy: " + max_energy + "took" + max_energy_time + '\n'



    average_energy = mean(calculated_energies[1])
    average_string = "Average energy: " + average_energy +'\n'
    median_energy = median(calculated_energies[1])
    median_string = "Median energy: " + median_energy +'\n'
    list_to_write = [lowest_string, highest_string, average_string, median_string]
    f.writelines(list_to_write)

    try:
        stddev = stdev(calculated_energies[1])
        print("Standard deviation: ", stddev)
    except:
        print("Standard deviation is not available for single run!")
    average_time = mean(calculated_energies[2])
    print("Average time: ", average_time)
    if all_energies:
        print("All energies: ", calculated_energies[1])
    if all_timings:
        print("All timings: ", calculated_energies[2])
    if messages:
        print("All messages: ", calculated_energies[3])

    f.close()
    if repetitive != 0:
        graph_runs(repetitive, calculated_energies[4])
    print()
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


class Test_Run:
    """ Simulation of a single function with a sing set of parameters performed multiple times"""
    def __init__(self, function_to_test, number_of_tests, states_mode, *args, init_state = None, repetitive = 0):
        """Test the class function_to_test  number_of_tests times using the argument_list provided.
           The states mode determines what initial state is used.
           init_state defines the initial state for mode 3
           repetive provides the period at which energy samples should be taken, 0 = dont take any samples.
          
           0 = Use all 0s
           1 = Use all 1s
           2 = Use random
           3 = Use the one from argument_list
       
           return [min, max, avg, median,  std]"""
        self.array_size = len(args[1])
        self.fe =[]
        self.rst =[]
        self.m =[]
        self.r = []

        for i in range(number_of_tests):
            states_for_testing = self.restore_states(states_mode)
            inst = function_to_test(states_for_testing, *args)
            if not repetitive != 0:
                inst.run_simulation()
            else:
                inst.run_simulation_period(repetitive)
            fe, rst, m, r = inst.items_to_return()
            self.fe.append(fe)
            self.rst.append(rst)
            self.m.append(m)
            self.r.append(r)
        del inst

        self.name = function_to_test.__name__
        self.number_of_tests = number_of_tests
        self.min_energy, self.min_energy_indeces = self.get_min(self.fe)
        self.min_energy_count = len(self.min_energy_indeces)
        self.max_energy, self.max_energy_indeces = self.get_max(self.fe)
        self.average_energy = mean(self.fe)
        self.median_energy = median(self.fe)
        self.stddev_energy = self.get_stddev(self.fe)

        self.average_time = mean(self.rst)
        self.stddev_time = self.get_stddev(self.rst)

    def get_min(self, l):
        min_energy = inf 
        min_energy_indeces = []
        for i, value in enumerate(l):
            if min_energy > value:
                min_energy = value
                min_energy_indeces = [i]
            elif min_energy == value:
                min_energy_indeces.append(i)
        return min_energy, min_energy_indeces
        
    def get_max(self, l):
        max_energy = -inf 
        max_energy_indeces = []
        for i, value in enumerate(l):
            if max_energy < value:
                max_energy = value
                max_energy_indeces = [i]
            elif max_energy == value:
                max_energy_indeces.append(i)
        return max_energy, max_energy_indeces

   
    def get_stddev(self, l):
        if len(l) == 1:
            return 0
        else:
            return stdev(l)


    def restore_states(self, states_mode):        
        if states_mode == 0:
            return [0 for i in range(self.array_size)]
        elif states_mode  == 1:
            return [1 for i in range(self.array_size)]
        elif states_mode == 2:
            return [rnd.randint(0,1) for i in range(self.array_size)]
        elif states_mode == 3:
            return self.init_state[:]
        else:
            raise Exception("Invalid states_mode")
        return


    def graph_runs(self):
        """ Work in progress"""
        if self.number_of_tests > 9:
            ans = input(str("Are you sure you want to print " + str( self.number_of_tests) + " runs? 1 = yes"))
            if int(ans) != 1:
                return
        window_size = math.ceil(math.sqrt(self.number_of_tests))
        pre = str(window_size) + str(window_size)
        fig = plt.figure()
        for i, item in enumerate(self.r, 1):
            ax1 = fig.add_subplot(int(pre + str(i)))
            plt.plot(item[1],item[0])
            plt.ylabel('System Energy')
            plt.xlabel("Step number")
        plt.show()

    def print_test_results(self):
        print ("Number of Tests: ", self.number_of_tests)
        print ("Lowest energy: ", self.min_energy, " was achieved ", len(self.min_energy_indeces))
        print ("Highest energy: ", self.max_energy)
        print ("Average energy: ", self.average_energy)
        print ("Median energy: ", self.median_energy)
        print ("Standard deviation: ", self.stddev_energy)
        print ("Average time: ", self.average_time)
        print ("Standard Deviation for time: ", self.stddev_time)
        print ()
        return

class Test_Runs:
    def __init__(self, function_to_test, number_of_tests,states_mode,weights,bias, arguments, init_state = None):
        size = len(arguments)
        args = []
        for  item in arguments:
            a = [item[0]]
            b = item[0]
            step = float((item[1] - item[0]))/item[2]
            if item[0] == item[1]:
                args.append(a)
                continue
            for i in range(item[2]):
                b += step
                a.append(b)
            args.append(a)
        iterator = itertools.product(*args)
        self.instances = []
        self.parameters = []
        while True:
            try:
                v = iterator.__next__()
                print (v)
                self.parameters.append(v)
                self.instances.append(Test_Run(function_to_test, number_of_tests, states_mode, weights, bias, *v, init_state = init_state))
            except Exception:
                break
        
        return
        
        

    def searchmode_lowest(self):
        min_energy = inf 
        min_energy_indeces = []
        min_energy_count = []
        for i, item in enumerate(self.instances):
            value = item.min_energy
            if min_energy > value:
                min_energy = value
                min_energy_indeces = [i]
                min_energy_count = [item.min_energy_count]
            elif min_energy == value:
                min_energy_indeces.append(i)
                min_energy_count.append(item.min_energy_count) 
        print ("Minimum energy: ", min_energy, " was achieved ", len(min_energy_indeces), " times.")
        for item1, item2 in zip(min_energy_count, min_energy_indeces):
            print (item1, self.parameters[item2])
                    










