"""
This task manager program is designed for use by an office of varying users.
All users can assign and mark tasks as complete.
Admin has special priviliges such as creating user logins and viewing statistics and task metrics.
"""


# ===================== IMPORT SECTION ===============================
# We will use the datetime module to check whether tasks are overdue
import datetime

# ==================== FUNCTION SECTION ==============================

# allows user 'admin' to create a new user login on the system
def reg_user():
    """
    Asks user for username input
    Checks user.txt file to see if new user already exists
    Asks user to create a password then confirm password
    Writes new user login to user.txt file
    """
    print("You have chosen to add a new user to the system.")
    while True:
        new_username = input("Enter a username: ")
        with open('user.txt', 'r') as user_sheet:
            if new_username not in user_sheet.read():
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
                print("User already exists! Please try a differnent username.")


# allows the user to create a new task and writes it to text file
def add_task():
    """
    Asks user to enter name of user to assign the task to
    Asks user to enter task title
    Asks user for description of task
    Asks user for task due date
    Asks user to enter today's date
    Automatically sets task as incomplete
    Writes task detail to tasks.txt file
    """
    print("You have chosen to add a new task.")
    task_user = input(
        "Please enter the username of the person you wish to assign the task to: "
        )
    task_name = input("Please enter a title for the task you wish to assign: ")
    task_description = input("Enter a description for the task: ")
    task_due = input("Enter the due date for this task (dd Mon yyyy format): ")
    date_assigned = input("Enter today's date (dd Mon yyyy format): ")
    completed = "No"
    with open('tasks.txt', 'a') as task_sheet:
        task_sheet.write(f"{task_user}, {task_name}, {task_description}, {task_due}, {date_assigned}, {completed}\n")
    print(f"You have successfully added a new task for user: {task_user}")

# shows the user all currently assigned tasks in text file
def view_all():
    """
    Opens tasks.txt file
    Creates a list for each line then displays its contents
    """
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

# shows user the tasks assigned to them, stores each task in list for selection
def view_mine():
    """
    Opens tasks.txt file
    Starts task number counter at 0
    Checks each task in file
    Adds the task to the users tasks if their name is assigned to the task
    Increases task number counter by 1
    Adds task to all tasks instead if users name is not assigned to the task
    """
    with open('tasks.txt', 'r') as task_sheet:
        task_no = 0
        for line in task_sheet:
            tasks = line.split(', ')
            if username in tasks:
                print(f"""----------------------
Task No.{task_no}:      \t{tasks[1]}
Assigned to:      {tasks[0]}
Date assigned:    {tasks[4]} 
Due date:         {tasks[3]}
Task complete?    {tasks[5]}
\nTask description:    \n{tasks[2]}
""")
                task_no += 1
                user_tasks.append(tasks)
            else:
                all_tasks.append(tasks)

# Checks whether a task is marked as complete in text file
def check_complete():
    return task_choice[-1]

# overwrites everything in text file with most up to date data
def write_to_file():
    """
    Concatenates all tasks and user tasks lists
    Converts the new list to a string
    Writes all the tasks to the tasks.txt file
    """
    tasks_to_write = all_tasks + user_tasks
    all_tasks_string = "".join(", ".join(tasks) for tasks in tasks_to_write)
    with open('tasks.txt', 'w') as task_sheet:
        task_sheet.write(all_tasks_string)

# marks task as complete in text file
def mark_complete():
    """
    Changes task choice list item to Yes
    Uses write to file function above to update the text file
    Provides confirmation to user
    """
    task_choice[-1] = "Yes\n"
    write_to_file()
    print("Task marked as complete! Returning to task selection menu...")

# reassigns user the task is assigned to in text file
def reassign_user():
    """
    Asks user to enter name of user to reassign task to
    Updates task choice list item 0 to value entered by user
    Uses write to file function above to update text file
    Provides confirmation to user
    """
    while True:
        assign_to = input("""
        Please enter the name of the user you wish to assign the task to:
        """).lower()
        task_choice[0] = assign_to
        write_to_file()
        print(f"Task successfully re-assigned to user: {assign_to}")
        break

# edits due date of task within text file
def change_due_date():
    """
    Asks user to enter new due date
    Updates task choice list due date value
    Uses write to file function to update text file
    Provides confirmation for user
    """
    new_due_date = input("""
    Please enter the new due date in dd MON yyyy format: 
    """)
    task_choice[-2] = new_due_date
    write_to_file()
    print(f"Due date for task changed to: {new_due_date}")

# Converts date format 'MON' to 'mm'
def convert_date_format(month):
    if month == "Jan":
        month = "1"
    elif month == "Feb":
        month = "2"
    elif month == "Mar":
        month = "3"
    elif month == "Apr":
        month = "4"
    elif month == "May":
        month = "5"
    elif month == "Jun":
        month = "6"
    elif month == "Jul":
        month = "7"
    elif month == "Aug":
        month = "8"
    elif month == "Sep":
        month = "9"
    elif month == "Oct":
        month = "10"
    elif month == "Nov":
        month = "11"
    elif month == "Dec":
        month = "12"
    return month

# calculates percentage of task type such as incomplete or overdue
def calc_percentage(list1):
    """
    Takes list argument such as 'incomplete tasks'
    Calculates percentage against all tasks
    Returns output to user
    """
    percentage = len(list1) / len(all_tasks) * 100
    return percentage

# Reads task overview and user overview files then displays them in the console
def display_statistics(): 
    with open('task_overview.txt', 'r') as task_overview:
        task_overview_read = task_overview.read()
        print(task_overview_read)
    with open('user_overview.txt', 'r') as user_overview:
        user_overview_read = user_overview.read()
        print(user_overview_read)

# ==================== LOGIN SECTION =========================

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


# =========================  MAIN MENU =============================

while True:
    # Presenting menu to user. 
    # Which menu the user will see will depend on if they are logged in as admin
    # user input will be converted to lowercase
    if username == 'admin':
        menu = input('''Select one of the following Options below:
    r - Register a new user
    a - Add a new task
    va - View all tasks
    vm - View my tasks
    gr - Generate reports
    ds - View statistics
    e - Exit
    : ''').lower()

    else:
        menu = input('''Select one of the following Options below:
    a - Add a new task
    va - View all tasks
    vm - View my tasks
    e - Exit
    : ''').lower()

    # Option to new user account to system. Only appears for admin in the menu
    if menu == 'r':
        if username == 'admin':
            reg_user()
        else:
            print("Access denied. Please contact the admin to add new users.")


    # allows user to create a new task and assign it to any user
    elif menu == 'a':
        add_task()


    # Allows user to view all current tasks
    elif menu == 'va':
        view_all()


    # Allows user to see their own currently assigned tasks
    # Creates two lists that will store data for writing any changes to our tasks file
    elif menu == 'vm':
        all_tasks = []
        user_tasks = []
        view_mine()
        while True:

            # Gives user option to select and edit one of their tasks
            select_task = (input("""
            Enter task number to edit a task, or type '-1' to return to main menu: 
            """))

            if select_task != "-1":
                task_choice = user_tasks[int(select_task)]
                # Runs a check to see if task is complete, 
                # if it is complete it cannot be edited
                check_complete()
                if check_complete() == "No\n":
                    while True:
                        edit_selection = input("""
                        ---------------------------------
                        Please choose one of the following options:
                        1. (Press 1) to mark task as complete
                        2. (Press 2) to change user task is assigned to
                        3. (Press 3) to change the due date for this task
                        0. (Press 0) to return to task selection
                        ---------------------------------
                        """)
                        if edit_selection == "1":
                            mark_complete()
                            break    # while loop will break here, as the task is now complete and can't be edited
                        elif edit_selection == "2":
                            reassign_user()
                        elif edit_selection == "3":
                            change_due_date()
                        elif edit_selection == "0":
                            break
                        else:
                            print("Please choose a valid option and try again.")
                else:
                    print("Task has already been completed and cannot be edited.")
            else:
                break

    # Allows admin user to generate report documents
    elif menu == 'gr':
        """
        First off, we will create several lists to store our data
        Then, we open our tasks file
        We will loop through each line and append each task to our all_tasks list

        Then, depending which criteria are met, we will add each task to the appropriate list
        If the task is complete, it will go in completed_tasks
        If the task is incomplete, it will go in incomplete_tasks
        We will use the datetime module to check whether a task is overdue
        Then, add it to the appropriate list if necessary

        Once we've added the tasks to the appropriate lists, we will calculate a couple of percentages
        Then, write our data to the task overview file, creating the file if it doesnt exist already
        """
        all_tasks = []
        completed_tasks = []
        incomplete_tasks = []
        overdue_tasks = []
        all_users = []

        with open('tasks.txt', 'r') as task_sheet:
            for line in task_sheet:
                tasks = line.split(', ')
                all_tasks.append(tasks)
                if tasks[-1] == "Yes\n":
                    completed_tasks.append(tasks)
                if tasks[-1] == "No\n":
                    incomplete_tasks.append(tasks)
                due_date = tasks[-2].split(' ')
                due_date[1] = convert_date_format(due_date[1])
                today = datetime.datetime.today()
                due_date = [int(date) for date in due_date]
                if datetime.datetime(due_date[2], due_date[1], due_date[0]
                    ) < today and tasks[-1] == "No\n":
                    overdue_tasks.append(tasks)

        percentage_incomplete = calc_percentage(incomplete_tasks)
        percentage_overdue = calc_percentage(overdue_tasks)

        # Here is where we write the data to our task overview file:
        with open('task_overview.txt', 'w+') as task_overview: 
            task_overview.write(
                f"""
<-------- TASK OVERVIEW REPORT -------->
------------------------------------------------------------
Total number of tasks generated and tracked: {len(all_tasks)}
Total number of completed tasks: {len(completed_tasks)}
Total number of uncompleted tasks: {len(incomplete_tasks)}
Total number of tasks overdue: {len(overdue_tasks)}
Percentage of incomplete tasks: {round(percentage_incomplete)}%
Percentage of tasks overdue: {round(percentage_overdue)}%
------------------------------------------------------------
"""
        )

        # Next we will grab the list of users from our user sheet
        with open('user.txt', 'r') as user_sheet:
            for line in user_sheet:
                user = line.split(', ')
                user = user[0]
                all_users.append(user)

        # Here, we will open the file in write mode, so we can overwrite any previous data
        # Then, we will write some global stats to the file
        with open('user_overview.txt', 'w') as user_overview: 
            user_overview.write(
                f"""
< -------- USER OVERVIEW REPORT -------->
------------------------------------------------------------

Total number of users registered: {len(all_users)}
Total number of tasks generated: {len(all_tasks)}

------------------------------------------------------------
"""
        )


        """
        Next up, we need to create some lists to contain data for each user
        We will cycle through every task and see if it belongs to the user
        Then we will append the task to the appropriate list for the user
        Then we will calculate some percentages

        Lastly, with the user_overview file open in append mode
        We will write the appropriate statistics to the file for each user
        """


        for user in all_users:
            # First, we create our lists
            tasks_for_user = []
            complete_tasks_for_user = []
            incomplete_tasks_for_user = []
            overdue_tasks_for_user = []

            # Then, we use conditionals to add our tasks to the appropriate list
            for task in all_tasks:
                if task[0] == user:
                    tasks_for_user.append(task)
            for task in completed_tasks:
                if task[0] == user:
                    complete_tasks_for_user.append(task)
            for task in incomplete_tasks:
                if task[0] == user:
                    incomplete_tasks_for_user.append(task)
            for task in overdue_tasks:
                if task[0] == user:
                    overdue_tasks_for_user.append(task)

            # Here, we will calculate our percentages
            percentage_assigned_for_user = calc_percentage(tasks_for_user)
            percentage_complete_for_user = calc_percentage(complete_tasks_for_user)
            percentage_incomplete_for_user = calc_percentage(incomplete_tasks_for_user)
            percentage_overdue_for_user = calc_percentage(overdue_tasks_for_user)

            # Finally, we write the user's data to the file in append mode here
            with open('user_overview.txt', 'a') as user_overview_append:
                user_overview_append.write(f"""
User: {user}
Number of tasks assigned: {len(tasks_for_user)}
Percentage of tasks assigned: {round(percentage_assigned_for_user)}%
Percentage of tasks completed: {round(percentage_complete_for_user)}%
Percentage of tasks still to complete: {round(percentage_incomplete_for_user)}%
Percentage of tasks overdue: {round(percentage_overdue_for_user)}%

------------------------------------------------------------
"""
        )

        print()
        print("Reports successfully generated.")
        print()

    # Allows user to view total number of users and tasks. Option only visible to admin in main menu.
    elif menu == 'ds':
        display_statistics()
    # Exits the program
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    # Prompts user to make a valid choice from the menu again
    else:
        print("You have made a wrong choice, Please Try again")