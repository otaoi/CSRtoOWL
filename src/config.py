import os
import sys
from dotenv import load_dotenv

load_dotenv()

CLINIC_URL = os.getenv("OWL_CLINIC_URL")

if not CLINIC_URL:
    print("URL not found")
    sys.exit(1)