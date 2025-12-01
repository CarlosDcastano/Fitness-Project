import csv
import os
from csv import DictReader

def leer_csv(ruta_del_archivo):
    """
    Lee un archivo CSV y devuelve una lista de diccionarios.
    Cada fila del CSV será un diccionario cuyas claves son los encabezados.
    """
    try:
        with open(ruta_del_archivo, newline='', encoding='utf-8') as archivo:
            return list(csv.DictReader(archivo))
    except FileNotFoundError:
        print(f"[ERROR] No se encontró el archivo: {ruta_del_archivo}")
        return []

def escribir_csv(nuevos_datos, ruta):
    """
    Agrega filas nuevas a cualquier CSV sin sobrescribir encabezados ni contenido existente.
    Usa leer_csv para obtener los encabezados del archivo existente.

    Parámetros:
    - nuevos_datos: lista de diccionarios con los datos a agregar
    - ruta: ruta del archivo CSV
    """

    if len(nuevos_datos) == 0:
        raise ValueError("No hay datos para agregar")

    # Leer contenido existente usando leer_csv
    datos_existentes = leer_csv(ruta)
    archivo_vacio = len(datos_existentes) == 0

    # Determinar encabezados
    if not archivo_vacio:
        encabezados = list(datos_existentes[0].keys())
    else:
        encabezados = list(nuevos_datos[0].keys())

    # Abrir el archivo en modo 'a' para agregar al final
    with open(ruta, 'a', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=encabezados)

        # Escribir encabezado solo si el archivo estaba vacío
        if archivo_vacio:
            escritor.writeheader()

        # Escribir las filas nuevas
        escritor.writerows(nuevos_datos)


def sobrescribir_csv(datos, ruta):
    if len(datos) == 0:
        raise ValueError("No hay datos para escribir.")

    encabezados = list(datos[0].keys())

    with open(ruta, 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=encabezados)
        escritor.writeheader()
        escritor.writerows(datos)





