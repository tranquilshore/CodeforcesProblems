
'''
#shortest possible and easy solution

s = raw_input()
t = raw_input()
char_map = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}

x1, y1 = int(char_map[s[0]]), int(s[1])
x2, y2 = int(char_map[t[0]]), int(t[1])

count = max(abs(x1-x2),abs(y1-y2))
print count
while (str(x1)+str(y1) != str(x2)+str(y2) ):
    if x1 < x2:
        print "R",
        x1 += 1
    elif x1 > x2:
        print "L",
        x1 -= 1
    if y1 < y2:
        print "U",
        y1 += 1
    elif y1 > y2:
        print "D",
        y1 -= 1
    print
'''

#my solution
from collections import defaultdict
s = raw_input()
d = raw_input()
char_map = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}

x1, y1 = int(char_map[s[0]]), int(s[1])
x2, y2 = int(char_map[d[0]]), int(d[1])

count = 0
directions = list()

def distance(x1,y1,x2,y2):
    dist = (x1-x2)**2 + (y1-y2)**2
    return dist

def left(x1,y1,x2,y2):
    Lx,Ly = x1-1,y1
    L_dist = distance(Lx,Ly,x2,y2)
    return Lx,Ly,L_dist

def leftUp(x1,y1,x2,y2):
    LUx,LUy = x1-1,y1+1
    LU_dist = distance(LUx,LUy,x2,y2)
    return LUx,LUy,LU_dist

def up(x1,y1,x2,y2):
    Ux,Uy = x1,y1+1
    U_dist = distance(Ux,Uy,x2,y2)
    return Ux,Uy,U_dist

def rightUp(x1,y1,x2,y2):
    RUx,RUy = x1+1,y1+1
    RU_dist = distance(RUx,RUy,x2,y2)
    return RUx,RUy,RU_dist

def right(x1,y1,x2,y2):
    Rx,Ry = x1+1,y1
    R_dist = distance(Rx,Ry,x2,y2)
    return Rx,Ry,R_dist

def rightDown(x1,y1,x2,y2):
    RDx,RDy = x1+1,y1-1
    RD_dist = distance(RDx,RDy,x2,y2)
    return RDx,RDy,RD_dist

def down(x1,y1,x2,y2):
    Dx,Dy = x1,y1-1
    D_dist = distance(Dx,Dy,x2,y2)
    return Dx,Dy,D_dist

def leftDown(x1,y1,x2,y2):
    LDx,LDy = x1-1,y1-1
    LD_dist = distance(LDx,LDy,x2,y2)
    return LDx,LDy,LD_dist

code_exec = True
if x1 == x2 and y1 == y2:
    code_exec = False

if code_exec == True:
    while True:
        if (x1 == 1 and (y1 > 1 and y1 < 8)):#left edge
            d = defaultdict()
            Ux,Uy,U_dist = up(x1,y1,x2,y2)
            d["U_dist"] = U_dist

            Rx,Ry,R_dist = right(x1,y1,x2,y2)
            d["R_dist"] = R_dist

            Dx,Dy,D_dist = down(x1,y1,x2,y2)
            d["D_dist"] = D_dist

            RUx,RUy,RU_dist = rightUp(x1,y1,x2,y2)
            d["RU_dist"] = RU_dist

            RDx,RDy,RD_dist = rightDown(x1,y1,x2,y2)
            d["RD_dist"] = RD_dist

            min_dir = min(d, key=d.get)
            if min_dir == "U_dist":
                directions.append("U")
                x1,y1 = Ux,Uy
                count += 1
            if min_dir == "R_dist":
                directions.append("R")
                x1,y1 = Rx,Ry
                count += 1
            if min_dir == "D_dist":
                directions.append("D")
                x1,y1 = Dx,Dy
                count += 1
            if min_dir == "RU_dist":
                directions.append("RU")
                x1,y1 = RUx, RUy
                count += 1
            if min_dir == "RD_dist":
                directions.append("RD")
                x1,y1 = RDx,RDy
                count += 1
        elif (x1 > 1 and x1 < 8) and y1 == 1: #bottom edge
            d = defaultdict()
            Lx,Ly,L_dist = left(x1,y1,x2,y2)
            d["L_dist"] = L_dist

            LUx,LUy,LU_dist = leftUp(x1,y1,x2,y2)
            d["LU_dist"] = LU_dist

            Ux,Uy,U_dist = up(x1,y1,x2,y2)
            d["U_dist"] = U_dist

            RUx,RUy,RU_dist = rightUp(x1,y1,x2,y2)
            d["RU_dist"] = RU_dist

            Rx,Ry,R_dist = right(x1,y1,x2,y2)
            d["R_dist"] = R_dist

            min_dir = min(d,key=d.get)
            if min_dir == "L_dist":
                directions.append("L")
                x1,y1 = Lx,Ly
                count += 1
            if min_dir == "LU_dist":
                directions.append("LU")
                x1,y1 = LUx,LUy
                count += 1
            if min_dir == "U_dist":
                directions.append("U")
                x1,y1 = Ux,Uy
                count += 1
            if min_dir == "RU_dist":
                directions.append("RU")
                x1,y1 = RUx,RUy
                count+= 1
            if min_dir == "R_dist":
                directions.append("R")
                x1,y1 = Rx,Ry
                count += 1
        elif x1 == 8 and (y1 > 1 and y1 < 8):#right edge
            d = defaultdict()
            Ux,Uy,U_dist = up(x1,y1,x2,y2)
            d["U_dist"] = U_dist

            LUx,LUy,LU_dist = leftUp(x1,y1,x2,y2)
            d["LU_dist"] = LU_dist

            Lx,Ly,L_dist = left(x1,y1,x2,y2)
            d["L_dist"] = L_dist

            LDx,LDy,LD_dist = leftDown(x1,y1,x2,y2)
            d["LD_dist"] = LD_dist

            Dx,Dy,D_dist = down(x1,y1,x2,y2)
            d["D_dist"] = D_dist

            min_dir = min(d,key=d.get)
            if min_dir == "U_dist":
                directions.append("U")
                x1,y1 = Ux,Uy
                count += 1
            if min_dir == "LU_dist":
                directions.append("LU")
                x1,y1 = LUx,LUy
                count += 1
            if min_dir == "L_dist":
                directions.append("L")
                x1,y1 = Lx,Ly
                count += 1
            if min_dir == "LD_dist":
                directions.append("LD")
                x1,y1 = LDx,LDy
                count += 1
            if min_dir == "D_dist":
                directions.append("D")
                x1,y1 = Dx,Dy
                count += 1
        elif (x1 > 1 and x1 < 8) and y1 == 8:#top edge
            d = defaultdict()
            Lx,Ly,L_dist = left(x1,y1,x2,y2)
            d["L_dist"] = L_dist

            LDx,LDy,LD_dist = leftDown(x1,y1,x2,y2)
            d["LD_dist"] = LD_dist

            Dx,Dy,D_dist = down(x1,y1,x2,y2)
            d["D_dist"] = D_dist

            RDx,RDy,RD_dist = rightDown(x1,y1,x2,y2)
            d["RD_dist"] = RD_dist

            Rx,Ry,R_dist = right(x1,y1,x2,y2)
            d["R_dist"] = R_dist

            min_dir = min(d,key=d.get)
            if min_dir == "L_dist":
                directions.append("L")
                x1,y1 = Lx,Ly
                count += 1
            if min_dir == "LD_dist":
                directions.append("LD")
                x1,y1 = LDx,LDy
                count += 1
            if min_dir == "D_dist":
                directions.append("D")
                x1,y1 = Dx,Dy
                count += 1
            if min_dir == "RD_dist":
                directions.append("RD")
                x1,y1 = RDx,RDy
                count += 1
            if min_dir == "R_dist":
                directions.append("R")
                x1,y1 = Rx,Ry
                count += 1
        elif x1 == 1 and y1 == 8:#top left corner
            d = defaultdict()
            Rx,Ry,R_dist = right(x1,y1,x2,y2)
            d["R_dist"] = R_dist

            RDx,RDy,RD_dist = rightDown(x1,y1,x2,y2)
            d["RD_dist"] = RD_dist

            Dx,Dy,D_dist = down(x1,y1,x2,y2)
            d["D_dist"] = D_dist

            min_dir = min(d,key=d.get)
            if min_dir == "R_dist":
                directions.append("R")
                x1,y1 = Rx,Ry
                count += 1
            if min_dir == "RD_dist":
                directions.append("RD")
                x1,y1 = RDx,RDy
                count += 1
            if min_dir == "D_dist":
                directions.append("D")
                x1,y1 = Dx,Dy
                count += 1
        elif x1 == 8 and y1 == 8:#top right corner
            d = defaultdict()
            Lx,Ly,L_dist = left(x1,y1,x2,y2)
            d["L_dist"] = L_dist

            LDx,LDy,LD_dist = leftDown(x1,y1,x2,y2)
            d["LD_dist"] = LD_dist

            Dx,Dy,D_dist = down(x1,y1,x2,y2)
            d["D_dist"] = D_dist

            min_dir = min(d,key=d.get)
            if min_dir == "L_dist":
                directions.append("L")
                x1,y1 = Lx,Ly
                count += 1
            if min_dir == "LD_dist":
                directions.append("LD")
                x1,y1 = LDx,LDy
                count += 1
            if min_dir == "D_dist":
                directions.append("D")
                x1,y1 = Dx,Dy
                count += 1
        elif x1 == 8 and y1 == 1:#bottom right corner
            d = defaultdict()
            Ux,Uy,U_dist = up(x1,y1,x2,y2)
            d["U_dist"] = U_dist

            LUx,LUy,LU_dist = leftUp(x1,y1,x2,y2)
            d["LU_dist"] = LU_dist

            Lx,Ly,L_dist = left(x1,y1,x2,y2)
            d["L_dist"] = L_dist

            min_dir = min(d,key=d.get)
            if min_dir == "U_dist":
                directions.append("U")
                x1,y1 = Ux,Uy
                count += 1
            if min_dir == "LU_dist":
                directions.append("LU")
                x1,y1 = LUx,LUy
                count += 1
            if min_dir == "L_dist":
                directions.append("L")
                x1,y1 = Lx,Ly
                count += 1
        elif x1 == 1 and y1 == 1:#bottom left corner
            d = defaultdict()
            Ux,Uy,U_dist = up(x1,y1,x2,y2)
            d["U_dist"] = U_dist

            RUx,RUy,RU_dist = rightUp(x1,y1,x2,y2)
            d["RU_dist"] = RU_dist

            Rx,Ry,R_dist = right(x1,y1,x2,y2)
            d["R_dist"] = R_dist

            min_dir = min(d,key=d.get)
            if min_dir == "U_dist":
                directions.append("U")
                x1,y1 = Ux,Uy
                count += 1
            if min_dir == "RU_dist":
                directions.append("RU")
                x1,y1 = RUx,RUy
                count += 1
            if min_dir == "R_dist":
                directions.append("R")
                x1,y1 = Rx,Ry
                count += 1
        else:
            d = defaultdict()
            LUx,LUy,LU_dist = leftUp(x1,y1,x2,y2)
            d["LU_dist"] = LU_dist

            Ux,Uy,U_dist = up(x1,y1,x2,y2)
            d["U_dist"] = U_dist

            RUx,RUy,RU_dist = rightUp(x1,y1,x2,y2)
            d["RU_dist"] = RU_dist

            Rx,Ry,R_dist = right(x1,y1,x2,y2)
            d["R_dist"] = R_dist

            RDx,RDy,RD_dist = rightDown(x1,y1,x2,y2)
            d["RD_dist"] = RD_dist

            Dx,Dy,D_dist = down(x1,y1,x2,y2)
            d["D_dist"] = D_dist

            LDx,LDy,LD_dist = leftDown(x1,y1,x2,y2)
            d["LD_dist"] = LD_dist

            Lx,Ly,L_dist = left(x1,y1,x2,y2)
            d["L_dist"] = L_dist

            min_dir = min(d,key=d.get)
            if min_dir == "LU_dist":
                directions.append("LU")
                x1,y1 = LUx,LUy
                count += 1
            if min_dir == "U_dist":
                directions.append("U")
                x1,y1 = Ux,Uy
                count += 1
            if min_dir == "RU_dist":
                directions.append("RU")
                x1,y1 = RUx,RUy
                count += 1
            if min_dir == "R_dist":
                directions.append("R")
                x1,y1 = Rx,Ry
                count += 1
            if min_dir == "RD_dist":
                directions.append("RD")
                x1,y1 = RDx,RDy
                count += 1
            if min_dir == "D_dist":
                directions.append("D")
                x1,y1 = Dx,Dy
                count += 1
            if min_dir == "LD_dist":
                directions.append("LD")
                x1,y1 = LDx,LDy
                count += 1
            if min_dir == "L_dist":
                directions.append("L")
                x1,y1 = Lx,Ly
                count += 1
        if x1 == x2 and y1 == y2:
            break
    print count
    for i in directions:
        print i
else:
    print "0"



            










