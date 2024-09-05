def display_intro():
    print("Welcome to the Choose Your Own Adventure Game!")
    print("In this game, you will make choices that will shape the outcome of the story.")
    print("Let's begin your adventure!")

def first_decision():
    print("\nYou find yourself at a crossroad in a dense forest.")
    print("Do you want to:")
    print("1. Take the left path")
    print("2. Take the right path")

    choice = input("Enter the number of your choice: ")
    if choice == '1':
        left_path()
    elif choice == '2':
        right_path()
    else:
        print("Invalid choice. Please try again.")
        first_decision()

def left_path():
    print("\nYou take the left path and soon come across a mysterious old man.")
    print("He offers you two choices:")
    print("1. Accept a magical amulet from him")
    print("2. Politely refuse and continue on your way")

    choice = input("Enter the number of your choice: ")
    if choice == '1':
        magical_amulet()
    elif choice == '2':
        continue_journey()
    else:
        print("Invalid choice. Please try again.")
        left_path()

def right_path():
    print("\nYou take the right path and find a beautiful waterfall.")
    print("Do you want to:")
    print("1. Swim in the waterfall")
    print("2. Explore the cave behind the waterfall")

    choice = input("Enter the number of your choice: ")
    if choice == '1':
        swim_waterfall()
    elif choice == '2':
        explore_cave()
    else:
        print("Invalid choice. Please try again.")
        right_path()

def magical_amulet():
    print("\nThe old man smiles and gives you a magical amulet.")
    print("You soon discover that the amulet grants you the ability to understand animals.")
    print("You use this power to befriend a wise old owl who helps you find a hidden treasure.")
    print("Congratulations! You have found the treasure and won the game!")

def continue_journey():
    print("\nWithout the amulet, your journey is challenging.")
    print("You encounter various obstacles but manage to overcome them.")
    print("Eventually, you find your way out of the forest and return home safely.")
    print("You may not have found treasure, but you’ve had a memorable adventure!")

def swim_waterfall():
    print("\nAs you swim in the waterfall, you feel refreshed and relaxed.")
    print("However, you soon realize that the water is enchanted, and you begin to shrink!")
    print("You find yourself in a magical land where you need to solve puzzles to return to your normal size.")
    print("After solving the puzzles, you find your way back to the real world.")
    print("Your adventure ends here. Thank you for playing!")

def explore_cave():
    print("\nYou enter the cave and discover ancient drawings on the walls.")
    print("As you examine the drawings, you find a hidden exit that leads to a beautiful meadow.")
    print("In the meadow, you find a small village where you are welcomed as a hero.")
    print("You enjoy a peaceful life in the village and live happily ever after.")
    print("Congratulations on your adventure!")

def main():
    display_intro()
    first_decision()

if __name__ == "__main__":
    main()
