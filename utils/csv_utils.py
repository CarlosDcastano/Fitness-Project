import csv

def read_csv(path):
    """
    Lee un archivo CSV y devuelve una lista de diccionarios.
    Cada fila del CSV será un diccionario cuyas claves son los encabezados.
    """
    try:
        with open(path, newline='', encoding='utf-8') as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        print(f"[ERROR] No se encontró el archivo: {path}")
        return []


def write_csv(path, data, fieldnames):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)