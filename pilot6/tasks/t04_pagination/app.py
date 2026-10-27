def page_count(total_items, page_size):
    if total_items < 0 or page_size <= 0:
        raise ValueError('invalid pagination arguments')
    return total_items // page_size
