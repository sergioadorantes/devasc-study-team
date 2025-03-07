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

def crear_tipo_proyecto():
    tipo = input("Ingresa el código del tipo de proyecto (máx 10 caracteres): ").strip()
    nombre = input("Ingresa el nombre del tipo de proyecto: ").strip()
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO tipoproyecto (tipo, nombre) VALUES (%s, %s)", (tipo, nombre))
        conn.commit()
        print("Tipo de proyecto creado correctamente.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

def obtener_tipos_proyecto():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tipoproyecto")
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    
    print("\nLista de Tipos de Proyecto:")
    for row in resultados:
        print(f"Código: {row[0]} | Nombre: {row[1]}")
    print()

def obtener_tipo_proyecto():
    tipo = input("Ingresa el código del tipo de proyecto a buscar: ").strip()
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tipoproyecto WHERE tipo = %s", (tipo,))
    resultado = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if resultado:
        print(f"Tipo de Proyecto encontrado: Código: {resultado[0]} | Nombre: {resultado[1]}")
    else:
        print("No se encontró el tipo de proyecto.")

def actualizar_tipo_proyecto():
    tipo = input("Ingresa el código del tipo de proyecto a actualizar: ").strip()
    nuevo_nombre = input("Ingresa el nuevo nombre: ").strip()
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("UPDATE tipoproyecto SET nombre = %s WHERE tipo = %s", (nuevo_nombre, tipo))
        conn.commit()
        if cursor.rowcount > 0:
            print("Tipo de proyecto actualizado correctamente.")
        else:
            print("No se encontró el tipo de proyecto.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

def eliminar_tipo_proyecto():
    tipo = input("Ingresa el código del tipo de proyecto a eliminar: ").strip()
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("DELETE FROM tipoproyecto WHERE tipo = %s", (tipo,))
        conn.commit()
        if cursor.rowcount > 0:
            print("Tipo de proyecto eliminado correctamente.")
        else:
            print("No se encontró el tipo de proyecto.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

def menu():
    while True:
        print("\n MENÚ CRUD - Tipos de Proyecto")
        print("1️⃣ Crear tipo de proyecto")
        print("2️⃣ Ver todos los tipos de proyecto")
        print("3️⃣ Buscar un tipo de proyecto")
        print("4️⃣ Actualizar un tipo de proyecto")
        print("5️⃣ Eliminar un tipo de proyecto")
        print("0️⃣ Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            crear_tipo_proyecto()
        elif opcion == "2":
            obtener_tipos_proyecto()
        elif opcion == "3":
            obtener_tipo_proyecto()
        elif opcion == "4":
            actualizar_tipo_proyecto()
        elif opcion == "5":
            eliminar_tipo_proyecto()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
