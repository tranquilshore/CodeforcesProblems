import itertools
n = raw_input().split()
n = [int(x) for x in n]
cb = list(itertools.combinations(n,3))
t = list()
for x in cb:
    t.append((x[0] + x[1] - x[2])*(x[1] + x[2] - x[0])*(x[2] + x[0] - x[1]))

anyOnePositiveFlag = False
anyOneZeroButNoPositive = False
allNegative = False

for i in t:
    if i > 0:
        anyOnePositiveFlag = True

for i in t:
    if i == 0 and anyOnePositiveFlag == False:
        anyOneZeroButNoPositive = True

for i in t:
    if i < 0 and anyOnePositiveFlag == False and anyOneZeroButNoPositive == False:
        allNegative = True

if anyOnePositiveFlag == True:
    print "TRIANGLE"
if anyOneZeroButNoPositive == True:
    print "SEGMENT"
if allNegative == True:
    print "IMPOSSIBLE"
        
    

    
