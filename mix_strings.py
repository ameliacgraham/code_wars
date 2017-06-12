def count_occurences(string):
    count = 0
    for char in string:
        count += 1
    return count

def mix(s1, s2):
    """
    >>> mix("Are they here", "yes, they are here")
    '2:eeeee/2:yy/=:hh/=:rr'

    >>> mix("looping is fun but dangerous", "less dangerous than coding")
    '1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg'

    >>> mix(" In many languages", " there's a pair of functions")
    '1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt'

    >>> mix("Lords of the Fallen", "gamekult")
    '1:ee/1:ll/1:oo'
    """

    from operator import itemgetter, attrgetter
    s1_counts = {}
    s2_counts = {}
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    max_counts = []
    pairs = []
    for char in s1:
        if char in alpha:
            s1_counts[char] = s1_counts.get(char, 0) + 1
    for char in s2:
        if char in alpha:
            s2_counts[char] = s2_counts.get(char, 0) + 1

    for key, value in s1_counts.items():
        if value > s2_counts.get(key) and value > 1:
            max_counts.append(("1", value, "{}".format(key * value)))
        elif value == s2_counts.get(key) and value > 1:
            max_counts.append(("=", value, "{}".format(key * value)))
    for key, value in s2_counts.items():
        if value > s1_counts.get(key) and value > 1:
            max_counts.append(("2", value, "{}".format(key * value)))

    sorted_list = sorted(max_counts, key=itemgetter(2))
    sorted_list = sorted(sorted_list, key=itemgetter(1), reverse=True)
    for tup in sorted_list:
        pairs.append("{}:{}".format(tup[0], tup[2]))
    return "/".join(pairs)



if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"