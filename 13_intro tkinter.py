"""
GUI (Graphical User Interface)
    - interface that a user have graphically
    - There is a library called tkinter (built-in python library) for creating
    graphical user interfaces
        - It helps us to create GUI application
"""
import tkinter as tk
import tkinter.font as tfont
from tkinter import Entry
from tkinter import ttk

# Tk (class inside tkinter module) - helps us to create a window
window = tk.Tk() #this will create a window object for a Tk class inside tkinter module
window.title("My Application")
window.minsize(width=400, height=300) #This method sets the minimum size of the window, size given in pixels

custom_font = tfont.Font(family="Times New Roman", size=15, weight='bold') #Inside tk library, we have font module, inside which we have Font() class/function/ method, ...... can use slant='italic'

# label = tk.Label(text="Hello World!", font=custom_font) #There is a class Label inside tk module to add text inside my window, we put this inside label object, this Label class displays the text
label = ttk.Label(text="Hello World!", font=custom_font, padding=15) # padding - to makes spaces between any two components/ widgets, it also provides spaces before and after the component

label.pack() #Pack method of the Label class - to bring the component on the window, due to this method the window gets automatically resized to the size of the text, this pack() method is very important, if not, use nothing will happen, .... can use side="top" (by default), expand=true
# label.config(font=("Courier New", 25, "underline")) #another way

#Modifies the text
label["text"] = "Have a nice day!" #modifies the existing text
label.config(text="My new app") #another way, a config() method can change any of the properties (text, font etc.) of the Label() class

#Buttons - a clickable components on my windows, we have a Button class to create buttons on my window, we also have a lot of attributes in this class like text etc.
# counter = 0
def function_button():
    """
    global counter
    counter += 1
    label.config(text=f "The button got clicked {counter} times!")
    """
    input_text = user_input.get()
    label.config(text=input_text)

# button = tk.Button(text="Click", command=function_button) #when the button is pressed, the command will call the functions to perform task
button = ttk.Button(text="Click", command=function_button)
button.pack(pady=10) #provides padding before and after the quit button

#Entry() class - the entry component is used to take the user input just like how input function does in regular program
# user_input = tk.Entry(width=30) #you can use show="*"
user_input = ttk.Entry(width=30)
user_input.pack()
# print(user_input.get()) #a get() method fetches the text that is entered by user

#tkinter.ttk - themed tkinter library/module. A separate module

# destroy() method of Tk() class - to quit the window
quit_button = ttk.Button(text="Quit", command=window.destroy)
quit_button.pack()

#separator - to separate the widgets/ components, by default 1 pixel dot(.)
sep = ttk.Separator(orient="horizontal")
sep.pack(fill='x')

#Text widget - helps us to create textbox which allows to enter multi-line text, earlier we have Entry() for single line text
text = tk.Text(height=5, width=25)
text.pack(pady=10)

text.focus() #for cursor blinking

text.insert("1.0", "Enter your comments") #In first argument -> 1 means the 1st line, 0 means 0th character, In second argument -> the default text provide to the user
#text["state"] = "disabled" #to disable the widget
'''
def enable_text():
    text["state"] = "normal" #to enable the widget (by default)
enable_button = ttk.Button(text="Enable the box", command=enable_text)
enable_button.pack()
'''
#How to fetch the text entered inside the widget ?
text_data = text.get("1.0", "end")
print(text_data)

def text_function():
    text_data = text.get("1.0", "end")
    print(text_data)

text_button = ttk.Button(text="Get text", command=text_function)
text_button.pack()

#Check button widget - it is used to create checkboxes
# check_option = tk.IntVar() #IntVar() - a class of tkinter used for integers
check_option = tk.StringVar()

def check_option_task():
    print(check_option.get(), type(check_option.get()))

check_button = ttk.Checkbutton(text="Agree with the terms & conditions?", variable=check_option,
                               command=check_option_task, onvalue="Yes", offvalue="No")
check_button.pack()

#Radio buttons widget - useful to pick between different options, chose only values out of these options
def get_radio_value():
    print(radio_value.get())

radio_value = tk.StringVar()

option_1 = ttk.Radiobutton(text="Male", variable=radio_value, value="male", command=get_radio_value)
option_2 = ttk.Radiobutton(text="Female", variable=radio_value, value="female", command=get_radio_value)
option_1.pack()
option_2.pack()

#Combo boxes - it allows the user to select one value from the dropdown
selected_country = tk.StringVar()
countries = ttk.Combobox(textvariable=selected_country, values=("Australia", "Canada", "India", "Sweden", "US"))
countries.pack()
countries["state"] = "readonly" #to restrict the user from writing its own value

def display_country(event):
    msg = f"Selected country is {selected_country.get()}"
    country_label = ttk.Label(text=msg)
    country_label.pack()
    # print(f"Selected country is {selected_country.get()}")

countries.bind("<<ComboboxSelected>>", display_country)  #to bind the combo boxes with the event

#Listbox - similar to combobox, it's not going to have dropdown rather a list wherein multiple options can be selected
food_items = ("Pizza", "Burger", "Garlic bread", "Nachos", "Salad")
favourite_food = tk.StringVar(value=food_items)

food_list = tk.Listbox(listvariable=favourite_food, height=5, selectmode="extended")
food_list.pack()

def get_fav_food(event):
    food_indices = food_list.curselection()
    for i in food_indices:
        print(food_list.get(i))

food_list.bind("<<ListboxSelect>>", get_fav_food)

#Spinbox widget - it's like a counter with up and down arrow to increase/ decrease a value
counter = tk.IntVar(value=10)

def get_spin_box_value():
    print(f"Current spinbox value: {spin_box.get()}")

spin_box = ttk.Spinbox(from_=0, to=20, textvariable=counter, wrap=True, command=get_spin_box_value) #values=(10, 15, 20, 25) this will show only these values,..... value=tuple(range(5, 105, 5))
spin_box.pack()

print(f"Initial spinbox value: {spin_box.get()}")


window.mainloop() #mainloop() function/METHOD helps us to see the window and keeps it open until we close it manually, NEED TO CODE EVERYTHING INSIDE THIS
