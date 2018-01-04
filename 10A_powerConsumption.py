user_input = raw_input().split()
user_input = [int(x) for x in user_input]

n = user_input[0]
p1 = user_input[1]
p2 = user_input[2]
p3 = user_input[3]
t1 = user_input[4]
t2 = user_input[5]

work_perd = list()

for i in range(n):
    period = raw_input().split()
    period = [int(x) for x in period]
    start = period[0]
    end = period[1]
    work_perd.append((start,end))

power_consump = 0

if n == 1:
    print (work_perd[0][1] - work_perd[0][0])*p1
else:
    power_consump += (work_perd[0][1] - work_perd[0][0])*p1
    for i in range(len(work_perd)-1):
        idle = work_perd[i+1][0] - work_perd[i][1]
        if idle >= t1:
            power_consump += t1*p1
            idle -= t1
            if idle >= t2:
                power_consump += t2*p2
                idle -= t2
                if idle >= 0:
                    power_consump += p3*idle
            else:
                power_consump += idle*p2
        else:
            power_consump += idle*p1
        power_consump += (work_perd[i+1][1] - work_perd[i+1][0])*p1
    print power_consump        
        
