import json
import random
import csv
import os
import re

random.seed(329)

def filterSpecial(content):
    RE_IN = re.compile(r'\\u\w* ')
    id = []
    for m in RE_IN.finditer(content):
        id.append([m.start(), m.end()])
    s = len(id)
    while s > 0:
        content = content[:id[s - 1][0]] + " " + content[id[s - 1][2]:]
        s -= 1
    return content



with open("../res/data/immigration.json") as input_file:
    imm = json.load(input_file)
with open("../res/data/coronavirus.json") as input_file:
    co = json.load(input_file)
print(len(imm))
print(len(co))
print('----------------------------------------')



count = dict()
for i in imm:
    a = i['source']
    count[a] = count.get(a, 0) + 1
print(len(count))



count = dict()
for i in co:
    a = i['source']
    count[a] = count.get(a, 0) + 1
print(len(count))



#with open("../res/final/imm_filter.json", "w+") as f:
#    json.dump(imm_r, f, indent=4)
#with open("../res/final/co_filter.json", "w+") as f:
#    json.dump(co_r, f, indent=4)




"""
with open("../res/training/imm_sample_blind.json") as input_file:
    imm_s = json.load(input_file)
with open("../res/training/co_sample_blind.json") as input_file:
    co_s = json.load(input_file)
print(len(imm_s))
print(len(co_s))
print('----------------------------------------')

imm_st = set()
co_st = set()
for i in imm_s:
    imm_st.add(i['ID'])
for i in co_s:
    co_st.add(i['ID'])
print(len(imm_st))
print(len(co_st))
print('----------------------------------------')

res_i = random.sample(range(len(imm) - len(imm_st)), 20)
res_c = random.sample(range(len(co) - len(co_st)), 15)
print(len(res_i), res_i)
print(len(res_c), res_c)
print('----------------------------------------')

new_imm = []
for i in imm:
    if i['ID'] not in imm_st:
        new_imm.append(i)

new_co = []
for i in co:
    if i['ID'] not in co_st:
        new_co.append(i)
print(len(new_imm))
print(len(new_co))
print('----------------------------------------')

imm_sample= []
imm_sample_n = []
for i in res_i:
    # row = [imm[i]['title'],imm[i]['date'],imm[i]['content'],imm[i]['ID']]
    # csvWriter.writerow(row)
    imm_sample_n.append(
        {'topic': new_imm[i]['title'], 'date': new_imm[i]['date'], 'content': new_imm[i]['content'],
         'ID': new_imm[i]['ID'],
         'sub_0': '', 'sub_1': '', 'sub_2': '', "sub_3": '', 'sub_4': '', 'sub_5': '', 'sub_6': '', 'sub_7': '',
         'sub_8': '', 'sub_9': ''})
    imm_sample.append(new_imm[i])


co_sample = []
co_sample_n = []
for i in res_c:
    # row = [imm[i]['title'],imm[i]['date'],imm[i]['content'],imm[i]['ID']]
    # csvWriter.writerow(row)
    co_sample_n.append(
        {'topic': new_co[i]['title'], 'date': new_co[i]['date'], 'content': new_co[i]['content'],
         'ID': new_co[i]['ID'],
         'sub_0': '', 'sub_1': '', 'sub_2': '', "sub_3": '', 'sub_4': '', 'sub_5': '', 'sub_6': '', 'sub_7': '',
         'sub_8': '', 'sub_9': ''})
    co_sample.append(new_co[i])
"""

"""

with open("../res/training/new_co_sample.json", "w+") as f:
    json.dump(co_sample, f, indent=4)
with open("../res/training/new_co_sample_blind.json", "w+") as f:
    json.dump(co_sample_n, f, indent=4)
print('done')
"""
