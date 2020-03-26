#! usr/bin/env python3
#Arnas Steponavicius
#Adapted from Ian McLoughlin

from match import match

if __name__ == "__main__":
    tests = [
        ["a.b|b*", "bbbbbbb", True],
        ["a.b|b*", "bbbn", False],
        ["a.b", "ab", True],
        ["a.b", "anb", False],
        ["a*", "bbbbb", False],
        ["a*", "aaaa", True],
        ["a+.b", "aaab", True],
        ["a+.b", "aaabbbbb", False],
        ["a?", "aaaaaa", False],
        ["a?", "a", True],
    ]

    for test in tests:
        assert match(test[0], test[1]) == test[2], test[0] + \
        (" should match " if test[2] else " should not match ") + test[1]