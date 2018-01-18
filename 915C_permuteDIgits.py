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