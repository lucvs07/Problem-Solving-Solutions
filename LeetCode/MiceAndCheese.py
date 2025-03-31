class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        reward1.sort()
        reward2.sort()
        n = len(reward1)
        soma = 0
        if k == 0 :
            return sum(reward2)
        if k == n:
            return sum(reward1)
        print(reward1[-k:])
        print(reward2[k:])
        soma = sum(reward1[-k:]) + sum(reward2[k:])
        return soma
        