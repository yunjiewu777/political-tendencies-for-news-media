import json
import random
import csv
import os

random.seed(329)

with open("../res/data/coronavirus.json") as input_file:
    co = json.load(input_file)

count = dict()
for i in co:
    a = i['source']
    count[a] = count.get(a, 0) + 1


a = {k: v for k, v in sorted(count.items(), key=lambda item: item[1], reverse=True)}

sou = []
for k in a:
    if a[k] >=10:
        sou.append(k)


print(a)
print(sou)




"""
final_co = []
fox = []
cnn = []
for article in co:
    if article['source'] in ['Fox News']:
        fox.append(article)
    elif article['source'] in ['CNN (Web News)']:
        cnn.append(article)
    elif article['source'] in ['BBC News']:
        final_co.append(article)
print(len(final_co))

res = random.sample(range(len(cnn)), 30)
for index in res:
    final_co.append(cnn[index])
print(len(final_co))

res = random.sample(range(len(fox)), 30)
for index in res:
    final_co.append(fox[index])
print(len(final_co))

with open("../res/data/imm_final.json", "w+") as f:
    json.dump(final_co, f, indent=4)
print(len(final_co))
"""
