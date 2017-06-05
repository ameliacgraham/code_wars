def make_readable(seconds):
    """
    Write a function, which takes a non-negative integer (seconds) as input 
    and returns the time in a human-readable format (HH:MM:SS)

    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59
    The maximum time never exceeds 359999 (99:59:59)

    >>> make_readable(0)
    '00:00:00'

    >>> make_readable(5)
    '00:00:05'

    >>> make_readable(60)
    '00:01:00'

    >>> make_readable(86399)
    '23:59:59'

    >>> make_readable(359999)
    '99:59:59'
    """
    # hh = seconds / 3600
    # mm = (seconds % 3600) / 60
    # ss = (seconds % 3600) % 60

    # if hh < 10:
    #     hh = "0" + str(hh)
    # if mm < 10:
    #     mm = "0" + str(mm)
    # if ss < 10:
    #     ss = "0" + str(ss)
    # return "{}:{}:{}".format(hh, mm, ss)

    return '{:02}:{:02}:{:02}'.format(seconds / 3600, seconds / 60 % 60, seconds % 60)

    
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT!\n"