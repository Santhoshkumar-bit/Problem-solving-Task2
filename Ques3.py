input_string = "Being human"

output_string = ""

vowels = "aeiouAEIOU"

for i in input_string:
    if i not in vowels:
        output_string += i 

print("Original string:", input_string)
print("String with vowels removed:", output_string)
