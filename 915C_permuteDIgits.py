a=list(raw_input())
b=int(raw_input())
fix=''
a.sort()
a.reverse()
while(len(a)>0):
    for i in range(0,len(a)):
        num=fix+a[i]+"".join(sorted(a[:i]+a[i+1:]))
        if(int(num)<=b):
            fix+=a[i]
            a=a[:i]+a[i+1:]
            break
print(fix)

'''
#my first solution - gave memory exceeded error, where i was calulating every permute and storing

import itertools

a = raw_input()
b = raw_input()

a = list(a)
b = int(b)

p_list = list(itertools.permutations(a,len(a)))
#p_list = [[int(x) for x in y] for y in p_list]

ans = 0
a_ans = ''
for i in p_list:
    tsum = ''
    for j in range(len(a)):
        tsum += i[j]
    if int(tsum) <= b and int(tsum) > ans:
        ans = int(tsum)
        a_ans = tsum

print a_ans 
'''