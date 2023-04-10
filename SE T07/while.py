# Initial states for the while loop to run on initiation
run = True
num = 0
index = 0

# While logic
while run:
    # Input request
    input_num = input("Please enter a number: ")
    # Condition to end while loop
    if int(input_num) == -1:
        # End While Loop
        run = False
        # Continue outside of while loop once escape condition is met
        continue
    # If end condition not met, colate input numbers and index
    num += int(input_num)
    index += 1
    # Calculation for average
    average = num/index

print(average)