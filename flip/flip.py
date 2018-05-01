def flip_dict_of_lists(dict, dict_type=None, key_func=None):
    """
    Returns a "flipped" dictionary of lists from the given dictionnary of lists.
    What I mean by "flipped" is this:

    >>> d = {'a': [1, 2], 'b': [3, 1], 'c': [2]}
    >>> flip_dict_of_lists(d)
    {1:  ['a', 'b'], 2: ['a', 'c'], 3: ['b']}
    """
    if dict_type is not None:
        flipped_dict = dict_type()
    else:
        flipped_dict = {}
    for key in dict.keys():
        for item in dict[key]:
            if key_func is not None:
                item = key_func(item)
            if item in flipped_dict:
                flipped_dict[item].append(key)
            else:
                flipped_dict[item] = [key]
    
    return flipped_dict