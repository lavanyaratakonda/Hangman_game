import tkinter as tk
from tkinter import messagebox
import random
import word_file
import hangman_stages

class HangmanGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.master.geometry("500x500")
        
        self.lives = 6
        self.chosen_word = random.choice(word_file.words)
        self.display = ['_' for _ in self.chosen_word]

        # GUI Components
        self.label_word = tk.Label(master, text=' '.join(self.display), font=("Helvetica", 24))
        self.label_word.pack(pady=20)

        self.label_stage = tk.Label(master, text=hangman_stages.stages[self.lives], font=("Courier", 12))
        self.label_stage.pack(pady=20)

        self.entry = tk.Entry(master, font=("Helvetica", 18), width=5, justify='center')
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess, font=("Helvetica", 14))
        self.guess_button.pack(pady=10)

        self.reset_button = tk.Button(master, text="Reset Game", command=self.reset_game)
        self.reset_button.pack(pady=5)

    def check_guess(self):
        guessed_letter = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if not guessed_letter or len(guessed_letter) != 1 or not guessed_letter.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")
            return

        if guessed_letter in self.display:
            messagebox.showinfo("Already Guessed", f"You already guessed '{guessed_letter}'")
            return

        if guessed_letter in self.chosen_word:
            for idx, letter in enumerate(self.chosen_word):
                if letter == guessed_letter:
                    self.display[idx] = guessed_letter
        else:
            self.lives -= 1

        self.label_word.config(text=' '.join(self.display))
        self.label_stage.config(text=hangman_stages.stages[self.lives])

        # Win condition
        if '_' not in self.display:
            messagebox.showinfo("Congratulations!", f"You won! The word was '{self.chosen_word}'")
            self.disable_game()

        # Lose condition
        elif self.lives == 0:
            messagebox.showerror("Game Over", f"You lost! The word was '{self.chosen_word}'")
            self.disable_game()

    def disable_game(self):
        self.guess_button.config(state=tk.DISABLED)
        self.entry.config(state=tk.DISABLED)

    def reset_game(self):
        self.lives = 6
        self.chosen_word = random.choice(word_file.words)
        self.display = ['_' for _ in self.chosen_word]
        self.label_word.config(text=' '.join(self.display))
        self.label_stage.config(text=hangman_stages.stages[self.lives])
        self.guess_button.config(state=tk.NORMAL)
        self.entry.config(state=tk.NORMAL)

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanGUI(root)
    root.mainloop()
