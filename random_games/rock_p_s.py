import random 
def play():
    user = input(" type 'r' for rock , 'p' for paper and 's' for scissors\n")
    computer = random.choice(['r','p','s'])
    if user == computer :
        return print("it\' a tie")
    # r > s , s > p , p > r
    if win(user, computer):
        return print("you won !")

    return print("you lost ha :p ")


def win(player, opponent):
    # we return true if player wins 
    # r > s , s > p , p > r
    if (player == 'r' and opponent == 's ') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True 


print("we are going to play rock paper scissors for some fun :) ")
print("what's your choice ? ")
play()