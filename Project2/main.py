import random
class Pet:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.hunger = 50 # 0 is starving, 100 is full
        self.tiredness = 50 # 0 is not tired, 100 is sleepy
        self.sleeping = False # false = not sleeping, true = sleeping

    def feed(self):
        if self.sleeping:
            print(f'{self.name} is sleeping...')
        elif self.hunger > 80 and not self.sleeping:
            print(f'{self.name} is too full and cannot eat anymore')
        else:
            print(f'{self.name} is eating!')
            self.hunger += 20
            self.hunger = max(self.hunger, 0)

    def sleep(self):
        if self.tiredness < 70:
            print(f'{self.name} is not tired')
        elif self.sleeping:
            print(f'{self.name} is already asleep...')
        else:
            self.sleeping = True
            print(f'{self.name} has fallen asleep...')

    def wake_up(self):
        if not self.sleeping:
            print(f'{self.name} is already awake...')
        else:
            self.tiredness = 0
            self.sleeping = False
            print(f'{self.name} is awake...')

    def exercise(self):
        if self.tiredness > 50 and self.hunger < 50:
            print(f'{self.name} is hungry and tired and cannot exercise...')
        elif self.hunger < 50:
            print(f'{self.name} is hungry and cannot exercise...')
        elif self.tiredness > 50:
            print(f'{self.name} is too tired and cannot exercise...')
        else:
            self.hunger -= 20
            self.tiredness += 20

    def pass_time(self):
        activities = ['chasing a laser', 'starring out the window', 'chasing a mouse']
        self.age += 1
        self.hunger -= 10
        self.tiredness += 10
        self.hunger = max(self.hunger, 0)
        self.tiredness = min(self.tiredness, 100)
        activity = random.choice(activities)
        print(f'{self.name} is bored and is {activity}...')
        self.grow()

    def grow(self):
        if self.age <= 1:
            print(f'{self.name} is still a kitten...')
        elif self.age > 1 and self.age <= 10:
            print(f'{self.name} is an adult...')
        else:
            print(f'{self.name} is an old cat...')

if __name__ =="__main__":
    pet_name = str(input("Please enter your pet name: "))
    pet = Pet(pet_name)
    while True:
        print(f'Age: {pet.age}')
        print(f'Hunger: {pet.hunger}')
        print(f'Tiredness: {pet.tiredness}')
        print("\n--- Menu ---")
        print("1. Feed pet")
        print("2. Put pet to sleep")
        print("3. Wake pet up")
        print("4. Exercise pet")
        print("5. Let time pass")
        print("6. Quit")
        choice = input("Choose an action: ")

        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.sleep()
        elif choice == "3":
           pet.wake_up()
        elif choice == "4":
           pet.exercise()
        elif choice == "5":
            pet.pass_time()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
