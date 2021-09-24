import random
# the computer picks a number and u guess it 
def guess(max): 
    random_nb = random.randint(1, max)
    guess = 0
    while guess != random_nb:
        guess = int(input(f"guess a number between 1 and {max} : ")) 
        if guess < random_nb:
            print("sorry , guess again . Too low ")
        elif guess > random_nb :
            print("sorry , guess again . Too high ")
        
        
    (print(f"concratulation ,you have guess the number {random_nb} correctly "))

#guess(10)

def computer_guess(x):
    low = 1 
    high = x
    feedback = ""
    while feedback != 'c' :
        if low != high :
            guess = random.randint(low, high)
        else :
            guess = high 
        feedback = input(f"is our {guess} too high (h), too low (l) or correct (c) ?? ").lower()
        if feedback == 'h' : 
            high = guess -1 
        elif feedback == 'l' :
            low = guess + 1

    print(f"yay i the computer guessed the number {guess} correctly ")
print("guess a number and the computer will try to find it ")
try:
    x = int(input("enter your number : "))
except Exception as erreur:
    print(erreur)
    quit()
computer_guess(x)




