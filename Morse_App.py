import tkinter as tk
from tkinter import ttk
import morse_dict as morse_dict
from pynput import keyboard 
import time

def on_key_release(key): #what to do on key-release
    time_taken = round(time.time() - t, 2)*1000 #rounding the long decimal float
    print("The key",key," is pressed for",time_taken,'ms')
    return False #stop detecting more key-releases

def on_key_press(key): #what to do on key-press
    return False #stop detectding more key-presses

with keyboard.Listener(on_press = on_key_press) as press_listener: #setting code for listening key-press
    press_listener.join()

t = time.time() #reading time in sec

with keyboard.Listener(on_release = on_key_release) as release_listener: #setting code for listening key-release
    release_listener.join()


# root = tk.Tk()
# root.title('Morse Code')
# root.geometry('400x225')

# button = ttk.Button(root, text = 'Button')
# #button.bind('<Key>', lambda event: print(event))
# root.bind('<KeyDown>', lambda event: print(event))
# button.pack()

# root.mainloop()