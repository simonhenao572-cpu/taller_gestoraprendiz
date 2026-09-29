"""
GESTOR DE APRENDICES - Cascaron base
Clase 3: CRUD con PyMongo | Ficha 3231102 (ADSO - SENA)

Objetivo del reto:
    Completar las 4 funciones del CRUD (registrar, listar, actualizar y
    eliminar). La CONEXION y el MENU ya estan hechos: no tienes que
    escribirlos, solo rellenar lo que esta marcado con  # TODO.

Antes de empezar:
    1. Crea y activa tu entorno virtual.
    2. Instala el driver:   pip install "pymongo[srv]"
    3. Reemplaza <password> por la clave real de tu usuario de BD.
    4. Ejecuta:             python gestor_aprendices_base.py
"""

from pymongo import MongoClient

# =====================================================================
#  CONEXION   (ya esta lista - solo cambia tu <password>)
# =====================================================================
URI = "mongodb+srv://admin_sena:hola123@cluster0.2zhh6i9.mongodb.net/"

cliente = MongoClient(URI)
db = cliente["sena_adso_db"]
aprendices = db["aprendices"]

# Prueba de vida: confirma que la conexion funciona al arrancar
try:
    cliente.admin.command("ping")
    print("OK - Conexion exitosa a MongoDB Atlas\n")
except Exception as e:
    print("ERROR - No se pudo conectar:", e)
    print("Revisa: (1) tu <password>  (2) tu IP en Atlas  (3) pymongo[srv]\n")


# =====================================================================
#  OPERACIONES CRUD    <-- ESTO ES LO QUE DEBES COMPLETAR
# =====================================================================

def registrar():
    """CREATE - Pide los datos e inserta un aprendiz."""
    # TODO:
    #   1. Pide nombre, ficha y edad con input().
    #   2. Recuerda: input() devuelve TEXTO. Convierte ficha y edad con int().
    #   3. Arma un diccionario:  {"nombre": ..., "ficha": ..., "edad": ...}
    #   4. Inserta con:          aprendices.insert_one(...)
    try:
        nombre = input("Nombre: ")
        ficha = int(input("Ficha: "))
        edad = int(input("Edad: "))
    except ValueError:
        print("Ficha y edad deben ser numeros. Intenta de nuevo.\n")
        return
    aprendices.insert_one({"nombre": nombre, "ficha": ficha, "edad": edad})
    print("Aprendiz registrado.\n")


def listar():
    """READ - Muestra todos los aprendices de la coleccion."""
    # TODO:
    #   1. Recorre aprendices.find() con un ciclo for.
    #   2. Imprime el nombre, la ficha y la edad de cada uno.
    for a in aprendices.find():
        print(f"Nombre: {a.get('nombre')} | Ficha: {a.get('ficha')} | Edad: {a.get('edad')}")
    print()


def actualizar():
    """UPDATE - Cambia la edad de un aprendiz buscado por su nombre."""
    # TODO:
    #   1. Pide el nombre del aprendiz y la nueva edad (int()).
    #   2. Usa:  aprendices.update_one({"nombre": ...}, {"$set": {"edad": ...}})
    #   3. No olvides $set (si no, no funciona como esperas).
    nombre = input("Nombre del aprendiz: ")
    try:
        edad = int(input("Nueva edad: "))
    except ValueError:
        print("La edad debe ser un numero.\n")
        return
    r = aprendices.update_one({"nombre": nombre}, {"$set": {"edad": edad}})
    if r.matched_count == 0:
        print("No se encontro ese aprendiz.\n")
    else:
        print("Edad actualizada.\n")


def eliminar():
    """DELETE - Elimina un aprendiz buscado por su nombre."""
    # TODO:
    #   1. Pide el nombre del aprendiz a eliminar.
    #   2. Usa:  aprendices.delete_one({"nombre": ...})
    nombre = input("Nombre del aprendiz a eliminar: ")
    r = aprendices.delete_one({"nombre": nombre})
    if r.deleted_count == 0:
        print("No se encontro ese aprendiz.\n")
    else:
        print("Aprendiz eliminado.\n")


# =====================================================================
#  MENU Y BUCLE PRINCIPAL   (ya esta listo - no necesitas cambiarlo)
# =====================================================================

def menu():
    print("""
=== GESTOR DE APRENDICES ===
1. Registrar aprendiz   (Create)
2. Listar aprendices    (Read)
3. Actualizar edad      (Update)
4. Eliminar aprendiz    (Delete)
5. Salir
""")


while True:
    menu()
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        registrar()
    elif opcion == "2":
        listar()
    elif opcion == "3":
        actualizar()
    elif opcion == "4":
        eliminar()
    elif opcion == "5":
        print("Hasta la proxima!")
        break
    else:
        print("Opcion no valida, intenta de nuevo.\n")
