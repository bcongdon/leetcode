class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 1
        for fast in xrange(0, len(nums)):
            if nums[slow - 1] != nums[fast]:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        return len(nums[:slow])
