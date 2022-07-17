import random
import string

from hang_tree import hang_tree
from words import words_

print('-- Hangan game --\n')


def get_valid(words):
    word = ' '
    while ' ' in word or '-' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid(words_)
    word_letters = set(word)  # word to letters
    alphabet = set(string.ascii_uppercase)
    used_letter = set()

    life = 6

    while len(word_letters) > 0 and life > 0:
        print(hang_tree[life])
        print(f'\nused : ', ' '.join(used_letter))
        word_list = [letter if letter in used_letter else '_' for letter in word]
        print('word : ', ' '.join(word_list))

        user_letter = input('try a letter > ').upper()
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                life -= 1
                print('🚨🚨🚨 letter is not in word')

        elif user_letter in used_letter:
            print('letter have already been entered!')
        else:
            print('❌❌❌ invalid character!, try again.')

    if life == 0:
        print(f'{hang_tree[0]}\nsorry, you failed 💔🥲\nthe word is ', word)
    else:
        print(f'word : {word}\nyaaay, you won❤️‍🔥💯\nRESPECT ++ ')


hangman()
