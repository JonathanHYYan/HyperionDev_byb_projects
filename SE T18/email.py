### --- OOP Email Simulator --- ###
from datetime import date
# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email(object):
    '''
    Email class that contains title, content and a read state initially set to False
    '''
    # Declare the class variable, with default value, for emails. 
    date = str(date.today)
    has_been_read = False

    # Initialise the instance variables for emails.
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content


    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True


# --- Lists --- #
# Initialise an empty list to store the email objects.
emails = []
# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox():
    '''
    Creates 3 emails from the same address with various subject lines and content
    '''
    email_address = 'email@email.com'
    # Create 3 sample emails and add it to the Inbox list. 
    email_1 = Email( email_address, 'Welcome to HyperionDev!', 'hello')
    email_2 = Email( email_address, 'Great work on the bootcamp', 'how are you')
    email_3 = Email( email_address, 'Your excellent marks!', 'goodbye')
    emails.extend([email_1, email_2, email_3])


def list_emails():
    '''
    Displays a list of emails with their corresponding indexes
    '''
    # Create a function which prints the email’s subject_line, along with a corresponding number.
    for index, email in enumerate(emails):
        print(str(index) + '    ' +email.subject_line)
    


def read_email(index):
    '''
    Takes an index and displays email based on email list index
    fires mark as read function after email is displayed
    '''
    # Create a function which displays a selected email. 
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    print("=====================================")
    print('')
    print("Subject: " + str(emails[int(index)-1].subject_line))
    print("Message: \n\t" + str(emails[int(index)-1].email_content))
    print('')
    print("Email from " + str(emails[int(index)-1].email_address) + " marked as read")
    print('')
    emails[int(index)-1].mark_as_read()


def unread_list(emails):
    '''
    Creates a list of emails that are currently unread
    '''
    unread_list = []
    for email in emails:
        if not email.has_been_read:
            unread_list.append(email)
    return unread_list
    

# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.
populate_inbox()


# Fill in the logic for the various menu operations.
while True:
    print('')
    print('You have ' + str(len(emails)) + ' emails in your inbox')
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        # add logic here to read an email
        while True:
            # Asks for an index 
            print('')
            email_index = input('Enter a number for the email you would like to read: ')
            if int(email_index) not in range(1, len(emails)+1):
                print(str(email_index) + " is not in range of the number of emails available")
            else:
                read_email(email_index)
                break

    elif user_choice == 2:
        unread_emails = 0
        for email in emails:
            if not email.has_been_read:
                unread_emails += 1
        print('')
        print("You have " + (str(unread_emails)) + ' unread emails')
        print('')
       

        # add logic here to view unread emails
        for email in emails:
            if not email.has_been_read:
                print('====================================')
                print("Subject: " + str(email.subject_line))
            
    elif user_choice == 3:
        # add logic here to quit appplication
        break
    else:
        print('====================================')
        print("Oops - incorrect input.")
    print('=====================================')