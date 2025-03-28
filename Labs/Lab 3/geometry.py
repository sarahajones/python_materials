
# This program allows the user to choose various
# geometry calculations from a menu. This program
# imports the circle and rectangle modules.

import circle
import rectangle

# The main function.


def main():

    # The choice variable controls the loop
    # and holds the user's menu choice.
    choice = 0

    while not (choice == 11):
        # display the menu.
        display_menu()

        # Get the user's choice.
        choice = int(input('Enter your choice: '))

        # Perform the selected action.
        if choice == 1:
            r = float(input("Enter the circle's radius: "))
            print(f'The area is {circle.area(r):.3f}.')
        elif choice == 2:
            radius = float(input("Enter the circle's radius: "))
            print(f'The circumference is {circle.circumference(radius):.3f}')
        elif choice == 3:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print(f'The area is {rectangle.area(width, length):.3f}')
        elif choice == 4:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print(f'The perimeter is {rectangle.perimeter(width, length):.3f}')





        elif choice == 11:
            print("Exiting the program...")
        else:
            print("Error: invalid selection.")

# The display_menu function displays a menu.


def display_menu():
    print("        MENU for ")
    print("1) Area of a circle")
    print("2) Circumference of a circle")
    print("3) Area of a rectangle")
    print("4) Perimeter of a rectangle")

    print("5) Quit")


# Call the main function.
main()
