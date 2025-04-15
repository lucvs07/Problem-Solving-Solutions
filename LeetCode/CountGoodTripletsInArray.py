class Solution(object):
    def goodTriplets(self, nums1, nums2):
        hash_map = {}
        for index, value in enumerate(nums1):
            hash_map[value] = index
        n = len(nums2)
        result = 0
        st = []
        for num in nums2:
            idnum = hash_map[num]
            left = bisect.bisect_left(st, idnum)
            right = (n - 1 - idnum) - (len(st) - left)
            result += left * right
            bisect.insort(st, idnum)
        return result
