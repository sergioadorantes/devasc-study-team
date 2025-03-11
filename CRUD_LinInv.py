import mysql.connector

def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mysql",
            database="dbtaller"
        )
        if conexion.is_connected():
            print("Conexión a la base de datos exitosa :D")
        return conexion
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        exit()

def insertar_linea(cursor, conexion):
    clave = input("Ingrese la clave de la línea de investigación: ")
    nombre = input("Ingrese el nombre de la línea de investigación: ")
    sql = "INSERT INTO lineainv (clave, nombre) VALUES (%s, %s)"
    valores = (clave, nombre)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Línea de investigación insertada correctamente.")

def obtener_lineas(cursor):
    cursor.execute("SELECT * FROM lineainv")
    lineas = cursor.fetchall()
    if lineas:
        for linea in lineas:
            print(linea)
    else:
        print("No hay líneas de investigación registradas.")

def actualizar_linea(cursor, conexion):
    clave = input("Ingrese la clave de la línea a actualizar: ")
    nuevo_nombre = input("Ingrese el nuevo nombre: ")
    sql = "UPDATE lineainv SET nombre = %s WHERE clave = %s"
    valores = (nuevo_nombre, clave)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Línea de investigación actualizada correctamente.")

def eliminar_linea(cursor, conexion):
    clave = input("Ingrese la clave de la línea a eliminar: ")
    sql = "DELETE FROM lineainv WHERE clave = %s"
    valores = (clave,)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Línea de investigación eliminada correctamente.")

def menu():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    while True:
        print("\n> > > Menú < < <")
        print("1. Insertar línea de investigación")
        print("2. Ver líneas de investigación")
        print("3. Actualizar línea de investigación")
        print("4. Eliminar línea de investigación")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            insertar_linea(cursor, conexion)
        elif opcion == "2":
            obtener_lineas(cursor)
        elif opcion == "3":
            actualizar_linea(cursor, conexion)
        elif opcion == "4":
            eliminar_linea(cursor, conexion)
        elif opcion == "5":
            cursor.close()
            conexion.close()
            print("Conexión cerrada. Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()