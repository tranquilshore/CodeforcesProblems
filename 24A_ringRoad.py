n = input()
road = [map(int,raw_input().split()) for i in range(n)]

c1 = 0
c2 = 0
p = 1
pr = 0

for i in range(n):
    for r in road:
        if r != pr:
            if r[0] == p:
                p = r[1]
                c1 += r[2]
                pr = r
                break
            if r[1] == p:
                p = r[0]
                c2 += r[2]
                pr = r
                break

print min(c1,c2)
