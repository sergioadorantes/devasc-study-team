import tkinter as tk
from tkinter import messagebox, simpledialog
from conexion import conectar

def abrir_crud_empleados():
    ventana_emp = tk.Toplevel()
    ventana_emp.title("CRUD - Empleados")
    ventana_emp.geometry("700x500")
    ventana_emp.configure(bg="black")

    titulo = tk.Label(ventana_emp, text="CRUD EMPLEADOS", font=("Stencil", 25, "bold"), fg="orange", bg="black")
    titulo.pack(pady=20)

    def validar_sexo(sexo):
        return sexo in ['M', 'F', 'O']

    def crear_empleado():
        nombre = simpledialog.askstring("💋 Crear Empleado", "Nombre del empleado:")
        puesto = simpledialog.askstring("💋 Crear Empleado", "Puesto:")
        sexo = simpledialog.askstring("💋 Crear Empleado", "Sexo (M/F/O):")
        telefono = simpledialog.askstring("💋 Crear Empleado", "Teléfono:")

        if nombre and puesto and sexo and telefono:
            sexo = sexo.upper()
            if not validar_sexo(sexo):
                messagebox.showwarning("💋 Atención", "El sexo debe ser 'M', 'F' o 'O'.")
                return

            try:
                conexion = conectar()
                cursor = conexion.cursor()
                cursor.execute(
                    "INSERT INTO empleados (nombre, puesto, sexo, telefono) VALUES (%s, %s, %s, %s)",
                    (nombre, puesto, sexo, telefono)
                )
                conexion.commit()
                conexion.close()
                messagebox.showinfo("💋 Éxito", "Empleado creado correctamente.")
            except Exception as e:
                messagebox.showerror("💋 Error", f"No se pudo crear el empleado.\n{e}")

    def leer_empleados():
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM empleados")
            empleados = cursor.fetchall()
            conexion.close()

            texto = "\n".join([
                f"ID: {e[0]} | Nombre: {e[1]} | Puesto: {e[2]} | Sexo: {e[3]} | Tel: {e[4]}"
                for e in empleados
            ])
            messagebox.showinfo("💋 Empleados Registrados", texto if texto else "No hay empleados registrados.")
        except Exception as e:
            messagebox.showerror("💋 Error", f"No se pudo leer la tabla empleados.\n{e}")

    def actualizar_empleado():
        idemp = simpledialog.askinteger("💋 Actualizar Empleado", "ID del empleado a modificar:")
        nombre = simpledialog.askstring("💋 Actualizar Empleado", "Nuevo nombre:")
        puesto = simpledialog.askstring("💋 Actualizar Empleado", "Nuevo puesto:")
        sexo = simpledialog.askstring("💋 Actualizar Empleado", "Nuevo sexo (M/F/O):")
        telefono = simpledialog.askstring("💋 Actualizar Empleado", "Nuevo teléfono:")

        if idemp and nombre and puesto and sexo and telefono:
            sexo = sexo.upper()
            if not validar_sexo(sexo):
                messagebox.showwarning("💋 Atención", "El sexo debe ser 'M', 'F' o 'O'.")
                return

            try:
                conexion = conectar()
                cursor = conexion.cursor()
                cursor.execute(
                    "UPDATE empleados SET nombre=%s, puesto=%s, sexo=%s, telefono=%s WHERE idemp=%s",
                    (nombre, puesto, sexo, telefono, idemp)
                )
                conexion.commit()
                conexion.close()
                messagebox.showinfo("💋 Éxito", "Empleado actualizado correctamente.")
            except Exception as e:
                messagebox.showerror("💋 Error", f"No se pudo actualizar el empleado.\n{e}")

    def eliminar_empleado():
        idemp = simpledialog.askinteger("💋 Eliminar Empleado", "ID del empleado a eliminar:")
        if idemp:
            try:
                conexion = conectar()
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM empleados WHERE idemp=%s", (idemp,))
                conexion.commit()
                conexion.close()
                messagebox.showinfo("💋 Éxito", "Empleado eliminado correctamente.")
            except Exception as e:
                messagebox.showerror("💋 Error", f"No se pudo eliminar el empleado.\n{e}")

    # Botones estilizados
    botones = [
        ("💋 Crear", crear_empleado),
        ("💋 Leer", leer_empleados),
        ("💋 Actualizar", actualizar_empleado),
        ("💋 Eliminar", eliminar_empleado),
    ]

    for texto, funcion in botones:
        btn = tk.Button(
            ventana_emp,
            text=texto,
            command=funcion,
            font=("Stencil", 16),
            bg="white",
            fg="black",
            width=25
        )
        btn.pack(pady=10)