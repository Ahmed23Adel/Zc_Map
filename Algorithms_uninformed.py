from collections import deque
from ProblemFormulation import  *


class Node:
    '''Node data structure for search space bookkeeping.'''

    def __init__(self, state, parent, action, path_cost):
        '''Constructor for the node state with the required parameters.'''
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    @classmethod
    def root(cls, init_state):
        '''Factory method to create the root node.'''
        return cls(init_state, None, None, 0)

    @classmethod
    def child(cls, problem, parent, action):
        '''Factory method to create a child node.'''
        return cls(
            problem.result(parent.state, action),
            parent,
            action,
            parent.path_cost + problem.step_cost(parent.state, action))


def solution(node):
    '''A method to extract the sequence of actions representing the solution from the goal node.'''
    actions = []
    cost = node.path_cost
    while node.parent is not None:
        actions.append(node.action)
        node = node.parent
    actions.reverse()
    return actions, cost

def bfs_tree(problem, verbose=False):
    '''Breadth-first tree search implementation.'''
    if problem.goal_test(problem.init_state): return solution(Node.root(problem.init_state))
    frontier = deque([Node.root(problem.init_state)])
    # if verbose: visualizer = Visualizer(problem)
    while frontier:
        # if verbose: visualizer.visualize(frontier)
        node = frontier.pop()
        for action in problem.actions(node.state):
            child = Node.child(problem, node, action)
            if problem.goal_test(child.state):
                return solution(child)
            frontier.appendleft(child)

def bfs_graph(problem, verbose=False):
    '''Breadth-first graph search implementation.'''
    if problem.goal_test(problem.init_state): return solution(Node.root(problem.init_state))
    frontier = deque([Node.root(problem.init_state)])
    explored = {problem.init_state}
    while frontier:
        # if verbose: visualizer.visualize(frontier)
        node = frontier.pop()
        for action in problem.actions(node.state):
            child = Node.child(problem, node, action)
            if child.state not in explored:
                if problem.goal_test(child.state):
                    return solution(child)
                frontier.appendleft(child)
                explored.add(child.state)


from collections import deque
import copy

def dls_tree(problem, limit,verbose=False):
    '''Breadth-first tree search implementation.'''
    if problem.goal_test(problem.init_state): return solution(Node.root(problem.init_state))
    frontier = deque([Node.root(problem.init_state)])
    # if verbose: visualizer = Visualizer(problem)
    while frontier:
        counter=0
        cond=True
        # if verbose: visualizer.visualize(frontier)
        node = frontier.pop()
        temp= node.parent#copy.deepcopy(node)
        while cond:
          if(temp!=None):
             temp=temp.parent
             counter+=1
          else:cond=False

        if counter==limit: # same parent
          continue

        for action in problem.actions(node.state):
            child = Node.child(problem, node, action)
            if problem.goal_test(child.state):
                return solution(child)
            frontier.append(child)
    return None

def dls_graph(problem, limit, verbose=False):
    counter=0
    cond=True
    '''Depth-First graph search implementation.'''
    if problem.goal_test(problem.init_state): return solution(Node.root(problem.init_state))
    frontier = deque([Node.root(problem.init_state)])
    explored = {problem.init_state}
    # if verbose: visualizer = Visualizer(problem)
    while frontier:
        # if verbose: visualizer.visualize(frontier)
        node = frontier.pop()
        temp= node.parent#copy.deepcopy(node)
        while cond:
          if(temp!=None):
             temp=temp.parent
             counter+=1
          else:cond=False

        if counter==limit: # same parent
          continue
        for action in problem.actions(node.state):
            child = Node.child(problem, node, action)
            if child.state not in explored:
                if problem.goal_test(child.state):
                    return solution(child)
                frontier.append(child)
                explored.add(child.state)
        counter+=1


from collections import deque

def dfs_tree(problem, verbose=False):
    '''Depth-First tree search implementation.'''
    if problem.goal_test(problem.init_state): return solution(Node.root(problem.init_state))
    frontier = deque([Node.root(problem.init_state)])
    # if verbose: visualizer = Visualizer(problem)
    while frontier:
        # if verbose: visualizer.visualize(frontier)
        node = frontier.pop()
        for action in problem.actions(node.state):
            child = Node.child(problem, node, action)
            if problem.goal_test(child.state):
                return solution(child)
            frontier.append(child)

def dfs_graph(problem, verbose=False):
    '''Depth-First graph search implementation.'''
    if problem.goal_test(problem.init_state): return solution(Node.root(problem.init_state))
    frontier = deque([Node.root(problem.init_state)])
    explored = {problem.init_state}
    # if verbose: visualizer = Visualizer(problem)
    while frontier:
        # if verbose: visualizer.visualize(frontier)
        node = frontier.pop()
        for action in problem.actions(node.state):
            child = Node.child(problem, node, action)
            if child.state not in explored:
                if problem.goal_test(child.state):
                    return solution(child)
                frontier.append(child)
                explored.add(child.state)


from collections import deque
import copy


def ids_tree(problem, limit, verbose=False):
    cond = True
    new_limit = limit
    ret = None
    while cond:
        if (ret == None):
            ret = dls_tree(problem, new_limit, verbose=True)
            new_limit += 1
            print("new limit is", new_limit)
        else:
            print("Path=", ret[0], "cost=", ret[1])
            cond = False


def ids_graph(problem, limit, verbose=False):
    cond = True
    new_limit = limit
    ret = None
    while cond:
        if (ret == None):
            ret = dls_graph(problem, new_limit, verbose=True)
            new_limit += 1
            print("new limit is", new_limit)
        else:
            print("Path=", ret[0], "cost=", ret[1])
            cond = False
