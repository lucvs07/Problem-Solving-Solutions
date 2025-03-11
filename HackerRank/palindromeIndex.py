def palindromeIndex(s):
    # Check if the string is already a palindrome
    if s == s[::-1]:
        return -1  # If it is, return -1 as no removal is needed
    
    # Iterate through the string
    for i in range(len(s)):
        # Check for the first mismatch
        if s[i] != s[-i-1]:
            # Check if removing the character at the current index makes it a palindrome
            if s[i+1:len(s)-i] == s[i+1:len(s)-i][::-1]:
                return i  # Return the index if it does
            
            # Check if removing the character at the mirrored index makes it a palindrome
            elif s[i:len(s)-i-1] == s[i:len(s)-i-1][::-1]:
                return len(s)-i-1  # Return the mirrored index if it does
    
    # If no single removal can make it a palindrome, return -1
    return -1
print(palindromeIndex('aaab'))