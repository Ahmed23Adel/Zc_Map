from math import inf
from time import time
from itertools import count
class Environment:
    '''
    Abstract base class for an (interactive) environment formulation.
    It declares the expected methods to be used to solve it.
    All the methods declared are just placeholders that throw errors if not overriden by child "concrete" classes!
    '''
    
    def __init__(self):
        '''Constructor that initializes the problem. Typically used to setup the initial state.'''
        self.state = None
    
    def actions(self):
        '''Returns an iterable with the applicable actions to the current environment state.'''
        raise NotImplementedError
    
    def apply(self, action):
        '''Applies the action to the current state of the environment and returns the new state from applying the given action to the current environment state; not necessarily deterministic.'''
        raise NotImplementedError
    
    @classmethod
    def new_random_instance(cls):
        '''Factory method to a problem instance with a random initial state.'''
        raise NotImplementedError


def action_from_q(env, q, verbose=True):
    '''Get the best action for the current state of the environment from Q-values'''
    return max((action for action in env.actions()), key=lambda action: q.get((env.state, action), 0))


def q_learning(env, q={}, n={}, f=lambda q, n: (q+1)/(n+1), alpha=lambda n: 0.5, error=1e-6, verbose=False):
    '''Q-learning implementation that trains on an environment till no more actions can be taken'''
    index = 0
    # if verbose: visualizer = Visualizer(env)
    cnt = 0
    while env.state is not None:
        # if verbose: visualizer.visualize([env.state])
        if verbose: print(env.state)
        cnt +=1
        state = env.state
        action = max(env.actions(),
                     key=lambda next_action: f(q.get((state, next_action), 0), n.get((state, next_action), 0)))
        n[(state, action)] = n.get((state, action), 0) + 1
        reward = env.apply(action)
        q[(state, action)] = q.get((state, action), 0) \
                           + alpha(n[state, action]) \
                           * (reward
                              + env.discount * max((q.get((env.state, next_action), 0) for next_action in env.actions()), default=0)
                              - q.get((state, action), 0))
       
        # print(env.state, end="")
        # if env.state[1] == True :
        # if env.state[0] == 1754 or env.state[0] == 4386 or env.state[0] == 3063 or env.state[0] == 4386:
        #     print(env.state)
        # elif env.state[1] == True:
        #     print(env.state, end="")
            # print("")
            # index = 0
    print("It took {} steps".format(cnt))
    return q, n


def q_learning_exploit(env, q={}, n={}, f=lambda q, n: (q+1)/(n+1), alpha=lambda n: 0.5, error=1e-6):
    '''Q-learning implementation that trains on an environment till no more actions can be taken'''
    op_stats = []
    # if verbose: visualizer = Visualizer(env)
    cnt = 0
    while env.state is not None:
        # if verbose: visualizer.visualize([env.state])
        op_stats.append(env.state[0])
        cnt +=1
        state = env.state
        action = max(env.actions(),
                     key=lambda next_action: f(q.get((state, next_action), 0), n.get((state, next_action), 0)))
        n[(state, action)] = n.get((state, action), 0) + 1
        reward = env.apply(action)
        q[(state, action)] = q.get((state, action), 0) \
                           + alpha(n[state, action]) \
                           * (reward
                              + env.discount * max((q.get((env.state, next_action), 0) for next_action in env.actions()), default=0)
                              - q.get((state, action), 0))
    print("It took {} steps".format(cnt))
    return op_stats


def simulate(env_ctor, n_iterations=inf, duration=inf, **q_learning_params):
    '''A helper function to train for a fixed number of iterations or fixed time'''
    for param in ('q', 'n'): q_learning_params[param] = q_learning_params.get(param, {})
    start_time = time()
    i = count()
    while time() < start_time + duration and next(i) < n_iterations:
        env = env_ctor()
        q, n = q_learning(env, **q_learning_params)
        print("Finished {} iteration".format(i))
    return q_learning_params['q'], q_learning_params['n']


def simulate_exploit(env_ctor, n_iterations=inf, duration=inf, **q_learning_params):
    '''A helper function to train for a fixed number of iterations or fixed time'''
    for param in ('q', 'n'): q_learning_params[param] = q_learning_params.get(param, {})
    start_time = time()
    i = count()
    while time() < start_time + duration and next(i) < n_iterations:
        env = env_ctor()
        op_states = q_learning_exploit(env, **q_learning_params)
        # print("Finished {} iteration".format(i))
    return op_states


class LellyMapsDelivery(Environment):
    '''Dynamic Tom & Jerry world'''
    
    def __init__(self, map, max_reward = 100000000, discount = 0.3):
        ## State  (pos, carry, NBLeft, HBLEFT, OneLeft, ABLeft)
        self.state = (6278, False, 4, 4, 0 , 0) # Position
        self.zc_map = map
        self.max_reward = max_reward
        self.discount = discount
        self._height = 81
        self._width = 78
        self._action_values = {'up': -self._width, 'down': +self._width, 'left': -1, 'right': +1,
                               'diagonal_up_right':-self._width+1, 'diagonal_up_left':-self._width-1,
                               'diagonal_down_right': self._width + 1, 'diagonal_down_left': self._width - 1}

    
    def actions(self):
        if self.state is None: return []
        if (self.state[2] == 0 and self.state[3] == 0 and self.state[4] == 4 and self.state[5] == 4 ):
            return["Delivered!"]
        index = self.state[0]
        possible_moves = []
        if (index // self._width > 0) and (self.zc_map [index + self._action_values['up']] != "#"):
            possible_moves.append('up')
        if (index // self._width < self._height - 1) and (self.zc_map[index + self._action_values['down']] != "#"):
            possible_moves.append('down')
        if (index % self._width > 0) and (self.zc_map[index + self._action_values['left']] != "#"):
            possible_moves.append('left')
        if (index % self._width < self._width - 1) and (self.zc_map[index + self._action_values['right']] != "#"):
            possible_moves.append('right')
        # diagonals
        if (index % self._width < self._width - 1) and (index // self._width > 0) and (self.zc_map[index + self._action_values['diagonal_up_right']] != "#"):
            possible_moves.append('diagonal_up_right')
        if (index % self._width > 0) and (index // self._width > 0) and (self.zc_map[index + self._action_values['diagonal_up_left']] != "#"):
            possible_moves.append('diagonal_up_left')
        if (index // self._width < self._height - 1) and (index % self._width < self._width - 1) and (self.zc_map[index + self._action_values['diagonal_down_right']] != "#"):
            possible_moves.append('diagonal_down_right')
        if (index // self._width < self._height - 1) and (index % self._width > 0) and (self.zc_map[index + self._action_values['diagonal_down_left']] != "#"):
            possible_moves.append('diagonal_down_left')

        if self.state[0] == 3063 and self.state[1]  == False and self.state[2] >0:
            return ['pick']
            # possible_moves.append('pick') ## Nano
        if self.state[0] == 3177 and self.state[1]  == False and self.state[3] >0:
            return ['pick']
            # possible_moves.append('pick') ## Helmy
        if self.state[0] == 4386 and self.state[1]  == True and self.state[4] <4:
            return ['drop']
            # possible_moves.append('drop') ## One stop
        if self.state[0] == 1754 and self.state[1]  == True and self.state[5] <4:
            return ['drop']
            # possible_moves.append('drop') ## Academic
        return possible_moves
    

    def apply_helper(self, agent, action_func):
        self.state = (action_func(agent), self.state[1], self.state[2], self.state[3], self.state[4] , self.state[5]); 
        if self.state[1] == True: return -0.5
        if self.state[1] == False: return -1

    def apply(self, action):
        up = lambda position: position + self._action_values["up"]
        down = lambda position: position + self._action_values["down"]
        left = lambda position: position + self._action_values["left"]
        right = lambda position: position + self._action_values["right"]
        diagonal_up_right = lambda position: position + self._action_values["diagonal_up_right"]
        diagonal_up_left = lambda position: position + self._action_values["diagonal_up_left"]
        diagonal_down_right = lambda position: position + self._action_values["diagonal_down_right"]
        diagonal_down_left = lambda position: position + self._action_values["diagonal_down_left"]
        agent = self.state[0] 

        if action == "up": 
            return self.apply_helper(agent, up)
        elif action == "down": 
            return self.apply_helper(agent, down)
        elif action == "left": 
            return self.apply_helper(agent, left)
        elif action == "right": 
            return self.apply_helper(agent, right)
        elif action == "diagonal_up_right": 
            return self.apply_helper(agent, diagonal_up_right)
        elif action == "diagonal_up_left": 
            return self.apply_helper(agent, diagonal_up_left)
        elif action == "diagonal_down_right": 
            return self.apply_helper(agent, diagonal_down_right)
        elif action == "diagonal_down_left": 
            return self.apply_helper(agent, diagonal_down_left)

        elif action == "pick": 
            if self.state[0] == 3063:
                self.state  = (self.state[0], True, self.state[2]-1,  self.state[3],  self.state[4],  self.state[5])
            if self.state[0] == 3177:
                self.state  = (self.state[0], True, self.state[2],  self.state[3]-1,  self.state[4],  self.state[5])
            return +10

        elif action == "drop": 
            if self.state[0] == 4386: # one stop
                self.state  = (self.state[0], False, self.state[2],  self.state[3],  self.state[4] +1,  self.state[5])
            if self.state[0] == 1754:
                self.state  = (self.state[0], False, self.state[2],  self.state[3],  self.state[4],  self.state[5]+1)
            return +10
        elif action == "Delivered!": 
            self.state = None
            return +self.max_reward       

    @classmethod
    def new_random_instance(cls, map):
        return cls(map)


import numpy as np
import csv
import json
from random import random

def get_map():
    """read the map as 1d array

    Returns:
        list: 1d array of the map
    """
    data = np.array(list(csv.reader(open(r"D:\Zewail\Year 4\AI\proj2\final_zc_map.csv"))))
    data = data.ravel()
    return data
map = get_map()


def get_id(row,col):
   """return string to be identified in the front end

   Args:
       row (int): row of cell
       col (int): col of cell

   Returns:
       _type_: _description_
   """
   return "cell-"+str(row)+"-"+str(col)



def alg_output_to_cells(alg_output):
   """geenerate list of cells ids to colorize in the front end, to send them back to the front end

   Args:
       alg_output (string): indicies of all cells to be visited

   Returns:
       list: all cells ids
   """
   output = []
   width = 78

   for op in alg_output:
       idx_row = op //width
       idx_col = op % width
       output.append(get_id(idx_row, idx_col))
   return output

def run_RL():
    print("run_RL Ahmed")
    # op_states = [6278, 6200, 6122, 6044, 5966, 5888, 5810, 5732, 5654, 5576, 5498, 5420, 5342, 5264, 5187, 5110, 5033, 4956, 4879, 4802, 4725, 4648, 4571, 4494, 4417, 4340, 4263, 4186, 4109, 4032, 3955, 3878, 3801, 3724, 3647, 3570, 34]
    # tmp = alg_output_to_cells(op_states)
    # print(tmp)
    # return tmp
    q, n = {}, {}
    fileqkeys = open('D:\Zewail\Year 4\AI\proj2\qkeys.txt', 'r')
    fileqvals = open('D:\Zewail\Year 4\AI\proj2\qvals.txt', 'r')
    linesqkeys = fileqkeys.readlines()
    linesqvals = fileqvals.readlines()

    idx = 0
    print("Starting reading the file")
    for qk, qv in zip(linesqkeys, linesqvals):
        idx +=1
        eles = qk.split(",")
        t = (int(eles[0][2:]), True if "True" in eles[1] else False, int(eles[2]), int(eles[3]), int(eles[4]), int(eles[5][:-1]))
        mov = "up" if "'up'" in eles[-1] else "down" if "'down'" in eles[-1] else "right" if "'right'" in eles[-1] \
                        else "left" if "'left'" in eles[-1] \
                        else "diagonal_up_right" if "'diagonal_up_right'" in eles[-1] \
                        else "diagonal_up_left" if "'diagonal_up_left'" in eles[-1] \
                        else "diagonal_down_right" if "'diagonal_down_right'" in eles[-1] \
                        else "diagonal_down_left" if "'diagonal_down_left'" in eles[-1]  else "pick" if "'pick'" in eles[-1]  else "drop"
        
        q[(t, mov)] = float(qv)

    print("Done reading keys and values")
    op_states =simulate_exploit(lambda: LellyMapsDelivery.new_random_instance(map), n_iterations=1, q=q, n=n, f=lambda q, n: q) # test
    print("Dene finding the path")
    return alg_output_to_cells(op_states)


