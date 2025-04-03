class Solution:
  # More Efficent
     def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        trip, imax, dmax = 0, 0, 0
        for k in range(n):
            trip = max(trip, dmax * nums[k])
            dmax = max(dmax, imax - nums[k])
            imax = max(imax, nums[k])
        return trip
