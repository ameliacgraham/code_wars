def sum_two_smallest_numbers(numbers):
    """
    Create a function that returns the sum of the two lowest positive
    numbers given an array of minimum 4 integers. 
    No floats or empty arrays will be passed.

    >>> sum_two_smallest_numbers([5, 8, 12, 18, 22])
    13

    >>> sum_two_smallest_numbers([7, 15, 12, 18, 22])
    19

    >>> sum_two_smallest_numbers([25, 42, 12, 18, 22])
    30


    """
    # if numbers[0] < numbers[1]:
    #     first_smallest = numbers[0]
    #     second_smallest = numbers[1]
    # else:
    #     first_smallest = numbers[1]
    #     second_smallest = numbers[0]
    
    # for num in numbers[2:]:
    #     if num < first_smallest and num < second_smallest:
    #         second_smallest = first_smallest
    #         first_smallest = num
    #     elif num < second_smallest:
    #         second_smallest = num

    # return first_smallest + second_smallest

    return sum(sorted(numbers)[:2])

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT!\n"