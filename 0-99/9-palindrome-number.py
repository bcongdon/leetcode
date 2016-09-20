import math


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x < 10:
            return True
        h = int(math.log10(x))
        while h >= 0 and x > 9:
            h_digit = (x / 10 ** h) % 10
            l_digit = x % 10
            if not h_digit == l_digit:
                return False
            x /= 10
            h -= 2
            print x
        return True