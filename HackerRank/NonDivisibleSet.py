def nonDivisibleSubset(k, s):
    remainders = [0] * k
    for n in s:
        remainders[n % k] += 1
    
    res = min(remainders[0], 1)
    
    for i in range(1, (k // 2) + 1):
        if i != k - i:
            res += max(remainders[i], remainders[k - i])
        else:
            res += min(remainders[i], 1)
    return res
    

k = 3
s = [1, 7, 2, 4]
nonDivisibleSubset(k, s) # Expected output: 3