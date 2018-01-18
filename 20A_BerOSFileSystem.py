s = raw_input().split('/')
s = filter(lambda x: x != '',s)
ans = ''
if len(s) == 0:
    print "/"
else:
    for i in s:
        ans += '/'+i
    print ans 