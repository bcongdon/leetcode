class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = sml = lrg = nums[0]
        for i in nums[1:]:
            c_lrg = max(i, i * lrg, i * sml)
            c_sml = min(i, i * lrg, i * sml)
            lrg = c_lrg
            sml = c_sml
            mx = max(lrg, mx)
        return mx

# Explanation:
# mx  - current maximum product
# sml - max negative product up to the current pos
# lrg - maximum positive product up to the current pos
#
# 'sml' and 'lrg' both have to be maintained because maximum products can be
# attained by multiplying to large-magnitude negative numbers

# Given [2,3,-2,4,6]
#     sml =  2, lrg =   2, mx = 2
#  3: sml =  2, lrg =   6, mx = 6
# -2: sml = -2, lrg =  -2, mx = 6
#  4: sml = -8, lrg =   4, mx = 6
#  6: sml =  6, lrg =  24, mx = 24
#  Returns 24
