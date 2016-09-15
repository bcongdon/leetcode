class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = [[]]
        for x in nums:
            subsets.extend([small_set + [x] for small_set in subsets])
        return subsets

# Explanation
# Fairly self-explanatory. Essentially, the task is to find the powerset
# of nums.