import tkinter as tk
from Final_2_gui import HangmanGui  # this imports the Hangman_Gui class

def load_words(file_path):        # this will load the words into the txt file
    try:
        with open(file_path, 'r') as file:
            # this will read all the lines, strips the extra spaces, and keep only non-empty lines
            words = [line.strip() for line in file.readlines() if line.strip()]
        return words
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")  # this will give the specific file name
        return []

if __name__ == '__main__':
    # this will load the words from the file
    words = load_words('words.txt')

    # this will check if the list is empty (no words)
    if not words:
        print("Word list is empty. Exiting the program.")
        exit()  # this is to exit the program if there aren't andy words loaded

    # this is to start the Hangman game GUI with the loaded words
    app = HangmanGui(words)
    app.mainloop()  # this will start the  loop to show the GUI page