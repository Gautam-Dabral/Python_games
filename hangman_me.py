import random
import string
from playsound import playsound
from hangman_visual import lives_visual_dict
from words import words 

# url = 'https://www.randomlists.com/data/words.json'

def get_valid_word(words):
    choosen_word = random.choice(words)
    while '-' in choosen_word or ' ' in choosen_word:
        choosen_word = random.choice(words)
    return choosen_word

def hangman():
    word = get_valid_word(words).upper()

    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    while len(word_letters) > 0 and lives > 0:
        
        print('You have used these letter :', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word ]

        print('The Word is :', ''.join(word_list), end='\n\n')

        inp_letter = input('Enter an alphabet : ').upper()
        if inp_letter in (alphabet - used_letters):
            used_letters.add(inp_letter)
            if inp_letter in word_letters:
                word_letters.remove(inp_letter)
            else: 
                print(lives_visual_dict[lives])
                lives -= 1
        elif inp_letter in used_letters:
            print('You have already used that alphabet. Please try again.')
        else: print('Invalid input. Please try again')
        print('Lives remaining :', lives)

    if lives > 0:
        print(f"Yeaa! you guessed {word} correctly and saved the man!")
        playsound('sounds\\never_gonna.mp3')
    else:
        print("Hanged!! You could'nt save the man!")
        playsound('sounds\stab_wasted.mp3')
    


hangman()