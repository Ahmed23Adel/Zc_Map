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
