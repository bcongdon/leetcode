class Solution(object):
    bitCounts = {}
    def bitCount(self, num):
        if num in self.bitCounts:
            return self.bitCounts[num]
        else:
            count = 0
            for i in range(32):
                if num & (1 << i):
                    count += 1
            self.bitCounts[num] = count
            return count
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        c = []
        for i in range(num + 1):
            c.append(self.bitCount(i))
        return c
