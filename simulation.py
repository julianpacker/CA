import random as rnd
import statistics

def calculate_system_energy(states, weights, bias):
    """Energy is calculated by E = - Wij * Si *Sj + Bi *si
        for all Si and Sj connections and own biases"""
    energy = 0
    for i in range(len(weights)):
        for j, weight in enumerate(weights[i][i:], start=i):
            energy -= (weight * states[i] * states[j])
        energy += (bias[i] * states[i])
    return energy


def calculate_local_field(states, weights, bias, element):
    """Calculates local field for specific element"""
    local_energy = 0
    for index, weight in enumerate(weights[element]):
        local_energy += weight * states[index]
    local_energy -= bias[element]
    return local_energy


def generate_local_field(states, weights, bias):
    """Generates local field by calculating it for each element"""
    # local_e_list = []
    # for index, state in enumerate(states):
    #     local_e_list.append(calculate_local_field(states, weights, bias, index))
    # return
    g = lambda x: calculate_local_field(states, weights, bias, x)
    l_list = list(map(g, range(len(states))))
    return l_list


def update_local_field(states, weights, local_list, element):
    """Updates local field after changing one state"""
    coeff = 1
    if states[element] == 0:
        coeff = -1
    for i in range(len(local_list)):
        local_list[i] += coeff * weights[element][i]
    return local_list


def run_simulation_basic(states, weights, bias, counter, local):
    """Basic simulation with no noise, choosing variable to test at random"""
    c = counter
    size = len(states) - 1
    while c != 0:
        c -= 1
        index = rnd.randint(0, size)  # find a random state to check local
        if local[index] < 0 and states[index] == 1:
            states[index] = 0
            update_local_field(states, weights, local, index)
        elif local[index] > 0 and states[index] == 0:
            states[index] = 1
            update_local_field(states, weights, local, index)
    return calculate_system_energy(states, weights, bias)


def run_simulation_theirs(states, weights, bias, counter, local, noise_level):
    """Simulating with a specified noise level that decreases with counter"""
    c = counter
    size = len(states) - 1
    while c != 0:
        c -= 1
        index = rnd.randint(0, size)
        testing_level = ((rnd.random() - 0.5) / noise_level) * (c / counter)
        # testing_level centered around 0 with some noise to allow hill climbing
        if local[index] < testing_level and states[index] == 1:
            states[index] = 0
            update_local_field(states, weights, local, index)
        elif local[index] > testing_level and states[index] == 0:
            states[index] = 1
            update_local_field(states, weights, local, index)
    return calculate_system_energy(states, weights, bias)


def run_simulation_flip(states, weights, bias, counter, local, wait_period, init_flip, dec_flip):
    """Run descent until no change for weight_period, save old state """
    count = 0
    nsc = 0
    nsc_period = wait_period
    size = len(states) - 1
    old_best_state = states[:]
    old_best_e = 1000000000000000000
    flip_p = init_flip
    num_of_flips = 0

    while count < counter:
        count += 1
        if nsc == nsc_period:
            num_of_flips += 1
            new_e = calculate_system_energy(states, weights, bias)
            flip_p = int(flip_p - dec_flip)  ## change the flip amount here
            if flip_p <= 0: 
                print("Done Flipping! ")
                break
            print("New challenger", new_e)
            if new_e < old_best_e:
                old_best_state = states[:]
                old_best_e = new_e
            else:
                states = old_best_state[:]

            for f in range(flip_p):
                ind = rnd.randint(0, (len(states) - 1))
                states[ind] = rnd.randint(0, 1)
            print ("after flip", calculate_system_energy(states,weights,bias))
        index = rnd.randint(0, size)
        if local[index] < 0 and states[index] == 1:
            states[index] = 0
            update_local_field(states, weights, local, index)
            nsc -= 1

        elif local[index] > 0 and states[index] == 0:
            states[index] = 1
            update_local_field(states, weights, local, index)
            nsc -= 1
        else:
            if nsc < 0:
                nsc = 0
            nsc += 1
    else:
        print("Out of time!")
        
    new_e = calculate_system_energy(states, weights, bias)
    if  new_e > old_best_e:
        states = old_best_state[:]
    print("Flip Number", num_of_flips)
    return calculate_system_energy(states, weights, bias)


def test_basic(states, weights, bias, counter, local, times):
    """Runs basic test "times" amount of times and prints output min, stdev and mode (if exists)"""
    outputs = []
    while times != 0:
        times -= 1
        tstates = states[:]
        tlocal = local[:]
        output = run_simulation_basic(tstates, weights, bias, counter, tlocal)
        outputs.append(output)
    print("Results for basic: ")
    # print(outputs)
    print("min: ", round(min(outputs), 1), "stddev: ", round(statistics.stdev(outputs), 1))
    try:
        print("mode: ", statistics.mode(outputs))
    except statistics.StatisticsError:
        print("No common mode")
    return


def test_theirs(states, weights, bias, counter, local, noise, times):
    """Runs theirs test (noise) "times" amount of times and prints output min, stdev and mode (if exists)"""
    outputs = []
    while times != 0:
        times -= 1
        tstates = states[:]
        tlocal = local[:]
        output = run_simulation_theirs(tstates, weights, bias, counter, tlocal, noise)
        outputs.append(output)
    print("Results for theirs: ")
    # print(outputs)
    print("min: ", round(min(outputs), 1), "stddev: ", round(statistics.stdev(outputs), 1))
    try:
        print("mode: ", statistics.mode(outputs))
    except statistics.StatisticsError:
        print("No common mode")
    return
