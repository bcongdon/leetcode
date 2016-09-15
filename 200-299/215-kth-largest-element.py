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
# The task is to find the kth largest element for a given array. We can use
# a partitioning system similar to quicksort to achieve this without sorting.
# We simply use a similar system to QuickSort, wherein we pick a random pivot,
# and partition the list into sublists. We're guaranteed that the new_pivot is
# sorted correctly in the list. Thus, we do a binary-search-esque approach to
# keep partitioning until we get new_pivot == k. Then, just return the current
# value at nums[k].

# Runtime - Worst: O(n^2), Average: O(nlogn)
# Just like with Quicksort, we could get very unlucky with our random pivot
# indices, and end up having to sort the entire array to get k. However,
# on average, we will run a fraction of the entire Quicksort, so runtime will
# be something like O(nlogn / c), which is O(nlogn)

# Space Complexity - O(1)
# The sorting / partitioning operation is done in place.
