from words import words
import random as r
import string
def choose_word():
    word = r.choice(words)
    while "-" in word or " " in word:
        word = r.choice(words)
    return word.upper()
def check(word):
    check_list = []
    for i in word:
        if i in used_letters:
            check_list.append(i)
        else:
            check_list.append('-')
    return ' '.join(check_list)
name = input("Please enter your name: ").upper()
print('*'*25)
guess_word = str()
chance = 10
used_letters = str()
word = choose_word()
size = len(word)
print(f"Hello {name}.Welcome to the Hangman Game.\nYou have {chance} chance.")
print(f"The word has {size} letters.")
# print(word)
while True:
    user_letter = input("Guess a letter: ").upper()
    chance -= 1
    if len(user_letter) > 1:
        print("Please enter only one letter!")
    else:
        if chance == 0:
            print("Your chance is over.")
            print("The word was {}".format(word))
            break
        else:
            if user_letter in word:
                used_letters += user_letter + " "
                value = str(word).count(user_letter)
                print(f"There are {value} {user_letter} in the word.\n\
You have used these letters: {used_letters}")
                guess_word += user_letter*value
                print(check(word))
                if set(guess_word) == set(word):
                    print(" WINNER ".center(30,'!'))
                    break
            else:
                used_letters += user_letter + " "
                print(f"You have used these letters: {used_letters}")
                print(f"{user_letter} is not used in the word")
                print(check(word))
    print('-'*30)
