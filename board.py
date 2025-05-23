import tkinter as tk
from constants import *
from checker import Checker

class Board:
    def init(self, canvas):
        self.canvas = canvas
        # Ініціалізовано поле
        self.squares = []
        for _ in range(BOARD_SIZE):
            self.squares.append([None] * BOARD_SIZE)
        self.selected = None
        self.turn = 'red'
        self.create_pieces()

    def create_pieces(self):
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                if (r + c) % 2 != 0:
                    if r < 3:
                        self.squares[r][c] = Checker(r, c, 'white')
                    elif r > 4:
                        self.squares[r][c] = Checker(r, c, 'red')

    def draw_board(self):
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                x1, y1 = c * SQUARE_SIZE, r * SQUARE_SIZE
                x2, y2 = x1 + SQUARE_SIZE, y1 + SQUARE_SIZE
                color = LIGHT_COLOR if (r + c) % 2 == 0 else DARK_COLOR
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

    def get_valid_moves(self, r, c):
        moves = {}
        piece = self.squares[r][c]
        if not piece or piece.color != self.turn:
            return moves
        directions = [(-1, -1), (-1, 1)] if piece.color == 'red' or piece.king else []
        directions += [(1, -1), (1, 1)] if piece.color == 'white' or piece.king else []
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE:
                if not self.squares[nr][nc]:
                    moves[(nr, nc)] = None
                elif self.squares[nr][nc].color != piece.color:
                    jr, jc = nr + dr, nc + dc
                    if 0 <= jr < BOARD_SIZE and 0 <= jc < BOARD_SIZE and not self.squares[jr][jc]:
                        moves[(jr, jc)] = (nr, nc)
        return moves

    
    def move(self, r, c, nr, nc):
        piece = self.squares[r][c]
        self.squares[r][c] = None
        self.squares[nr][nc] = piece
        piece.row, piece.col = nr, nc
        jumped = self.get_valid_moves(r,c).get((nr,nc))
        if jumped:
            jr,jc = jumped
            self.squares[jr][jc] = None
        if (piece.color=='red' and nr==0) or (piece.color=='white' and nr==BOARD_SIZE-1):
            piece.make_king()

    def draw_pieces(self):
        self.canvas.delete("piece")
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                piece = self.squares[r][c]
                if piece:
                    x = c * SQUARE_SIZE + SQUARE_SIZE // 2;
                    y = r * SQUARE_SIZE + SQUARE_SIZE // 2
                    rad = SQUARE_SIZE // 2 - 5
                    col = RED_PIECE_COLOR if piece.color == 'red' else WHITE_PIECE_COLOR
                    self.canvas.create_oval(x - rad, y - rad, x + rad, y + rad, fill=col, tags="piece")
                    if piece.king:
                        self.canvas.create_text(x, y, text="K", fill="gold", font=(None, 24), tags="piece")