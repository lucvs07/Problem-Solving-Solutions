class Solution:
    def convertDateToBinary(self, date: str) -> str:
        nums = date.split("-")
        n = len(nums)
        res = ''
        for i, num in enumerate(nums) :
            bin_n = bin(int(num))[2:]
            
            if i < len(nums) - 1:
                res += bin_n + "-"
            else:
                res += bin_n
        return res
        
