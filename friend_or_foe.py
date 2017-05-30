def friend(people):
    """
    Make a program that filters a list of strings and 
    returns a list with only your friends name in it.

    If a name has exactly 4 letters in it, 
    you can be sure that it has to be a friend of yours!

    >>> friend(["Alex", "Erin", "Medalis"])
    ['Alex', 'Erin']

    """

    return [person for person in people if len(person) == 4]

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT!\n"