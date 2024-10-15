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

def create_new_workflow():
    workflow = str(input("Input Workflow name: "))
    if os.path.exists(workflow):
        print("This Workflow already exists!")
    else:
        path = os.path.join(workflow)
        os.mkdir(path)

def create_new_stage():
    stage = str(input("Input Stage name: "))
    if os.path.exists(stage):
        print("This Stage already exists!")
    else:
        path = os.path.join(stage)
        os.mkdir(path)

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
    more = True
    choice = str(input("Do you have an existing Base Directory: (y/n)"))
    if choice == 'n':
        create_basedir()
    basedir = str(input("Please enter your Base Directory name: "))
    os.chdir(basedir)
    print(f"You are in {basedir}")
    workflow = str(input("Do you want to create a new Workflow directory: "))
    if workflow == 'y':
        create_new_workflow()
        while more:
            more_workflow = str(input("Do you want to create more Workflow directories (y/n): "))
            if more_workflow == 'y':
                create_new_workflow
            else:
                more = False
    while true:
        more = True
        valid = True
        while valid:
            workflow = str(input("Enter Workflow name: "))
            if os.path.exists(workflow):
                os.chdir(workflow)
                valid = False
            else:
                print("This workflow does not exists. Please try again!")
        stage = str(input("Do you want to create a Stage directory: "))
        if stage == 'y':
            create_new_stage()
            while more:
                more_stage = str(input("Do you want to create more Stage directories (y/n): "))
                if more_stage == 'y':
                    create_new_stage()
                else:
                    more = False

        valid = True
        while valid:
            stage = str(input("Enter Stage name: "))
            if os.path.exists(stage):
                os.chdir(stage)
                valid = False
            else:
                print("This stage name does not exists. Please try again!")
            

        option = str(input("To create a text file enter T/ To update a text file enter U: "))
        if option == 'T':
            create_meeting()
        elif option == 'U':
            update_meeting()

        home = os.path.expanduser(f"~/Uni//Uni_Projects/Project1/{basedir}") # this will be different on jupyterhub since your on local laptop rn
        os.chdir(home)

main()