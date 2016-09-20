class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        bit_found = False
        for x in range(32):
            if x % 2 == 0 and num & (1 << x):
                if bit_found:
                    return False
                bit_found = True
            elif x % 2 and num & (1 << x):
                    return False
        return bit_found and num > 0
