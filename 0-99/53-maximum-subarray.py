class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = sum_ = -2**32
        for i in nums:
            curr = max(i, curr + i)
            sum_ = max(curr, sum_)
        return sum_

# Explanation
# curr is the current sum. sum_ is the current maximum sum.
# As the loop iterates through the list, if the sum goes down (due to a
# negative number), then sum_ is maintained. It's only when a new sum
# begins where curr is then reassigned and sum is updated.

# Given [-2,1,-3,4,-1,2,1,-5,4]:
# -2: curr = -2, sum = -2
#  1: curr =  1, sum =  1
# -3: curr = -2, sum =  1
#  4: curr =  4, sum =  4
# -1: curr =  3, sum =  4
#  2: curr =  5, sum =  5
#  1: curr =  6, sum =  6
# -5: curr =  1, sum =  6
#  4: curr =  5, sum =  6
#  Returns 6
