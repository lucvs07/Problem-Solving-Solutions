from typing import List
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        for row in grid:
            for num in row:
                arr.append(num)
        arr.sort()
        n = len(arr)
        res = 0
        md = arr[n//2]
        
        for i in arr :
            if i % x != md % x:
                return -1
            res += abs(md-i)//x
        return res