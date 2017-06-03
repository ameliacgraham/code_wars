def array_diff(a, b):
    """
    It should remove all values from list a, which are present in list b.
    If a value is present in b, all of its occurrences must be removed from the other:

    >>> array_diff([1,2],[1])
    [2]

    >>> array_diff([1,2,2,2,3],[2])
    [1, 3]
    """
    seen = set(b)
    
    return [x for x in a if x not in seen]

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT!\n"