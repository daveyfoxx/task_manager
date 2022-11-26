#====Login Section====
print("Welcome to Task Manager. Please log in to continue.")

# Create list 'user_credentials' and add each line from the file as a list item
user_credentials = []
with open('user.txt', 'r') as user_sheet:
    for line in user_sheet:
        line = line.strip('\n')
        line = line.replace(', ', '')
        user_credentials.append(line)

# Ask user to login and determine if details match
# I have chosen to merge both username and password both in the user_credentials list above,
# and for the user's login entry. Ensuring the password entered is associated with that specific user
while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    login_entry = username + password
    if login_entry in user_credentials:
        print("You are now logged in.")
        break
    else:
        print("Incorrect login credentials. Please try again")

while True:
    # Presenting menu to user. Which menu the user will see will depend on if they are logged in as admin
    # user input will be converted to lowercase
    if username == 'admin':
        menu = input('''Select one of the following Options below:
    r - Register a new user
    a - Add a new task
    va - View all tasks
    vm - View my tasks
    vs - View statistics
    e - Exit
    : ''').lower()

    else:
        menu = input('''Select one of the following Options below:
    a - Add a new task
    va - View all tasks
    vm - View my tasks
    e - Exit
    : ''').lower()

    # Let's admin add new user to system. This option only appears for admin in the menu
    # However, I have also added a failsafe to prevent another user from accessing this accidentally
    if menu == 'r':
        if username == 'admin':
            print("You have chosen to add a new user to the system.")
            while True:
                new_username = input("Enter a username: ")
                new_password = input("Enter a password: ")
                confirm_new_password = input("Confirm password: ")
                if new_password == confirm_new_password:
                    with open('user.txt', 'a') as user_sheet:
                        user_sheet.write(f"\n{new_username}, {new_password}")
                        print(f"User: {new_username} has been successfully added.\n")
                        break
                else:
                    print("Please ensure you type the correct password and try again.")
        else:
            print("Access denied. Please contact the admin to add new users.")

    # Let's user create a new task and assign it to a certain user
    elif menu == 'a':
        print("You have chosen to add a new task.")
        task_user = input("Please enter the username of the person you wish to assign the task to: ")
        task_name = input("Please enter a title for the task you wish to assign: ")
        task_description = input("Enter a description for the task: ")
        task_due = input("Enter the due date for this task: ")
        date_assigned = input("Enter today's date: ")
        completed = "No"
        with open('tasks.txt', 'a') as task_sheet:
            task_sheet.write(f"\n{task_user}, {task_name}, {task_description}, {task_due}, {date_assigned}, {completed}")
        print(f"You have successfully added a new task for user: {task_user}")

    # Allows user to view all current tasks
    elif menu == 'va':
        with open('tasks.txt', 'r') as task_sheet:
            for line in task_sheet:
                tasks = line.split(', ')
                print(f"""----------------------
Task:             {tasks[1]}
Assigned to:      {tasks[0]}
Date assigned:    {tasks[4]} 
Due date:         {tasks[3]}
Task complete?    {tasks[5]}
\nTask description: \n{tasks[2]}
""")

    # Allows user to see their own currently assigned tasks
    elif menu == 'vm':
        with open('tasks.txt', 'r') as task_sheet:
            for line in task_sheet:
                tasks = line.split(', ')
                if username in tasks:
                    print(f"""----------------------
Task:             {tasks[1]}
Assigned to:      {tasks[0]}
Date assigned:    {tasks[4]} 
Due date:         {tasks[3]}
Task complete?    {tasks[5]}
\nTask description: \n{tasks[2]}
""")

    # Allows user to view total number of users and tasks. Option only visible to admin in main menu.
    elif menu == 'vs':
        task_count = 0
        with open('tasks.txt', 'r') as task_sheet:
            for line in task_sheet:
                task_count += 1
        print("------------------------")
        print("Statistics:")
        print(f"Total number of tasks: {task_count}")
        user_count = 0
        with open('user.txt', 'r') as user_sheet:
            for line in user_sheet:
                user_count += 1
        print(f"Total number of users: {user_count}")
        print("------------------------")

    # Exits the program
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    # Prompts user to make a valid choice from the menu again
    else:
        print("You have made a wrong choice, Please Try again")