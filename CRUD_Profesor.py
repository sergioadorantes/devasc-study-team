import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mysql",
            database="dbtaller"
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        exit()

def crear_profesor():
    conexion = conectar()
    cursor = conexion.cursor()
    nombre = input("Ingrese el nombre del profesor: ")
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
    if not profesores:
        print("No hay profesores registrados.")
    else:
        for profesor in profesores:
            print(profesor)
    cursor.close()
    conexion.close()

def actualizar_profesor():
    conexion = conectar()
    cursor = conexion.cursor()
    idprofesor = input("Ingrese el ID del profesor a actualizar: ")
    nuevo_nombre = input("Ingrese el nuevo nombre: ")
    sql = "UPDATE profesor SET nombreProf = %s WHERE idprofesor = %s"
    cursor.execute(sql, (nuevo_nombre, idprofesor))
    conexion.commit()
    print("Profesor actualizado con éxito.")
    cursor.close()
    conexion.close()

def eliminar_profesor():
    conexion = conectar()
    cursor = conexion.cursor()
    idprofesor = input("Ingrese el ID del profesor a eliminar: ")
    sql = "DELETE FROM profesor WHERE idprofesor = %s"
    cursor.execute(sql, (idprofesor,))
    conexion.commit()
    print("Profesor eliminado con éxito.")
    cursor.close()
    conexion.close()

def menu():
    while True:
        print("\n> > > Menú < < <")
        print("1. Agregar Profesor")
        print("2. Ver Profesores")
        print("3. Actualizar Profesor")
        print("4. Eliminar Profesor")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_profesor()
        elif opcion == "2":
            leer_profesores()
        elif opcion == "3":
            actualizar_profesor()
        elif opcion == "4":
            eliminar_profesor()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

menu()