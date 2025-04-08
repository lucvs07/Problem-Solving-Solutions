from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for num in nums :
            # Check if the number is already in the dictionary
            if num in freq :
                freq[num] += 1
            else :
                freq[num] = 1
            # Check if any number has a frequency greater than 1
            if freq[num] > 1 :
                return True
        return False
    
    # Another approach using set
    def containsDuplicateSet(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))    