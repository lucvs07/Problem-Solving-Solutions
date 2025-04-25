class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        counter = Counter([0])
        res = 0
        prefix = 0
        for i in range(n):
            prefix += 1 if nums[i] % modulo == k else 0
            res += counter[(prefix - k + modulo) % modulo]
            counter[prefix % modulo] += 1
        return res
        
