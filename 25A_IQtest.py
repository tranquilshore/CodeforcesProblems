n = input()
l = raw_input().split()

l = [int(x) for x in l]
l_count = list()
for i in range(n):
    count = 0
    for j in range(n):
        if i == j:
            continue
        if abs(l[i] - l[j])%2 != 0:
            count += 1
    l_count.append(count)

for i in range(len(l_count)):
    if l_count[i] == n-1:
        print i+1
        break


