import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import date
from conexion import conectar

def abrir_crud_pedidos():
    ventana_ped = tk.Toplevel()
    ventana_ped.title("CRUD - Pedidos")
    ventana_ped.geometry("750x550")
    ventana_ped.configure(bg="black")

    titulo = tk.Label(ventana_ped, text="CRUD PEDIDOS", font=("Stencil", 25, "bold"), fg="orange", bg="black")
    titulo.pack(pady=20)

    def obtener_clientes():
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("SELECT idcliente, usuario FROM clientes")
            datos = cursor.fetchall()
            conexion.close()
            return datos
        except Exception as e:
            messagebox.showerror("💋 Error", f"No se pudieron obtener los clientes.\n{e}")
            return []

    def obtener_empleados():
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("SELECT idemp, nombre FROM empleados")
            datos = cursor.fetchall()
            conexion.close()
            return datos
        except Exception as e:
            messagebox.showerror("💋 Error", f"No se pudieron obtener los empleados.\n{e}")
            return []

    def crear_pedido():
        clientes = obtener_clientes()
        empleados = obtener_empleados()

        if not clientes or not empleados:
            return

        dic_cli = {f"{c[1]} (ID: {c[0]})": c[0] for c in clientes}
        dic_emp = {f"{e[1]} (ID: {e[0]})": e[0] for e in empleados}

        seleccion_cli = simpledialog.askstring("💋 Crear Pedido", "Selecciona cliente:\n" + "\n".join(dic_cli.keys()))
        seleccion_emp = simpledialog.askstring("💋 Crear Pedido", "Selecciona empleado:\n" + "\n".join(dic_emp.keys()))
        total = simpledialog.askfloat("💋 Crear Pedido", "Total del pedido:")
        estpedido = simpledialog.askstring("💋 Crear Pedido", "Estado (Ej: Pendiente, Enviado, Entregado):")

        idcli = dic_cli.get(seleccion_cli)
        idemp = dic_emp.get(seleccion_emp)

        if idcli and idemp and total is not None and estpedido:
            try:
                conexion = conectar()
                cursor = conexion.cursor()
                cursor.execute(
                    "INSERT INTO pedidos (idcliente, idemp, fecha, total, estpedido) VALUES (%s, %s, %s, %s, %s)",
                    (idcli, idemp, date.today(), total, estpedido)
                )
                conexion.commit()
                conexion.close()
                messagebox.showinfo("💋 Éxito", "Pedido creado correctamente.")
            except Exception as e:
                messagebox.showerror("💋 Error", f"No se pudo crear el pedido.\n{e}")

    def leer_pedidos():
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT p.idpedido, c.usuario, e.nombre, p.fecha, p.total, p.estpedido
                FROM pedidos p
                JOIN clientes c ON p.idcliente = c.idcliente
                JOIN empleados e ON p.idemp = e.idemp
            """)
            pedidos = cursor.fetchall()
            conexion.close()

            texto = "\n".join([
                f"ID: {p[0]} | Cliente: {p[1]} | Empleado: {p[2]} | Fecha: {p[3]} | Total: ${p[4]} | Estado: {p[5]}"
                for p in pedidos
            ])
            messagebox.showinfo("💋 Pedidos Registrados", texto if texto else "No hay pedidos registrados.")
        except Exception as e:
            messagebox.showerror("💋 Error", f"No se pudo leer la tabla pedidos.\n{e}")

    def actualizar_pedido():
        idpedido = simpledialog.askinteger("💋 Actualizar Pedido", "ID del pedido a modificar:")

        clientes = obtener_clientes()
        empleados = obtener_empleados()
        if not clientes or not empleados:
            return

        dic_cli = {f"{c[1]} (ID: {c[0]})": c[0] for c in clientes}
        dic_emp = {f"{e[1]} (ID: {e[0]})": e[0] for e in empleados}

        seleccion_cli = simpledialog.askstring("💋 Actualizar Pedido", "Nuevo cliente:\n" + "\n".join(dic_cli.keys()))
        seleccion_emp = simpledialog.askstring("💋 Actualizar Pedido", "Nuevo empleado:\n" + "\n".join(dic_emp.keys()))
        fecha_str = simpledialog.askstring("💋 Actualizar Pedido", "Nueva fecha (AAAA-MM-DD):")
        total = simpledialog.askfloat("💋 Actualizar Pedido", "Nuevo total:")
        estpedido = simpledialog.askstring("💋 Actualizar Pedido", "Nuevo estado:")

        idcli = dic_cli.get(seleccion_cli)
        idemp = dic_emp.get(seleccion_emp)

        if idpedido and idcli and idemp and fecha_str and total is not None and estpedido:
            try:
                conexion = conectar()
                cursor = conexion.cursor()
                cursor.execute(
                    "UPDATE pedidos SET idcliente=%s, idemp=%s, fecha=%s, total=%s, estpedido=%s WHERE idpedido=%s",
                    (idcli, idemp, fecha_str, total, estpedido, idpedido)
                )
                conexion.commit()
                conexion.close()
                messagebox.showinfo("💋 Éxito", "Pedido actualizado correctamente.")
            except Exception as e:
                messagebox.showerror("💋 Error", f"No se pudo actualizar el pedido.\n{e}")

    def eliminar_pedido():
        idpedido = simpledialog.askinteger("💋 Eliminar Pedido", "ID del pedido a eliminar:")
        if idpedido:
            try:
                conexion = conectar()
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM pedidos WHERE idpedido=%s", (idpedido,))
                conexion.commit()
                conexion.close()
                messagebox.showinfo("💋 Éxito", "Pedido eliminado correctamente.")
            except Exception as e:
                messagebox.showerror("💋 Error", f"No se pudo eliminar el pedido.\n{e}")

    # Botones estilizados
    botones = [
        ("💋 Crear", crear_pedido),
        ("💋 Leer", leer_pedidos),
        ("💋 Actualizar", actualizar_pedido),
        ("💋 Eliminar", eliminar_pedido),
    ]

    for texto, funcion in botones:
        btn = tk.Button(
            ventana_ped,
            text=texto,
            command=funcion,
            font=("Stencil", 16),
            bg="white",
            fg="black",
            width=25
        )
        btn.pack(pady=10)