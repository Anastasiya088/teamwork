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
