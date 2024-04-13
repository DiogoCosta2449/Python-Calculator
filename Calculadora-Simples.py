# Autor : Diogo Costa
# Data : 2024-04-13 
# Descrição: Calculadora simples com interface gráfica

# Importa a biblioteca tkinter
import tkinter as tk

# Funções para as operações matemáticas
def sum():
    try:
        soma = eval(entry.get())
        result.config(text=str(soma))
    except:
        result.config(text="Invalid input")

# Interface da calculadora
root = tk.Tk()
root.title("Calculadora")
root.geometry("225x343")  # Ajuste das dimensões da janela
root.resizable(False, False)
root.configure(background="white")
root.attributes("-alpha", 0.97, "-topmost", True)

# Label do título
label = tk.Label(
    root, 
    text="Calculadora", 
    foreground="#444", 
    background="#f7f7f7",
    height=2,
    width=14, 
    font=("Segoe UI", 20, "bold"),
    borderwidth=1,  # Add borderwidth property
    relief="raised"  # Add relief property
)
label.grid(row=0, column=0, columnspan=5, pady=0, padx=0)

# Campo de entrada para os números e operações
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
entry.grid(row=1, column=0, columnspan=4, ipady=0, ipadx=0, pady=0, padx=0)

# Resultado da conta
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

# Botões para as operações
buttons = [
    ('C', 3, 0), ('%', 3, 1), ('÷', 3, 2), ('x', 3, 3),
    ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('-', 4, 3),
    ('4', 5, 0), ('5', 5, 1), ('6', 5, 2), ('+', 5, 3),
    ('1', 6, 0), ('2', 6, 1), ('3', 6, 2), ('=', 6, 3),
    ('0', 7, 0), ('.', 7, 1), ('⌫', 7, 2)
]

for (text, row, column) in buttons:
    button = tk.Button(
        root,
        text=text,
        font=("opensans", 14, "bold" ),
        foreground="#222",
        background="grey",
        width=3,
        height=0,
        command=lambda t=text: on_button_click(t),
        borderwidth=1,
        relief="groove",
        highlightbackground="gray",  # Add highlightbackground property with the desired color
        highlightthickness=1  # Add highlightthickness property with the desired thickness
    )
    if text == '=':
        button.config(width=3, height=3)
        button.grid(row=row, column=column, padx=0, pady=0, rowspan=2, columnspan=2)
    else:
        button.grid(row=row, column=column, padx=0, pady=1)

# Função para clicar nos botões
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
        entry.delete(len(entry.get())-1, tk.END)
    elif value == '%':
        entry.insert(tk.END, '/100')
    elif value == 'x':
        entry.insert(tk.END, '*')
    elif value == '÷':
        entry.insert(tk.END, '/')
    else:
        entry.insert(tk.END, value)
    

#Finaliza a interface
root.mainloop()
