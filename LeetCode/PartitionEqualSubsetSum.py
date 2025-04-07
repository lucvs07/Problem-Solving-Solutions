class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0 :
            return False
        target = sum(nums) // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            if num > target :
                continue
            for i in range(target, num - 1, -1):
                if dp[i - num]:
                    dp[i] = True
        return dp[target]
