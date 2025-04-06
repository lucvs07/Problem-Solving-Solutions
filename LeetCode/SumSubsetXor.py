class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(index, curr_xor):
            if index == len(nums):
                return curr_xor
            include = dfs(index + 1, curr_xor ^ nums[index])
            exclude = dfs(index + 1, curr_xor)
            return include + exclude
        return dfs(0,0)
        
