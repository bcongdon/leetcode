class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) / 2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] < nums[right]:
                right = mid - 1
            else:
                left = mid + 1
        return nums[left]

# Explanation
# We're looking for the only place in the array where nums[i] < nums[i - 1]
# This is the 'pivot' point in the sorted array. As the array is sorted, we can
# easily do a binary search on it to find this point in sublinear time.

# Runtime - O(logn)
# Simple binary search on nums - which is a sorted array, so runtime is
# logarithmic.

# Space complexity - O(1)
# Comparisons done in-place
