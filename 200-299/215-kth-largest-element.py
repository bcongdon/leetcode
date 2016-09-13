from random import randint


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            pivot_idx = randint(left, right)
            new_pivot = self.partitionAroundIndex(nums, left, right, pivot_idx)
            if new_pivot == k - 1:
                return nums[new_pivot]
            elif new_pivot > k - 1:
                right = new_pivot - 1
            else:
                left = new_pivot + 1

    def partitionAroundIndex(self, nums, left, right, idx):
        pivot = nums[idx]
        new_pivot = left
        # Swap pivot with right
        nums[idx], nums[right] = nums[right], nums[idx]
        for x in xrange(left, right):
            if nums[x] > pivot:
                nums[x], nums[new_pivot] = nums[new_pivot], nums[x]
                new_pivot += 1
        # Swap pivot back in
        nums[new_pivot], nums[right] = nums[right], nums[new_pivot]
        return new_pivot

# Explanation
# TODO
