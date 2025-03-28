# The triangle module has functions that perform
# calculations related to triangles.

# The area function accepts a triangles's base and
# height as arguments and returns the triangles's area.


def area(base, height):
    calc = (base * height)/2
    return calc

# The perimeter function accepts a triangles's 3 lengths
# and returns the triangle's perimeter.


def perimeter(a, b, c):
    length = a + b + c
    return length
