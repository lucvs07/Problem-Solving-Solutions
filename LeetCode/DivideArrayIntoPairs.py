from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums.sort()
        count = {}
        for i in nums :
            if i in count:
                count[i] += 1
            else :
                count[i] = 1
        for key, value in count.items():
            if value % 2 != 0 :
                return False
        return True
