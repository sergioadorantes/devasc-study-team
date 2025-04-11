import tkinter as tk
from tkinter import messagebox, simpledialog
from conexion import conectar

def abrir_crud_clientes():
    ventana_cli = tk.Toplevel()
    ventana_cli.title("CRUD - Clientes")
    ventana_cli.geometry("700x500")
    ventana_cli.configure(bg="black")

    titulo = tk.Label(ventana_cli, text="CRUD CLIENTES", font=("Stencil", 25, "bold"), fg="orange", bg="black")
    titulo.pack(pady=20)

    # Función para obtener empleados
    def obtener_empleados():
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("SELECT idemp, nombre FROM empleados")
            empleados = cursor.fetchall()
            conexion.close()
            return empleados
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron cargar los empleados.\n{e}")
            return []

    def crear_cliente():
        usuario = simpledialog.askstring("💋 Crear Cliente", "Nombre de usuario:")
        nivel = simpledialog.askstring("💋 Crear Cliente", "Nivel del cliente:")
        telefono = simpledialog.askstring("💋 Crear Cliente", "Teléfono:")
        descuento = simpledialog.askfloat("💋 Crear Cliente", "Descuento (%):")

        empleados = obtener_empleados()
        if not empleados:
            return

        opciones = {f"{e[1]} (ID: {e[0]})": e[0] for e in empleados}
        seleccion = simpledialog.askstring("💋 Crear Cliente", "Selecciona el empleado asignado:\n" + "\n".join(opciones.keys()))
        idemp = opciones.get(seleccion)

        if usuario and nivel and telefono and descuento is not None and idemp:
            try:
                conexion = conectar()
                cursor = conexion.cursor()
                cursor.execute(
                    "INSERT INTO clientes (usuario, nivel, telefono, descuento, idemp) VALUES (%s, %s, %s, %s, %s)",
                    (usuario, nivel, telefono, descuento, idemp)
                )
                conexion.commit()
                conexion.close()
                messagebox.showinfo("💋 Éxito", "Cliente creado correctamente.")
            except Exception as e:
                messagebox.showerror("💋 Error", f"No se pudo crear el cliente.\n{e}")

    def leer_clientes():
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT c.idcliente, c.usuario, c.nivel, c.telefono, c.descuento, e.nombre 
                FROM clientes c JOIN empleados e ON c.idemp = e.idemp
            """)
            clientes = cursor.fetchall()
            conexion.close()

            texto = "\n".join([
                f"ID: {c[0]} | Usuario: {c[1]} | Nivel: {c[2]} | Tel: {c[3]} | Desc: {c[4]}% | Empleado: {c[5]}"
                for c in clientes
            ])
            messagebox.showinfo("💋 Clientes Registrados", texto if texto else "No hay clientes registrados.")
        except Exception as e:
            messagebox.showerror("💋 Error", f"No se pudo leer la tabla clientes.\n{e}")

    def actualizar_cliente():
        idcli = simpledialog.askinteger("💋 Actualizar Cliente", "ID del cliente a modificar:")
        usuario = simpledialog.askstring("💋 Actualizar Cliente", "Nuevo usuario:")
        nivel = simpledialog.askstring("💋 Actualizar Cliente", "Nuevo nivel:")
        telefono = simpledialog.askstring("💋 Actualizar Cliente", "Nuevo teléfono:")
        descuento = simpledialog.askfloat("💋 Actualizar Cliente", "Nuevo descuento:")

        empleados = obtener_empleados()
        if not empleados:
            return

        opciones = {f"{e[1]} (ID: {e[0]})": e[0] for e in empleados}
        seleccion = simpledialog.askstring("💋 Actualizar Cliente", "Nuevo empleado asignado:\n" + "\n".join(opciones.keys()))
        idemp = opciones.get(seleccion)

        if idcli and usuario and nivel and telefono and descuento is not None and idemp:
            try:
                conexion = conectar()
                cursor = conexion.cursor()
                cursor.execute(
                    "UPDATE clientes SET usuario=%s, nivel=%s, telefono=%s, descuento=%s, idemp=%s WHERE idcliente=%s",
                    (usuario, nivel, telefono, descuento, idemp, idcli)
                )
                conexion.commit()
                conexion.close()
                messagebox.showinfo("💋 Éxito", "Cliente actualizado correctamente.")
            except Exception as e:
                messagebox.showerror("💋 Error", f"No se pudo actualizar el cliente.\n{e}")

    def eliminar_cliente():
        idcli = simpledialog.askinteger("💋 Eliminar Cliente", "ID del cliente a eliminar:")
        if idcli:
            try:
                conexion = conectar()
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM clientes WHERE idcliente=%s", (idcli,))
                conexion.commit()
                conexion.close()
                messagebox.showinfo("💋 Éxito", "Cliente eliminado correctamente.")
            except Exception as e:
                messagebox.showerror("💋 Error", f"No se pudo eliminar el cliente.\n{e}")

    # Botones estilizados
    botones = [
        ("💋 Crear", crear_cliente),
        ("💋 Leer", leer_clientes),
        ("💋 Actualizar", actualizar_cliente),
        ("💋 Eliminar", eliminar_cliente),
    ]

    for texto, funcion in botones:
        btn = tk.Button(
            ventana_cli,
            text=texto,
            command=funcion,
            font=("Stencil", 16),
            bg="white",
            fg="black",
            width=25
        )
        btn.pack(pady=10)
