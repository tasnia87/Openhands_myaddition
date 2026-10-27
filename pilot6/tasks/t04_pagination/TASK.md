# Pagination boundaries

Return the number of pages required for total_items items with page_size items per page. A partially filled last page counts as one page. Zero items requires zero pages. total_items is a nonnegative integer and page_size is a positive integer. Negative total_items or nonpositive page_size must raise ValueError.

Repair app.py only. Preserve the existing public function signatures. Run the provided recorder before editing and after each repair attempt.
