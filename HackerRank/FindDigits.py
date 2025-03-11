def findDigits(n):
    counter = 0
    digits = [int(d) for d in str(n)]
    
    for d in digits:
        if d != 0 and n % d == 0:
            counter += 1
    return counter
print(findDigits(1012)) # 3