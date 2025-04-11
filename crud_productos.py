import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from conexion import conectar

def abrir_crud_productos():
    ventana_prod = tk.Toplevel()
    ventana_prod.title("CRUD - Productos")
    ventana_prod.geometry("700x500")
    ventana_prod.configure(bg="black")

    titulo = tk.Label(ventana_prod, text="CRUD PRODUCTOS", font=("Stencil", 25, "bold"), fg="orange", bg="black")
    titulo.pack(pady=20)

    # Función auxiliar para obtener categorías
    def obtener_categorias():
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("SELECT idcat, nombre_categoria FROM categoria")
            categorias = cursor.fetchall()
            conexion.close()
            return categorias
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron cargar las categorías.\n{e}")
            return []

    def crear_producto():
        nombre = simpledialog.askstring("💋 Crear Producto", "Nombre del producto:")
        descripcion = simpledialog.askstring("💋 Crear Producto", "Descripción:")
        stock = simpledialog.askinteger("💋 Crear Producto", "Stock disponible:")
        precio = simpledialog.askfloat("💋 Crear Producto", "Precio unitario:")
        
        categorias = obtener_categorias()
        if not categorias:
            return
        
        opciones = {f"{c[1]} (ID: {c[0]})": c[0] for c in categorias}
        seleccion = simpledialog.askstring("💋 Crear Producto", "Selecciona la categoría:\n" + "\n".join(opciones.keys()))
        idcat = opciones.get(seleccion)

        if nombre and descripcion and stock is not None and precio is not None and idcat:
            try:
                conexion = conectar()
                cursor = conexion.cursor()
                cursor.execute(
                    "INSERT INTO productos (nombre_producto, descripcion, stock, idcat, preciounit) VALUES (%s, %s, %s, %s, %s)",
                    (nombre, descripcion, stock, idcat, precio)
                )
                conexion.commit()
                conexion.close()
                messagebox.showinfo("💋 Éxito", "Producto creado correctamente.")
            except Exception as e:
                messagebox.showerror("💋 Error", f"No se pudo crear el producto.\n{e}")

    def leer_productos():
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT p.idproducto, p.nombre_producto, p.descripcion, p.stock, c.nombre_categoria, p.preciounit 
                FROM productos p JOIN categoria c ON p.idcat = c.idcat
            """)
            productos = cursor.fetchall()
            conexion.close()

            texto = "\n".join([f"ID: {p[0]} | Nombre: {p[1]} | Desc: {p[2]} | Stock: {p[3]} | Cat: {p[4]} | Precio: ${p[5]}" for p in productos])
            messagebox.showinfo("💋 Productos Registrados", texto if texto else "No hay productos registrados.")
        except Exception as e:
            messagebox.showerror("💋 Error", f"No se pudo leer la tabla productos.\n{e}")

    def actualizar_producto():
        idprod = simpledialog.askinteger("💋 Actualizar Producto", "ID del producto a modificar:")
        nombre = simpledialog.askstring("💋 Actualizar Producto", "Nuevo nombre del producto:")
        descripcion = simpledialog.askstring("💋 Actualizar Producto", "Nueva descripción:")
        stock = simpledialog.askinteger("💋 Actualizar Producto", "Nuevo stock:")
        precio = simpledialog.askfloat("💋 Actualizar Producto", "Nuevo precio:")

        categorias = obtener_categorias()
        if not categorias:
            return

        opciones = {f"{c[1]} (ID: {c[0]})": c[0] for c in categorias}
        seleccion = simpledialog.askstring("💋 Actualizar Producto", "Selecciona la nueva categoría:\n" + "\n".join(opciones.keys()))
        idcat = opciones.get(seleccion)

        if idprod and nombre and descripcion and stock is not None and precio is not None and idcat:
            try:
                conexion = conectar()
                cursor = conexion.cursor()
                cursor.execute(
                    "UPDATE productos SET nombre_producto=%s, descripcion=%s, stock=%s, idcat=%s, preciounit=%s WHERE idproducto=%s",
                    (nombre, descripcion, stock, idcat, precio, idprod)
                )
                conexion.commit()
                conexion.close()
                messagebox.showinfo("💋 Éxito", "Producto actualizado correctamente.")
            except Exception as e:
                messagebox.showerror("💋 Error", f"No se pudo actualizar el producto.\n{e}")

    def eliminar_producto():
        idprod = simpledialog.askinteger("💋 Eliminar Producto", "ID del producto a eliminar:")
        if idprod:
            try:
                conexion = conectar()
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM productos WHERE idproducto=%s", (idprod,))
                conexion.commit()
                conexion.close()
                messagebox.showinfo("💋 Éxito", "Producto eliminado correctamente.")
            except Exception as e:
                messagebox.showerror("💋 Error", f"No se pudo eliminar el producto.\n{e}")

    # Botones estilizados
    botones = [
        ("💋 Crear", crear_producto),
        ("💋 Leer", leer_productos),
        ("💋 Actualizar", actualizar_producto),
        ("💋 Eliminar", eliminar_producto),
    ]

    for texto, funcion in botones:
        btn = tk.Button(
            ventana_prod,
            text=texto,
            command=funcion,
            font=("Stencil", 16),
            bg="white",
            fg="black",
            width=25
        )
        btn.pack(pady=10)
