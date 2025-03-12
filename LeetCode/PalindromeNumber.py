class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        n = int(str(x)[::-1])
        if n == x :
            return True
        else :
            return False
        
