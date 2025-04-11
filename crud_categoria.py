import tkinter as tk
from tkinter import messagebox, simpledialog
from conexion import conectar

def abrir_crud_categoria():
    ventana_cat = tk.Toplevel()
    ventana_cat.title("CRUD - Categoría")
    ventana_cat.geometry("600x400")
    ventana_cat.configure(bg="black")

    titulo = tk.Label(ventana_cat, text="CRUD CATEGORÍA", font=("Stencil", 25, "bold"), fg="orange", bg="black")
    titulo.pack(pady=20)

    # FUNCIONES CRUD CON ESTILO Y CONEXIÓN
    def crear_categoria():
        nombre = simpledialog.askstring("💋 Crear Categoría", "Nombre de la categoría:")
        if nombre:
            try:
                conexion = conectar()
                if conexion:
                    cursor = conexion.cursor()
                    cursor.execute("INSERT INTO categoria (nombre_categoria) VALUES (%s)", (nombre,))
                    conexion.commit()
                    conexion.close()
                    messagebox.showinfo("💋 Éxito", "Categoría creada correctamente.")
            except Exception as e:
                messagebox.showerror("💋 Error", f"No se pudo crear la categoría.\n{e}")

    def leer_categoria():
        try:
            conexion = conectar()
            if conexion:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM categoria")
                categorias = cursor.fetchall()
                conexion.close()

                texto = "\n".join([f"ID: {c[0]} | Nombre: {c[1]}" for c in categorias])
                messagebox.showinfo("💋 Categorías Registradas", texto if texto else "No hay categorías registradas.")
        except Exception as e:
            messagebox.showerror("💋 Error", f"No se pudo leer la tabla.\n{e}")

    def actualizar_categoria():
        idcat = simpledialog.askinteger("💋 Actualizar Categoría", "ID de la categoría a modificar:")
        nuevo_nombre = simpledialog.askstring("💋 Actualizar Categoría", "Nuevo nombre:")
        if idcat and nuevo_nombre:
            try:
                conexion = conectar()
                if conexion:
                    cursor = conexion.cursor()
                    cursor.execute("UPDATE categoria SET nombre_categoria=%s WHERE idcat=%s", (nuevo_nombre, idcat))
                    conexion.commit()
                    conexion.close()
                    messagebox.showinfo("💋 Éxito", "Categoría actualizada correctamente.")
            except Exception as e:
                messagebox.showerror("💋 Error", f"No se pudo actualizar la categoría.\n{e}")

    def eliminar_categoria():
        idcat = simpledialog.askinteger("💋 Eliminar Categoría", "ID de la categoría a eliminar:")
        if idcat:
            try:
                conexion = conectar()
                if conexion:
                    cursor = conexion.cursor()
                    cursor.execute("DELETE FROM categoria WHERE idcat=%s", (idcat,))
                    conexion.commit()
                    conexion.close()
                    messagebox.showinfo("💋 Éxito", "Categoría eliminada correctamente.")
            except Exception as e:
                messagebox.showerror("💋 Error", f"No se pudo eliminar la categoría.\n{e}")

    # BOTONES ESTILIZADOS
    botones = [
        ("💋 Crear", crear_categoria),
        ("💋 Leer", leer_categoria),
        ("💋 Actualizar", actualizar_categoria),
        ("💋 Eliminar", eliminar_categoria),
    ]

    for texto, funcion in botones:
        btn = tk.Button(
            ventana_cat,
            text=texto,
            command=funcion,
            font=("Stencil", 16),
            bg="white",
            fg="black",
            width=20
        )
        btn.pack(pady=10)
