"""Clean and normalize transaction data"""
from dateutil import parser
import re

def clean_amount(amount_str):
    """Convert amount string to float, removing currency symbols"""
    if not amount_str:
        return 0.0
    
    # Remove currency symbols and commas
    cleaned = re.sub(r'[^\d.]', '', str(amount_str))
    
    try:
        return float(cleaned)
    except ValueError:
        return 0.0

def normalize_date(date_str):
    """Parse date string to standard format YYYY-MM-DD"""
    if not date_str:
        return None
    
    try:
        parsed_date = parser.parse(date_str)
        return parsed_date.strftime('%Y-%m-%d')
    except:
        return None

def normalize_phone(phone_str):
    """Clean phone number to standard format"""
    if not phone_str:
        return None
    
    # Remove spaces and special characters
    cleaned = re.sub(r'[^\d+]', '', str(phone_str))
    
    # Add + if missing and starts with country code
    if cleaned and not cleaned.startswith('+'):
        cleaned = '+' + cleaned
    
    return cleaned

def clean_transaction(tx):
    """Apply all cleaning functions to a transaction"""
    cleaned = tx.copy()
    
    cleaned['amount'] = clean_amount(tx.get('amount'))
    cleaned['date'] = normalize_date(tx.get('date'))
    cleaned['phone'] = normalize_phone(tx.get('phone'))
    
    return cleaned
