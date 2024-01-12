from Tkinter import *
import Tkinter as tk

master = tk.Tk()

def create_window(): #Definion und Festlegung neues Fenster
    toplevel = Toplevel()
    toplevel.title('result')
    toplevel.geometry('1500x1000')
    toplevel.focus_set()

Button(master, text='forward', command=create_window).pack(padx=5, anchor=N, pady=4)

master.mainloop()
