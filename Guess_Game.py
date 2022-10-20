import random
from playsound import playsound
# Generates a random number and makes the user guess

def guess (x):
    high,low=x,1
    random_no = random.randint(low, high)

    guess = int(input(f'\nEnter a number between 1 and {x} : '))
    
    while guess != random_no:
        if guess > random_no:
            playsound('D:\\Python_VSCode\\sounds\\thats_the_wrong_no.mp3')
            print("\nSike!!!, That's the wrong number (guess lower) : ")
            guess=int(input())
        elif guess < random_no:
            playsound('D:\\Python_VSCode\\sounds\\thats_the_wrong_no.mp3')
            print("\nSike!!!, That's the wrong number (guess Higher) : ")
            guess=int(input())
    
    if guess==random_no:
        print(f'\n YAYYY!!! {guess} is right, You guessed correctly !!\n')
        print("\n****************** G A M E  O V E R ******************\n\n\n")
        playsound('D:\\Python_VSCode\\sounds\\never_gonna_give_you_up.mp3')

def main():
    print('\n****************** G U E S S  G A M E ******************\n\n\n')
    
    x=int(input('Enter the higher range for the guess game : '))

    guess(x)

main()

