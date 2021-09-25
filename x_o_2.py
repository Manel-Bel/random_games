from random import randint as ri
from timeit import default_timer as timer

tableau = [ ' ' for x in range(10)]

# le dessin du tableau
def affiche_tableau(board):
    print('  '+board[1]+'  '+'|  '+board[2]+'  '+'|  '+board[3]+'  ')
    print('-----------------')
    print('  '+board[4]+'  '+'|  '+board[5]+'  '+'|  '+board[6]+'  ')
    print('-----------------')
    print('  '+board[7]+'  '+'|  '+board[8]+'  '+'|  '+board[9]+'  ')
    print("\n")
def mark_positon(board, pos, l):
    board[pos] = l

def winner(board,le):
    if board[1] == board[2] == board[3] == le \
    or board[1] == board[4] == board[7] == le \
    or board[1] == board[5] == board[9] == le \
    or board[2] == board[5] == board[8] == le \
    or board[3] == board[6] == board[9] == le \
    or board[5] == board[4] == board[7] == le \
    or board[4] == board[5] == board[6] == le \
    or board[7] == board[8] == board[9] == le :
        if le == 'x':
            print('yaaay ! you win ,omedetoo ')
        else :
            print(' YOU LOST ! ')
        quit()

def computer_move(board):
    move = ri(0, 9)
    while board[move] != ' ' :
        move = ri(0, 9)
    return move

def board_full(board):
    for x in board:
        if x == ' ' :
            return False
    return True

def board_full_2(board):
    if board.count(' ') > 1 :
        return False
    return True
#this one is less effecient

def player_move(board):
    move = int(input("enter the possiton u want to mark\n"))
    while move <= 0 or move >= 10 or board[move] != ' ' :
        print('please select another posti')
        move = int(input())
    return move


def main(board):
    print('we are going to play tic tac toe\n here is the board')
    affiche_tableau(board)
    while not board_full(board):
        mark_positon(board, player_move(board), 'x')
        affiche_tableau(board)
        winner(board, 'x')
        mark_positon(board, computer_move(board), 'o')
        print("this is the computer move\n")
        affiche_tableau(board)
        winner(board, 'o')
    print("it's a tie!")

main(tableau)
