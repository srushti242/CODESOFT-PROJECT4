import tkinter as tk
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("500x600")

        # Label for displaying game result
        self.result_var = tk.StringVar()
        self.result_label = tk.Label(root, textvariable=self.result_var, font=("Arial", 30))
        self.result_label.pack(pady=10)

        # Radio buttons for user's choice
        self.user_choice_var = tk.StringVar()
        self.user_choice_var.set("rock")  # Default choice
        self.rock_radio = tk.Radiobutton(root, text="Rock",font=16, variable=self.user_choice_var, value="rock")
        self.rock_radio.pack(anchor=tk.W)
        self.rock_radio.place(x=200, y=53)
        self.rock_radio.pack(pady=10)


        self.paper_radio = tk.Radiobutton(root, text="Paper",font=16, variable=self.user_choice_var, value="paper")
        self.paper_radio.pack(anchor=tk.W)
        self.paper_radio.place(x=200, y=53)
        self.paper_radio.pack(pady=10)

        self.scissors_radio = tk.Radiobutton(root, text="Scissors",font=16, variable=self.user_choice_var, value="scissors")
        self.scissors_radio.pack(anchor=tk.W)
        self.scissors_radio.place(x=200, y=53)
        self.scissors_radio.pack(pady=10)


        # Button to play the game
        self.play_button = tk.Button(root, text="Play",font=16, command=self.play)
        self.play_button.pack(pady=10)

        # Label for displaying computer's choice
        self.computer_choice_var = tk.StringVar()
        self.computer_choice_label = tk.Label(root, textvariable=self.computer_choice_var, font=("Arial", 20))
        self.computer_choice_label.pack(pady=5)

    def play(self):
        # Get user's choice
        user_choice = self.user_choice_var.get()

        # Generate computer's choice
        computer_choice = random.choice(["rock", "paper", "scissors"])

        # Display computer's choice
        self.computer_choice_var.set(f"Computer's choice: {computer_choice.capitalize()}")

        # Determine the winner
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            result = "You win!"
        else:
            result = "Computer wins!"

        # Display the result
        self.result_var.set(result)

def main():
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
