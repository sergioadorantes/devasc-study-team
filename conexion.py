import mysql.connector
from tkinter import messagebox

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",         
            password="mysql",         
            database="zorriana"
        )
        if conexion.is_connected():
            print("✅ Conexión exitosa a la base de datos.")
            return conexion
    except mysql.connector.Error as e:
        messagebox.showerror("Error de Conexión", f"No se pudo conectar a la base de datos.\n{e}")
        return None
