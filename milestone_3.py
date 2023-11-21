import random

word_list = ['Apple', 'Mango', 'Strawberry', 'Banana', 'Grapes']
word = random.choice(word_list)
print(word)

def check_guess(guess):
    guess.lower()
    if (guess in word):
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')
    print(guess)

def ask_for_input():
    guess = input('Enter a single letter: ')

    if (len(guess)==1 and guess.isalpha()):
        print('Good guess!')
    else:
        print('Invalid letter. Please, enter a single alphabetical character.')
    check_guess(guess)

while True:
    ask_for_input()