import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from services.sheets.sheets_connection import sheet
import logging

logger = logging.getLogger(__name__)

def obtener_datos():
    if sheet is None:
        logger.warning("Google Sheets no disponible. Retornando datos de ejemplo.")
        return [["1", "Item ejemplo", "Val 1", "2026-05-26"]]
    return sheet.get_all_values()[1:]