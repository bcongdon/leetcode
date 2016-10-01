class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        rows = [[1]]
        while len(rows) < numRows:
            new_row = [1]
            for i in xrange(1, len(rows[-1])):
                new_row.append(rows[-1][i - 1] + rows[-1][i])
            new_row.append(1)
            rows.append(new_row)
        return rows
