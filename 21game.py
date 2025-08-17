class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts - 1:
            return 1.0
        dp = [0.0] * (n + 1)
        for x in range(k, n + 1):
            dp[x] = 1.0
        W = n - k + 1
        for x in range(k - 1, -1, -1):
            dp[x] = W / maxPts
            W += dp[x]
            if x + maxPts <= n:
                W -= dp[x + maxPts]
        return dp[0]
