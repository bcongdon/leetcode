class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[[] for _ in xrange(n)] for _ in xrange(n)]
        ctr = 1
        for layer in xrange(0, n / 2 + 1):
            # TopLeft->Right
            for x in xrange(layer, n - layer - 1):
                res[layer][x] = ctr
                ctr += 1
            # TopRight->Down
            for y in xrange(layer, n - layer - 1):
                res[y][n - layer - 1] = ctr
                ctr += 1
            # BottomRight->Left
            for x in xrange(n - layer - 1, layer, -1):
                res[n - layer - 1][x] = ctr
                ctr += 1
            # BottomLeft-Top
            for y in xrange(n - layer - 1, layer, -1):
                res[y][layer] = ctr
                ctr += 1
        if n % 2 == 1:
            res[n/2][n/2] = ctr
        return res

# Explanation
# The dreaded spiral matrix... Just iterate in layers and do the four sides of
# each shell. There's a bit of a special case in the middle, but it's pretty
# easy to fix because this matrix is always square.

# Runtime - O(n^2)
# Need to populate n^2 elements in the matrix, so runtime is O(n^2)

# Space Complexity - O(n^2)
# Similar reasoning to runtime
