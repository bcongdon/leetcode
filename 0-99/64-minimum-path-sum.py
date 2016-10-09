class Solution(object):
    solved = {}

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.solved = {}
        self.solved[(len(grid) - 1, len(grid[0]) - 1)] = grid[-1][-1]
        res = self.minPathCost(0, 0, grid, len(grid) - 1, len(grid[0]) - 1)
        print(self.solved)
        return res

    def minPathCost(self, x, y, grid, tx, ty):
        if (x, y) in self.solved:
            return self.solved[(x, y)]
        elif x < 0 or x > tx or y < 0 or y > ty:
            return 2**32
        else:
            res = (min(self.minPathCost(x + 1, y, grid, tx, ty),
                       self.minPathCost(x, y + 1, grid, tx, ty)) +
                   grid[x][y])
            self.solved[(x, y)] = res
            return res
