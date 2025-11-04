import numpy as np
import customtkinter as ctk
from random import random

# Class APP is a class to handle the GUI frame. It creates a signle window with two frame: the main one containing
# the display of the game; the second one containing the START button to start the game.
class App(ctk.CTk):

    def __init__(self,dimension):
        super().__init__()
        self.N = dimension[0]
        self.M = dimension[1]

        self.title('Game Of Life')
        self.geometry('900x750')

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=0)


        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        start_button = ctk.CTkButton(self.button_frame, text='START', command=self.start_button_function)
        start_button.pack(fill='x')
        
        self.display_frame = ctk.CTkFrame(self)
        self.display_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

        self.gamegrid = [(i,j,0) for i in range(self.N) for j in range(self.M)]

    def start_button_function(self):
        print('GAME OF LIFE')
        print(self.gamegrid)



if __name__ == '__main__':

    dimension=(5,5)
    app=App(dimension)
    app.mainloop()
