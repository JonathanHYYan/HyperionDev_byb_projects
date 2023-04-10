# Function to check input is a floating integer
def num_check(num):
    try:
        is_float = int(num)
        return True
    except ValueError:
        return False

# While loop to continue to ask the number of students registering incase of a typo
while True:
    # Input variable for the number of students that is being registered
    num_students = input("How many students are you registering: ")

    # If statement with the input check
    if num_check(num_students):
        # For loop to loop through registry process for each student and create the txt doc
        for i in range(round(float(num_students))):
            student_id = input("Please enter your student ID: ")
            with open('reg_form.txt', 'a') as file:
                file.write(student_id + '     ' + '..............' +'\n')
        # File closure outside of for loop to ensure file closes when all the students are registered
        file.close()
        break
    else:
        print('No valid input detected, please enter a number.')
        continue
