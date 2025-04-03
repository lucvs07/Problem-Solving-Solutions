from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        for n in nums :
            if n in freq :
                freq[n] += 1
            else :
                freq[n] = 1
        
        for k, v in freq.items() :
            if v == 1 :
                return k