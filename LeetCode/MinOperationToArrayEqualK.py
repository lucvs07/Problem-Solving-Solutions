class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums_set = set()
        for num in nums :
            if num < k :
                return -1
            elif num > k :
                nums_set.add(num)
        return len(nums_set)
        
        

        
