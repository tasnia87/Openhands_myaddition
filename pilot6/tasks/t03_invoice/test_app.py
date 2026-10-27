import json
import pytest
from app import import_invoice

def test_numeric_price():
    assert import_invoice(json.dumps([{'sku':'A','unit_price':2.5,'quantity':4}])) == [{'sku':'A','total':10.0}]

def test_string_price():
    assert import_invoice(json.dumps([{'sku':'B','unit_price':'3.25','quantity':2}])) == [{'sku':'B','total':6.5}]

def test_empty():
    assert import_invoice('[]') == []

def test_invalid_price():
    with pytest.raises(ValueError):
        import_invoice(json.dumps([{'sku':'C','unit_price':'bad','quantity':1}]))

def test_missing_price():
    with pytest.raises(KeyError):
        import_invoice(json.dumps([{'sku':'D','quantity':1}]))
