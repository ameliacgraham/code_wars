def printer_error(s):
    """
    In a factory a printer prints labels for boxes. For one kind of boxes the 
    printer has to use colors which, for the sake of simplicity, are named with 
    letters from a to m.

    The colors used by the printer are recorded in a control string. 
    For example a "good" control string would be aaabbbbhaijjjm meaning that the 
    printer used three times color a, four times color b, then one time color a...

    Sometimes there are problems: lack of colors, technical malfunction and a "bad" 
    control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm.

    You have to write a function printer_error which given a string will output the 
    error rate of the printer as a string representing a rational whose numerator is
    the number of errors and the denominator the length of the control string. 
    Don't reduce this fraction to a simpler expression.

    >>> printer_error("aaabbbbhaijjjm")
    '0/14'

    >>> printer_error("aaaxbbbbyyhwawiwjjjwwm")
    '8/22'
    """

    bad_colors = set(['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    mistakes = 0
    for color in s:
        if color in bad_colors:
            mistakes += 1
    return "{}/{}".format(mistakes, len(s))

    # return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT!\n"