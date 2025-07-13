import time
import random
from copy import deepcopy


pieces = {
    "r": "♜", "n": "♞", "b": "♝", "q": "♛", "k": "♚", "p": "♟",
    "R": "♖", "N": "♘", "B": "♗", "Q": "♕", "K": "♔", "P": "♙",
    ".": "."
}


def init_board():
    return [
        list("rnbqkbnr"),
        list("pppppppp"),
        list("........"),
        list("........"),
        list("........"),
        list("........"),
        list("PPPPPPPP"),
        list("RNBQKBNR")
    ]


def print_board(board):
    print("\n  a b c d e f g h")
    for i in range(8):
        print(8 - i, end=" ")
        for piece in board[i]:
            print(pieces.get(piece, "."), end=" ")
        print(8 - i)
    print("  a b c d e f g h\n")


def parse_position(pos):
    if len(pos) != 2: return None
    col = ord(pos[0]) - ord('a')
    row = 8 - int(pos[1])
    if 0 <= row < 8 and 0 <= col < 8:
        return row, col
    return None


PIECE_VALUES = {
    'p': -1, 'n': -3, 'b': -3, 'r': -5, 'q': -9, 'k': -100,
    'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9, 'K': 100
}


POSITION_BONUS = {
    'P': [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [5, 5, 5, 5, 5, 5, 5, 5],
        [1, 1, 2, 3, 3, 2, 1, 1],
        [0.5,0.5,1,2.5,2.5,1,0.5,0.5],
        [0, 0, 0, 2, 2, 0, 0, 0],
        [0.5,-0.5,-1,0,0,-1,-0.5,0.5],
        [0.5,1,1,-2,-2,1,1,0.5],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
}


def get_piece_moves(board, pos, piece):
    row, col = pos
    moves = []

    if piece.upper() == 'P':
        direction = 1 if piece.islower() else -1
        start_row = 1 if piece.islower() else 6
        if 0 <= row + direction < 8 and board[row + direction][col] == '.':
            moves.append((row + direction, col))
            if row == start_row and board[row + 2*direction][col] == '.':
                moves.append((row + 2*direction, col))
        for dcol in [-1, 1]:
            new_col = col + dcol
            if 0 <= new_col < 8 and 0 <= row + direction < 8:
                target = board[row + direction][new_col]
                if target != '.' and target.isupper() != piece.isupper():
                    moves.append((row + direction, new_col))

    elif piece.upper() == 'R':
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        for dr, dc in directions:
            for i in range(1,8):
                nr, nc = row + dr*i, col + dc*i
                if not (0 <= nr < 8 and 0 <= nc < 8): break
                target = board[nr][nc]
                if target == '.':
                    moves.append((nr, nc))
                elif target.isupper() != piece.isupper():
                    moves.append((nr, nc))
                    break
                else: break

    elif piece.upper() == 'N':
        for dr, dc in [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < 8 and 0 <= nc < 8:
                target = board[nr][nc]
                if target == '.' or target.isupper() != piece.isupper():
                    moves.append((nr, nc))

    elif piece.upper() == 'B':
        directions = [(1,1),(1,-1),(-1,1),(-1,-1)]
        for dr, dc in directions:
            for i in range(1,8):
                nr, nc = row + dr*i, col + dc*i
                if not (0 <= nr < 8 and 0 <= nc < 8): break
                target = board[nr][nc]
                if target == '.':
                    moves.append((nr, nc))
                elif target.isupper() != piece.isupper():
                    moves.append((nr, nc))
                    break
                else: break

    elif piece.upper() == 'Q':
        return get_piece_moves(board, pos, 'R') + get_piece_moves(board, pos, 'B')

    elif piece.upper() == 'K':
        for dr in [-1,0,1]:
            for dc in [-1,0,1]:
                if dr == 0 and dc == 0: continue
                nr, nc = row + dr, col + dc
                if 0 <= nr < 8 and 0 <= nc < 8:
                    target = board[nr][nc]
                    if target == '.' or target.isupper() != piece.isupper():
                        moves.append((nr, nc))
    return moves


def evaluate_board(board):
    score = 0
    for i in range(8):
        for j in range(8):
            piece = board[i][j]
            if piece != '.':
                score += PIECE_VALUES.get(piece, 0)
                if piece.upper() == 'P':
                    if piece.isupper():
                        score += POSITION_BONUS['P'][i][j]
                    else:
                        score -= POSITION_BONUS['P'][7-i][j]
    return score


def minimax(board, depth, alpha, beta, maximizing):
    if depth == 0:
        return evaluate_board(board), None

    best_move = None
    if maximizing:
        max_eval = float('-inf')
        for move in get_all_moves(board, True):
            new_board = make_move(deepcopy(board), move[0], move[1])
            eval_score, _ = minimax(new_board, depth-1, alpha, beta, False)
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move
            alpha = max(alpha, eval_score)
            if beta <= alpha: break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in get_all_moves(board, False):
            new_board = make_move(deepcopy(board), move[0], move[1])
            eval_score, _ = minimax(new_board, depth-1, alpha, beta, True)
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move
            beta = min(beta, eval_score)
            if beta <= alpha: break
        return min_eval, best_move


def get_all_moves(board, is_white):
    moves = []
    for i in range(8):
        for j in range(8):
            piece = board[i][j]
            if piece != '.' and piece.isupper() == is_white:
                for move in get_piece_moves(board, (i, j), piece):
                    moves.append(((i, j), move))
    return moves


def make_move(board, start, end):
    sr, sc = start
    er, ec = end
    board[er][ec] = board[sr][sc]
    board[sr][sc] = '.'
    return board


def is_valid_move(board, start, end, turn):
    sr, sc = start
    er, ec = end
    if not (0 <= sr < 8 and 0 <= sc < 8 and 0 <= er < 8 and 0 <= ec < 8):
        return False
    piece = board[sr][sc]
    if piece == '.' or (turn == "white" and not piece.isupper()) or (turn == "black" and not piece.islower()):
        return False
    valid_moves = get_piece_moves(board, start, piece)
    return end in valid_moves


def get_computer_move(board):
    print("Computer is thinking...")
    start_time = time.time()
    _, move = minimax(board, 3, float('-inf'), float('inf'), False)
    print(f"Computer took {time.time() - start_time:.2f} sec")
    return move


def main():
    board = init_board()
    turn = "white"
    print("Welcome to Chess AI (You are White)")
    print("Enter moves like: e2 e4 — Type 'exit' to quit\n")

    while True:
        print_board(board)

        if turn == "white":
            move = input("Your move: ").strip()
            if move.lower() == "exit": break

            try:
                start_str, end_str = move.split()
                start = parse_position(start_str)
                end = parse_position(end_str)

                if not start or not end or not is_valid_move(board, start, end, turn):
                    print("❌ Invalid move. Try again.")
                    continue

                board = make_move(board, start, end)
                turn = "black"
            except:
                print("❌ Format should be like 'e2 e4'.")
                continue
        else:
            computer_move = get_computer_move(board)
            if computer_move:
                s, e = computer_move
                board = make_move(board, s, e)
                print(f" Computer played: {chr(s[1]+97)}{8-s[0]} {chr(e[1]+97)}{8-e[0]}")
                turn = "white"
            else:
                print("✅ Computer has no valid moves. You win!")
                break

if __name__ == "__main__":
    main()
