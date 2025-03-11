def caesarCipher(s, k):
    shift = k % 26
    def shift_char(c):
        if c.islower():
            return chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
        elif c.isupper():
            return chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
        return c

    return ''.join(shift_char(c) for c in s)

print(caesarCipher('middle-Outz', 2)) # okffng-Qwvb