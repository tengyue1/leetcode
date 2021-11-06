class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        dp = [[-1 for i in range(n)] for j in range(n)]
        
        dp[0][n-1] = grid[0][0] + grid[0][n-1]
        
        for k in range(1, m):
            new_dp = [[-1 for i in range(n)] for j in range(n)]
            for i in range(min(k+1, n)):
                for j in range(n-1, n-min(k+1, n)-1, -1):
                    previous_max_gains = [
                        dp[i-1][j-1] if i > 0 and j > 0 else 0,
                        dp[i-1][j] if i > 0 else 0,
                        dp[i-1][j+1] if i > 0 and j < n - 1 else 0,
                        dp[i][j-1] if j > 0 else 0,
                        dp[i][j],
                        dp[i][j+1] if j < n - 1 else 0,
                        dp[i+1][j-1] if i < n - 1 and j > 0 else 0,
                        dp[i+1][j] if i < n - 1 else 0,
                        dp[i+1][j+1] if i < n - 1 and j < n - 1 else 0,
                    ]
                    current_gain = grid[k][i] if i == j else (grid[k][i] + grid[k][j])
                    new_dp[i][j] = max(new_dp[i][j], max(previous_max_gains) + current_gain)
            dp = new_dp
        
        return max([max(row) for row in dp])
                    