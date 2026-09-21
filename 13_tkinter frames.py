"""
Frames
    - provides more flexibility while laying out the component in our window
    - it gives us a separate sub-window inside ethe main window
"""
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("My Application")

my_frame = ttk.Frame()
my_frame.pack(side="left", fill="both", expand=True)

label1 = tk.Label(my_frame, text="Hello World!", bg="red")
label1.pack(side="top", fill='both', expand=True) # side="left" it reserves all the vertical spaces, 'y' means vertical spaces y-axis, 'x' means horizontal spaces x-axis, 'both' means both axis

label2 = tk.Label(window, text="How are you?", bg="blue")
label2.pack(side="top", fill='both', expand=True) #they stuck one after the another

label3 = tk.Label(window, text="Have a nice day!", bg="green")
label3.pack(side="top", fill='both', expand=True) #they stuck one after the another

window.mainloop()