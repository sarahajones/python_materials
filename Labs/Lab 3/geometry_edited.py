
# This program allows the user to choose various
# geometry calculations from a menu. This program
# imports the circle and rectangle modules.

import circle
import rectangle
import triangle
import sphere
import cylinder

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
        elif choice == 5:
            base = float(input("Enter the triangle's base': "))
            height = float(input("Enter the triangle's height': "))
            print(f'The area is {triangle.area(base, height):.3f}')
        elif choice == 6:
            a = float(input("Enter the length of the first side of the triangle: "))
            b = float(input("Enter the length of the second side of the triangle: "))
            c = float(input("Enter the length of the third side of the triangle: "))
            print(f'The perimeter is {triangle.perimeter(a, b, c):.3f}')
        elif choice == 7:
            radius = float(input("Enter the sphere's radius: "))
            print(f'The surface area is {sphere.surface_area(radius):.3f}')
        elif choice == 8:
            radius = float(input("Enter the spheres's radius: "))
            print(f'The volume is {sphere.volume(radius):.3f}')
        elif choice == 9:
            radius = float(input("Enter the cylinder's radius: "))
            height = float(input("Enter the cylinder's height: "))
            print(f'The surface area is {cylinder.surface_area(radius, height):.3f}')
        elif choice == 10:
            radius = float(input("Enter the cylinder's radius: "))
            height = float(input("Enter the cylinder's height: "))
            print(f'The volume is {cylinder.volume(radius, height):.3f}')
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
    print("5) Area of a triangle")
    print("6) Perimeter of a triangle")
    print("7) Surface area of a sphere")
    print("8) Volume of a sphere")
    print("9) Surface area of a cylinder")
    print("10) Volume of a cylinder")
    print("11) Quit")


# Call the main function.

main()
