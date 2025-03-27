from typing import List
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even = [n for n in nums if n % 2 == 0]
        if not even:
            return -1
        
        freq = {}
        for n in even:
            if n in freq:
                freq[n] +=1
            else:
                freq[n] = 1
        k = float('-inf')
        l = float('inf')
        for n, m in freq.items():
            if m > k or (m == k and n < l):
                k = m
                l = n
        return l
         
        