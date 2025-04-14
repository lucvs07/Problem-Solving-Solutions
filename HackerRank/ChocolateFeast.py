def chocolateFeast(n, c, m):
    # Write your code here
    buy = n // c
    rest = buy
    while rest >= m :
        extra = rest // m
        buy += extra
        rest = rest % m + extra
    return buy
