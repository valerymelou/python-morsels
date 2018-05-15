def with_previous(iterable, **kwargs):
    """
    A function that accepts a sequence (a list for example) and returns a new
    iterable (anything you can loop over) that includes a tuple of each item
    and the previous item (the item just before it). The first "previous item"
    should be None.

    For example:
    >>> with_previous("hello")
    [('h', None), ('e', 'h'), ('l', 'e'), ('l', 'l'), ('o', 'l')]
    >>> with_previous([1, 2, 3])
    [(1, None), (2, 1), (3, 2)]
    """
    previous = kwargs.get('fillvalue', None)
    for item in iterable:
        yield item, previous
        previous = item
