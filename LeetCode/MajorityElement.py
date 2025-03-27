from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for n in nums :
            if n in freq :
                freq[n] += 1
            else :
                freq[n] = 1
        
        for key, value in freq.items():
            if value > len(nums) // 2:
                return key