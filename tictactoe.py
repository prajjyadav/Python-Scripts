def displayBoard(board):
    print(*board[:3])
    print(*board[3:6])
    print(*board[6:])
    print()


def checkWin(b, m):
    return ((b[0] == m and b[1] == m and b[2] == m) or
            (b[3] == m and b[4] == m and b[5] == m) or
            (b[6] == m and b[7] == m and b[8] == m) or
            (b[0] == m and b[3] == m and b[6] == m) or
            (b[1] == m and b[4] == m and b[7] == m) or
            (b[2] == m and b[5] == m and b[8] == m) or
            (b[0] == m and b[4] == m and b[8] == m) or
            (b[2] == m and b[4] == m and b[6] == m))


def evaluate(board):
    pwin = checkWin(board, '0')
    owin = checkWin(board, 'X')
    if (pwin):
        return 10
    elif (owin):
        return -10

    return 0


def checkDraw(board):
    return '·' not in board


def minmax(board, depth, isMax):
    avaibleSquares = [i for i in range(9) if board[i] == '·']

    score = evaluate(board)

    if (score != 0):
        return score / depth
    if (len(avaibleSquares) == 0):
        return 0

    best = float('-inf') if isMax else float('inf')
    for i in avaibleSquares:
        board[i] = '0' if isMax else 'X'
        if isMax:
            best = max(best, minmax(board, depth + 1, not isMax))
        else:
            best = min(best, minmax(board, depth + 1, not isMax))
        board[i] = '·'

    return best


def getComputerMove(board):
    avaibleSquares = [i for i in range(9) if board[i] == '·']

    bestVal = float('-inf')
    bestMove = -1

    for i in avaibleSquares:
        board[i] = '0'
        moveVal = minmax(board, 1, False)
        board[i] = '·'
        if moveVal > bestVal:
            bestMove = i
            bestVal = moveVal

    return bestMove


finished = False
board = ['·'] * 9

turn = '0'

displayBoard(board)


while not finished:

    if turn == '0':
        print('Player go: (0-8)')
        move = int(input())
        if board[move] != '·':
            print('Invalid move!')
            continue
    else:
        move = getComputerMove(board)

    board[move] = turn

    if checkWin(board, turn):
        finished = True
        displayBoard(board)
        if turn == '0':
            print('Noughts won!')
        else:
            print('Crosses won!')
        continue

    if checkDraw(board):
        finished = True
        displayBoard(board)
        print('It was a draw!')
        continue
    displayBoard(board)
    if turn == '0':
        turn = 'X'
    else:
        turn = '0'

