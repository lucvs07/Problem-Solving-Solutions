from typing import List
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        hash_map = {}
        nums = nums1 + nums2
        for n in nums:
            if n[0] in hash_map:
                hash_map[n[0]] += n[1]
            else:
                hash_map[n[0]] = n[1]
        sorted_hash_map = sorted(hash_map.items(), key=lambda x: x[0])
        res = [[key, value] for key, value in sorted_hash_map]
        return res
        

        