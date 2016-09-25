class Solution(object):
    known_heights = {0: 1, 1: 1}

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.known_heights:
            return self.known_heights[n]
        else:
            self.known_heights[n] = (self.climbStairs(n-1) +
                                     self.climbStairs(n-2))
            return self.known_heights[n]
