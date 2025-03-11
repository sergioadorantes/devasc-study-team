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

def crear_profesor(nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "INSERT INTO profesor (nombreProf) VALUES (%s)"
    cursor.execute(sql, (nombre,))
    conexion.commit()
    print("Profesor agregado con éxito.")
    cursor.close()
    conexion.close()

def leer_profesores():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM profesor")
    profesores = cursor.fetchall()
    for profesor in profesores:
        print(profesor)
    cursor.close()
    conexion.close()

def actualizar_profesor(idprofesor, nuevo_nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "UPDATE profesor SET nombreProf = %s WHERE idprofesor = %s"
    cursor.execute(sql, (nuevo_nombre, idprofesor))
    conexion.commit()
    print("Profesor actualizado con éxito.")
    cursor.close()
    conexion.close()

def eliminar_profesor(idprofesor):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "DELETE FROM profesor WHERE idprofesor = %s"
    cursor.execute(sql, (idprofesor,))
    conexion.commit()
    print("Profesor eliminado con éxito.")
    cursor.close()
    conexion.close()

    # Link a mi repositorio de GitHub: https://github.com/sergioadorantes/devasc-study-team