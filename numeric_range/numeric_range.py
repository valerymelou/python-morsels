def numeric_range(numbers):
    """
    Returns the difference between the largest and the smallest number numbers
    of the given list.
    """
    max_number = None
    min_number = None

    for number in numbers:
        if max_number == None and min_number == None:
            max_number = min_number = number
        if number >= max_number:
            max_number = number
        if number <= min_number:
            min_number = number
    
    if max_number is not None and min_number is not None:
        return max_number - min_number
    return 0