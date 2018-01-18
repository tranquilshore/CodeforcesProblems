n,k  = raw_input().split()
n = int(n)
k = int(k)

s = raw_input().split()
s = [int(x) for x in s ]

s.sort()

for i in range(len(s)):
    if k%s[i] == 0:
        tans = s[i]

print k/tans