chessboard = []
try:
    while True:
        r = raw_input()
        if r != "":
            chessboard.append(r)
        else:
            break
except EOFError:
    pass

count = 0
whiteFlag = False

for r in chessboard:
    if "W" in r:
        whiteFlag = True
        pass
    else:
        count += 1

s = list()
col_chessboard = list()
for i in range(8):
    s = [""]
    for j in range(8):
        s[0] += chessboard[j][i]
    col_chessboard.append(s[0])

if whiteFlag == True:
    for r in col_chessboard:
        if "W" in r:
            pass
        else:
            count += 1

    print count
else:
    print count
