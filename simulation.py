import random as rnd
from math import inf

class Simulation:
    "Parent of all simulations"
    def __init__(self, states, weights, bias, counter):
        assert len(states) == len(weights) == len(bias)
        self.counter = counter
        self.states = states
        self.weights = weights
        self.bias = bias
        self.generate_local_field()
        self.size = len(bias) - 1
        self.c = counter
        self.current_energy = inf
        self.name = self.__class__.__name__
        return

    def calculate_system_energy(self):
        """Energy is calculated by E = - Wij * Si *Sj + Bi *si
           for all Si and Sj connections and own biases"""
        energy = 0
        for i in range(len(self.weights)):
            for j, weight in enumerate(self.weights[i][i:], start=i):
                energy -= (weight * self.states[i] * self.states[j])
            energy += (self.bias[i] * self.states[i])
        return energy


    def calculate_local_field(self, element):
        """Calculates local field for specific element"""
        local_energy = 0
        for index, weight in enumerate(self.weights[element]):
            local_energy += weight * self.states[index]
        local_energy -= self.bias[element]
        return local_energy


    def generate_local_field(self):
        """Generates local field by calculating it for each element"""
        g = lambda x: self.calculate_local_field(x)
        self.local = list(map(g, range(len(self.states))))


    def update_local_field(self, element):
        """Updates local field after changing one state"""
        coeff = 1
        if self.states[element] == 0:
            coeff = -1
        for i in range(len(self.local)):
            self.local[i] += coeff * self.weights[element][i]

    def run_simulation(self):
        while self.c != 0:
            self.simulation_step()
        return self.calculate_system_energy()
    
    def state_change(self, index, level = 0):
        if self.local[index] < level and self.states[index] == 1:
            self.states[index] = 0
            self.update_local_field(index)
        elif self.local[index] > level and self.states[index] == 0:
            self.states[index] = 1
            self.update_local_field(index)

class Simulation_Basic(Simulation):
    " Simulation using the basic algorithm"
    def __init__(self, states, weights, bias, counter):
        super().__init__(states, weights, bias, counter)   
   
    def simulation_step(self):
        """Basic simulation with no noise, choosing variable to test at random"""
        self.c -= 1
        index = rnd.randint(0, self.size)  # find a random state to check local
        self.state_change(index)
        return
    

class Simulation_Noise(Simulation):
    "Simulation using noise to make decisison if to change state"
    def __init__(self, states, weights, bias, counter, noise_level):
        self.noise_level = noise_level
        super().__init__(states,weights,bias,counter)

    def simulation_step(self):
        self.c -= 1
        index = rnd.randint(0, self.size)
        testing_level = ((rnd.random() - 0.5)*1000 / self.noise_level) * (self.c / self.counter)
        # testing_level centered around 0 with some noise to allow hill climbing
        self.state_change(index, testing_level)

def run_simulation_flip(states, weights, bias, counter, wait_period, init_flip, dec_flip):
    """Run descent until no change for weight_period, save old state """
    count = 0
    nsc = 0
    nsc_period = wait_period
    size = len(states) - 1
    old_best_state = states[:]
    old_best_e = 1000000000000000000
    flip_p = init_flip
    num_of_flips = 0
    local = generate_local_field(states,weights,bias)
    while count < counter:
        count += 1
        if nsc == nsc_period:
            num_of_flips += 1
            new_e = calculate_system_energy(states, weights, bias)
            flip_p = int(flip_p - dec_flip)  ## change the flip amount here
            if flip_p <= 0: 
                break
            if new_e < old_best_e:
                old_best_state = states[:]
                old_best_e = new_e
            else:
                states = old_best_state[:]

            for f in range(flip_p):
                ind = rnd.randint(0, (len(states) - 1))
                states[ind] = rnd.randint(0, 1)
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
       
       
    new_e = calculate_system_energy(states, weights, bias)
    if  new_e > old_best_e:
        states = old_best_state[:]
    return [calculate_system_energy(states, weights, bias),num_of_flips]

def run_simulation_1_update(states, weights, bias, counter,  noise_level):
    """Simulating with a specified noise level that decreases with counter.
    Every 10 counts, choose the largest local field and switch its state"""
    c = counter
    size = len(states) - 1
    local = generate_local_field(states,weights,bias)
    while c != 0:
        c -= 1
        if c % 100 == 0:
            # flip largest local field
            #print(calculate_system_energy(states, weights, bias))
            min_local_index = local.index(min(local))
            #print("min: ", local[min_local_index])
            if states[min_local_index] == 1:
                states[min_local_index] = 0
                update_local_field(states, weights, local, min_local_index)

            #print(calculate_system_energy(states, weights, bias))
            max_local_index = local.index(max(local))
            if states[max_local_index] == 0:
                states[max_local_index] = 1
                update_local_field(states, weights, local, max_local_index)

            #print(calculate_system_energy(states, weights, bias))
            continue

        index = rnd.randint(0, size)
        testing_level = ((rnd.random() - 0.5) / noise_level) * (c / counter)
        # testing_level centered around 0 with some noise to allow hill climbing
        if local[index] < testing_level and states[index] == 1:
            #print(local[index])
            states[index] = 0
            update_local_field(states, weights, local, index)
        elif local[index] > testing_level and states[index] == 0:
            states[index] = 1
            update_local_field(states, weights, local, index)
    return [calculate_system_energy(states, weights, bias)]


