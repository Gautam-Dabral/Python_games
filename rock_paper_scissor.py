import random
from playsound import playsound

def iswin (u, c):
    if (u == 'r' and c == 's') or (u == 'p' and c == 'r') or (u == 's' and c == 'p'):
        return 'u'
    return 'c'

def play():
    user = input('r for rock, p for paper, s for scissors\n')
    computer = random.choice(['r','p','s'])
    print('Computer Chose -', computer)

    if user==computer:
        print( "---It's a Draw---" )
        playsound('sounds\\pipe_sad.mp3')
    elif iswin (user, computer) == 'u':
        print('---You Win!!---')
        playsound('D:\\VSCode\\Projects\\Kylie_ying\\sounds\\yeah_boi.mp3')
    else:
        print('---Computer Wins!!---')
        playsound('D:\\VSCode\\Projects\\Kylie_ying\\sounds\\stab_wasted.mp3')

play()
