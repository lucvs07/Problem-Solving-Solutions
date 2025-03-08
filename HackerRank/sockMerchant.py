def sockMerchant(ar):
    counter = {}
    for s in ar:
        if s in counter:
            counter[s] += 1
        else:
            counter[s] = 1
    
    pairs = 0
    for count in counter.values():
        pairs += count // 2
    
    return pairs

# Example usage:
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sockMerchant(ar))  # Output should be 3