class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        res = 0
        counter = {}
        n = len(nums)
        right = 0
        distinct = len(set(nums))
        for left in range(n):
            if left > 0:
                remove = nums[left - 1]
                counter[remove] -= 1
                if counter[remove] == 0:
                    counter.pop(remove)
            while right < n and len(counter) < distinct:
                add = nums[right]
                counter[add] = counter.get(add, 0) + 1
                right += 1
            if len(counter) == distinct:
                res += n - right + 1
        return res
        
