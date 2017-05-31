def unique_in_order(iterable):
    """
    Implement the function unique_in_order which takes as argument a
    sequence and returns a list of items without any elements with the 
    same value next to each other and preserving the original order of elements.

    >>> unique_in_order('AAAABBBCCDAABBB')
    ['A', 'B', 'C', 'D', 'A', 'B']

    >>> unique_in_order(['A', 'A', 'B', 'C', 'D', 'A', 'B'])
    ['A', 'B', 'C', 'D', 'A', 'B']
    """
    ordered_unique = []
    prev = None

    for i in range(len(iterable)):
        if iterable[i] != prev:
            ordered_unique.append(iterable[i])
            prev = iterable[i]
    return ordered_unique

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT!\n"