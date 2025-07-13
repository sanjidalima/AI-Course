import tkinter as tk
from tkinter import messagebox
import math

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe (You: X | Computer: O)")
        self.root.configure(bg='#f0f0f0')
        self.board = [' ' for _ in range(9)]
        self.buttons = []
        self.player = 'X'
        self.computer = 'O'
        self.create_board()

    def create_board(self):
        frame = tk.Frame(self.root, bg='#f0f0f0', pady=20)
        frame.pack()
        for i in range(9):
            button = tk.Button(frame, text=' ', font=('Helvetica', 24, 'bold'), height=3, width=6,
                               bg='#dcdcdc', fg='black',
                               command=lambda i=i: self.on_click(i))
            button.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons.append(button)

    def on_click(self, index):
        if self.board[index] == ' ':
            self.make_move(index, self.player)
            self.buttons[index]['bg'] = '#ff9999'  
            if self.check_winner(self.player):
                self.highlight_winner(self.player)
                messagebox.showinfo("Game Over", "🎉 You win!")
                self.reset_board()
                return
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
                return
            self.root.after(500, self.computer_move)

    def make_move(self, index, player):
        self.board[index] = player
        self.buttons[index]['text'] = player
        self.buttons[index]['state'] = 'disabled'
        if player == self.computer:
            self.buttons[index]['bg'] = '#9999ff'  # O এর জন্য নীল

    def is_draw(self):
        return ' ' not in self.board

    def check_winner(self, player):
        self.winning_combo = None
        win_combinations = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]
        for combo in win_combinations:
            if all(self.board[i] == player for i in combo):
                self.winning_combo = combo
                return True
        return False

    def computer_move(self):
        best_score = -math.inf
        best_move = None
        for move in self.available_moves():
            self.board[move] = self.computer
            score = self.minimax(0, False)
            self.board[move] = ' '
            if score > best_score:
                best_score = score
                best_move = move
        self.make_move(best_move, self.computer)
        if self.check_winner(self.computer):
            self.highlight_winner(self.computer)
            messagebox.showinfo("Game Over", "💻 Computer wins!")
            self.reset_board()
        elif self.is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset_board()

    def minimax(self, depth, is_maximizing):
        if self.check_winner(self.computer):
            return 1
        elif self.check_winner(self.player):
            return -1
        elif self.is_draw():
            return 0

        if is_maximizing:
            best_score = -math.inf
            for move in self.available_moves():
                self.board[move] = self.computer
                score = self.minimax(depth + 1, False)
                self.board[move] = ' '
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for move in self.available_moves():
                self.board[move] = self.player
                score = self.minimax(depth + 1, True)
                self.board[move] = ' '
                best_score = min(score, best_score)
            return best_score

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def highlight_winner(self, player):
        if self.winning_combo:
            for i in self.winning_combo:
                self.buttons[i]['bg'] = '#90ee90'  # বিজয়ী চিহ্ন গুলো সবুজ করা হবে
        for btn in self.buttons:
            btn['state'] = 'disabled'

    def reset_board(self):
        self.board = [' ' for _ in range(9)]
        for btn in self.buttons:
            btn.config(text=' ', state='normal', bg='#dcdcdc')

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
