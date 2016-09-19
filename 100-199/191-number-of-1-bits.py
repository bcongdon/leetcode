class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        max_pow, num_ones = 0, 0
        while 2 ** max_pow < n:
            max_pow += 1
        while n > 0:
            if n - 2 ** max_pow >= 0:
                n -= 2 ** max_pow
                num_ones += 1
            max_pow -= 1
        return num_ones
