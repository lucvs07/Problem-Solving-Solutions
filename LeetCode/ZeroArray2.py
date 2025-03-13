from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        # Bin Search to fin the min of queries
        left, right = 0, len(queries)
        
        while left < right:
            mid =(left + right) // 2
            if self.canTransform(nums, queries[:mid]):
                right = mid
            else :
                left = mid + 1
        
        if left == len(queries) and not self.canTransform(nums, queries):
            return -1
        return left

    def canTransform(self, nums: List[int], queries: List[List[int]]) -> bool :
        # diff array to track the range updates
        diff = [0] * (len(nums) + 1)
        
        # queries to diff array
        for l, r, val in queries:
            diff[l] += val
            diff[r + 1] -= val
        
        # prefix sum decrement to each position
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += diff[i]
            if prefix_sum < nums[i]:
                return False
        return True
        