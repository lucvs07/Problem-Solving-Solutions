from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_h = sorted(heights)
        counter = 0
        for i in range(len(sorted_h)):
            if heights[i] != sorted_h[i]:  
                counter += 1
        return counter

        
        