s1 = "Guvi Geek network solution"
s2 = "Being human"

def longest_common_substring(s1, s2):
    # Initialize variables to store the length and starting index of the longest common substring
    max_length = 0
    start_index = 0

    # Iterate through each possible starting position in s1
    for i in range(len(s1)):
        # Check substrings starting from i in s1 and see if they are in s2
        for j in range(len(s1) - i + 1):
            if s1[i:i + j] in s2:
                if j > max_length:
                    max_length = j
                    start_index = i

    return s1[start_index:start_index + max_length]
