"""Useful Utilities
"""
from collections import Counter
import string
import re


def string_to_list_in_pairs(s):
    """Convert string into list of pairs

    Args:
        s (str): the string to be split into pairs

    Returns:
        str: list of pairs from the input string
    """
    # https://stackoverflow.com/questions/26987901/convert-string-in-to-listin-pairs-in-python
    return [''.join(pair) for pair in zip(s[:-1], s[1:])]


def common_pairs(l1, l2):
    """Gives the list intersection of two lists including duplicates

    Args:
        l1 (list): list1
        l2 (list): list2

    Returns:
        list: containing the intersection
    """
    # https://stackoverflow.com/questions/37645053/intersection-of-two-lists-including-duplicates/37645155
    return list((Counter(l1) & Counter(l2)).elements())


def ssimilarity(s1, s2):
    """Compute similarity of two strings

    Args:
        s1 (str): string1
        s2 (str): string2

    Returns:
        float: the percentage similarity between the two strings
    """
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    pairs_s1 = string_to_list_in_pairs(s1)
    pairs_s2 = string_to_list_in_pairs(s2)
    num_common_pairs = len(common_pairs(pairs_s1, pairs_s2))
    num_pairs = len(pairs_s1) + len(pairs_s2)
    if num_pairs == 0:
        return 0

    return (2 * (num_common_pairs)) / (num_pairs)


def strip_punctuations(s, strip_space=False):
    """Strip pnuctuations from a string

    Args:
        s (str): string
        strip_space (bool, optional): whether to remove space

    Returns:
        str: String with the punctuation removed
    """
    _s = ''
    punctuations = string.punctuation
    if strip_space:
        punctuations += ' '
    for ch in s:
        if ch in list(punctuations):
            if strip_space is False:
                _s += ' '
        else:
            _s += ch
    # Replaces any number of spaces with one space
    _s = re.sub(r"\s+", ' ', _s)
    return _s
