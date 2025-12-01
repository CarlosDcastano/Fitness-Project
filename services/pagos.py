from utils.csv_utils import *
from miembros import *
import os



RUTA_MIEMBROS = os.path.join("data", "miembros.csv")
RUTA_PAGOS = os.path.join("data", "pagos.csv")



def registrar_pago():
    miembros = leer_csv(RUTA_MIEMBROS)
    



