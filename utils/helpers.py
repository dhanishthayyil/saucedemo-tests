def is_sorted_ascending(values):
    return values == sorted(values)

def is_sorted_descending(values):
    return values == sorted(values, reverse=True)