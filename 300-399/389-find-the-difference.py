# Hashmap Solution
from collections import defaultdict


class HashmapSolution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_d, t_d = defaultdict(int), defaultdict(int)
        for c in s:
            s_d[c] += 1
        for c in t:
            t_d[c] += 1
        for c in t_d:
            if s_d[c] != t_d[c]:
                return c

# Bit Manipulation Solution


class BitManipulationSolution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        char_codes = map(ord, s + t)
        x = char_codes[0]
        for i in char_codes[1:]:
            x = x ^ i
        return chr(x)

# Explanation
# Anything xor'd with itself is 0, so if we go through and xor all characters
# in both strings, the pairs of characters will xor each other to 0 and we are
# left with only the char code of the added character.
