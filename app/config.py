import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    APP_ENV = os.getenv("APP_ENV", "development")
    APP_PORT = int(os.getenv("APP_PORT", 8100))
    AI_BASE_URL = os.getenv("AI_BASE_URL", "")
    AI_TIMEOUT = int(os.getenv("AI_TIMEOUT", 40))
    VERIFY_SSL = os.getenv("VERIFY_SSL", "false").lower() == "true"
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")