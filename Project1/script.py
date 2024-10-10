import os
#os.getcwd() shows path
def create_basedir():
    basedir = str(input('Please enter a name for your base directory: '))
    if os.path.exists(basedir):
        print("This directory already exists!")
        pass
    else:
        path = os.path.join(basedir)
        os.mkdir(path)
        print(f"{basedir} is created!")

def create_new_workflow_stages():
    workflow = str(input("Input Workflow name: "))
    stage = str(input("Input Stage name:  "))
    path1 = os.path.join(workflow)
    path2 = os.path.join(stage)
    os.mkdir(path1)
    os.mkdir(path2)

def create_meeting():
    filename = str(input("Enter filename: "))
    f = open(filename + '.txt', 'w')
    people = str(input("Input all of the attendees: "))
    f.write(people)
    f.close()

def update_meeting():
    filename = str(input("Enter filename: "))
    f = open(filename + '.txt', 'a')
    people = str(input("Input all of the attendees: "))
    f.write(', ' + people)
    f.close()


def main():
    true = True
    choice = str(input("Do you have an existing Base Directory: (y/n)"))
    if choice == 'n':
        create_basedir()
    basedir = str(input("Please enter your Base Directory name: "))
    os.chdir(basedir)
    print(f"You are in {basedir}")
    workflow_stages = str(input("Do you want to create a new set of Workflow and Stages directory: "))
    if workflow_stages == 'y':
        create_new_workflow_stages()
    while true:
        folder = str(input("Do you want to enter into Workflow or Stage: "))
        os.chdir(folder)
        option = str(input("To create a text file enter T/ To update a text file enter U: "))
        if option == 'T':
            create_meeting()
        elif option == 'U':
            update_meeting()

        home = os.path.expanduser(f"~/Uni/Project1/{basedir}") # this will be different on jupyterhub since your on local laptop rn
        os.chdir(home)
        pass

main()