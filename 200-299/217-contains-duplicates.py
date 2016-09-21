class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        n_dict = {}
        for i in nums:
            if i in n_dict:
                return True
            else:
                n_dict[i] = True
        return False
