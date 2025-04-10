def stones(n, a, b):
    steps = set()
    for i in range(n):
        step = i * a + (n-1-i) * b
        steps.add(step)
    return sorted(steps)
