import random
from collections import Counter

class HangmanGame:
    # the class is to handle the hangman game logic

    def __init__(self, word_list):
        # Selects a random word from the list of words in words.txt
        self.word = random.choice(word_list)
        self.letter_guessed = ''
        # Set the number of chances the player has (2 extra than the length of the word)
        self.chances = len(self.word) + 2

        # this is to check if the game is over
        self.game_over = False

    def guess_letter(self, guess: str) -> str:
        if not guess.isalpha() or len(guess) != 1:
            return "Invalid input. Please enter a single letter."
    # this is to check and make sure the person playing input a letter

        if guess in self.letter_guessed:
            return f"You already guessed '{guess}'."
    # this will check is they've already guessed the letter

        if guess in self.word:
            # Add the guessed letter to the list of guessed letters
            # (even if the letter appears more than once in the word)
            for letter in self.word:
                if letter == guess:
                    self.letter_guessed += guess
        # this checks if the letter guessed is in the word they are trying to guess

        all_guessed = True
        for letter in self.word:
            if letter not in self.letter_guessed:
                all_guessed = False
                break

        if all_guessed:
            self.game_over = True
            return f"🎉 Congratulations 🎉! You guessed the word: {self.word}"
    # this checks if all the letters in the word has been guessed correctly

        self.chances = self.chances - 1
        if self.chances == 0:
            self.game_over = True
            return f"😿 Game over 😿! The word was: {self.word}"
     # this will take away a chance for every letter guessed wrong till it runs out, and then it will check if the player ran out of chances and if they did, this will turn the game _over flag to true and the game will end

        return "✅ Correct ✅!" if guess in self.word else "❌ Wrong guess ❌!"
    # this weill come up depending on if they guessed the right letter or wrong letter

    def get_display_word(self):
        display_word = ''
        for char in self.word:
            if char in self.letter_guessed:
                display_word += char + ' '
            else:
                display_word += '_ '
        return display_word.strip()
    # this whole thing controls the guessing of the letters. if they guess the right letter it will instead of the line and if the letter isn't int the letter it will now change

    def is_game_over(self):
        return self.game_over
    # this check if the game is over and return True or False