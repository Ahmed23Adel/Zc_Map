from AILogic.ProblemFormulation import *
from  AILogic.Algorithms_uninformed import *
from AILogic.Algorithms_informed import *


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
 'H(D2)': [3017],
 'N(D1)': [3063],
 'H(D1)': [3177],
 'H(D3)': [3489],
 'O(D)': [4386],
 'CC(D1)': [4562],
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
 'H(D2)': 3017,
 'N(D1)': 3063,
 'H(D1)': 3177,
 'H(D3)': 3489,
 'O(D)': 4386,
 'CC(D1)': 562,
 'h': 3017,
 'n': 3063,
 's': 1626,
 'cc': 4562,
 'o': 4386,
 'd': 553,
 'e': 995,
 'w': 752,
 'ac': 2389,
'helmy':3017,
 'nano': 3063,
 'service': 1626,
 'culture complex': 4562,
 'one stop': 4386,
 'dorms': 553,
'onestop': 4386,
 'engineering': 995,
 'workshop': 752,
 'academic': 2389
}

def get_index_from_txt(txt):
    return mapper_to[txt]


from _datetime import datetime

def get_from_to_from_x(type1, type2, row1, col1, row2, col2):
 ROW_COUNT, COLS_COUNT = 81, 78
 from_pos = 0
 to_pos = 0
 if type1 == 'cord':
  print("type1",col1 + row1*COLS_COUNT)
  from_pos = int(col1) + int(row1)*COLS_COUNT
 if type1 == 'pos': # just look on x1
   from_pos = mapper_from[row1]
 if type2 == 'cord':
  print("typ2",[int(col2) + int(row2)*COLS_COUNT])
  to_pos = [int(col2) + int(row2)*COLS_COUNT]
 if type2 == 'pos': # just look on x1
   to_pos = mapper_to[row2]
 return from_pos, to_pos


def get_alg(alg, problem):
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

def get_id(row,col):
 return "cell-"+str(row)+"-"+str(col)


def alg_output_to_cells(alg_output, row1, col1):
   print("row1", row1, col1, type(row1))
   output = [get_id(row1,col1)]
   width = 78
   height = 81
   init_idx = int(row1)*width + int(col1)
   # print("row1*width + col1", row1*width + col1)
   action_vals = {'up': -width, 'down': +width, 'left': -1, 'right': +1,
    'diagonal_up_right': -width + 1, 'diagonal_up_left': -width - 1,
    'diagonal_down_right': width + 1, 'diagonal_down_left': width - 1}
   for op in alg_output:
       print("init_idx", init_idx)
       init_idx = init_idx + action_vals[op]
       idx_row = init_idx //width
       idx_col = init_idx % width
       print("newinit_idx",init_idx, idx_row, idx_col)
       output.append(get_id(idx_row, idx_col))
   return output

def get_row1_col1(type1,row1,col1, width = 78, height=81):
   if type1 =="cord":
      return row1, col1
   elif type1 == "pos":
      index = mapper_from[row1]
      row1, col1 = index //width, index % width
      return row1, col1


def run(alg, type1, type2, row1, col1, row2, col2):
    zc_map = get_map()
    start_time = datetime.now()
    print("get_from_to_from_x",get_from_to_from_x(type1, type2, row1, col1, row2, col2))
    problem = ZcMap(*get_from_to_from_x(type1, type2, row1, col1, row2, col2), zc_map)
    sol = get_alg(alg,problem)
    end_time = datetime.now()
    print("Time ",end_time - start_time)
    print("sol", (sol))
    output = sol[0]
    print("output",output)
    row1, col1 = get_row1_col1(type1, row1, col1)
    print(row1, col1)
    print("alg_output_to_cells",alg_output_to_cells(output, row1, col1))
    return end_time - start_time, alg_output_to_cells(output, int(row1), int(col1))