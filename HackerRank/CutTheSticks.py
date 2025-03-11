def cutTheSticks(arr):
    res = []  # Initialize an empty list to store the result
    while len(arr) > 0:  # Continue until the array is empty
        res.append(len(arr))  # Append the current length of the array to the result
        min_val = min(arr)  # Find the minimum value in the array
        arr = [x - min_val for x in arr if x != min_val]  # Subtract the minimum value from each element and filter out zeros
    return res  # Return the result list
arr = [5, 4, 4, 2, 2, 8]
print(cutTheSticks(arr)) # Expected output: [6, 4, 2, 1]