def find_outlier(integers):
    """
    You are given an array (which will have a length of at least 3, but could be
    very large) containing integers. The array is either entirely comprised of 
    odd integers or entirely comprised of even integers except for a single 
    integer N. Write a method that takes the array as an argument and returns N.

    >>> find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])
    11

    >>> find_outlier([160, 3, 1719, 19, 11, 13, -21])
    160

    >>> find_outlier([2,6,8,10,3])
    3
    """

    # if sum(integers) % 2 != 0:
    #     for num in integers:
    #         if num % 2 != 0:
    #             return num
    # else:
    #     for num in integers:
    #         if num % 2 == 0:
    #             return num

    odds = [x for x in integers if x % 2 != 0]
    evens = [x for x in integers if x % 2 == 0]
    return odds[0] if len(odds) < len(evens) else evens[0]

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT!\n"