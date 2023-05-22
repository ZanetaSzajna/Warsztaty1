# stworzneie tablicy
board=[" "  for x in range(10)]
print(board)

# drukowanie tabeli
def print_board(bord):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
print_board(board)

# funkcja wskazująca wygrana
def winner(board, symbol):
    #board - miejsce w tablicy
    #symbol - kółko/ lub krzyżyk w tym miejscu

    return (board[7] == symbol and board[8] == symbol and board[9] == symbol) or (
            board[4] == symbol and board[5] == symbol and board[6] == symbol) or (
            board[1] == symbol and board[2] == symbol and board[3] == symbol) or (
            board[1] == symbol and board[4] == symbol and board[7] == symbol) or (
            board[2] == symbol and board[5] == symbol and board[8] == symbol) or (
            board[3] == symbol and board[6] == symbol and board[9] == symbol) or (
            board[1] == symbol and board[5] == symbol and board[9] == symbol) or (
            board[3] == symbol and board[5] == symbol and board[7] == symbol)

# funkcja wpisująca w pozycje nasz symbol
def insert_symbol(symbol, pos):
    board[pos] = symbol

# funkcja sprawdzająca czy pole jest wolne:

def space_free(pos):
    return board[pos] == ' '

# sprawdzenie czy  tablica jest pełna

def board_full (board):
    if board.count(' ') > 1:
        return False
    else:
        return True
#losowanie pozycji przez komputer
def select_comp(sym):
    import random
    lenght = len(sym)
    r = random.randrange(0, lenght)
    return sym[r]

def player_move():

    # zakładamy prawdę
    run = True
    while run:

        move = input('Please select a position to place an \'O\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if space_free(move):
                    run = False
                    insert_symbol('O', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')
def computer_move():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if winner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = select_comp(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = select_comp(edgesOpen)

    return move

#funkcja główna

def main():
    print('Welcome to Tic Tac Toe!')
    print_board(board)

    while not (board_full(board)):
        if not (winner(board, 'X')):
            player_move()
            print_board(board)
        else:
            print('Sorry, X\'s won this time!')
            break

        if not (winner(board, 'O')):
            move = computer_move()
            if move == 0:
                print('Draw!')
            else:
                insert_symbol('X', move)
                print('Computer placed an \'X\' in position', move, ':')
                print_board(board)
        else:
            print('O\'s won this time! Good Job!')
            break

    if board_full(board):
        print('Draw!')

main()

while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        print("Bye Bye")
        break