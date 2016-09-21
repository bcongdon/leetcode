class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lo, hi = 0, 0
        while hi < len(nums):
            if nums[hi] != 0:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1
            hi += 1

# Explanation
# Two pointer method: lo is the last non-zero number, hi iterates through
# the list and passes non-zero integers back to lo when it finds a non-zero
# element.
