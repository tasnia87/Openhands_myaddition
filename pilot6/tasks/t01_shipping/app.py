def shipping_cost(subtotal, express=False):
    standard = 0.0 if subtotal > 50 else 5.0
    return standard + (8.0 if express else 0.0)
