import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Message", "Hello, Tkinter!")

root = tk.Tk()
root.title("Simple GUI")

# Definir cores personalizadas
bg_color = "#F0F0F0"
button_color = "#4C8BF5"

# Definir estilo do título
title_style = ("Helvetica", 16, "bold")

# Configurar a janela principal
root.configure(bg=bg_color)
root.geometry("300x200")

# Label de boas-vindas
label = tk.Label(root, text="Welcome to Tkinter!", font=title_style, bg=bg_color)
label.pack(pady=20)

# Botão estilizado
button_style = {"font": "Arial", "bg": button_color, "fg": "white", "width": 10, "height": 2}
button = tk.Button(root, text="Click Me", command=show_message, **button_style)
button.pack()

root.mainloop()
