import os
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "change-this-secret-for-production")
    DATABASE_PATH = os.getenv("DATABASE_PATH", str(ROOT_DIR / "database" / "chatbot.db"))
# SANDHU