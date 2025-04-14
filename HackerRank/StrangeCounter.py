def strangeCounter(t):
    # Write your code here
    start = 1
    val = 3
    while start + val <= t:
        start = start + val
        val *= 2
    res = val - (t - start)
    return res
