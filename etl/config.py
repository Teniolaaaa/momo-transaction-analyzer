"""Configuration for ETL pipeline"""
import os
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
LOGS_DIR = DATA_DIR / "logs"

# Database
DATABASE_PATH = DATA_DIR / "db.sqlite3"

# Transaction categories
CATEGORIES = {
    "AIRTIME": ["airtime", "credit"],
    "TRANSFER": ["sent", "transfer", "payment"],
    "RECEIVED": ["received", "deposit"],
    "WITHDRAWAL": ["withdraw", "cash"],
    "BILL_PAYMENT": ["bill", "utility", "electricity", "water"]
}

# Data quality thresholds
MIN_AMOUNT = 0
MAX_AMOUNT = 10000000
