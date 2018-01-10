n,t = raw_input().split()
n = int(n)
t = int(t)

house_dim = []
possible_positions = 2

for i in range(n):
    c,s = raw_input().split()
    c = int(c)
    s = float(s)
    xs = s/2
    house_dim.append((c-xs,c+xs))

house_dim.sort()

for i in range(len(house_dim)-1):
    if house_dim[i+1][0] - house_dim[i][1] == t:
        possible_positions += 1
    elif house_dim[i+1][0] - house_dim[i][1] > t:
        if house_dim[i][1]+t <= house_dim[i+1][0]:
            possible_positions += 1
        if house_dim[i+1][0]-t >= house_dim[i][1]:
            possible_positions += 1

print possible_positions

    