def numeric_range(numbers):
    """
    Returns the difference between largest and smallest of given numbers.
    """
    try:
        iterator = iter(numbers)
        maximum = minimum = next(iterator)
    except StopIteration:
        maximum = minimum = 0

    for number in numbers:
        if number > maximum:
            maximum = number
        if number < minimum:
            minimum = number
    
    return maximum - minimum
