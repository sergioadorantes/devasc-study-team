import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql",
        database="dbtaller"
    )
    if conexion.is_connected():
        print("Conexión a la base de datos exitosa :D")
except mysql.connector.Error as err:
    print(f"Error al conectar a la base de datos:c : {err}")
    exit()

def insertar_linea(clave, nombre):
    sql = "INSERT INTO lineainv (clave, nombre) VALUES (%s, %s)"
    valores = (clave, nombre)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Línea de investigación insertada correctamente.")

def obtener_lineas():
    cursor.execute("SELECT * FROM lineainv")
    for linea in cursor.fetchall():
        print(linea)

def actualizar_linea(clave, nuevo_nombre):
    sql = "UPDATE lineainv SET nombre = %s WHERE clave = %s"
    valores = (nuevo_nombre, clave)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Línea de investigación actualizada correctamente.")

def eliminar_linea(clave):
    sql = "DELETE FROM lineainv WHERE clave = %s"
    valores = (clave,)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Línea de investigación eliminada correctamente.")

def cerrar_conexion():
    cursor.close()
    conexion.close()
    print("Conexión cerrada.")
