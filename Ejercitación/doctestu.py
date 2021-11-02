import doctest
def suma(n, m):
    """
    >>> suma(2,2)
    4
    >>> suma(2, 3)
    5
    >>> suma(1, 1)
    3
    """
    return n+m
print(doctest.testmod())