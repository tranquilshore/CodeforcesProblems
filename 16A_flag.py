n,m = raw_input().split()
n = int(n)
m = int(m)

flag = []

for i in range(n):
    h = raw_input()
    flag.append(h)

different_flag = True
different_color_flag = False

if len(flag) == 2:
    if flag[0] == flag[1]:
        different_flag = False
elif len(flag) > 2:
    for i in range(1,len(flag) - 1):
        if flag[i-1] == flag[i] or flag[i] == flag[i+1]:
            different_flag = False

flag = [list(i) for i in flag]

for h_line in flag:
    h_set = set(h_line)
    if len(h_set) > 1:
        different_color_flag = True

if different_flag == True and different_color_flag == False:
    print "YES"
else:
    print "NO"


