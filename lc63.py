class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]

        # If the starting cell is blocked
        if obstacleGrid[0][0] == 1:
            return 0

        # Starting position
        dp[0][0] = 1

        # Fill the DP table
        for i in range(m):
            for j in range(n):

                # Obstacle cell
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0

                # Skip the starting cell
                elif i == 0 and j == 0:
                    continue

                else:
                    # Paths from above
                    if i > 0:
                        dp[i][j] += dp[i - 1][j]

                    # Paths from left
                    if j > 0:
                        dp[i][j] += dp[i][j - 1]

        return dp[m - 1][n - 1]