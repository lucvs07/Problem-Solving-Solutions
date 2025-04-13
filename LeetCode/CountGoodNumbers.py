class Solution:
    
    MOD = 10**9 + 7
    @staticmethod
    def mod_pow(base, exponent, mod):
        result = 1
        base %= mod
        while exponent > 0:
            if exponent % 2:
                result = (result * base) % mod
            base = (base * base) % mod
            exponent //= 2
        return result
    def countGoodNumbers(self, n: int) -> int:
        even_pos = (n+1) // 2
        odd_pos = n // 2
        n_even = Solution.mod_pow(5, even_pos, Solution.MOD)
        n_odd = Solution.mod_pow(4, odd_pos, Solution.MOD)
        return (n_even * n_odd) % Solution.MOD    
