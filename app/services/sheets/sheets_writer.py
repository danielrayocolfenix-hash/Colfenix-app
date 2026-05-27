
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from services.sheets.sheets_connection import sheet
import logging

logger = logging.getLogger(__name__)

def insertar_mantenimiento(datos):
    if sheet is None:
        logger.warning("Google Sheets no disponible. Datos no se guardaron.")
        return
    sheet.append_row(datos)