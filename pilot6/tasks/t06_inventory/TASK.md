# Shared inventory availability

Stock and reservation mappings contain nonnegative integer quantities keyed by SKU. Available quantity is stock minus reserved quantity, clamped to zero. Missing entries count as zero. available_units returns this quantity. can_fulfill accepts a mapping of SKU to requested nonnegative quantities and returns whether every request can be met; an empty request can be met. low_stock returns stock SKUs whose available quantity is strictly below threshold, sorted alphabetically. These operations must not modify their inputs.

Repair app.py only. Preserve the existing public function signatures. Run the provided recorder before editing and after each repair attempt.
