import math;

# Text variable so I can use indentation on the string
text = '''investment  - to calculate the amount of interest you'll earn on your investment
bond        - to calculate the amount you'll have to pay on a home loan
'''

# Print above text
print(text)

# Variable for the finance type
finance_input = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

# Logic check for finance_input
if finance_input.lower() == 'investment':

    # Variables for the investment calculation
    investment_amount = input("Please enter the investment amount in £ sterling: ")
    interest_rate = input("Please enter the interest rate: ")
    years_planned = input("Please input the number of years you plan on investing: ")
    interest = input("Please select if the interest type is 'simple' or 'compound': ")
    
    # Investment calculations depending on the type of interest
    if interest.lower() == "simple":
        print("Your investment will return as: £" + str(int(investment_amount)*(1 + (int(interest_rate)/100)*int(years_planned))))
    elif interest.lower() == "compound":
        print("Your investment will return as: £" + str(int(investment_amount)*math.pow((1 + int(interest_rate)/100), int(years_planned)))
)
              
   
elif finance_input.lower() == 'bond':

    # Variables for the bond calculation
    house_value = input("Please enter the value of your house: ")
    interest_rate = input("Please enter the interest rate: ")
    repayment_period = input("Please enter the number of months to repay the bond: ")
    
    # bond calculation
    repayment = ((int(interest_rate)/100)*int(house_value))/(1-(1+(int(interest_rate)/100))**(-int(repayment_period)))

    print("Monthly repayment will be: £" + str(repayment))

else:
    # Error cathcing if inccorect finance type was entered
    print("You have not entered a valid menu option")