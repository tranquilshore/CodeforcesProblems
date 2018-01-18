n,p,l,r = raw_input().split()
n = int(n)
p = int(p)
l = int(l)
r = int(r)

tabs = [i for i in range(1,n+1)]

seconds = 0

if l == tabs[0] and r == tabs[n-1]:
    print seconds
if l == tabs[0] and r != tabs[n-1]:
    if p >= l and p <= r:
        seconds += r - p + 1
    else:
        seconds += p - r + 1
    print seconds
if l != tabs[0] and r == tabs[n-1]:
    if p >= l and p <= r:
        seconds += p-l + 1
    else:
        seconds += l-p + 1
    print seconds

if l > tabs[0] and r < tabs[n-1]:
    if p >= l and p <= r:
        if abs(p-l) <= abs(p-r):
            seconds+= abs(p-l) + 2 + abs(r-l)
        else:
            seconds+= abs(p-r) + 2 + abs(r-l)
        print seconds
    if p < l:
        seconds += abs(l-p) + 1 + abs(r-l) + 1
        print seconds
    if p > r:
        seconds += abs(p-r) + 1 + abs(r-l) + 1
        print seconds
