import csv
import json

dic = {}
coun=0
with open("majestic_million.csv") as w:
    reader = csv.DictReader(w)
    for rows in reader:
        coun+=1
        if coun>1000000:
            break
        d = rows["Domain"]
        rank = rows["GlobalRank"]
        dic[d] = rank
f = open("majestic_million.json", 'w')
json.dump(dic, f)
