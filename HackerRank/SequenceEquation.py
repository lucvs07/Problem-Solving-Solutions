def permutationEquation(p):
    # Initialize an empty list to store the result
    result = []
    # Iterate over each number x from 1 to the length of the list p
    for x in range(1, len(p) + 1):
        # Find the index of x in the list p, then find the index of that result + 1 in the list p, and add 1 to the result
        result.append(p.index(p.index(x) + 1) + 1)
    # Return the final result list
    return result
print(permutationEquation([4, 3, 5, 1, 2])) 