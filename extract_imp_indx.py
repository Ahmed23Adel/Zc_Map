from ProblemFormulation import *

zc_map = get_map()
print("{")
for i,element in enumerate(zc_map):
    if "(" in str(element):
        print(" '{}': [{}],".format(element, i))

# print("}")
# mapper = {
#  'D(D2)': 553,
#  # 'Dorms': 553,
#  'w(D)': 752,
#  'D(D1)': 790,
#  'e(D)': 995,
#  'S(D)': 1626,
#  'AC(D)': 1754,
#  'AC(G20)': 1838,
#  'AC(G19)': 1839,
#  'AC(G18)': 1918,
#  'AC(G12)': 1997,
#  'AC(Zone B)': 2075,
#  'AC(G11)': 2076,
#  'AC(Zone B)': 2153,
#  'AC(G10)': 2154,
#  'AC(Zone B)': 2231,
#  'AC(G9)': 2232,
#  'AC(Zone B)': 2309,
#  'AC(G8)': 2310,
#  'AC(Toilets)': 2375,
#  'AC(G6, security room)': 2376,
#  'AC(G11)': 2384,
#  'AC(Zone B)': 2387,
#  'AC(G7)': 2388,
#  'AC(D)': 2389,
#  'AC(ATM)': 2454,
#  'AC(Security room)': 2457,
#  'AC(G12)': 2462,
#  'AC(Zone B)': 2465,
#  'AC(G6)': 2466,
#  'AC(D1)': 2534,
#  'AC(G1)': 2536,
#  'AC(F)': 2537,
#  'AC(F)': 2538,
#  'AC(F)': 2539,
#  'AC(G13)': 2540,
#  'AC(Zone B)': 2543,
#  'AC(G5)': 2544,
#  'AC(cats office)': 2614,
#  'AC(F)': 2615,
#  'AC(F)': 2616,
#  'AC(F)': 2617,
#  'AC(G14)': 2618,
#  'AC(G14)': 2692,
#  'AC(F)': 2693,
#  'AC(F)': 2694,
#  'AC(F)': 2695,
#  'AC(G15)': 2696,
#  'AC(G15)': 2770,
#  'AC(F)': 2771,
#  'AC(F)': 2772,
#  'AC(F)': 2773,
#  'AC(Locker)': 2848,
#  'AC(Locker)': 2849,
#  'AC(Locker)': 2850,
#  'AC(Locker)': 2851,
#  'AC(Locker)': 2852,
#  'H(D2)': 3017,
#  'N(D1)': 3063,
#  'H(D1)': 3177,
#  'H(D3)': 3489,
#  'O(D)': 4386,
#  'CC(D1)': 4562,
# }
# x ={
#     'H': [],
#     'N': [],
#     'S': [],
#     'CC': [],
#     'O': [],
#     'D': [],
#     'e': [],
#     'w': [],
#     'AC': [],
# }
# # H(D)
# for ele in mapper.keys():
#     tmp = ele.split("(")[0]
#     tmp2 = ele.split("(")[1][0]
#     if tmp2 == "D":
#         x[tmp].append(mapper[ele])
#
# print(x)
