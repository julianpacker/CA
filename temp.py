def run_simulation_flip(states, weights, bias, counter, local, wait_period, init_flip, dec_flip, parallel):
    """Run simulation flip but merges best cases"""
    count = 0

    while count < counter:
        count += 1
