class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        n = len(differences)
        prefix = [0] * (n + 1)
        for i in range(1,n+1):
            prefix[i] = prefix[i-1] + differences[i-1]
        min_prefix, max_prefix = min(prefix), max(prefix)

        low_x = lower - min_prefix
        high_x = upper - max_prefix

        if high_x < low_x :
            return 0
        else :
            return high_x - low_x + 1
