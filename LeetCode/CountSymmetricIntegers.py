class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        counter = 0
        for i in range(low, high + 1):
            char_i = str(i)
            n = len(char_i)
            if n % 2 != 0 :
                continue
            alg1 = char_i[:n//2]
            sum_alg1 = sum(int(digit) for digit in alg1)
            alg2 = char_i[n//2:]
            sum_alg2 = sum(int(digit) for digit in alg2)
            if sum_alg1 == sum_alg2 :
                counter += 1
        return counter
