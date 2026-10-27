# Invoice import

Import a JSON string containing a list of invoice rows. Each external row contains sku, unit_price, and quantity. unit_price may be a number or a numeric string. Return a list of dictionaries with sku and total; total is unit_price times quantity rounded to two decimal places. Empty input list returns an empty list. Invalid numeric prices must raise ValueError; missing required fields must raise KeyError.

Repair app.py only. Preserve the existing public function signatures. Run the provided recorder before editing and after each repair attempt.
