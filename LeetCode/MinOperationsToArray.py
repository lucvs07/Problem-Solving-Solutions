from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        i = 0
        while i <= len(nums) - 3:
            if nums[i] == 0:
                # Flip the three consecutive elements
                nums[i] = 1 - nums[i]
                nums[i + 1] = 1 - nums[i + 1]
                nums[i + 2] = 1 - nums[i + 2]
                operations += 1
            i += 1
        
        # Check if all elements are 1
        if all(num == 1 for num in nums):
            return operations
        else:
            return -1

