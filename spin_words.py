def spin_words(sentence):
    """
    Write a function that takes in a string of one or more words, and returns the 
    same string, but with all five or more letter words reversed. 
    Strings passed in will consist of only letters and spaces. 
    Spaces will be included only when more than one word is present.

    >>> spin_words("Hey fellow warriors")
    'Hey wollef sroirraw'

    >>> spin_words("This is a test")
    'This is a test'

    >>> spin_words("This is another test")
    'This is rehtona test'
    """

    words = sentence.split(" ")
    spun = []
    for word in words:
        if len(word) < 5:
            spun.append(word)
        else:
            backwards = ""
            for i in range(1, len(word) + 1):
                backwards += word[-i]
            spun.append(backwards)
    return " ".join(spun)

    # return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT!\n"