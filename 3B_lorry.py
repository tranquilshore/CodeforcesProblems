'''
Done using 01 knapsack
time limit is getting exceeded at test case 8
'''

n,v = raw_input().split()
n = int(n)
W = int(v)

wt = []
val = []
count = 1
for i in range(n):
    weight,value = raw_input().split()
    weight = int(weight)
    value = int(value)
    wt.append((weight,count))
    count += 1
    val.append(value)

k = [[None]*(W+1) for i in range(n+1)]

def knapsack(W,wt,val,n):
    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                k[i][j] = 0
            elif wt[i-1][0] <= j:
                k[i][j] = max(val[i-1] + k[i-1][j-wt[i-1][0]], k[i-1][j])
            else:
                k[i][j] = k[i-1][j]
    return k[n][W]
print knapsack(W,wt,val,n)

tmplst = []
for i in range(n,-1,-1):
    if k[i][W] > k[i-1][W]:
        tmplst.append(wt[i-1][1])
        W -= wt[i-1][0]

tmplst = [str(x) for x in tmplst]
print " ".join(tmplst)

    
    
