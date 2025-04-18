class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'

        for _ in range(2, n+1):
            s = self._rle(s)
        
        return s
    
    def _rle(self, s: str) -> str:
        res = []
        i = 0
        lenght = len(s)

        while i < lenght :
            curr_char = s[i]
            count = 0

            while i < lenght and s[i] == curr_char:
                count += 1
                i += 1
            res.append(str(count))
            res.append(curr_char)
        return ''.join(res)
