def flip_dict_of_lists(dict_of_lists, dict_type=None, key_func=lambda k: k):
    """
    Returns a "flipped" dictionary of lists from the given dictionnary of lists.
    What I mean by "flipped" is this:

    >>> d = {'a': [1, 2], 'b': [3, 1], 'c': [2]}
    >>> flip_dict_of_lists(d)
    {1:  ['a', 'b'], 2: ['a', 'c'], 3: ['b']}
    """
    if dict_type is not None:
        flipped = dict_type()
    else:
        flipped = {}
    for old_key, old_values in dict_of_lists.items():
        for old_value in old_values:
            new_key = key_func(old_value)
            new_value = old_key
            flipped.setdefault(new_key, []).append(new_value)
    
    return flipped
