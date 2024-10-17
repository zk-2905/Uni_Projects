import os
import csv
import pandas
#os.getcwd() shows path
def create_basedir():
    basedir = str(input('Please enter a name for your base directory: '))
    if os.path.exists(basedir): #checks if base directory already exists in system
        print("This directory already exists!")
        pass
    else:
        path = os.path.join(basedir) # adds basedir to the file path
        os.mkdir(path) # creates directory
        print(f"{basedir} is created!")

def create_new_workflow():
    workflow = str(input("Input Workflow name: "))
    if os.path.exists(workflow): # checks if workflow directory already exists
        print("This Workflow already exists!")
    else:
        path = os.path.join(workflow) # adds workflow directory to the file path
        os.mkdir(path) # creates directory

def create_new_stage():
    stage = str(input("Input Stage name: "))
    if os.path.exists(stage): # checks if stage directory already exists
        print("This Stage already exists!")
    else:
        path = os.path.join(stage) # adds stage directory to the file path
        os.mkdir(path) # creates directory

def create_meeting():
    filename = str(input("Enter filename: "))
    amount = int(input('How many people attended the meeting: '))
    with open(filename + '.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Firstname','Lastname','Role'])
        for i in range(amount):
            people = str(input("Enter the persons first name, last name and role seperated by commas: "))
            new_people = people.strip(' ').split(',')
            writer.writerow(new_people)

def count_files_folders(basedir):
    for root, dirs, files in os.walk(f'/Users/zk/Uni/Uni_Projects/Project1/{basedir}'): # path will be different on juypterhub
        print(f"\nIn directory: {root}")
        print(f"Number of subdirectories: {len(dirs)}")
        print(f"Number of files: {len(files)}")

def display_meeting():
    while True:
        filename = str(input("Enter filename: "))
        if not os.path.exists(filename + '.csv'):
            print("Invalid Filename, please try again.")
        elif filename == '':
            break
        else:
            csvFile = pandas.read_csv(filename +'.csv')
            print(csvFile)  
            break
    

def main():
    choice = str(input("Do you have an existing Base Directory: (y/n)"))
    if choice == 'n':
        create_basedir() #
    basedir = str(input("Please enter your Base Directory name: "))
    os.chdir(basedir) # cd into the base directory
    print(f"You are in {basedir}")

    while True:
        workflow = str(input("Do you want to create a new Workflow directory: "))
        if workflow == 'y':
            create_new_workflow()

        while True:
            more_workflow = str(input("Do you want to create more Workflow directories (y/n): "))
            if more_workflow == 'y':
                create_new_workflow()
            else:
                break
        check_files_folders = str(input("Do you want to check how many files and folders there (y/n):  "))
        if check_files_folders == 'y':
            count_files_folders(basedir)

        while True: # checks if workflow name exists and lets user re-enter workflow name
            workflow = str(input("Enter Workflow name: "))
            if os.path.exists(workflow):
                os.chdir(workflow)
                print(f"You are now in {workflow} ")
                break
            else:
                print("This workflow does not exists. Please try again!")
        stage = str(input("Do you want to create a Stage directory (y/n): "))
        if stage == 'y':
            create_new_stage()

        while True:
            more_stage = str(input("Do you want to create more Stage directories (y/n): "))
            if more_stage == 'y':
                create_new_stage()
            else:
                break

        while True: # checks if stage name exists and lets user re-enter stage name
            stage = str(input("Enter Stage name: "))
            if os.path.exists(stage):
                os.chdir(stage)
                print(f'You are now in {stage}')
                break
            else:
                print("This stage name does not exists. Please try again!")
        print("\n--- Menu ---")
        print("1. Create a meeting")
        print("2. Display meeting information")
        print(f"3. Go back to {basedir}")
        choice = int(input("Choose your action: "))
        if choice == 1:
            create_meeting()
        elif choice == 2:
            display_meeting()
        elif choice == 3:
            home = os.path.expanduser(f"~/Uni//Uni_Projects/Project1/{basedir}") # this will be different on jupyterhub since your on local laptop rn
            os.chdir(home)

main()