def subtotal(items):
    return sum(item["price"] * item["quantity"] for item in items)


def discount_amount(amount, discount_percent):
    return amount * discount_percent


def order_total(items, discount_percent=0):
    amount = subtotal(items)
    discount = discount_amount(amount, discount_percent)
    return round(amount - discount, 2)