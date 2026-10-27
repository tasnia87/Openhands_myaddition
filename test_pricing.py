import pytest

from pricing import order_total


def test_no_discount():
    items = [{"price": 20, "quantity": 2}]
    assert order_total(items, discount_percent=0) == pytest.approx(40)


def test_ten_percent_discount():
    items = [{"price": 20, "quantity": 2}]
    assert order_total(items, discount_percent=10) == pytest.approx(36)


def test_full_discount():
    items = [{"price": 15, "quantity": 2}]
    assert order_total(items, discount_percent=100) == pytest.approx(0)


def test_empty_order():
    assert order_total([], discount_percent=10) == pytest.approx(0)