class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ''.join(char for char in s if char.isalnum())
        clean_s = clean_s.lower()
        invert_s = clean_s[::-1]
        if clean_s == invert_s :
            return True
        return False    