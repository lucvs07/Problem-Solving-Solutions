class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        visto = [False] * 101
        for i in range(len(nums) - 1, -1, -1):
            if visto[nums[i]]:
                return i // 3 + 1
            visto[nums[i]] = True
        return 0
        
