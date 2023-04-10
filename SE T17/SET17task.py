#=====importing libraries===========
import os
from datetime import datetime, date

# Format string into easy to read manner
DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

# Converted original task_list list variable into a function
def open_task():
    '''
    Converted this task_list[] variable into a function to be called when needed
    so the tasks.txt and user.txt file will always be updated when using features without
    having to close and re-open the program just to get the newest instance of the
    txt files
    '''
    with open("tasks.txt", 'r') as task_file:
        task_data = task_file.read().split("\n")
        task_data = [t for t in task_data if t != ""]

    # Empty array to hold lists extracted from task.txt
    task_list = []
    for t_str in task_data:
        curr_t = {}

        # Split by semicolon and manually add each component
        task_components = t_str.split(";")
        curr_t['username'] = task_components[0]
        curr_t['title'] = task_components[1]
        curr_t['description'] = task_components[2]
        curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
        curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
        curr_t['completed'] = True if task_components[5] == "Yes" else False

        task_list.append(curr_t)
    return task_list


#====Login Section====
'''
This code reads usernames and password from the user.txt file to 
allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print('')
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print('')
        print("Wrong password")
        continue
    else:
        print('')
        print("Login Successful!")
        logged_in = True


#===========Modularised Functions===================

# Function to match username input to user.txt usernames
def username_match(username_input, file):
        '''This function takes in a string input of a username and a file (user.txt)
        and compares the input to the list of users registered in the file
        (user.txt)'''
        username_list = []
        for line in file:
            username_list.append(line.split(';')[0])

        if username_input in username_list:
            return True
        else:
            return False


# Function to override specific line when replacement is created to prevent code repetition
def file_override(new_task, line_num):
    '''
    File takes in the task_list and an index number and removes the original
    task after an edited version has been created
    '''
    with open("tasks.txt", "r+") as task_file:
        task_list_to_write = []
        for new in new_task:
            str_attrs = [
                new['username'],
                new['title'],
                new['description'],
                new['due_date'].strftime(DATETIME_STRING_FORMAT),
                new['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if new['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    with open("tasks.txt", "r+") as task_file:
        lines = task_file.readlines()
        # Line Deletion occurs here
        del lines[int(line_num)-1]
        task_file.seek(0)
        task_file.truncate()
        task_file.writelines(lines)
    print("Task successfully updated.")


# Function to print task list to prevent code repetition
def print_task(task_list, index):
    disp_str = f"=================================================================\n"
    disp_str += '\n'
    disp_str += f"Assignment: \t\t {task_list.index(index)+1}\n"
    disp_str += f"Task: \t\t\t {index['title']}\n"
    disp_str += f"Assigned to: \t\t {index['username']}\n"
    disp_str += f"Date Assigned: \t\t {index['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
    disp_str += f"Due Date: \t\t {index['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
    disp_str += f"Completed: \t\t {index['completed']}\n"
    disp_str += f"Task Description: \n\t {index['description']}\n"
    print(disp_str)


# Function to add consisten barriers without having to repeat print() version
def spacing():
    '''
    Function creates a double dashed line in the terminal to segment sections
    for improved user legibility
    '''
    print("=================================================================\n")   


# Function to register a new user
def reg_user():
    '''
    Refactored user registry code into a function, outputs a new user if
    the username is not already in user.txt and the new password passes 
    confirmation
    '''
    while True:
        with open('user.txt', 'r+') as user_registry:
            new_username = input("New Username: ")
            
            # Using the matching function check the username input is not already in user.txt file
            if not username_match(new_username, user_registry):
                # - Request input of a new password
                new_password = input("New Password: ")

                # - Request input of password confirmation.
                confirm_password = input("Confirm Password: ")
                        # - Check if the new password and confirmed password are the same.
                if new_password == confirm_password:
                    # - If they are the same, add them to the user.txt file,
                    user_data = []
                    user_data.append(new_username + ';' + new_password)
                    user_registry.write("\n")
                    user_registry.write("\n".join(user_data))
                    print("New user added")
                    user_registry.close()
                    break
                # - Otherwise you present a relevant message.
                else:
                    print("Passwords do no match, please try again")
            else:
                print('Sorry username is taken')


# Function to add a new task into tasks.txt
def add_task():
        '''
        Function checks the inputted username is available before adding a new
        task in task.txt and assigning it to the inputted username
        '''
        task_list = open_task()
        with open('user.txt', 'r+') as user_registry:
            task_username = input("Name of person assigned to task: ")
            # Check user exists in user.txt before assigning task in tasks.txt
            if not username_match(task_username, user_registry):
                print('')
                print("User does not exist. Please enter a valid username")
                user_registry.close()
            else:
                task_title = input("Title of Task: ")
                task_description = input("Description of Task: ")
                while True:
                    try:
                        task_due_date = input("Due date of task (YYYY-MM-DD): ")
                        due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                        break

                    except ValueError:
                        print("Invalid datetime format. Please use the format specified")


                # Then get the current date.
                curr_date = date.today()
                ''' Add the data to the file task.txt and
                    Include 'No' to indicate if the task is complete.'''
                new_task = {
                    "username": task_username,
                    "title": task_title,
                    "description": task_description,
                    "due_date": due_date_time,
                    "assigned_date": curr_date,
                    "completed": False
                }

                task_list.append(new_task)
                with open("tasks.txt", "w") as task_file:
                    task_list_to_write = []
                    for t in task_list:
                        str_attrs = [
                            t['username'],
                            t['title'],
                            t['description'],
                            t['due_date'].strftime(DATETIME_STRING_FORMAT),
                            t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                            "Yes" if t['completed'] else "No"
                        ]
                        task_list_to_write.append(";".join(str_attrs))
                    task_file.write("\n".join(task_list_to_write))
                task_file.close()
                print("Task successfully added.")
       

#  Function to iterate through task list and print all tasks
def view_all():
        '''
        This function prints all tasks to the terminal. 
        In addition, uses the open_task() function instead of the original
        task_list[] variable because if previous menu options i.e. add_task,
        reg_user was called the txt files on the original task_list[] variable
        would be the original instance rather than an instance of the now modified
        .txt files
        '''
        task_list = open_task()
        spacing()
        for task in task_list:
            disp_str = f"Task: \t\t {task['title']}\n"
            disp_str += f"Assigned to: \t {task['username']}\n"
            disp_str += f"Date Assigned: \t {task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {task['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {task['description']}\n"
            print(disp_str)
            spacing()


# Function to view tasks specific to logged in user
def view_mine():
    '''
    Creates list of tasks assigned to current signed in user
    with the additional features for modifying assigned user and due date
    then outputs information to the terminal
    '''
    task_list = open_task()
    user_total = 0
    user_task_list = []

    # Total number of tasks for user
    for task in task_list:
        if task['username'] == curr_user:
            user_total += 1
            user_task_list.append(task)
    spacing()
    print("You have " + str(user_total) + " task(s)")
    print('')
    # Input request to show all tasks or specific task based on index
    view_task = input("Enter a task number or 'a' to view all: ")
    if view_task == "a":
        for task in task_list:
            if task['username'] == curr_user:
                print_task(task_list,task)

        spacing()

    # Escape back to main menu
    elif view_task == '-1':
        return
    
    # View specific task based on index
    else:
       
        task = user_task_list[int(view_task)-1]
        if task['username'] == curr_user:
            print_task(task_list, task)
            spacing()

        # Check complete status before offering to change complete status
        if not task['completed']:
            mark_task = input("Mark task as complete? (Y/N) ")
            if mark_task.lower() == 'y':
                task_complete = {
                    "username": task['username'],
                    "title": task['title'],
                    "description": task['description'],
                    "due_date": task['due_date'],
                    "assigned_date": task['assigned_date'],
                    "completed": True
                }
                task_list.append(task_complete)
                file_override(task_list, view_task)

            elif mark_task.lower() == 'n':
                # Edit Task only available if compelte status is false
                edit_task = input("Would you like to edit the task? (Y/N) ")
                if edit_task.lower() == 'y':
                    edit_option = input('''Please select what you would like to edit:
(a) - Assignee
(d) - Due date of assignment
:''')
                    # Multiple edit options
                    if edit_option.lower() == 'a':
                        while True:
                            with open('user.txt', 'r+') as user_registry:
                                new_assignee = input('Please enter a new assignee: ')
                                if not username_match(new_assignee, user_registry):
                                    print("User does not exist. Please enter a valid username")
                                    user_registry.close()
                                else:
                                    file_change = {
                                        "username": str(new_assignee),
                                        "title": task_list['title'],
                                        "description": task_list['description'],
                                        "due_date": task_list['due_date'],
                                        "assigned_date": task_list['assigned_date'],
                                        "completed": task_list['completed']
                                    }
                                    task_list.append(file_change)
                                    # File override function removes line that is currently obeserved in terminal
                                    file_override(task_list, view_task)
                                    break

                    elif edit_option.lower() == 'd':
                        while True:
                            try:
                                new_due_date = input("Due date of task (YYYY-MM-DD): ")
                                due_date_str = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
                                break

                            except ValueError:
                                print("Invalid datetime format. Please use the format specified")
                        file_change = {
                            "username": task_list['username'],
                            "title": task_list['title'],
                            "description": task_list['description'],
                            "due_date": due_date_str,
                            "assigned_date": task_list['assigned_date'],
                            "completed": task_list['completed']
                        }
                        task_list.append(file_change)
                        file_override(task_list, view_task)                
                    else:
                        print("Incorrect input, please select from options provided.")
            
            else:
                print("Incorrect input, please select from options provided.")


# Function to generate task_overview.txt and user_overview.txt
def generate_file():
    '''
    This function generates a task_overview.txt and user_overview.txt based on
    user.txt and tasks.txt.
    '''
    if not os.path.exists("task_overview.txt") or not os.path.exists("user_overview.txt"):
        task_list = open_task()
        total_task = len(task_list)
        # Create task_overview.txt file
        with open('task_overview.txt', 'x') as task_overview:
            completed_counter = 0
            overdue_counter = 0

            # Logic check to calculate task status
            for task in task_list:
                if task['completed']:
                    completed_counter += 1
                elif not task['completed'] and task['due_date'] < datetime.today():
                    overdue_counter += 1

            # String formatted to display string in a user friendly way in both txt and terminal print
            task_overview.write("Total number of task(s):   {0}".format(str(total_task)) + "\n")
            task_overview.write("Task(s) completed:         {0}".format(str(completed_counter)) + "\n")
            task_overview.write("Task(s) incomplete:        {0}".format(str(total_task-completed_counter)) + "\n")
            task_overview.write("Task(s) overdue:           {0}".format(str(overdue_counter)) + "\n")
            task_overview.write("Percentage incomplete:     {0}".format(str(((total_task-completed_counter)/total_task)*100.00)) + "%" + "\n")
            task_overview.write("Percentage overdue:        {0}".format(((overdue_counter/total_task)*100)) + "%")
        task_overview.close()

        # Create user_overview.txt file
        with open('user_overview.txt', 'x') as user_overview:
            total_user = 0
            user_list = []

            with open('user.txt', 'r+') as user_registry:
                for line in user_registry:
                    total_user += 1
            user_registry.close()

            # Iterate through task list for total counts of users and tasks
            for task in task_list:
                user_list.append(task['username'])
                
            # Create unique list of users based on user.txt
            user_set = set(user_list)

            # String format to displary totals
            user_overview.write("Total number of users: \t\t" + str(total_user) + "\n")
            user_overview.write("Total number of task(s): \t" + str(total_task) + "\n")
            user_overview.write("===================================================\n")

            # Logic to create statistics for each user
            for user in user_set:
                user_total_task = user_list.count(user)
                user_tasks_completed = 0
                user_overdue = 0

                for task in task_list:
                    if task['completed'] and task['username'] == user:
                        user_tasks_completed += 1
                    elif not task['completed'] and task['due_date'] < datetime.today() and task['username'] == user:
                        user_overdue += 1
                        
                # String Format to display task status for each user
                user_overview.write(str(user).capitalize() + " has " + str(user_total_task) + " task(s).\n")
                user_overview.write(str(user).capitalize() + " has " + str((user_list.count(user)/total_task)*100) + "%" + " of all assignments.\n")
                user_overview.write(str(user).capitalize() + " has completed " + str((user_tasks_completed/user_total_task)*100) + "%" + " of their task(s).\n")
                user_overview.write(str(user).capitalize() + " has " + str(((user_total_task-user_tasks_completed)/user_total_task)*100) + "%" + " of their task(s) incomplete.\n")
                user_overview.write(str(user).capitalize() + " has " + str((user_overdue/user_total_task)*100) + "%" + " of their task(s) overdue.\n")
                user_overview.write("===================================================\n")
        
        # Visual indicator generator function has fired
        print("")
        print("######################################")
        print("Task and User Overview files generated")
        print("######################################")
    else:
        spacing()
        print('Files are already generated')
        print('')
        spacing()


# Function to read & display task_overview.txt and user.overview.txt
def display_stats():
    '''
    Function checkts for task_overview.txt and user_overview.txt files
    and if they are not available runs generate_file() to create said files
    and then displays them in the terminal
    '''
    # Check task_overview.txt and user_overview.txt files and fire generate function if they are not present
    if not os.path.exists("task_overview.txt") or not os.path.exists("user_overview.txt"):
        generate_file()

    # Open, read and display user_overview.txt
    with open('user_overview.txt', 'r') as user_overview:
        print('===================================================')
        print("")
        for lines in user_overview.readlines():
            
            print(lines)
    user_overview.close()

        # Open, read and display taskr_overview.txt
    with open('task_overview.txt', 'r') as task_overview:
        for lines in task_overview.readlines():
            print(lines)
    task_overview.close()


while True:

    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - generate reports
ds - Display statistics
e - Exit
: ''').lower()
    # Refeaction options with code converted into functions at the top of the page
    if menu.lower() == 'r':
        reg_user()

    elif menu.lower() == 'a':
        add_task()
        

    elif menu.lower() == 'va':
        view_all()
            
    elif menu.lower() == 'vm':
        view_mine()

    # Generate File option
    elif menu.lower() == 'gr':
        generate_file()

    elif menu.lower() == 'ds' and curr_user == 'admin': 
        display_stats()


    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")