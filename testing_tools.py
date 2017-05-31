import random as rnd
import time 
import math
import itertools
from math import inf
from statistics import stdev, mean, median
import matplotlib.pyplot as plt


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
            return Exception("Invalid states_mode")



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

    def save_test_results(self, file_name = "results.txt"):
        f = open(file_name, 'w')
        string1 = "Number of Tests: " + str(self.number_of_tests) + '\n'
        string2 = "Lowest energy: " + str(self.min_energy) + " was achieved "+ str(len(self.min_energy_indeces)) + " times. \n"
        string3 = "Highest energy: " + str(self.max_energy) + '\n'
        string4 = "Average energy: " + str(self.average_energy) + '\n'
        string5 = "Median energy: " + str(self.median_energy) + '\n'
        string6 = "Standard deviation: " + str(self.stddev_energy) + '\n'
        string7 = "Average time: " + str(self.average_time) + '\n'
        string8 = "Standard Deviation for time: " + str(self.stddev_time) + '\n'
        list_for_file = [string1, string2, string3, string4, string5, string6, string7, string8]
        f.writelines(list_for_file)
        f.close()

class Test_Runs:
    def __init__(self, function_to_test, number_of_tests,states_mode,weights,bias, arguments, init_state = None):
        size = len(arguments)
        args = []
        for  item in arguments:
            a = [item[0]]
            b = item[0]
            step = item[2] 
            while b < item[1]:
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
        self.list_of_min = []
        for item in self.instances:
            self.list_of_min.append(item.min_energy)
        self.list_of_min_indeces = [i for i in range(len(self.instances))]
        self.list_of_min, self.list_of_min_indeces = zip(*sorted(zip(self.list_of_min, self.list_of_min_indeces)))
        print("Minimum energy achieved was: ", self.list_of_min[0], " by: ", self.list_of_min_indeces[0])

    def searchmode_average(self):
        self.list_of_average= []
        for item in self.instances:
            self.list_of_average.append(item.average_energy)
        self.list_of_average_indeces = [i for i in range(len(self.instances))]
        self.list_of_average, self.list_of_min_average = zip(*sorted(zip(self.list_of_average, self.list_of_average_indeces)))
        print("Minimum averagen energy achieved was: ", self.list_of_average[0], " by: ", self.list_of_average_indeces[0])

    def searchmode_median(self):
        self.list_of_median = []
        for item in self.instances:
            self.list_of_median.append(item.median_energy)
        self.list_of_median_indeces = [i for i in range(len(self.instances))]
        self.list_of_median, self.list_of_median_indeces = zip(*sorted(zip(self.list_of_median, self.list_of_median_indeces)))
        print("Minimum energy achieved was: ", self.list_of_median[0], " by: ", self.list_of_median_indeces[0])
