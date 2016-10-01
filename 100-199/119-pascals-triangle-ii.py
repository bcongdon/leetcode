import math


class Solution(object):
    def binomCoef(self, n, k):
        print n, k
        return math.factorial(n) / (math.factorial(n - k) * math.factorial(k))

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        return [self.binomCoef(rowIndex, i) for i in range(rowIndex + 1)]
