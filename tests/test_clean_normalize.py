"""Tests for data cleaning functions"""
import pytest
from etl.clean_normalize import clean_amount, normalize_phone

def test_clean_amount():
    assert clean_amount('$1,000.50') == 1000.50
    assert clean_amount('1000') == 1000.0
    assert clean_amount('invalid') == 0.0

def test_normalize_phone():
    assert normalize_phone('0788123456').startswith('+')
    assert normalize_phone('+250788123456') == '+250788123456'
    assert normalize_phone(None) == None
