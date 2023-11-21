import random

word_list = ['Apple', 'Mango', 'Strawberry', 'Banana', 'Grapes']
word = random.choice(word_list)

guess = input('Enter a single letter: ')

if (len(guess)==1 and guess.isalpha()):
    print('Good guess!')
else:
    print('Oops! that is not valid input.')

print(word)