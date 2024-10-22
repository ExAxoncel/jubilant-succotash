class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        rows = [1] * m
        cols = [1] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = 0
                    cols[j] = 0

        for i in range(m):
            for j in range(n):
                if rows[i] == 0 or cols[j] == 0:
                    matrix[i][j] = 0
