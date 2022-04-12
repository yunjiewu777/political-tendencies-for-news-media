import json

coronavirus = json.load(open('coronavirus.json'))
healthcare = json.load(open('healthcare.json'))
immigration = json.load(open('immigration.json'))

for c in immigration:
    id = c['ID']
    with open('immigration/'+str(id)+'.txt', "w") as f:
        f.write(c['content'])