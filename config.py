from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / '.env')

class Settings:
    FLASK_HOST = os.getenv('FLASK_HOST', '0.0.0.0')
    FLASK_PORT = int(os.getenv('FLASK_PORT', '5000'))
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'

    APSIM_EXE = os.getenv('APSIM_EXE', '')
    APSIM_TEMPLATE = BASE_DIR / os.getenv('APSIM_TEMPLATE', 'apsim_templates/egypt_wheat_template.apsimx')
    OUTPUT_DIR = BASE_DIR / os.getenv('OUTPUT_DIR', 'outputs')

    WHATSAPP_VERIFY_TOKEN = os.getenv('WHATSAPP_VERIFY_TOKEN', '')
    WHATSAPP_PHONE_NUMBER_ID = os.getenv('WHATSAPP_PHONE_NUMBER_ID', '')
    WHATSAPP_ACCESS_TOKEN = os.getenv('WHATSAPP_ACCESS_TOKEN', '')

    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
    LLM_MODEL = os.getenv('LLM_MODEL', 'gpt-4.1-mini')

    DEFAULT_LANGUAGE = os.getenv('DEFAULT_LANGUAGE', 'en')
    DEFAULT_CROP = os.getenv('DEFAULT_CROP', 'wheat')
    DEFAULT_GOVERNORATE = os.getenv('DEFAULT_GOVERNORATE', 'Kafr El-Sheikh')

settings = Settings()
settings.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
