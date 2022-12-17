from AILogic.ProblemFormulation import *
from  AILogic.Algorithms_uninformed import *
from AILogic.Algorithms_informed import *
from AILogic.LocalSearch import *
from _datetime import datetime

mapper_to = {
 'D(D2)': [553],
 'w(D)': [752],
 'D(D1)': [790],
 'e(D)': [995],
 'S(D)': [1626],
 'AC(D)': [1754],
 'AC(G20)': [1838],
 'AC(G19)': [1839],
 'AC(G18)': [1918],
 'AC(G12)': [1997],
 'AC(Zone B)': [2075],
 'AC(G11)': [2076],
 'AC(Zone B)': [2153],
 'AC(G10)': [2154],
 'AC(Zone B)': [2231],
 'AC(G9)': [2232],
 'AC(Zone B)': [2309],
 'AC(G8)': [2310],
 'AC(Toilets)': [2375],
 'AC(G6, security room)': [2376],
 'AC(G11)': [2384],
 'AC(Zone B)': [2387],
 'AC(G7)': [2388],
 'AC(D)': [2389],
 'AC(ATM)': [2454],
 'AC(Security room)': [2457],
 'AC(G12)': [2462],
 'AC(Zone B)': [2465],
 'AC(G6)': [2466],
 'AC(D1)': [2534],
 'AC(G1)': [2536],
 'AC(F)': [2537],
 'AC(F)': [2538],
 'AC(F)': [2539],
 'AC(G13)': [2540],
 'AC(Zone B)': [2543],
 'AC(G5)': [2544],
 'AC(cats office)': [2614],
 'AC(F)': [2615],
 'AC(F)': [2616],
 'AC(F)': [2617],
 'AC(G14)': [2618],
 'AC(G14)': [2692],
 'AC(F)': [2693],
 'AC(F)': [2694],
 'AC(F)': [2695],
 'AC(G15)': [2696],
 'AC(G15)': [2770],
 'AC(F)': [2771],
 'AC(F)': [2772],
 'AC(F)': [2773],
 'AC(Locker)': [2848],
 'AC(Locker)': [2849],
 'AC(Locker)': [2850],
 'AC(Locker)': [2851],
 'AC(Locker)': [2852],
 'N(elevator)': [2987],
 'N(elevator)': [2988],
 'H(D2)': [3017],
 'H(Toilet)': [3018],
 'N(D1)': [3063],
 'N(elevator)': [3067],
 'H(Mosque)': [3095],
 'H(class4)': [3096],
 'H(class3)': [3097],
 'N(Toilet)': [3146],
 'H(Biology lab)': [3174],
 'H(class2)': [3175],
 'H(class1)': [3176],
 'H(D1)': [3177],
 'N(G004)': [3218],
 'N(Meeting room)': [3219],
 'H(Biology lab)': [3253],
 'H(stairs)': [3254],
 'N(Microscope)': [3295],
 'N(Microscope)': [3296],
 'N(G021)': [3299],
 'N(G022)': [3300],
 'H(elevator)': [3332],
 'H(chemistry lab)': [3334],
 'N(Microscope)': [3374],
 'N(G018)': [3377],
 'H(office)': [3411],
 'H(chemistry lab)': [3413],
 'N(communication)': [3453],
 'N(communication)': [3454],
 'H(D3)': [3489],
 'H(Toilet)': [3490],
 'O(D)': [4386],
 'CC(D1)': [4562],
'H': [3017, 3177, 3489], 
'N': [3063],
'S': [1626], 
'CC': [4562],
'O': [4386], 
'D': [553, 790],
'e': [995],
'w': [752],
'AC': [2389, 2534],
'h': [3017, 3177, 3489], 
'n': [3063],
's': [1626], 
'cc': [4562],
'o': [4386], 
'd': [553, 790],
'e': [995],
'w': [752],
'ac': [2389, 2534],
'helmy': [3017, 3177, 3489], 
'nano': [3063],
'service': [1626], 
'culture complex': [4562],
'one stop': [4386], 
'onestop': [4386],
'dorms': [553, 790],
'engineering': [995],
'workshop': [752],
'academic': [2389, 2534]
}

mapper_from = {
   'D(D2)': 553,
   'w(D)': 752,
   'D(D1)': 790,
   'e(D)': 995,
   'S(D)': 1626,
   'AC(D)': 1754,
   'AC(G20)': 1838,
   'AC(G19)': 1839,
   'AC(G18)': 1918,
   'AC(G12)': 1997,
   'AC(Zone B)': 2075,
   'AC(G11)': 2076,
   'AC(Zone B)': 2153,
   'AC(G10)': 2154,
   'AC(Zone B)': 2231,
   'AC(G9)': 2232,
   'AC(Zone B)': 2309,
   'AC(G8)': 2310,
   'AC(Toilets)': 2375,
   'AC(G6, security room)': 2376,
   'AC(G11)': 2384,
   'AC(Zone B)': 2387,
   'AC(G7)': 2388,
   'AC(D)': 2389,
   'AC(ATM)': 2454,
   'AC(Security room)': 2457,
   'AC(G12)': 2462,
   'AC(Zone B)': 2465,
   'AC(G6)': 2466,
   'AC(D1)': 2534,
   'AC(G1)': 2536,
   'AC(F)': 2537,
   'AC(F)': 2538,
   'AC(F)': 2539,
   'AC(G13)': 2540,
   'AC(Zone B)': 2543,
   'AC(G5)': 2544,
   'AC(cats office)': 2614,
   'AC(F)': 2615,
   'AC(F)': 2616,
   'AC(F)': 2617,
   'AC(G14)': 2618,
   'AC(G14)': 2692,
   'AC(F)': 2693,
   'AC(F)': 2694,
   'AC(F)': 2695,
   'AC(G15)': 2696,
   'AC(G15)': 2770,
   'AC(F)': 2771,
   'AC(F)': 2772,
   'AC(F)': 2773,
   'AC(Locker)': 2848,
   'AC(Locker)': 2849,
   'AC(Locker)': 2850,
   'AC(Locker)': 2851,
   'AC(Locker)': 2852,
   'N(elevator)': 2987,
   'N(elevator)': 2988,
   'H(D2)': 3017,
   'H(Toilet)': 3018,
   'N(D1)': 3063,
   'N(elevator)': 3067,
   'H(Mosque)': 3095,
   'H(class4)': 3096,
   'H(class3)': 3097,
   'N(Toilet)': 3146,
   'H(Biology lab)': 3174,
   'H(class2)': 3175,
   'H(class1)': 3176,
   'H(D1)': 3177,
   'N(G004)': 3218,
   'N(Meeting room)': 3219,
   'H(Biology lab)': 3253,
   'H(stairs)': 3254,
   'N(Microscope)': 3295,
   'N(Microscope)': 3296,
   'N(G021)': 3299,
   'N(G022)': 3300,
   'H(elevator)': 3332,
   'H(chemistry lab)': 3334,
   'N(Microscope)': 3374,
   'N(G018)': 3377,
   'H(office)': 3411,
   'H(chemistry lab)': 3413,
   'N(communication)': 3453,
   'N(communication)': 3454,
   'H(D3)': 3489,
   'H(Toilet)': 3490,
   'O(D)': 4386,
   'CC(D1)': 4562,
   'H': 3017, 
   'N': 3063,
   'S': 1626, 
   'CC': 4562,
   'O': 4386, 
   'D': 553,
   'e': 995,
   'w': 752,
   'AC': 2389,
   'h': 3017, 
   'n': 3063,
   's': 1626, 
   'cc': 4562,
   'o': 4386, 
   'd': 553,
   'e': 995,
   'w': 752,
   'ac': 2389,
   'helmy': 3017, 
   'nano': 3063,
   'service': 1626, 
   'culture complex': 4562,
   'one stop': 4386, 
   'onestop': 4386,
   'dorms': 553,
   'engineering': 995,
   'workshop': 752,
   'academic': 2389
}

def get_index_from_txt(txt):
    return mapper_to[txt]




def get_from_to_from_x(type1, type2, row1, col1, row2, col2):
   """get location user want to start from, and place user wants to go to

   Args:
       type1 (_type_): if cord: I will look at row1, and col1 as coordenates (row1,col), if pos, then user selected for example AC(G19),
       and I shall look for what what is the value of AC(G19)
       type2 (_type_): if cord: I will look at row2, and col2 as coordenates (row2,co2), if pos, then user selected for example AC(G19),
       and I shall look for what what is the value of AC(G19)
       row1 (_type_): either coordinates or name for place like N(Micro)
       col1 (_type_):  either coordinates or 'empty' if type1 = pos
       row2 (_type_): either coordinates or name for place like N(Micro)
       col2 (_type_): either coordinates or 'empty' if type2 = pos

   Returns:
       from_pos, to_pos: tuple, tuple 
   """
   COLS_COUNT = 78
   from_pos = 0
   to_pos = 0
   if type1 == 'cord': # then calculate the index 
      from_pos = int(col1) + int(row1)*COLS_COUNT
   if type1 == 'pos': # just look on x1
      from_pos = mapper_from[row1]

   if type2 == 'cord': ## then calculate the index  
      to_pos = [int(col2) + int(row2)*COLS_COUNT]
   if type2 == 'pos': # just look on x1
      to_pos = mapper_to[row2]

   return from_pos, to_pos


def get_alg(alg, problem):
   """get the reuslt of algoithrm specified by alg

   Args:
       alg (string): name of algoithrm
       problem (zc_map): problem to send it to algorithm

   Returns:
       _type_: _description_
   """
   if alg == 'bfs':
      return bfs_graph(problem)
   if alg == 'dfs':
      return dfs_graph(problem)
   if alg == 'dls':
      return dls_graph(problem)
   if alg == 'ids':
      return ids_graph(problem)
   if alg == 'greedy':
      return greedy_best_first(problem)
   if alg == 'ucs':
      return ucs(problem)
   if alg == 'astar':
      return a_star(problem)
   if alg == 'hillclimbing':
      return hill_climbing(problem)
   if alg == 'simulatedannealing':
      return simulated_annealing(problem,lambda t: exp(-t))

def get_id(row,col):
   """return string to be identified in the front end

   Args:
       row (int): row of cell
       col (int): col of cell

   Returns:
       _type_: _description_
   """
   return "cell-"+str(row)+"-"+str(col)


def alg_output_to_cells(alg_output, row1, col1):
   """geenerate list of cells ids to colorize in the front end, to send them back to the front end

   Args:
       alg_output (string): indicies of all cells to be visited
       row1 (int): intial row state of  user 
       col1 (int): intial col state of  user

   Returns:
       list: all cells ids
   """
   output = [get_id(row1,col1)]
   width = 78
   init_idx = int(row1)*width + int(col1) 

   action_vals = {'up': -width, 'down': +width, 'left': -1, 'right': +1,
    'diagonal_up_right': -width + 1, 'diagonal_up_left': -width - 1,
    'diagonal_down_right': width + 1, 'diagonal_down_left': width - 1}

   for op in alg_output:
       init_idx = init_idx + action_vals[op]
       idx_row = init_idx //width
       idx_col = init_idx % width
       output.append(get_id(idx_row, idx_col))
   return output


def alg_output_to_cells_local_search(alg_output, row1, col1):
   """as local search return all indices to cells that have been already visited

   Args:
       alg_output (string): indicies of all cells to be visited
       row1 (int): intial row state of  user 
       col1 (int): intial col state of  user

   Returns:
       list: all cells ids
   """
   output = []
   width = 78
   init_idx = int(row1)*width + int(col1)

   for op in alg_output:
       init_idx = op 
       idx_row = init_idx //width
       idx_col = init_idx % width
       output.append(get_id(idx_row, idx_col))
   return output




def get_row1_col1(type1,row1,col1, width = 78, height=81):
   """extact row1, and col1 from the front, if pos, it will look in mapper_from

   Args:
       type1 (_type_): if cord: I will look at row1, and col1 as coordenates (row1,col), if pos, then user selected for example AC(G19),
       and I shall look for what what is the value of AC(G19)
       row1 (_type_): either coordinates or name for place like N(Micro)
       col1 (_type_):  either coordinates or 'empty' if type1 = pos
       width (int, optional): width of the map. Defaults to 78.
       height (int, optional): height of the map. Defaults to 81.

   Returns:
       _type_: _description_
   """
   if type1 =="cord":
      return row1, col1

   elif type1 == "pos":
      index = mapper_from[row1]
      row1, col1 = index //width, index % width
      return row1, col1


def run(alg, type1, type2, row1, col1, row2, col2):
   """run algorithm specifed by alg, and intial state and goal

   Args:
       alg (string): algorithm user chosen
       type1 (_type_): if cord: I will look at row1, and col1 as coordenates (row1,col), if pos, then user selected for example AC(G19),
       and I shall look for what what is the value of AC(G19)
       type2 (_type_): if cord: I will look at row2, and col2 as coordenates (row2,co2), if pos, then user selected for example AC(G19),
       and I shall look for what what is the value of AC(G19)
       row1 (_type_): either coordinates or name for place like N(Micro)
       col1 (_type_):  either coordinates or 'empty' if type1 = pos
       row2 (_type_): either coordinates or name for place like N(Micro)
       col2 (_type_): either coordinates or 'empty' if type2 = pos

   Returns:
       _type_: _description_
   """
   zc_map = get_map()
   start_time = datetime.now()
   problem = ZcMap(*get_from_to_from_x(type1, type2, row1, col1, row2, col2), zc_map)
   sol = get_alg(alg,problem)
   end_time = datetime.now()
   # print("Time ",end_time - start_time)
   output = sol[0]
   path_cost = sol[1]
   row1, col1 = get_row1_col1(type1, row1, col1)   
   alg_ouptut_to_cells = alg_output_to_cells(output, int(row1), int(col1)) if not (alg == 'simulatedannealing' or alg == 'hillclimbing') else alg_output_to_cells_local_search(output, int(row1), int(col1))
   return end_time - start_time, alg_ouptut_to_cells, path_cost