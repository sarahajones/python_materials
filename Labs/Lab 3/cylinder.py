# The cylinder module has functions that perform
# calculations related to cylinders.

import math

pi = math.pi

# The surface area function accepts a cylinder's radius and height
# as arguments and returns the cylinder's surface area.


def surface_area(radius, height):
    calc = (2 * pi * radius * height) + (2 * pi * (radius ** 2))
    return calc

# The volume function accepts a cylinder's radius and height
# and returns the cylinder's volume.


def volume(radius, height):
    calc = pi * (radius ** 2) * height
    return calc
