import json

def import_invoice(payload):
    return [build_line(row) for row in json.loads(payload)]

def build_line(row):
    normalized = normalize_row(row)
    return {'sku': normalized['sku'], 'total': calculate_total(normalized)}

def normalize_row(row):
    return {'sku': row['sku'], 'price': row['unit_price'], 'quantity': row['quantity']}

def calculate_total(line):
    return round(float(line['unit_price']) * line['quantity'], 2)
