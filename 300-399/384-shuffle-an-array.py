from random import randint


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        :type size: int
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        res = list(self.nums)
        for i in range(len(self.nums)):
            j = randint(0, len(self.nums) - 1)
            res[i], res[j] = res[j], res[i]
        return res
