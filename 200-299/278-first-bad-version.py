class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) / 2
            if isBadVersion(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
