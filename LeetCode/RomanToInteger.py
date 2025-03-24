class Solution:
    def romanToInt(self, s: str) -> int:
        r = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        res = 0
        n = len(s)
        for i in range(n):
            if i + 1 < n and r[s[i]] < r[s[i+1]]:
                res -= r[s[i]]
            else:
                res += r[s[i]]
        return res