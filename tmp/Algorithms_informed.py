from heapq import heappush, heappop
from itertools import count
from ProblemFormulation import *
counter = count()


class Node:
    '''Node data structure for search space bookkeeping.'''

    def __init__(self, state, parent, action, path_cost, heuristic):
        '''Constructor for the node state with the required parameters.'''
        self.state = state
        self.parent = parent
        self.action = action
        self.g = path_cost
        self.h = heuristic
        self.f = path_cost + heuristic

    @classmethod
    def root(cls, problem):
        '''Factory method to create the root node.'''
        init_state = problem.init_state
        return cls(init_state, None, None, 0, problem.heuristic(init_state))

    @classmethod
    def child(cls, problem, parent, action):
        '''Factory method to create a child node.'''
        child_state = problem.result(parent.state, action)
        return cls(
            child_state,
            parent,
            action,
            parent.g + problem.step_cost(parent.state, action),
            problem.heuristic(child_state))


def solution(node):
    '''A method to extract the sequence of actions representing the solution from the goal node.'''
    actions = []
    cost = node.g
    while node.parent is not None:
        actions.append(node.action)
        node = node.parent
    actions.reverse()
    return actions, cost

def greedy_best_first(problem, verbose=False):
    '''Greedy best-first search implementation.'''
    frontier = [(None, None, Node.root(problem))]
    explored = set()
    # if verbose: visualizer = Visualizer(problem)
    while frontier:
        # if verbose: visualizer.visualize(frontier)
        _, _, node = heappop(frontier)
        if node.state in explored: continue
        if problem.goal_test(node.state):
            return solution(node)
        explored.add(node.state)
        for action in problem.actions(node.state):
            child = Node.child(problem, node, action)
            if child.state not in explored:
                heappush(frontier, (child.h, next(counter), child))



def ucs(problem, verbose=False):
    '''Greedy best-first search implementation.'''
    frontier = [(None, None, Node.root(problem))]
    explored = set()
    # if verbose: visualizer = Visualizer(problem)
    while frontier:
        # if verbose: visualizer.visualize(frontier)
        _, _, node = heappop(frontier)
        if node.state in explored: continue
        if problem.goal_test(node.state):
            return solution(node)
        explored.add(node.state)
        for action in problem.actions(node.state):
            child = Node.child(problem, node, action)
            if child.state not in explored:
                heappush(frontier, (child.g, next(counter), child))





def a_star(problem, verbose=False):
    '''Greedy best-first search implementation.'''
    frontier = [(None, None, Node.root(problem))]
    explored = set()
    # if verbose: visualizer = Visualizer(problem)
    while frontier:
        # if verbose: visualizer.visualize(frontier)
        _, _, node = heappop(frontier)
        if node.state in explored: continue
        if problem.goal_test(node.state):
            return solution(node)
        explored.add(node.state)
        for action in problem.actions(node.state):
            child = Node.child(problem, node, action)
            if child.state not in explored:
                heappush(frontier, (child.f, next(counter), child))


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
        if current_value <= next_value: return sols
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
        if current_value is 0 or T is 0: return sols  # Return if a goal state is found or if the temperature hits 0
        next_states = [problem.result(current_state, action) for action in problem.actions(current_state)]  # Generate all possible next states
        while True:  # Repeat the following till the current state is updated
            next_state = choice(next_states)  # Choose a random next state
            next_value = problem.heuristic(next_state)
            delta = current_value - next_value
            if delta > 0 or random() < exp(delta / T):  # Accept the randomly chosen state immediately if it is better than the current state or with a probability (exponentially) proportional to the temperature and how bad it is
                current_state, current_value = next_state, next_value
                sols.append(current_state)
                break
