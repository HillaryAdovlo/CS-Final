# the part that are for the start page, the actual game page and the end page I had help from AI putting it together. I asked it ' how do I put together multiple pages in gui for a game in tkinter '.

import tkinter as tk
from tkinter import messagebox
from Final_2_logic import HangmanGame

class HangmanGui(tk.Tk):
    def __init__(self, word_list):
        super().__init__()
        self.title("Hangman Game")
        self.word_list = word_list
        self.geometry("550x350")
        self.resizable(False, False)
    # this is to take care of th gui interface

        self.frames = {}
        for F in (StartPage, GamePage, EndPage):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)
    # for the self.frame section above, I had the help of AI to write it.

    def show_frame(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()
        if page_class == GamePage:
            frame.start_game()
        if page_class == EndPage:
            frame.update_result()

class StartPage(tk.Frame):

    def __init__(self, controller):
        super().__init__(controller)
        self.controller = controller
        label = tk.Label(self, text="Hangman!", font=("American Typewriter", 64))
        label.pack(pady=20)
        label = tk.Label(self, text="Click play to start", font=("American Typewriter",24 ))
        label.pack(pady=20)
        start_button = tk.Button(self, text="Play", font=("American Typewriter", 48),
                                 command=lambda: controller.show_frame(GamePage))
        start_button.pack(pady=10)

class GamePage(tk.Frame):             # this is for the actual page that the hangman is going to be happening on

    def __init__(self, controller):
        super().__init__(controller)
        self.controller = controller

        self.game = None

        self.label = tk.Label(self, text="Guess The word!", font=("Aril", 16))
        self.label.pack(pady=10)

        self.word_display = tk.Label(self, font=("Aril", 24))
        self.word_display.pack(pady=10)

        self.entry = tk.Entry(self, font=("Aril", 16))
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(self, text="Guess", font=("Aril", 14), command=self.make_guess)
        self.guess_button.pack(pady=5)

        self.chances_label = tk.Label(self, font=("Aril", 14))
        self.chances_label.pack(pady=5)

    def start_game(self):

        self.game = HangmanGame(self.controller.word_list)
        self.word_display.config(text=self.game.get_display_word())
        self.chances_label.config(text=f"Chances left: {self.game.chances}")
        self.entry.delete(0, tk.END)


    def make_guess(self):
        guess = self.entry.get().strip().lower()
        self.entry.delete(0, tk.END)
        result = self.game.guess_letter(guess)
        self.word_display.config(text=self.game.get_display_word())
        self.chances_label.config(text=f"Chances left: {self.game.chances}")

        if self.game.is_game_over():
            self.controller.frames[EndPage].set_result(result)
            self.controller.show_frame(EndPage)
        else:
            messagebox.showinfo("Result", result)


class EndPage(tk.Frame):      #this is the final page that shows if the person won or lost and asks the player if they want to play again

    def __init__(self, controller):
        super().__init__(controller)

        self.controller = controller
        self.result_label = tk.Label(self, text="", font=("Helvetica", 16))
        self.result_label.pack(pady=20)

        # this makes a Play Again button that goes back to the game screen
        play_again_button = tk.Button(self, text="Play Again", command=lambda: controller.show_frame(GamePage))
        play_again_button.pack(pady=10)

        exit_button = tk.Button(self, text="Exit", command=self.controller.destroy)
        exit_button.pack(pady=10)

    def set_result(self, result: str):
        """Update the result label with the result of the game."""
        self.result_label.config(text=result)


    def show_result_message(self, message: str):
        self.result_label.config(text=message)

    def update_result(self):
        pass  # this is to update the that shows up when the person looses

