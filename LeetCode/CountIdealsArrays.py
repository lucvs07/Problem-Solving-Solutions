class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9 + 7

        # Divisores
        divs = [[] for _ in range(maxValue + 1)]
        for div in range(1, maxValue + 1):
            for i in range(div, maxValue + 1, div):
                divs[i].append(div)
        
        # DP para as cadeias
        Kmax = int(maxValue.bit_length())
        f = [[0] * (maxValue + 1) for _ in range(Kmax+1)]
        
        # Base k = 1
        for value in range(1, maxValue + 1):
            f[1][value] = 1
        
        # Transições para k = 2 ... Kmax
        for k in range(2, Kmax + 1):
            for value in range(1, maxValue + 1):
                s = 0
                for d in divs[value]:
                    if d < value :
                        s += f[k-1][d]
                f[k][value] = s % MOD
        
        # Computar Binomiais
        C = [0] * (Kmax)
        C[0] = 1
        for j in range(1, Kmax):
            C[j] = C[j-1] * (n - j) * pow(j, MOD - 2, MOD) % MOD
        
        # Calcular Resposta Final
        res = 0
        for k in range(1, Kmax + 1) :
            total_chains = sum(f[k][1:]) % MOD
            res = (res + C[k - 1] * total_chains) % MOD
        
        return res
        
        
