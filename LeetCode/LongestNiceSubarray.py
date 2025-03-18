from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        start = 0
        maxLength = 0
        currAnd = 0
        
        for end in range(len(nums)):
            while currAnd & nums[end] != 0:
                currAnd ^= nums[start]
                start += 1
            
            currAnd |= nums[end]
            maxLength = max(maxLength, end - start + 1)
        
        return maxLength
