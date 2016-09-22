class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        n, counter = len(nums), 0
        currentLoc, startIdx, prevVal = 0, 0, nums[0]
        k %= n
        while counter < n:
            if currentLoc >= n and currentLoc % n == startIdx:
                startIdx += 1
                currentLoc = startIdx
                prevVal = nums[currentLoc]
            nextLoc = (currentLoc + k) % n
            nextVal = nums[nextLoc]
            nums[nextLoc] = prevVal
            prevVal = nextVal
            counter += 1
            currentLoc += k


class NaiveSolution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        nums[:k], nums[k:] = nums[n-k:], nums[:n-k]
