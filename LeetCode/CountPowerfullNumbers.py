class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def count(val):
            power = str(val)
            n = len(power) - len(s)

            if n < 0:
                return 0
            
            # create a dp to keep the number valid of power
            dp = [[0] * 2 for _ in range (n+1)]
            dp [n][0] = 1
            dp [n][1] = int (power[n:] >= s)

            # fill the dp in reverse
            for i in range(n-1, -1, -1):
                digit = int(power[i])

                dp[i][0] = (limit + 1) * dp[i + 1][0]

                if digit <= limit:
                    dp[i][1] = digit * dp[i + 1][0] +dp[i+1][1]
                else :
                    dp[i][1] = (limit + 1) * dp[i + 1][0]
            return dp[0][1]  # Add the return statement here
        return count(finish) - count(start - 1)
