from datetime import datetime
from app.services.sheets.sheets_reader import obtener_datos


def mantenimientos_hoy():

    hoy = datetime.now().strftime("%Y-%m-%d")

    datos = obtener_datos()

    total = 0

    for fila in datos:

        if len(fila) > 0 and fila[0] == hoy:
            total += 1

    return total


def mantenimientos_mes():
    mes = datetime.now().strftime("%Y-%m")
    datos = obtener_datos()
    total = 0
    for fila in datos:
        if len(fila) > 0 and fila[0].startswith(mes):
            total += 1

    return total

