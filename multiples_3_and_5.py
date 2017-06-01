def solution(number):
    """If we list all the natural numbers below 10 that are multiples of 3 or 5, 
    we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Finish the solution so that it returns the sum of all the multiples of 
    3 or 5 below the number passed in.

    Note: If the number is a multiple of both 3 and 5, only count it once.

    >>> solution(10)
    23
    """
    # multiples = []
    # for i in range(number):
    #     if i % 3 == 0 or i % 5 == 0:
    #         multiples.append(i)
    # return sum(multiples)

    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT!\n"