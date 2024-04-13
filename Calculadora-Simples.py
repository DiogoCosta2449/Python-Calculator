# Autor : Diogo Costa
# Data : 2024-04-13
# Descrição: Calculadora simples com interface gráfica

# Importa a biblioteca tkinter
import tkinter as tk

# Funções para as operações matemáticas
def sum():
    try:
        soma = float(entry1.get()) + float(entry2.get())
        result.config(text=str(soma))
    except ValueError:
        result.config(text="Invalid input")
def sub():
    try:
        subtracao = float(entry1.get()) - float(entry2.get())
        result.config(text=str(subtracao))
    except ValueError:
        result.config(text="Invalid input")
def mult():
    try:
        multiplicacao = float(entry1.get()) * float(entry2.get())
        result.config(text=str(multiplicacao))
    except ValueError:
        result.config(text="Invalid input")
def div():
    try:
        divisao = float(entry1.get()) / float(entry2.get())
        result.config(text=str(divisao))
    except ZeroDivisionError:
        result.config(text="Error:zero")

# Interface da calculadora
root = tk.Tk()
root.title("Calculadora")
root.geometry("200x225")
root.resizable(False, False)
root.configure(background="#1D1615")

# Label do título
label = tk.Label(
    root, 
    text="Calculadora", 
    foreground="white", 
    background="#1F1D1B", 
    width=100, 
    height=1, 
    font=("Courier", 18, "bold"))
label.pack()


# Campos de entrada para os números
entry1 = tk.Entry(root, justify='center',width=11,background="#E3E6E3",font=("bold"))
entry2 = tk.Entry(root, justify='center',width=11,background="#E3E6E3",font=("bold"))

# Labels para o primeiro número
tk.Label(
    root,
    text="Primeiro número:",
    font=("Aerial", 11),
    foreground="white",
    background="#1F1D1B",
    width=13,
    height=1,
    ).pack()
entry1.pack()

#Espaçamento
tk.Label(root, text="",background="#1D1615", font=("Courier", 3)).pack()

# Frame para os botões
frame_botoes = tk.Frame(root)
frame_botoes.pack()

#Espaçamento
tk.Label(root, text="",background="#1D1615", font=("Courier", 3)).pack()

# Label para o segundo número
tk.Label(
    root,
    text="Segundo número:",
    font=("Aerial", 11),
    foreground="white",
    background="#1F1D1B",
    width=13,
    height=1
).pack()
entry2.pack()

# Botões para as operações
# Soma
button_sum = tk.Button(
    frame_botoes,
    text="+",
    command=sum,
    background= "#484547",
    width=2,
    
    )
button_sum.pack(side=tk.LEFT)

# Subtração
button_sub = tk.Button(
    frame_botoes,
    text="-",
    command=sub,
    background= "#484547",
    width=2,
    )
button_sub.pack(side=tk.LEFT)

# Multiplicação
button_mult = tk.Button(
    frame_botoes,
    text="x",
    command=mult,
    background= "#484547",
    width=2,
    )
button_mult.pack(side=tk.LEFT)

# Divisão
button_div = tk.Button(
    frame_botoes,
    text="÷",
    command=div,
    background= "#484547",
    width=2,
    )
button_div.pack(side=tk.LEFT)

# Label para o resultado
result_label = tk.Label(
    root,
    text="=",
    font=("Aerial", 11),
    foreground="white",
    background="#1F1D1B",
    width=3,
    height=1
)
result_label.pack()

# Resultado da conta
result = tk.Label(
    root,
    text="",
    font=("Aerial", 13),
    foreground="black",
    background="#E3E6E3",
    width=9,
    height=1
)
result.pack()

#Finaliza a interface
root.mainloop()
