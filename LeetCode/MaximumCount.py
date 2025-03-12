from typing import List
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        arr = [0] * 2
        for n in nums:
            if n < 0 :
                arr[0] += 1
            if n > 0:
                arr[1] += 1
        return max(arr)
        