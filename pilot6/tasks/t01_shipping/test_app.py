import pytest
from app import shipping_cost

@pytest.mark.parametrize('subtotal,express,expected', [
    (0, False, 5), (49.99, False, 5), (50, False, 0),
    (50.01, False, 0), (20, True, 13), (50, True, 8), (70, True, 8)
])
def test_shipping(subtotal, express, expected):
    assert shipping_cost(subtotal, express) == pytest.approx(expected)
