class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for div in [2, 3, 5]:
            while num % div == 0 and abs(num) > 0:
                num /= div
        return num == 1
