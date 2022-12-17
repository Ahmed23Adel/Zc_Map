
def hill_climbing(problem):
    '''Hill climbing search implementation.'''
    current_state = problem.init_state
    current_value = problem.heuristic(current_state)
    # if verbose: visualizer = Visualizer(problem)
    sols = []
    while True:
        # if verbose: visualizer.visualize([current_state])
        next_state, next_value = None, None
        for action in problem.actions(current_state):
            new_state = problem.result(current_state, action)
            new_value = problem.heuristic(new_state)
            if next_value is None or next_value > new_value:
                next_state, next_value = new_state, new_value
        if current_value <= next_value: return (sols,0)
        sols.append(current_state)
        current_state, current_value = next_state, next_value



from random import choice, random
from math import exp
from itertools import count


def simulated_annealing(problem, schedule, verbose=False):
    '''Simulated annealing search implementation.'''
    current_state = problem.init_state
    current_value = problem.heuristic(current_state)
    # if verbose: visualizer = Visualizer(problem)
    sols = []
    for t in count():
        # if verbose: visualizer.visualize([current_state])
        T = schedule(t)  # A function that determines the "temperature" (acceptability of a bad state) as a function of the step count
        print("T", T)
        if current_value is 0 or T < 0.0000001: return [sols,0]  # Return if a goal state is found or if the temperature hits 0
        next_states = [problem.result(current_state, action) for action in problem.actions(current_state)]  # Generate all possible next states
        print("outer true")
        while True:  # Repeat the following till the current state is updated
            next_state = choice(next_states)  # Choose a random next state
            next_value = problem.heuristic(next_state)
            delta = current_value - next_value
            print("delta",delta, T)
            print(current_state, problem.zc_map[current_state])
            try:
                if delta > 0 or random() > exp(delta / (T+0.00000001)):  # Accept the randomly chosen state immediately if it is better than the current state or with a probability (exponentially) proportional to the temperature and how bad it is
                    sols.append(current_state)
                    current_state, current_value = next_state, next_value
                    break
            except:
                sols.append(current_state)
                current_state, current_value = next_state, next_value
                break
