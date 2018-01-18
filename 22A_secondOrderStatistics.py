import operator, itertools
n = int(raw_input())
l = raw_input().split()
l = [int(x) for x in l]

l.sort()

groups = itertools.groupby(l,lambda x:x)

i = 0
ans = 0
if len(l) > 0:
    for key,group in groups:
        if i == 1:
            ans = key
        i += 1
    if ans == 0:
        print "NO"
    else:
        print ans
else:
    print "NO"
