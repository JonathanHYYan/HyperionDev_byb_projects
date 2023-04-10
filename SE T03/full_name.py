# Create input variable
full_name = input("Please enter your full name: ")

# First logic check
if len(full_name) == 0:
    print("You haven't entered anything. Please enter your full name")
# Second logic check
elif len(full_name) <= 4:
    print("You have entered less than 4 characters. Please make sure you have entered your name and surname")
# Third logic check
elif len(full_name) > 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name")
# Final else statement if all previous checks are passed    
else:
    print("Thank you for entering your name")