# Check the input is a integer or floating number
def num_check(num):
    try:
        is_float = int(num)
        return True
    except ValueError:
        try:
            is_float = int(num)
            return True
        except ValueError:
            print("No number detected. Please try again.")
            return False

# Check the operation is viable
def operand_check(symbol):
    if symbol.strip() in ['+','-','/','x']:
        return True
    else:
        print("No valid operand detected. Please try again.")
        return False
    
# Function to create or append to existing file
def write_to_file(file_name, calculation):
    with open(file_name+'.txt', 'a') as file:
        file.write(calculation)
        file.writelines('\n')

# Function to read existing file
def read_file(file_name):
    try:
        with open(file_name + '.txt', 'r') as file:
            print(file.read())
            return True
    except FileNotFoundError as error:
        print('There is no such file.')
        return False

# Function to calculate based on input and save to a file
def calculation_function():
        file_name = "file"
        # Embedded while loop to continuosly run calculation feature
        while True:
            num_1 = input('''Please enter a number (1 of 2) or (e) to esc back to main menu: ''')
            if num_1 == 'e':
                break
            elif not num_check(num_1):
                continue
            num_2 = input('''Please enter a number (2 of 2) or (e) to esc back to main menu: ''')
            if float(num_2) == 0.0:
                print("Sorry division by 0 is infinity! Please try again")
                break
            elif num_2 == 'e':
                break
            elif not num_check(num_2):
                continue

            operation = input("What operation would you like to enact (i.e. +,-,/,x ): ")
            if not operand_check(operation):
                continue

            # Calculation depending on operand if all inputs successfully pass criteria
            if operation.strip() == '+':
                answer = float(num_1)+float(num_2)
                print(answer)
                write_to_file(file_name, 'Addition calculation: {num1} + {num2}'.format(num1 = num_1, num2 = num_2))
                break
            elif operation.strip() == '-':
                answer = float(num_1)-float(num_2)
                print(answer)
                write_to_file(file_name, 'Subtraction calculation: {num1} - {num2}'.format(num1 = num_1, num2 = num_2))
                break
            elif operation.strip() == '/':
                answer = float(num_1)/float(num_2)
                print(answer)
                write_to_file(file_name, 'Division calculation: {num1} / {num2}'.format(num1 = num_1, num2 = num_2))
                break
            elif operation.strip() == 'x':
                answer = float(num_1)*float(num_2)
                print(answer)
                write_to_file(file_name, 'Multiplication calculation: {num1} * {num2}'.format(num1 = num_1, num2 = num_2))
                break
        print('Your calcualtion is saved to file named: ' + str(file_name) + '.txt')
        print('If you wish to exit the program please press (e)')


# While loop to continuously run the program restting on incorrect inputs and breaking if program full runs
while True:         
    mode_select = input("Please enter feature 'Calculator' or search for a filename: ")
    if mode_select == 'e':
        break
    elif mode_select.lower() == 'calculator':
        calculation_function()

    else: 
        # If else conditions depending on whether requested file exists
        if read_file(mode_select.lower().strip()):
            print('If you wish to exit the program please press (e)')
            break
        else:
            print("File does not exist, please try again")
            print('If you wish to exit the program please press (e)')