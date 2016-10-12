class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        r, c = len(matrix), len(matrix[0])
        lo, hi = 0, r * c - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            curr = matrix[mid / c][mid % c]
            
            if curr == target:
                return True
            elif curr < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False