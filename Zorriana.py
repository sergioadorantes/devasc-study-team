import tkinter as tk
from tkinter import messagebox
from crud_productos import abrir_crud_productos
from crud_categoria import abrir_crud_categoria
from crud_empleados import abrir_crud_empleados
from crud_clientes import abrir_crud_clientes
from crud_pedidos import abrir_crud_pedidos

# Funciones de los botones (por ahora sólo muestran mensaje)
def abrir_productos():
    messagebox.showinfo("PRODUCTOS", "Abrir CRUD de Productos")

def abrir_categoria():
    messagebox.showinfo("CATEGORÍA", "Abrir CRUD de Categoría")

def abrir_empleados():
    messagebox.showinfo("EMPLEADOS", "Abrir CRUD de Empleados")

def abrir_clientes():
    messagebox.showinfo("CLIENTES", "Abrir CRUD de Clientes")

def abrir_pedidos():
    messagebox.showinfo("PEDIDOS", "Abrir CRUD de Pedidos")

# Ventana principal
ventana = tk.Tk()
ventana.title("Zorriana - Menú Principal")
ventana.geometry("900x550")
ventana.configure(bg="black")

# Título
titulo = tk.Label(ventana, text="ZORRIANA", font=("Comic Sans MS", 50, "bold"), fg="orange", bg="black")
titulo.pack(pady=10)

# Frame para botones
botones_frame = tk.Frame(ventana, bg="black")
botones_frame.pack(side="left", padx=50)

# Lista de opciones con botones
opciones = [
    ("💋 PRODUCTOS", abrir_crud_productos),
    ("💋 CATEGORÍA", abrir_crud_categoria),
    ("💋 EMPLEADOS", abrir_crud_empleados),
    ("💋 CLIENTES", abrir_crud_clientes),
    ("💋 PEDIDOS", abrir_crud_pedidos),
]

for texto, comando in opciones:
    btn = tk.Button(botones_frame, text=texto, command=comando, font=("Stencil", 20, "bold"),
                    bg="white", fg="black", width=15, height=1)
    btn.pack(pady=10)

# Mensaje de bienvenida
bienvenido = tk.Label(ventana, text="BIENVENIDO", font=("Stencil", 35, "bold"), fg="orange", bg="black")
bienvenido.place(x=580, y=200)

# Emoji de zorro
zorro = tk.Label(ventana, text="🦊", font=("Arial", 50), bg="black")
zorro.place(x=650, y=300)

ventana.mainloop()