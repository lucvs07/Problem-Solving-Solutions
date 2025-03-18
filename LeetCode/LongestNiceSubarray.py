from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        start = 0  # Initialize the start pointer of the sliding window
        maxLength = 0  # Initialize the maximum length of the nice subarray
        currAnd = 0  # Initialize the current AND result of the subarray
        
        for end in range(len(nums)):  # Iterate through each element in nums with the end pointer
            while currAnd & nums[end] != 0:  # Check if the current AND result conflicts with nums[end]
                currAnd ^= nums[start]  # Remove the effect of nums[start] from currAnd
                start += 1  # Move the start pointer to the right
            
            currAnd |= nums[end]  # Include nums[end] in the current AND result
            maxLength = max(maxLength, end - start + 1)  # Update the maximum length of the nice subarray
        
        return maxLength  # Return the maximum length of the nice subarray
