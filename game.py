import tkinter as tk
from board import Board

class Game:
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("Шашки на Tkinter")
        self.canvas=tk.Canvas(self.root,width=BOARD_SIZE*SQUARE_SIZE,height=BOARD_SIZE*SQUARE_SIZE)
        self.canvas.pack()
        self.board=Board(self.canvas)
        self.board.draw_board()
        self.board.draw_pieces()
        self.canvas.bind("<Button-1>",self.click)

    def click(self,event):
        c,r=event.x//SQUARE_SIZE,event.y//SQUARE_SIZE
        if self.board.selected:
            sr,sc=self.board.selected
            moves=self.board.get_valid_moves(sr,sc)
            if (r,c) in moves:
                self.board.move(sr,sc,r,c)
                win=self.board.check_winner()
                if win:
                    tk.messagebox.showinfo("Гра завершена",f"Переміг {win}!")
                    self.root.quit();return
                self.board.turn='white' if self.board.turn=='red' else 'red'
                self.board.selected=None
                self.board.draw_board();self.board.draw_pieces();return
        piece=self.board.squares[r][c]
        if piece and piece.color==self.board.turn:
            self.board.selected=(r,c)
            for (mr,mc),_ in self.board.get_valid_moves(r,c).items():
                x1,y1=mc*SQUARE_SIZE,mr*SQUARE_SIZE
                self.canvas.create_rectangle(x1,y1,x1+SQUARE_SIZE,y1+SQUARE_SIZE,outline="yellow",width=3,tags="highlight")

    def run(self): self.root.mainloop()
