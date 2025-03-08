def birthday(s, d, m):
    counter = 0
    for i in range(len(s) - m + 1): 
        # Obtendo a soma dentro do intervalo definido pela variavel m
        if sum(s[i:i+m]) == d: 
            counter += 1
    return counter

