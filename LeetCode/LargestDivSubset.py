class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums :
            return []
        n = len(nums)
        dp = [1] * n
        prev = [-1] * n
        max_len = 1
        max_index = 0
        nums.sort()
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            if dp[i] > max_len :
                max_len = dp[i]
                max_index = i
        res = []
        while max_index != -1:
            res.append(nums[max_index])
            max_index = prev[max_index]
        res.reverse()
        return res
        
