def migratoryBirds(arr):
    birds = {}
    for b in arr:
        if b in birds:
            birds[b] += 1
        else:
            birds[b] = 1
    sorted_birds = sorted(birds.items(), key=lambda item: (-item[1], item[0]))
    return sorted_birds[0][0]

print(migratoryBirds([1, 4, 4, 4, 5, 3]))