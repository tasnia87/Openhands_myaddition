def available_units(stock, reserved, sku):
    return max(0, stock.get(sku, 0) + reserved.get(sku, 0))

def can_fulfill(stock, reserved, request):
    return all(available_units(stock, reserved, sku) >= count for sku, count in request.items())

def low_stock(stock, reserved, threshold):
    return sorted(sku for sku in stock if available_units(stock, reserved, sku) < threshold)
