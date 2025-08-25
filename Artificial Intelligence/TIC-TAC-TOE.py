import tkinter as tk
from tkinter import messagebox

# --------- Game Logic ----------
def analyzeboard(board):
    cb = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in range(0,8):
        if(board[cb[i][0]] != 0 and
           board[cb[i][0]] == board[cb[i][1]] and
           board[cb[i][0]] == board[cb[i][2]]):
            return board[cb[i][2]]
    return 0

def minimax(board, player):
    x = analyzeboard(board)
    if x != 0:
        return (x * player)
    pos = -1
    value = -2
    for i in range(9):
        if board[i] == 0:
            board[i] = player
            score = -minimax(board, (player * -1))
            board[i] = 0
            if score > value:
                value = score
                pos = i
    if pos == -1:
        return 0
    return value

def CompTurn(board):
    pos = -1
    value = -2
    for i in range(9):
        if board[i] == 0:
            board[i] = 1
            score = -minimax(board, -1)
            board[i] = 0
            if score > value:
                value = score
                pos = i
    return pos

# --------- GUI Class ----------
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Tic Tac Toe")
        self.root.geometry("400x500")
        self.root.configure(bg="#222831")

        self.board = [0]*9
        self.buttons = []
        self.mode = None  # 1=single, 2=multi
        self.turn = -1    # X always starts (user)

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.root, text="Tic Tac Toe", font=("Arial", 24, "bold"), bg="#222831", fg="#FFD369")
        title.pack(pady=20)

        # Buttons grid
        frame = tk.Frame(self.root, bg="#393E46")
        frame.pack()

        for i in range(9):
            btn = tk.Button(frame, text=" ", font=("Arial", 32, "bold"), width=3, height=1,
                            bg="#EEEEEE", command=lambda i=i: self.make_move(i))
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons.append(btn)

        # Mode selection
        self.mode_label = tk.Label(self.root, text="Choose Mode", font=("Arial", 14), bg="#222831", fg="white")
        self.mode_label.pack(pady=10)

        mode_frame = tk.Frame(self.root, bg="#222831")
        mode_frame.pack()

        tk.Button(mode_frame, text="Single Player", font=("Arial", 12, "bold"),
                  bg="#FFD369", command=lambda: self.set_mode(1)).pack(side="left", padx=10)
        tk.Button(mode_frame, text="Two Players", font=("Arial", 12, "bold"),
                  bg="#00ADB5", fg="white", command=lambda: self.set_mode(2)).pack(side="left", padx=10)

        # Reset button
        self.reset_btn = tk.Button(self.root, text="Restart Game", font=("Arial", 12, "bold"),
                                   bg="#FF2E63", fg="white", command=self.reset_game)
        self.reset_btn.pack(pady=20)

    def set_mode(self, mode):
        self.mode = mode
        if mode == 1:
            messagebox.showinfo("Mode Selected", "Single Player: You are X, Computer is O")
        else:
            messagebox.showinfo("Mode Selected", "Two Players: X starts first")

    def make_move(self, pos):
        if self.board[pos] != 0 or self.mode is None:
            return

        if self.turn == -1:
            self.board[pos] = -1
            self.buttons[pos].config(text="X", fg="#FF2E63")
        else:
            self.board[pos] = 1
            self.buttons[pos].config(text="O", fg="#00ADB5")

        winner = analyzeboard(self.board)
        if winner != 0:
            self.end_game(winner)
            return

        if 0 not in self.board:
            self.end_game(0)
            return

        self.turn *= -1

        # If single player and it's computer's turn
        if self.mode == 1 and self.turn == 1:
            comp_pos = CompTurn(self.board)
            self.make_move(comp_pos)

    def end_game(self, winner):
        if winner == 0:
            messagebox.showinfo("Result", "It's a Draw!")
        elif winner == -1:
            messagebox.showinfo("Result", "X Wins!")
        else:
            messagebox.showinfo("Result", "O Wins!")

        self.reset_game()

    def reset_game(self):
        self.board = [0]*9
        for btn in self.buttons:
            btn.config(text=" ", state="normal")
        self.turn = -1

# --------- Run Game ----------
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()