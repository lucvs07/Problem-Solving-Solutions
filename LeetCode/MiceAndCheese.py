from typing import List

class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        
        # Passo 1: assumimos que todos os queijos serão comidos pelo rato 2
        total = sum(reward2)

        # Passo 2: calculamos a diferença de benefício ao trocar esse queijo do rato 2 para o rato 1
        # Cada item é uma tupla: (ganho extra ao dar ao rato 1, índice do queijo)
        diffs = [reward1[i] - reward2[i] for i in range(n)]

        # Passo 3: ordenamos essas diferenças do maior para o menor
        # Ou seja, vamos escolher os k queijos onde o rato 1 faz mais diferença positiva
        diffs.sort(reverse=True)

        # Passo 4: somamos os k maiores ganhos extras ao total
        # Isso equivale a dar esses k queijos ao rato 1
        total += sum(diffs[:k])

        return total
