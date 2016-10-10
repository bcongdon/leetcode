class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        idx = len(nums1) - 1
        hi1, hi2 = m - 1, n - 1
        while hi1 >= 0 and hi2 >= 0:
            if nums1[hi1] > nums2[hi2]:
                nums1[idx] = nums1[hi1]
                hi1 -= 1
            else:
                nums1[idx] = nums2[hi2]
                hi2 -= 1
            idx -= 1
        while hi2 >= 0:
            nums1[idx] = nums2[hi2]
            hi2 -= 1
            idx -= 1
