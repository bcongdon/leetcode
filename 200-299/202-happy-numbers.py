class Solution(object):
    happynums = {}

    def checkHappy_(self, n, prev):
        orig = n
        if n in self.happynums:
            return self.happynums[n]
        digits = 0
        while n > 0:
            digits += (n % 10) ** 2
            n /= 10
        if digits == 1:
            self.happynums[orig] = True
            return True
        elif digits in prev:
            return False
        else:
            prev[digits] = True
            return self.checkHappy_(digits, prev)

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return self.checkHappy_(n, {})
