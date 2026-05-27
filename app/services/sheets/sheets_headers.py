
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from services.sheets.sheets_connection import sheet


def obtener_encabezados():
    if sheet is None:
        return ["ID", "Nombre", "Valor", "Fecha"]  # Encabezados por defecto
    return sheet.row_values(1)
