class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        
        # Optimize k if it's larger than the total number of elements
        k = k % total
        
        # Create an empty result grid of dimensions m x n
        res = [[0] * n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                # Flattened 1D index
                old_1d = r * n + c
                
                # Shifted 1D index
                new_1d = (old_1d + k) % total
                
                # Map back to 2D row and column
                new_r = new_1d // n
                new_c = new_1d % n
                
                res[new_r][new_c] = grid[r][c]
                
        return res