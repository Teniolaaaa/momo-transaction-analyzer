"""Main ETL pipeline script"""
import argparse
import json
import logging
from pathlib import Path

from parse_xml import parse_transactions, validate_transaction
from clean_normalize import clean_transaction
from categorize import add_categories
from load_db import get_connection, create_tables, insert_transactions
from config import PROCESSED_DIR, LOGS_DIR

# Setup logging
LOGS_DIR.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    filename=LOGS_DIR / 'etl.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def export_to_json(conn, output_path):
    """Export data to JSON for frontend"""
    cursor = conn.cursor()
    
    # Get summary stats
    cursor.execute('SELECT COUNT(*), SUM(amount) FROM transactions')
    total_count, total_amount = cursor.fetchone()
    
    # Get categories
    cursor.execute('SELECT DISTINCT category FROM transactions')
    categories = [row[0] for row in cursor.fetchall()]
    
    # Get recent transactions
    cursor.execute('''
        SELECT date, type, amount, category, phone 
        FROM transactions 
        ORDER BY date DESC 
        LIMIT 50
    ''')
    
    recent = []
    for row in cursor.fetchall():
        recent.append({
            'date': row[0],
            'type': row[1],
            'amount': row[2],
            'category': row[3],
            'phone': row[4]
        })
    
    dashboard_data = {
        'total_transactions': total_count or 0,
        'total_amount': total_amount or 0,
        'categories': categories,
        'recent_transactions': recent
    }
    
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(dashboard_data, f, indent=2)
    
    logging.info(f'Exported dashboard data to {output_path}')

def run_pipeline(xml_path):
    """Execute full ETL pipeline"""
    logging.info('Starting ETL pipeline')
    
    # Parse XML
    logging.info(f'Parsing XML from {xml_path}')
    transactions = parse_transactions(xml_path)
    logging.info(f'Found {len(transactions)} transactions')
    
    # Validate and clean
    valid_transactions = [tx for tx in transactions if validate_transaction(tx)]
    logging.info(f'{len(valid_transactions)} valid transactions')
    
    cleaned_transactions = [clean_transaction(tx) for tx in valid_transactions]
    
    # Categorize
    categorized_transactions = add_categories(cleaned_transactions)
    
    # Load to database
    conn = get_connection()
    create_tables(conn)
    inserted = insert_transactions(conn, categorized_transactions)
    logging.info(f'Inserted {inserted} transactions to database')
    
    # Export for frontend
    export_to_json(conn, PROCESSED_DIR / 'dashboard.json')
    
    conn.close()
    logging.info('ETL pipeline completed')
    print(f'✓ Processed {inserted} transactions successfully')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run MoMo ETL pipeline')
    parser.add_argument('--xml', required=True, help='Path to XML input file')
    
    args = parser.parse_args()
    
    xml_file = Path(args.xml)
    if not xml_file.exists():
        print(f'Error: File {xml_file} not found')
        exit(1)
    
    run_pipeline(xml_file)

