class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lowest_to_reach_end = len(nums) - 1
        for x in xrange(len(nums) - 1, -1, -1):
            if x + nums[x] >= lowest_to_reach_end:
                lowest_to_reach_end = x
        return lowest_to_reach_end == 0

# Explanation
# Notice that if we can mark some index to the left of the end of the list
# that can be jumped to the end of the list, then any indexes that can jump
# to that 'known good' index are also valid solutions. Thus, we iterate
# iterate backwards through the list saving the lowest 'known good' position.
# If at the end, the lowest 'known good' position is 0, then we know that there
# is a jump path between 0 and the end of the list.
#
# I tried doing a recursive approach as well as a depth first search, but both
# of them struggled with sufficiently high n or jump values.

# Runtime - O(n)
# Space Complexity - O(1)
