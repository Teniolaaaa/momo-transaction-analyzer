"""Parse XML transaction data"""
import xml.etree.ElementTree as ET
from pathlib import Path

def parse_transactions(xml_path):
    """
    Read and parse XML file containing MoMo transactions
    Returns list of transaction dictionaries
    """
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    transactions = []
    
    for transaction in root.findall('.//transaction'):
        tx_data = {
            'id': transaction.find('id').text if transaction.find('id') is not None else None,
            'date': transaction.find('date').text if transaction.find('date') is not None else None,
            'amount': transaction.find('amount').text if transaction.find('amount') is not None else None,
            'type': transaction.find('type').text if transaction.find('type') is not None else None,
            'phone': transaction.find('phone').text if transaction.find('phone') is not None else None,
            'description': transaction.find('description').text if transaction.find('description') is not None else None
        }
        transactions.append(tx_data)
    
    return transactions

def validate_transaction(tx):
    """Check if transaction has required fields"""
    required_fields = ['date', 'amount', 'type']
    return all(tx.get(field) is not None for field in required_fields)
