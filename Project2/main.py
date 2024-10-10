import random

def pet_feed(hunger, name):
    if hunger > 80:
        print(f'{name} is too full and cannot eat anymore')
    else:
        print(f'{name} is eating!')
        hunger += 20
    return hunger

def pet_sleep(sleeping, tiredness, name):
    if tiredness < 70:
        print(f'{name} is not tired')
    elif sleeping:
        print(f'{name} is already asleep...')
    else:
        sleeping = True
        print(f'{name} has fallen asleep...')
        return sleeping

def pet_wake_up(sleeping, tiredness, name):
    if not sleeping:
        print(f'{name} is already awake...')
    else:
        tiredness = 0
        sleeping = False
        print(f'{name} is awake...')
        return sleeping, tiredness

def pet_exercise(hunger, tiredness, name):
    if tiredness > 50 and hunger > 50:
        print(f'{name} is hungry and tired and cannot exercise...')
    elif hunger > 50:
        print(f'{name} is hungry and cannot exercise...')
    elif tiredness > 80:
        print(f'{name} is too tired and cannot exercise...')
    else:
        hunger -= 20
        tiredness += 20
    return hunger, tiredness

def pet_pass_time(age, hunger, tiredness, name):
    activities = ['chasing a laser', 'starring out the window', 'chasing a mouse']
    age += 1
    hunger -= 10
    tiredness += 10
    activity = random.choice(activities)
    print(f'{name} is bored and is {activity}...')
    grow(age)
    return age, hunger, tiredness

def grow(age):
    pass

if __name__ =="__main__":
    pet_name = str(input("Please enter your pet name: "))
    age = 0
    hunger = 50 # 100 is full
    tiredness = 50 # 100 is sleepy
    sleeping = False # false = not sleeping, true = sleeping
    
    while True:
        print(f'Age: {age}')
        print(f'Hunger: {hunger}')
        print(f'Tiredness: {tiredness}')
        print("\n--- Menu ---")
        print("1. Feed pet")
        print("2. Put pet to sleep")
        print("3. Wake pet up")
        print("4. Exercise pet")
        print("5. Let time pass")
        print("6. Quit")
        choice = input("Choose an action: ")

        if choice == "1":
            hunger = pet_feed(hunger, pet_name)
        elif choice == "2":
            sleeping = pet_sleep(sleeping, tiredness, pet_name)
        elif choice == "3":
           (sleeping, tiredness) = pet_wake_up(sleeping, tiredness, pet_name)
        elif choice == "4":
           (hunger, tiredness) = pet_exercise(hunger, tiredness, pet_name)
        elif choice == "5":
            (age, hunger, tiredness) = pet_pass_time(age, hunger, tiredness, pet_name)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
