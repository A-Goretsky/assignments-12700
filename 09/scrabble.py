TRIPLE_WORD_SCORE = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
DOUBLE_WORD_SCORE = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10), (7,7))
TRIPLE_LETTER_SCORE = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
DOUBLE_LETTER_SCORE = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))

def make_scrabble_board():
    board=[]
    for i in range(15):
        line=[]
        for i in range(15):
            line.append('_')
        board.append(line)

    for r,c in TRIPLE_WORD_SCORE:
        board[r][c] = 'T'

    for r,c in DOUBLE_WORD_SCORE:
        board[r][c] = 'D'

    for r,c in TRIPLE_LETTER_SCORE:
        board[r][c]='t'

    for r,c in DOUBLE_LETTER_SCORE:
        board[r][c] = 'd'
    return board


def print_board(b):
    for line in b:
        print ( ' '.join(line))

def add_word_across(board, word, r, c):
    ans = 0
    word_mult = 1
    letter_mult = []
    ctr = 0
    for x in word:
        if board[r][c] == 'T':
            word_mult = word_mult * 3
            letter_mult.append(1)
        elif board[r][c] == 'D':
            word_mult = word_mult * 2
            letter_mult.append(1)
        elif board[r][c] == 't':
            letter_mult.append( 3 )
        elif board[r][c] == 'd':
            letter_mult.append( 2 )
        else:
            letter_mult.append(1)
        board[r][c + ctr] = x
        ctr += 1
    ans = score(word, word_mult, letter_mult)
    print(ans)
    print_board(board)
    return ans

def add_word_down(board, word, r, c):
    ans = 0
    word_mult = 1
    letter_mult = []
    ctr = 0
    for x in word:
        if board[r][c] == 'T':
            word_mult = word_mult * 3
            letter_mult.append(1)
        elif board[r][c] == 'D':
            word_mult = word_mult * 2
            letter_mult.append(1)
        elif board[r][c] == 't':
            letter_mult.append( 3 )
        elif board[r][c] == 'd':
            letter_mult.append( 2 )
        else:
            letter_mult.append(1)
        board[r+ctr][c] = x
        ctr += 1
    ans = score(word, word_mult, letter_mult)
    print_board(board)
    return ans

def score(w, w_mult, l_mult):
    res = 0
    temp = 0
    dict = {
    1:['A', 'E', 'I', 'O', 'L', 'N', 'R', 'S', 'T'],
    2:['D', 'G'],
    3:['B', 'C', 'M', 'P'],
    4:['F', 'H', 'V', 'W', 'Y'],
    5:['K'],
    8:['J', 'X'],
    10:['Q','Z']}
    for key, value in dict.items():
        w = w.upper()
        ctr = 0
        for x in w:
            if x in value:
                temp += key
                res = temp * l_mult[ctr]
                ctr+=1
    res = res * w_mult
    print(res)
    return res

board = make_scrabble_board()
print_board(board)
add_word_across(board, 'hello', 1, 1)
add_word_across(board, 'ox', 0, 0)
add_word_down(board, 'ox', 0, 7)
