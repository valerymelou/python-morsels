def deep_flatten(iterable):
    """
    a function that accepts a list of lists (or lists of tuples and lists) and
    returns a flattened version of that list of lists.
    """
    flattened = []
    try:
        iterator = iter(iterable)
        for item in iterator:
            if isinstance(item, str):
                flattened.append(item)
            else:
                flattened = flattened + deep_flatten(item)
    except TypeError:
        flattened.append(iterable)

    return flattened
