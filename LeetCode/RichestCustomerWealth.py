from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        arr = []
        for c in accounts:
            arr.append(sum(c))
        return max(arr)
        