def getTotalX(a, b):
    # determinar max
    num_max = b[0]
    # array multiplicações -> a
    multiplicacoes = [[i * j for j in range(1, num_max // i + 1)] for i in a]
    # array divisões -> b
    div = []
    for n in b:
        for count in range(1, num_max + 1):
            if n % count == 0:
                div.append(count)
    # juntar os arrays
    all_numbers = [item for sublist in multiplicacoes for item in sublist] + div
    # objeto para contar as aparições dos números
    count = {}
    for n in all_numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1
    # numero que buscado de aparições
    found = 0
    for key, value in count.items():
        if value == len(a) + len(b):
            found += 1
    
    return found

total = getTotalX([2, 6], [24, 36])
print(total)

total2 = getTotalX([2, 4], [16, 32, 96])
print(total2)