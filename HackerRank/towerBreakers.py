def towerBreakers(n, m):
    # If the height(m) of the tower is 1 or the number of towers(n) is even, the second player wins
    if m == 1 or n % 2 == 0:
        return 2
    # If the height(m) of the tower is greater than 1 and the number of towers(n) is odd, the first player wins
    return 1
print(towerBreakers(2, 2)) # 2