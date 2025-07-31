import tkinter as tk
from tkinter import messagebox
import math

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe AI (Unbeatable)")
        self.buttons = [tk.Button(root, text=" ", font=("Arial", 32), width=5, height=2, command=lambda i=i: self.human_move(i)) for i in range(9)]
        self.board = [' ' for _ in range(9)]
        self.create_board()

    def create_board(self):
        for i, btn in enumerate(self.buttons):
            row, col = divmod(i, 3)
            btn.grid(row=row, column=col)

    def human_move(self, index):
        if self.board[index] == ' ':
            self.board[index] = 'X'
            self.buttons[index].config(text='X', state='disabled')
            if self.check_winner('X'):
                self.end_game("You win! 🎉")
                return
            if self.is_draw():
                self.end_game("It's a draw!")
                return
            self.root.after(500, self.ai_move)

    def ai_move(self):
        best_score = -math.inf
        best_move = -1
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'O'
                score = self.minimax(False)
                self.board[i] = ' '
                if score > best_score:
                    best_score = score
                    best_move = i

        self.board[best_move] = 'O'
        self.buttons[best_move].config(text='O', state='disabled')
        if self.check_winner('O'):
            self.end_game("AI wins! 🤖")
        elif self.is_draw():
            self.end_game("It's a draw!")

    def minimax(self, is_maximizing):
        if self.check_winner('O'):
            return 1
        if self.check_winner('X'):
            return -1
        if self.is_draw():
            return 0

        if is_maximizing:
            best_score = -math.inf
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'O'
                    score = self.minimax(False)
                    self.board[i] = ' '
                    best_score = max(best_score, score)
            return best_score
        else:
            best_score = math.inf
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'X'
                    score = self.minimax(True)
                    self.board[i] = ' '
                    best_score = min(best_score, score)
            return best_score

    def check_winner(self, player):
        win_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        return any(all(self.board[i] == player for i in combo) for combo in win_combos)

    def is_draw(self):
        return ' ' not in self.board

    def end_game(self, message):
        for btn in self.buttons:
            btn.config(state='disabled')
        messagebox.showinfo("Game Over", message)

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
