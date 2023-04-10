# Open file from the directory to read 
file = open('DOB.txt', 'r')

# Empty strings to hold details from file read
names = ""
births = ""

# For loop to read lines from file
for line in file:
    # Split lines from files into list of lines
    people = line.split()
    # Use indexing to collect the correct information to concatenate into empty holders
    names += people[0] + ' ' + people[1] + '\n'
    births += people[2] + ' ' + people[3] + ' ' + people[4] + '\n'

# Print layout as requested
print('Name')
print(names)
print('\n')
print('Birthdate')
print(births)

# Always close file as mentioned in notes
file.close()