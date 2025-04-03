class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_left = -float('inf') #to store the max num of nums[i]
        max_right = [0] * n #to track the max num of nums[k]
        max_right[n-1] = nums[n-1]

        trip = 0
        for i in range(n-2, -1, -1):
            max_right[i] = max(nums[i], max_right[i+1])
        for j in range(1, n-1):
            max_left = max(max_left, nums[j-1])
            if max_left > nums[j]:
                n1 = max_left - nums[j]
                trip = max(trip, n1 * max_right[j+1])  
        return trip
