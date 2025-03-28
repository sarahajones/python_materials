# The sphere module has functions that perform
# calculations related to spheres.

import math

pi = math.pi

# The surface area function accepts a sphere's radius
# as an argument and returns the sphere's surface area.


def surface_area(radius):
    calc = 4 * pi * (radius ** 2)
    return calc

# The volume function accepts a sphere's radius
# and returns the sphere's volume.


def volume(radius):
    calc = (4 / 3) * pi * (radius ** 3)
    return calc
