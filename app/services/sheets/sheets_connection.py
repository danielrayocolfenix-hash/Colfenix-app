import gspread
from google.oauth2.service_account import Credentials
import sys
from pathlib import Path
import logging

# Añadir directorio app al path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from config.sheets_config import SHEET_NAME

logger = logging.getLogger(__name__)

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

sheet = None

try:
    credenciales = Credentials.from_service_account_file(
        "credenciales.json",
        scopes=SCOPES
    )

    cliente = gspread.authorize(credenciales)
    sheet = cliente.open(SHEET_NAME).sheet1
    logger.info("Google Sheets conectado correctamente")
except Exception as e:
    logger.warning(f"Error al conectar con Google Sheets: {str(e)}")
    logger.warning("La aplicación funcionará sin conexión a Sheets por ahora.")
    sheet = None

