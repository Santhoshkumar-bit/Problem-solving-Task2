input_string = "Guvi Geeks Network Private Limited"

#vowels (both uppercase and lowercase)
vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}

# Svowels counters
total_vowels = 0
vowel_counts = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}

#Through the string
for char in input_string:
    #To find character is a vowel
    if char in vowels:
        total_vowels += 1
        #individual vowel count
        if char.upper() in vowel_counts:
            vowel_counts[char.upper()] += 1

# Results
print(f"Total number of vowels: {total_vowels}")
for vowel in vowel_counts:
    print(f"Count of {vowel}: {vowel_counts[vowel]}")