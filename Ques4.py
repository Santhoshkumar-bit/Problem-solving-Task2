input_string = "Hello World"

unique_characters = set()

for i in input_string:
    if i not in unique_characters:
        unique_characters.add(i)

number_of_unique_characters = len(unique_characters)

print("Input string:", input_string)
print("Number of unique characters:", number_of_unique_characters)
