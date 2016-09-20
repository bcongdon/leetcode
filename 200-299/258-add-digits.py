class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        digits = map(int, list(str(num)))
        d_sum = sum(digits)
        return self.addDigits(d_sum)
