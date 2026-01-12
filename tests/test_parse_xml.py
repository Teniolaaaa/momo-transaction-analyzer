"""Tests for XML parsing"""
import pytest
from etl.parse_xml import validate_transaction

def test_validate_transaction_valid():
    tx = {
        'date': '2024-01-01',
        'amount': '1000',
        'type': 'transfer'
    }
    assert validate_transaction(tx) == True

def test_validate_transaction_missing_field():
    tx = {
        'date': '2024-01-01',
        'amount': '1000'
    }
    assert validate_transaction(tx) == False
