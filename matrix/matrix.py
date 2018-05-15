def matrix_from_string(string):
    """
    A function that accepts a string containing lines of numbers and returns a
    list of lists of numbers.

    For example:
    >>> matrix_from_string("3 4 5")
    [[3.0, 4.0, 5.0]]
    >>> matrix_from_string("3 4 5\n6 7 8")
    [[3.0, 4.0, 5.0], [6.0, 7.0, 8.0]]
    """
    matrix = []
    rows = string.strip('\n').split('\n') if string else []
    for row in rows:
        line = row.strip().split()
        if line != []:
            matrix.append([float(n) for n in line])
    return matrix