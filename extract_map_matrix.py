import csv
import numpy as np
data = np.array(list(csv.reader(open(r"CSV AI_ZC_map - Sheet1.csv"))))
print(data[1][4])
print(data.shape)
