import pickle
import numpy as np
import csv
import pandas as pd
import json


with open("../res/final/co_s", "rb") as fp:  # Unpickling
    s = pickle.load(fp)

source = s[15]

with open("../res/final/co_"+source, "rb") as fp:  # Unpickling
    tmp = pickle.load(fp)
print(len(tmp))
Csum = np.array([0, 0, 0])
for i in tmp:
    Csum = Csum + i
Csum = Csum / len(tmp)
print(Csum)

line1 = "\\rowcolor{A}\\cellcolor[HTML]{FFFFFF}"
line2 = "\\rowcolor{B}\\cellcolor[HTML]{FFFFFF}"
line3 = "\\rowcolor{C}\\multirow{-3}{*}{\\cellcolor[HTML]{FFFFFF}"+ source+ "}"

for i in Csum:
    line1 = line1 + "&" + str(round(i[0], 3))
    line2 = line2 + "&" + str(round(i[1], 3))
    line3 = line3 + "&" + str(round(i[2], 3))


line1 = line1 + "\\\\"
line2 = line2 + "\\\\"
line3 = line3 + "\\\\ \\hline \\hline"

print(line1 + "\n" + line2 + "\n" + line3)


"""
with open("../res/final/co_filter.json") as input_file:
    co = json.load(input_file)

tmp = []
for i in co:
    if i['source'] == "Vox":
        tmp.append(i)

print(len(tmp))
with open("../res/final/co_V.json", "w+") as f:
    json.dump(tmp, f, indent=4)
"""


"""
with open("../res/final/imm_Vox", "rb") as fp:  # Unpickling
    tmp = pickle.load(fp)
print(len(tmp))
Csum = np.array([0, 0, 0])
for i in tmp:
    Csum = Csum + i
Csum = Csum / len(tmp)
print(Csum)

line1 = "\\rowcolor{A}\\cellcolor[HTML]{FFFFFF}"
line2 = "\\rowcolor{B}\\cellcolor[HTML]{FFFFFF}"
line3 = "\\rowcolor{C}\\multirow{-3}{*}{\\cellcolor[HTML]{FFFFFF}Vox}"

for i in Csum:
    line1 = line1 + "&" + str(round(i[0], 3))
    line2 = line2 + "&" + str(round(i[1], 3))
    line3 = line3 + "&" + str(round(i[2], 3))


line1 = line1 + "\\\\"
line2 = line2 + "\\\\"
line3 = line3 + "\\\\ \\hline \\hline"

print(line1 + "\n" + line2 + "\n" + line3)
"""