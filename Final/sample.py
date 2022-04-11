import json
import random
import csv
import os

random.seed(329)


with open("../res/data/immigration.json") as input_file:
    imm = json.load(input_file)
res = random.sample(range(len(imm)), 15)
print(res)

print(imm[0])

imm_sample = []
imm_sample_n = []
os.remove('../res/training/imm_sample.csv')

csvFile = open('../res/training/imm_sample.csv', "a", newline="", encoding='utf-8')
csvWriter = csv.writer(csvFile)

csvWriter.writerow(["title", "date", "content", "ID", "sub_0", "sub_1", "sub_2", "sub_3"])

for i in res:
   row = [imm[i]['title'],imm[i]['date'],imm[i]['content'],imm[i]['ID']]
   csvWriter.writerow(row)
   imm_sample_n.append({'topic': imm[i]['title'], 'date':imm[i]['date'], 'content':imm[i]['content'], 'ID':imm[i]['ID'], 'sub_0':'','sub_1':'','sub_2':'',"sub_3":''})
   imm_sample.append(imm[i])

csvFile.close()
with open("../res/training/imm_sample.json", "w+") as f:
    json.dump(imm_sample, f, indent=4)
with open("../res/training/imm_sample_n.json", "w+") as f:
    json.dump(imm_sample_n, f, indent=4)
print('done')
