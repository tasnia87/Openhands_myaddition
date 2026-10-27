from copy import deepcopy
from app import available_units, can_fulfill, low_stock

def test_available_after_reservation():
    assert available_units({'A':10},{'A':4},'A') == 6

def test_over_reserved():
    assert available_units({'A':2},{'A':5},'A') == 0

def test_fulfillment_rejects_reserved_units():
    assert can_fulfill({'A':10},{'A':4},{'A':7}) is False

def test_low_stock_uses_available():
    assert low_stock({'B':10,'A':3},{'B':8},4) == ['A','B']

def test_no_reservations():
    assert available_units({'A':10},{},'A') == 10

def test_missing_and_empty():
    assert available_units({}, {}, 'X') == 0
    assert can_fulfill({}, {}, {}) is True

def test_inputs_unchanged():
    stock={'A':5}; reserved={'A':2}; request={'A':1}
    before=deepcopy((stock,reserved,request))
    available_units(stock,reserved,'A')
    can_fulfill(stock,reserved,request)
    low_stock(stock,reserved,4)
    assert (stock,reserved,request) == before
