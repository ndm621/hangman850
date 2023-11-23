import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word = self.word.lower()
        self.word_guessed = [a for a in ('_'*len(self.word)) ]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess.lower()
        if (guess in self.word):
            print(f'Good guess! {guess} is in the word.')

            for idx, letter in enumerate(self.word):
                if (letter == guess):
                    self.word_guessed[idx] = guess
                self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left.')
            

    def ask_for_input(self):
        try:
            while True:
                guess = input('Enter a single letter: ')

                if not(len(guess)==1 or guess.isalpha()):
                    print('Invalid letter. Please, enter a single alphabetical character.')
                elif guess in self.list_of_guesses:
                    print("You already tried that letter")
                else:
                    self.check_guess(guess)
                    self.list_of_guesses.append(guess)
                    print(self.list_of_guesses)
        except (KeyboardInterrupt, SystemExit):
            print(" \nKeyboard Input Terminated")
            

Fruits = Hangman(['Apple', 'Banana', 'Mango', 'Kiwi'], 10)
print(Fruits.word)
Fruits.ask_for_input()