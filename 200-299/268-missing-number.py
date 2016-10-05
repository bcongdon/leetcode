class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        s = (n * (n + 1)) / 2
        for i in nums:
            s -= i
        return s

# Explanation:
# Takes advantage of the fact that the summation of all integers from
# 0 .. n is n * (n+1) / 2
