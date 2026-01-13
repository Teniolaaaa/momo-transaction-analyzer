# Categorize transactions based on type and description
from config import CATEGORIES

def categorize_transaction(tx):
    # TODO: Add more patterns for withdrawals and deposits
    # NOTE: Some transactions might not match any category
    """
    Assign category to transaction based on type and description
    Returns category name as string
    """
    # Get the transaction type and description, convert to lowercase
    tx_type = str(tx.get('type', '')).lower()
    description = str(tx.get('description', '')).lower()
    
    # Combine them to search through
    combined_text = f"{tx_type} {description}"
    
    # Loop through each category and check if keywords match
    for category, keywords in CATEGORIES.items():
        for keyword in keywords:
            if keyword in combined_text:
                return category
    
    # If no match found, return OTHER as default
    return "OTHER"

def add_categories(transactions):
    """Add category field to each transaction in the list"""
    for tx in transactions:
        tx['category'] = categorize_transaction(tx)
    
    return transactions



