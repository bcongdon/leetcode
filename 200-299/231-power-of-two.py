class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bit_found = False
        for i in range(31):
            if n & (1 << i):
                if bit_found:
                    return False
                else:
                    bit_found = True
        return bit_found and not n & (1 << 31)
