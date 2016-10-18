class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in d and d[nums[i]] - i <= k:
                return True
            else:
                d[nums[i]] = i
        return False
