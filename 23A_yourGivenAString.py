import operator,itertools
def substrings(str):
    n = len(str)
    lst = [str[i:j+1] for i in range(n) for j in range(i,n)]
    return lst
input_str = raw_input()
s_list = substrings(input_str)
s_list.sort()
groups = itertools.groupby(s_list,lambda x:x)
count = 0
for key,group in groups:
    s = list(group)
    if len(s) >=2:
        if len(s[0]) > count:
            count = len(s[0])

print count
    


