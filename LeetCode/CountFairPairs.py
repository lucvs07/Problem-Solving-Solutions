class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        
        for i in range(n):
            min_val = lower - nums[i]
            max_val = upper - nums[i]
            
            left = bisect_left(nums, min_val, i+1)
            right = bisect_right(nums, max_val, i+1)
            count += right - left

        return count
