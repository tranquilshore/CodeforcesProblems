board = []
try:
    while True:
        r = raw_input()
        if r != "":
            board.append(r)
        else:
            break
except EOFError:
    pass

def check(board):
    count_x = 0
    count_0 = 0
    count_dot = 0

    for i in range(3):
        for j in board[i]:
            if j == 'X':
                count_x += 1
            if j == '0':
                count_0 += 1
            if j == '.':
                count_dot += 1

    if abs(count_x-count_0) >= 2:
        return "illegal"
    if count_0 > count_x:
        return "illegal"

    v_board = [[None]*3 for i in range(3)]
    d_board= [[]*3 for i in range(2)]
    h_board = [list(s) for s in board]
    for i in range(3):
        for j in range(3):
            v_board[i][j] = h_board[j][i]
            if i == j:
                d_board[0].append(h_board[i][j])
    for i,j in zip(range(3),range(2,-1,-1)):
        d_board[1].append(h_board[i][j])

    #either 0 wins or X's turn
    if count_x == count_0:
        for i,j in zip(h_board,v_board):
            if len(set(i)) == 1:
                if next(iter(set(i))) == 'X':
                    return "illegal"
            if len(set(j)) == 1:
                if next(iter(set(j))) == 'X':
                    return "illegal"
        for k in d_board:
            if len(set(k)) == 1:
                if next(iter(set(k))) == 'X':
                    return "illegal"
        
        for i,j in zip(h_board,v_board):
            if len(set(i)) == 1:
                if next(iter(set(i))) == '0':
                    return "the second player won"
            if len(set(j)) == 1:
                if next(iter(set(j))) == '0':
                    return "the second player won"
        for k in d_board:
            if len(set(k)) == 1:
                if next(iter(set(k))) == '0':
                    return "the second player won"
        return "first"
        
    if count_x == count_0+1:
        for i,j in zip(h_board,v_board):
            if len(set(i)) == 1:
                if next(iter(set(i))) == '0':
                    return "illegal"
            if len(set(j)) == 1:
                if next(iter(set(j))) == '0':
                    return "illegal"
        for k in d_board:
            if len(set(k)) == 1:
                if next(iter(set(k))) == '0':
                    return "illegal"
        
        for i,j in zip(h_board,v_board):
            if len(set(i)) == 1:
                if next(iter(set(i))) == 'X':
                    return "the first player won"
            if len(set(j)) == 1:
                if next(iter(set(j))) == 'X':
                    return "the first player won"
        for k in d_board:
            if len(set(k)) == 1:
                if next(iter(set(k))) == 'X':
                    return "the first player won"
        if count_dot > 0:
            return "second"
        else:
            return "draw"
        
print check(board)         

        