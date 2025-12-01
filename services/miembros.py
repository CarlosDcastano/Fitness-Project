from utils.csv_utils import leer_csv, escribir_csv, sobrescribir_csv
import os
from datetime import datetime, timedelta

RUTA_MIEMBROS = os.path.join("data", "miembros.csv")



def registrar_miembro():
    miembros = leer_csv(RUTA_MIEMBROS)
    print("===Registrar un miembro===")
    nombre=""
    documento = ""
    telefono = ""
    correo = ""
    plan = ""
    fecha_inicio = datetime.now().strftime("%Y-%m-%d")
    fecha_fin = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
    estado = ""

    planes = ("BASICO", "PREMIUM", "FULL")
    estados = ("ACTIVO", "INACTIVO")


    while not nombre:
        nombre = input("Ingrese el nombre: ").upper()
    while not documento:
        documento = input("Ingrese el documento: ")
    while not telefono or not telefono.isdigit():
        telefono = input("Ingrese el telefono: ")
    while not correo:
        correo = input("Ingrese el correo: ")
    while not plan or plan not in planes:
        plan = input("Ingrese plan (BÁSICO | PREMIUM | FULL): ").upper()
    while not estado or estado not in estados:
        estado = input("Ingrese el Estado: ").upper()
    
    
    
    if miembros:
        miembro_id = max(int(m["miembro_id"]) for m in miembros)
    else:
        miembro_id = 0

    existe = next((m for m in miembros if m["documento"] == documento), None)

    if existe:
        print("El miembro ya existe, no es posible agregarlo")
        return None
    
    else:
        nuevo_miembro = {
            "miembro_id" : miembro_id+1,
            "nombre" : nombre,
            "documento" : documento,
            "telefono" : telefono,
            "correo" : correo,
            "plan" : plan,
            "fecha_inicio" : fecha_inicio,
            "fecha_fin_plan" : fecha_fin,
            "estado" : estado,
        }
    
        escribir_csv([nuevo_miembro], RUTA_MIEMBROS)
    
        return nuevo_miembro

def listar_miembros():
    miembros = leer_csv(RUTA_MIEMBROS)
    if not miembros:
        print("No hay miembros por mostrar, esta vacío")
    else:
        for m in miembros:
            print(f"ID: {m['miembro_id']} |Nombre: {m['nombre']} |Estado: {m["estado"]}")

def buscar_miembro():
    miembros = leer_csv(RUTA_MIEMBROS)
    documento = ""
    while not documento:
        documento = input("Ingrese el documento: ")
    for m in miembros:
        if documento == m["documento"]:
            return m
    print(f"Documento {documento} No coincide con ninguno de los miembros") 

def actualizar_miembro():
    miembro = buscar_miembro()

    miembro["nombre"] = input("Ingrese el nuevo nombre: ")
    while not miembro["nombre"]:
        miembro["nombre"] = input("Debe ingresar un nombre: ")
    
