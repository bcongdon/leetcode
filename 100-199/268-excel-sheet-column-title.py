import string


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        digit_set, out = string.ascii_uppercase, ''
        while n:
            out, n = digit_set[(n - 1) % len(digit_set)] + out, (n-1) / len(digit_set)
        return out
