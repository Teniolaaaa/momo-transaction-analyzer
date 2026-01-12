"""Categorize transactions based on type and description"""
from etl.config import CATEGORIES

def categorize_transaction(tx):
    """
    Assign category to transaction based on type and description
    Returns category name
    """
    tx_type = str(tx.get('type', '')).lower()
    description = str(tx.get('description', '')).lower()
    
    combined_text = f"{tx_type} {description}"
    
    # Check each category's keywords
    for category, keywords in CATEGORIES.items():
        for keyword in keywords:
            if keyword in combined_text:
                return category
    
    # Default category if no match
    return "OTHER"

def add_categories(transactions):
    """Add category field to list of transactions"""
    for tx in transactions:
        tx['category'] = categorize_transaction(tx)
    
    return transactions
