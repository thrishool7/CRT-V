'''class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            for ele in row:
                if ele < 0:
                    count += 1
        return count'''
'''class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        rows,cols = len(grid),len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] < 0:
                    count += (cols - c)
                    break
        return count'''

