# Input string variable
input_string = input("Please enter a sentence to be alternated: ")
# Empty string to hold results for letter alternation
alternated_string_letters = ''

# For loop to iterate through each letter of the string and push it to the empty string holder
for i in range(0, len(input_string)):
    if not i % 2:
        alternated_string_letters += input_string[i].upper()
    else:
        alternated_string_letters += input_string[i].lower()

print(alternated_string_letters)

# Empty string to hold results word alternation
alternated_string_words = ''
# Split method to split sentence into list of words
split_input = input_string.split()

# For loop to iterate through each word and push it to the alternate word holder
for i in range(0, len(split_input)):
    if i % 2:
        alternated_string_words += split_input[i].upper() + ' '
    else:
         alternated_string_words += split_input[i].lower() + ' '

# Join method to reformat the list of string into a single string again
print(print(''.join(alternated_string_words)))