lcd = []
try:
    while True:
        r = raw_input()
        if r != "":
            lcd.append(r)
        else:
            break
except EOFError:
    pass

lcd = [list(x) for x in lcd]

noflag = False
right_diagonal_flag = False
left_diagonal_flag = False
middle_horizontal_flag = False
middle_vertical_flag = False

if lcd[0][0] == lcd[2][2]:
    right_diagonal_flag = True
else:
    noflag = True
    
if lcd[0][2] == lcd[2][0]:
    left_diagonal_flag = True
else:
    noflag = True

if lcd[1][0] == lcd[1][2]:
    middle_horizontal_flag = True
else:
    noflag = True

if lcd[0][1] == lcd[2][1]:
    middle_vertical_flag = True
else:
    noflag = True

if noflag == True:
    print "NO"
else:
    print "YES"
        
