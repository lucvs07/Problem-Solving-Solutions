def marsExploration(s):
    # Write your code here
    counter = 0
    sos = [s[i:i+3] for i in range(0, len(s), 3)]
    for c in sos :
        for i in range(3):
            if c[i] != 'SOS'[i]:
                counter += 1
    return counter 
