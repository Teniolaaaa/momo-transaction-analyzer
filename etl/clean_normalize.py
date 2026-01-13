# Clean and normalize transaction data
from dateutil import parser
import re

def clean_amount(amount_str):
    """Convert amount string to float, removing currency symbols and commas"""
    if not amount_str:
        return 0.0
    
    # Remove currency symbols, commas, and any other non-numeric chars
    cleaned = re.sub(r'[^\d.]', '', str(amount_str))
    
    try:
        return float(cleaned)
    except ValueError:
        # If conversion fails, return 0
        return 0.0

def normalize_date(date_str):
    """Parse date string to standard format YYYY-MM-DD"""
    if not date_str:
        return None
    
    try:
        # Use dateutil parser to handle different date formats
        parsed_date = parser.parse(date_str)
        return parsed_date.strftime('%Y-%m-%d')
    except:
        # If parsing fails, return None
        return None

def normalize_phone(phone_str):
    """Clean phone number to standard format with country code"""
    if not phone_str:
        return None
    
    # Remove spaces, dashes, and other special characters
    cleaned = re.sub(r'[^\d+]', '', str(phone_str))
    
    # Add + if missing (assuming it starts with country code)
    if cleaned and not cleaned.startswith('+'):
        cleaned = '+' + cleaned
    
    return cleaned

def clean_transaction(tx):
    """Apply all cleaning functions to a transaction"""
    cleaned = tx.copy()
    
    # Clean each field
    cleaned['amount'] = clean_amount(tx.get('amount'))
    cleaned['date'] = normalize_date(tx.get('date'))
    cleaned['phone'] = normalize_phone(tx.get('phone'))
    
    return cleaned

