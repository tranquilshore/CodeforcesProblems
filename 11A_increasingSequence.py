n = raw_input().split()
n = [int(x) for x in n]
a_size = n[0]
d = n[1]

a = raw_input().split()
a = [int(x) for x in a]

count = 0

for i in range(a_size-1):
    if a[i] < a[i+1]:
        continue
    elif a[i] == a[i+1]:
        a[i+1] += d
        count += 1
    else:
        val = (a[i] - a[i+1])//d + 1
        count += val 
        a[i+1] += val*d
print count


        
