import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "ug_feedback_db")
}

SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
DEBUG = os.getenv("DEBUG", "True") == "True"

# Session Configuration
SESSION_LIFETIME = timedelta(hours=2)
PERMANENT_SESSION_LIFETIME = timedelta(hours=2)

# Password Requirements
MIN_PASSWORD_LENGTH = 6
BCRYPT_ROUNDS = 12

# Academic Year Settings
CURRENT_ACADEMIC_YEAR = os.getenv("ACADEMIC_YEAR", "2025-26")
CURRENT_SEMESTER = int(os.getenv("SEMESTER", "2"))