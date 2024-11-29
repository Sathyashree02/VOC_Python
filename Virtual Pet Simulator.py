#Sathyashree's Virtual Pet Simulator
import random
import time

class Pet:
    def __init__(self, name):
        self.name = name
        self.happiness = 50
        self.hunger = 50

    def feed(self):
        if self.hunger > 0:
            self.hunger -= 10
            self.happiness -= 5
            print(f"{self.name} has been fed.")
        else:
            print(f"{self.name} is not hungry!")

    def play(self):
        if self.happiness < 100:
            self.happiness += 10
            self.hunger += 5
            print(f"{self.name} enjoyed playing!")
        else:
            print(f"{self.name} is already very happy!")

    def give_toy(self):
        if self.happiness < 100:
            happiness_increase = random.randint(5, 15)
            self.happiness += happiness_increase
            print(f"{self.name} received a toy! Happiness increased by {happiness_increase}.")
        else:
            print(f"{self.name} is already very happy!")

    def give_medicine(self):
        if self.happiness > 0:
            happiness_increase = random.randint(10, 20)
            self.happiness += happiness_increase
            print(f"{self.name} took medicine! Happiness increased by {happiness_increase}.")
        else:
            print(f"{self.name} is too sad to take medicine.")

    def check_status(self):
        print(f"{self.name}'s Happiness: {self.happiness}, Hunger: {self.hunger}")

    def update(self):
        self.hunger += 5
        self.happiness -= 2
        self.hunger = min(100, self.hunger)
        self.happiness = max(0, self.happiness)

    def is_alive(self):
        if self.hunger >= 100:
            print(f"{self.name} has become too hungry and has passed away.")
            return False
        elif self.happiness <= 0:
            print(f"{self.name} has become too sad and has passed away.")
            return False
        return True

class VirtualPetSimulator:
    def __init__(self):
        self.pets = []

    def add_pet(self, name):
        pet = Pet(name)
        self.pets.append(pet)
        print(f"{name} has been added to your pets!")

    def display_menu(self):
        print("\nMenu:")
        print("1. Feed Pet")
        print("2. Play with Pet")
        print("3. Give Pet a Toy")
        print("4. Give Pet Medicine")
        print("5. Check Pet Status")
        print("6. Quit")

    def random_event(self):
        event = random.choice(["find snack", "get sick"])
        if event == "find snack":
            snack_happiness = random.randint(5, 15)
            for pet in self.pets:
                pet.happiness += snack_happiness
                pet.happiness = min(100, pet.happiness)
            print(f"{', '.join(pet.name for pet in self.pets)} found a snack! Happiness increased.")
        elif event == "get sick":
            for pet in self.pets:
                pet.happiness -= 10
            print(f"{', '.join(pet.name for pet in self.pets)} got sick! Happiness decreased.")

    def run(self):
        print("Welcome to the Sathyashree's Virtual Pet Simulator!")
        num_pets = int(input("How many pets would you like to add? "))
        for _ in range(num_pets):
            pet_name = input("Enter the name of your pet: ")
            self.add_pet(pet_name)

        while True:
            self.display_menu()
            choice = input("Choose an action: ")

            if choice == '1':
                for pet in self.pets:
                    pet.feed()
            elif choice == '2':
                for pet in self.pets:
                    pet.play()
            elif choice == '3':
                for pet in self.pets:
                    pet.give_toy()
            elif choice == '4':
                for pet in self.pets:
                    pet.give_medicine()
            elif choice == '5':
                for pet in self.pets:
                    pet.check_status()
            elif choice == '6':
                print("Thanks for playing!")
                break
            else:
                print("Invalid choice. Please try again.")

            # Update pets and check if they are alive
            for pet in self.pets:
                pet.update()

            # Check for dead pets
            dead_pets = [pet for pet in self.pets if not pet.is_alive()]
            for dead_pet in dead_pets:
                self.pets.remove(dead_pet)

            # Check if all pets are dead
            if not self.pets:
                print("Game Over! All your pets have passed away.")
                if input("Would you like to start a new game? (yes/no): ").lower() == 'yes':
                    self.pets = []
                    self.run()  # Restart the game
                else:
                    print("Thanks for playing!")
                    break

            # Random event
            if random.random() < 0.3:  # 30% chance for a random event
                self.random_event()

            time.sleep(1)  # Wait a second before next action

if __name__ == "__main__":
    simulator = VirtualPetSimulator()
    simulator.run()