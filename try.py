import tkinter as tk
from tkinter import ttk

ws = tk.Tk()
ws.title('PythonGuides')
ws.geometry('300x200')

Button = ttk.Button(ws, text='Exit', command = lambda event: ws.destroy())
Button.pack()

ws.mainloop()