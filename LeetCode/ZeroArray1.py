from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        # diff array
        diff = [0] * (len(nums) + 1)
        for st, end in queries:
            diff[st] += 1
            diff[end + 1] -= 1
        
        freq = [0] * (len(nums))
        count = 0
        for i in range(len(nums)):
            count += diff[i]
            freq[i] = count
        for i in range(len(nums)):
            if nums[i] > freq[i]:
                return False
        return True
        