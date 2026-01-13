"""Database operations for storing transactions"""
import sqlite3
from config import DATABASE_PATH

def create_tables(conn):
    """Create transactions table if it doesn't exist"""
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id TEXT PRIMARY KEY,
            date TEXT,
            amount REAL,
            type TEXT,
            phone TEXT,
            description TEXT,
            category TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()

def insert_transactions(conn, transactions):
    """Insert or update transactions in database"""
    cursor = conn.cursor()
    
    for tx in transactions:
        cursor.execute('''
            INSERT OR REPLACE INTO transactions 
            (id, date, amount, type, phone, description, category)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            tx.get('id'),
            tx.get('date'),
            tx.get('amount'),
            tx.get('type'),
            tx.get('phone'),
            tx.get('description'),
            tx.get('category')
        ))
    
    conn.commit()
    return len(transactions)

def get_connection():
    """Create and return database connection"""
    conn = sqlite3.connect(DATABASE_PATH)
    return conn

