import csv
import numpy as np
import math

def get_map():
    """read the map as 1d array

    Returns:
        list: 1d array of the map
    """
    data = np.array(list(csv.reader(open(r"D:\Zewail\Year 4\AI\Project\Zc_Map\zcMapBackend\final_zc_map.csv"))))
    data = data.ravel()
    return data


class Problem:
    '''
    Abstract base class for problem formulation that supports a heuristic function.
    It declares the expected methods to be used by a search algorithm.
    All the methods declared are just placeholders that throw errors if not overriden by child "concrete" classes!
    '''

    def __init__(self):
        '''Constructor that initializes the problem. Typically used to setup the initial state and, if applicable, the goal state.'''
        self.init_state = None

    def actions(self, state):
        '''Returns an iterable with the applicable actions to the given state.'''
        raise NotImplementedError

    def result(self, state, action):
        '''Returns the resulting state from applying the given action to the given state.'''
        raise NotImplementedError

    def goal_test(self, state):
        '''Returns whether or not the given state is a goal state.'''
        raise NotImplementedError

    def step_cost(self, state, action):
        '''Returns the step cost of applying the given action to the given state.'''
        raise NotImplementedError

    def heuristic(self, state):
        '''Returns the heuristic value of the given state, i.e., the estimated number of steps to the nearest goal state.'''
        raise NotImplementedError


class ZcMap(Problem):
    '''Maze problem formulation.'''

    def __init__(self, init_state: int, goal_state :list, zc_map ,width = 78, height = 81):
        """_summary_
            intialize all important variables to start
        Args:
             init_state(int):  intial state, place for the user to start from
            goal_state(list): list of all possible place user wants to go to, Why? becuase if user wanted to go to Academic, there might be multiple doors for it
            zc_map(1d array): array map of the ac city
            width, height(int): width and height of the map.

        Returns:
            _type_: _description_
        """
        self.init_state = init_state
        self._goal_state = goal_state
        self._width = width
        self._height = height
        self.zc_map = zc_map
        self._action_values = {'up': -self._width, 'down': +self._width, 'left': -1, 'right': +1,
                               'diagonal_up_right':-self._width+1, 'diagonal_up_left':-self._width-1,
                               'diagonal_down_right': self._width + 1, 'diagonal_down_left': self._width - 1}

    def actions(self, state):
        """list all possible actions for specified state

        Args:
            state (int): state of agent. meaning where the agens is currenly is

        Returns:
            list: list of all actoins
        """
        index = state
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
        return possible_moves

    def result(self, state, action):
        """Return the result of performing an action while  the the agent in state 

        Args:
            state (int): location of the agent 
            action (string:key to _action_values): action chosen by the algorithm

        Returns:
            _type_: _description_
        """
        return state + self._action_values[action]

    def goal_test(self, state):
        """did the the agent hit the goal?

        Args:
            state (int): satate of the agent, where the agent is

        Returns:
            boolean: if true, means that agent hit the goal, otherwise false.
        """
        return state in self._goal_state

    def step_cost(self, state, action):
        """step cost for result of actoin

        Args:
            state (int): satate of the agent, where the agent is
            action (string:key to _action_values): action chosen by the algorithm

        Returns:
            int: step cost
        """
        new_state = self.result(state, action)
        if self.zc_map[new_state] == "r": # Raseef
            return 1
        if self.zc_map[new_state] == "|": # Road
            return 2
        if self.zc_map[new_state] == "*": # shagr
            return 3
        if self.zc_map[new_state] == "Ds": # Desert
            return 5
        if self.zc_map[new_state] == "P": # parking
            return 2
        return 1

    def heuristic_1(self, state):
        """first heuristic it's simple SLD

        Args:
            state (int): satate of the agent, where the agent is

        Returns:
            int: first heuristic value for specified state
        """
        row, col = state // self._width, state % self._width
        min_dis = 10000000000
        for goal in self._goal_state:
            row_g, col_g = goal // self._width, goal % self._width
            dis = math.sqrt((row - row_g)**2 + (col - col_g)**2)
            if dis < min_dis:
                min_dis = dis
        return min_dis

    def heuristic_2(self, state):
        """second heuristic it's simple max(horizental distance, vertical distance)


        Args:
            state (int): satate of the agent, where the agent is

        Returns:
            int: second heuristic value for specified state
        """
        row, col = state // self._width, state % self._width
        min_dis = 10000000000
        for goal in self._goal_state:
            row_g, col_g = goal // self._width, goal % self._width
            diff_x = abs(row - row_g)
            diff_y = abs(col-col_g)
            max_diff = max(diff_x, diff_y)
            if max_diff < min_dis:
                min_dis = max_diff
        return min_dis

    def heuristic(self, state):
        """final heuristic by finding the max between h1, and h2

        Args:
            state (int): satate of the agent, where the agent is

        Returns:
            int: heuristic value for specified state
        """
        h1, h2 = self.heuristic_1(state), self.heuristic_2(state)
        max_h = max(h1, h2)
        return max_h
