from __future__ import print_function
n,m = raw_input().split()
n = int(n)
m = int(m)

letter = []
try:
    while True:
        r = raw_input()
        if r != "":
            letter.append(r)
        else:
            break
except EOFError:
    pass

shades = []

for i in range(n):
    for j in range(m):
        if letter[i][j] == "*":
            shades.append((i,j))

start_x = min([x[0] for x in shades])
start_y = min([x[1] for x in shades])
end_x = max([x[0] for x in shades])
end_y = max([x[1] for x in shades])

ans = ""

for i in range(start_x,end_x+1):
    for j in range(start_y,end_y+1):
        ans += letter[i][j]
    print(ans)
    ans = ""




