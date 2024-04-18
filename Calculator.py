# Author: Diogo Costa
# Date: 2024-04-16
# Description: Calculator with graphical interface

# tkinter library
import tkinter as tk


# Functions for mathematical operations
def sum():
    try:
        total = eval(entry.get())
        result.config(text=str(total))
    except:
        result.config(text="Invalid input")


# Calculator interface
root = tk.Tk()
root.title("Calculator")
root.geometry("225x342")
# root.resizable(False, False)
root.configure(background="white")
root.attributes("-alpha", 0.97, "-topmost", True)

# Title label
label = tk.Label(
    root,
    text="Calculator",
    foreground="#444",
    background="#f7f7f7",
    height=2,
    width=14,
    font=("Segoe UI", 20, "bold"),
    borderwidth=1,
    relief="raised"
)
label.grid(row=0, column=0, columnspan=5, pady=0, padx=0)

# Entry field for numbers and operations
entry = tk.Entry(
    root,
    justify='center',
    width=25,
    font=("Segoe UI", 12),
    background="#f9f9f9",
    foreground="black",
    borderwidth=1,
    relief="groove",
)
entry.grid(row=1, column=0, columnspan=10, ipady=0, ipadx=0, pady=0, padx=0)

# Result of the calculation
result = tk.Label(
    root,
    text="",
    justify='center',
    font=("Segoe UI", 19, "bold"),
    foreground="black",
    background="white",
    borderwidth=1,
    relief="groove",
    width=15
)
result.grid(row=2, column=0, columnspan=4, pady=0, padx=0, ipady=0, ipadx=0)

# Menu bar
# Variável de controle para o modo selecionado
mode_var = tk.IntVar()
mode_var.set(1)  # Define o modo padrão como 'Standard'

# Menu bar
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Mode", menu=file_menu)
file_menu.add_radiobutton(label="Standard", variable=mode_var, value=1)
file_menu.add_radiobutton(label="Scientific", variable=mode_var, value=2)
file_menu.add_radiobutton(label="Programmer", variable=mode_var, value=3)

# Buttons for operations
buttons = [
    ('C', 4, 0), ('%', 4, 1), ('/', 4, 2), ('x', 4, 3),
    ('7', 5, 0), ('8', 5, 1), ('9', 5, 2), ('-', 5, 3),
    ('4', 6, 0), ('5', 6, 1), ('6', 6, 2), ('+', 6, 3),
    ('1', 7, 0), ('2', 7, 1), ('3', 7, 2), ('=', 7, 3),
    ('0', 8, 0), ('.', 8, 1), ('⌫', 8, 2)
]

for (text, row, column) in buttons:
    button = tk.Button(
        root,
        text=text,
        font=("opensans", 14, "bold"),
        foreground="#222",
        background="grey",
        width=3,
        height=0,
        command=lambda t=text: on_button_click(t),
        borderwidth=1,
        relief="groove",
        highlightbackground="gray",
        highlightthickness=1
    )
    if text == '=':
        button.config(width=3, height=3)
        button.grid(row=row, column=column, padx=0, pady=0, rowspan=2, columnspan=2)
    else:
        button.grid(row=row, column=column, padx=0, pady=1)


# Function for button clicks
def on_button_click(value):
    if value == '=':
        try:
            result.config(text=str(eval(entry.get())))
        except:
            result.config(text="Error")
    elif value == 'C':
        entry.delete(0, tk.END)
        result.config(text="")
    elif value == '⌫':
        entry.delete(len(entry.get()) - 1, tk.END)
    elif value == '%':
        entry.insert(tk.END, '/100')
    elif value == 'x':
        entry.insert(tk.END, '*')
    elif value == '÷':
        entry.insert(tk.END, '/')
    else:
        entry.insert(tk.END, value)


root.mainloop()