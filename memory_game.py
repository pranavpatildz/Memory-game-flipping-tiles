#importing libraries
import tkinter as tk
import random
import time
from tkinter import messagebox

#closing window
def fquit():
    root.destroy() 

#main window
class Win:
    def __init__(self, root):
        self.root = root
        self.root.geometry("700x400")
        self.root["bg"] = "#31A9B8"
        
        self.lb = tk.Label(root,text = "‖ Memory Tile Game ‖",font=("Colonna MT",33,"bold"),fg="#693D3D",bg="#31A9B8")
        self.lb.place(x=130,y=60)
  
        self.b_play = tk.Button(root, text = "Play",
                                pady=3,padx=10,
                                bg="#F18D9E",
                                fg="#003366",
                                font=("Fixedsys",15),
                                width=15,
                                command= lambda: self.new_window(MemoryTile))
        self.b_play.place(x=260,y=170)

        self.b_exit = tk.Button(root,text = "Quit",
                                pady=3,padx=10,
                                bg="#F18D9E",
                                fg="#003366",
                                font=("Fixedsys",15),
                                width=15,
                                command=fquit) 
        self.b_exit.place(x=260,y=260)     
     
 
    def new_window(self, _class):
        try:
            if self.new.state() == "normal":
                self.new.focus()
        except:
            self.new = tk.Toplevel(self.root)
            _class(self.new)
            
            
#second window where the game will be played
class MemoryTile:
    def __init__(self, root):
        self.root = root
        self.root.title("Play_Game")
        self.buttons = [[tk.Button(root,
                                   width=7,
                                   height=3,
                                   font=("arial",15),
                                   activebackground="#DFA7EB",
                                   command=lambda row=row, column=column: self.choose_tile(row, column)
                                   ) for column in range(6)] for row in range(4)]

        for row in range(4):
            for column in range(6):
                self.buttons[row][column].grid(row=row, column=column)
        self.first = None
        self.draw_board()
        
    def draw_board(self):
        self.answer = list('AABBCCDDEEFFGGHHIIJJKKLL')
        random.shuffle(self.answer)
        self.answer = [self.answer[:6],
                       self.answer[6:12],
                       self.answer[12:18],
                       self.answer[18:24],
                       self.answer[24:30],
                       self.answer[30:36]]
        
        for row in self.buttons:
            for button in row:
                button.config(text='', state=tk.NORMAL,bg="#F0F0F0")
        self.start_time = time.monotonic()
                       
    def choose_tile(self, row, column):
        self.buttons[row][column].config(text=self.answer[row][column],bg="#DFA7EB",disabledforeground="#003366")
        self.buttons[row][column].config(state=tk.DISABLED)
        if not self.first:
            self.first = (row, column)
        else:
            a,b = self.first
            if self.answer[row][column] == self.answer[a][b]:
                self.answer[row][column] = ''
                self.answer[a][b] = ''
                if not any(''.join(row) for row in self.answer):
                    duration = time.monotonic() - self.start_time
                    messagebox.showinfo(title='Success!', message='You win!\n\n Time: {:.1f}'.format(duration))
                    self.root.after(2000, self.draw_board)
            else:
                self.root.after(700, self.hide_tiles, row, column, a, b)
            self.first = None
    
    def hide_tiles(self, x1, y1, x2, y2):
        self.buttons[x1][y1].config(text='', state=tk.NORMAL,bg="#F0F0F0")
        self.buttons[x2][y2].config(text='', state=tk.NORMAL,bg="#F0F0F0")


if __name__ == "__main__":
    root = tk.Tk()
    app = Win(root)
    app.root.title("Memory_Tile_Game")
    root.mainloop()