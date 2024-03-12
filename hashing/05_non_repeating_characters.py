"""
Given a string S consisting of lowercase Latin Letters. Return the first non-repeating character in S. If there is no non-repeating character, return '$'.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Number of distinct characters).
Note: N = |S|
"""

from collections import OrderedDict


def nonrepeatingCharacter(word):
    repeatLetter = "$"
    new_dict = OrderedDict()
    for letter in word:
        if letter not in new_dict:
            new_dict[letter] = 1
        else:
            new_dict[letter] += 1
    for key, value in new_dict.items():
        if value == 1:
            repeatLetter = key
            return repeatLetter
    return repeatLetter


s = "hello"
print(nonrepeatingCharacter(s))
