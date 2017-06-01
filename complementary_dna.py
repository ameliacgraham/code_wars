def DNA_strand(dna):
    """
    In DNA strings, symbols "A" and "T" are complements of each other, 
    as "C" and "G". You have function with one side of the DNA (string, 
    except for Haskell); you need to get the other complementary side. 
    DNA strand is never empty or there is no DNA at all (again, except for Haskell).

    >>> DNA_strand("ATTGC")
    'TAACG'
    """

    pairs = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
    }

    complementay = ""

    for char in dna:
        value = pairs.get(char)
        complementay += value

    return complementay

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT!\n"