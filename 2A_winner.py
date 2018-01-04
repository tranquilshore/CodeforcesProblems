from collections import defaultdict
from itertools import groupby
from operator import itemgetter
import sys

d = defaultdict()
d1 = defaultdict()
num_of_rounds = int(raw_input())
tup_lst = list()

for i in range(0,num_of_rounds):
    name, score = raw_input().split(" ")
    tup_lst.append((name,int(score)))
    if name in d:
        d[name] = d[name] + int(score)
    else:
        d[name] = int(score)

max_val = max(d.values())
max_names = [key for key, value in d.iteritems() if value == max_val]

for i in tup_lst:
    if i[0] in d1:
        d1[i[0]] = d1[i[0]] + i[1]
        if d1[i[0]] >= max_val and i[0] in max_names:
            print i[0]
            break
    else:
        d1[i[0]] = i[1]
        if d1[i[0]] >= max_val and i[0] in max_names:
            print i[0]
            break
    

