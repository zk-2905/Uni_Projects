import random
class Pet:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.hunger = 50 # 0 is starving, 100 is full
        self.fatigue = 50 # 0 is not tired, 100 is sleepy
        self.sleeping = False # false = not sleeping, true = sleeping

    def feed(self):
        if self.sleeping:
            print(f'{self.name} is sleeping...')
        elif self.hunger < 20 and not self.sleeping:
            print(f'{self.name} is too full and cannot eat anymore')
        else:
            print(f'{self.name} is eating!')
            self.hunger -= 20
            self.hunger = max(self.hunger, 0) # make sure hunger isnt negative

    def sleep(self):
        if self.fatigue < 70:
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
            self.fatigue = 0
            self.sleeping = False
            print(f'{self.name} is awake...')

    def exercise(self):
        if self.sleeping:
            print(f'{self.name} is sleeping...')
        elif self.fatigue > 50 and self.hunger > 50:
            print(f'{self.name} is hungry and tired and cannot exercise...')
        elif self.hunger > 50:
            print(f'{self.name} is hungry and cannot exercise...')
        elif self.fatigue > 50:
            print(f'{self.name} is too tired and cannot exercise...')
        else:
<<<<<<< Updated upstream
=======
            print(f"{self.name} is exercising...")
>>>>>>> Stashed changes
            self.hunger += 20
            self.fatigue += 20
            self.hunger = min(self.hunger,100) # make sure hunger isnt over 100
            self.fatigue = min(self.fatigue, 100) # make sure tiredness is not over 100

    def pass_time(self):
        if self.sleeping:
            print(f'{self.name} is sleeping...')
        else:
            activities = ['chasing a laser', 'staring out the window', 'chasing a mouse']
            self.age += 1
            self.hunger += 10
            self.fatigue += 10
            self.hunger = min(self.hunger, 100)
            self.fatigue = min(self.fatigue, 100)
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
    start = True
    while start:
        pet_name = str(input("Please enter your pet name: "))
        pet = Pet(pet_name)
        death = random.randint(1,21) # randomise the age of when pet dies
        alive = True
        while alive: # game will continue unitl pet dies
            print(f'Age: {pet.age}')
            print(f'Hunger: {pet.hunger}')
            print(f'Fatigue: {pet.fatigue}')
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
            if pet.age == death:
                print(f'{pet_name} has DIED :(')
                restart = input("Do you want a new pet (y/n): ") # choice for user to have a new pet
                if restart == 'y': # user gets a new pet
                    alive = False
                else: # user ends game
                    alive = False
                    start = False
