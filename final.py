import pickle
import numpy as np
import csv

with open("../ABSA-PyTorch/co_CNN_result", "rb") as fp:  # Unpickling
    CNN = pickle.load(fp)
print(len(CNN))

with open("../ABSA-PyTorch/co_Fox_result", "rb") as fp:  # Unpickling
    Fox = pickle.load(fp)
print(len(Fox))

with open("../ABSA-PyTorch/co_BBC_result", "rb") as fp:  # Unpickling
    BBC = pickle.load(fp)
print(len(BBC))

csvFile = open('imm_final.csv', "a", newline="", encoding='utf-8')
csvWriter = csv.writer(csvFile)

Csum = np.array([0, 0, 0])
for i in CNN:
    Csum = Csum + i
Csum = Csum / len(CNN)
print(Csum)
for i in Csum:
    csvWriter.writerow([round(i[0], 3), round(i[1], 3), round(i[2], 3)])

Fsum = np.array([0, 0, 0])
for i in Fox:
    Fsum = Fsum + i
Fsum = Fsum / len(Fox)
print(Fsum)
for i in Fsum:
    csvWriter.writerow([round(i[0], 3), round(i[1], 3), round(i[2], 3)])

Bsum = np.array([0, 0, 0])
for i in BBC:
    Bsum = Bsum + i
Bsum = Bsum / len(BBC)
print(Bsum)
for i in Bsum:
    csvWriter.writerow([round(i[0], 3), round(i[1], 3), round(i[2], 3)])

csvFile.close()