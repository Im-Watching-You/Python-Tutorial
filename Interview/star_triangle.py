"""Star Triangle"""


def build_triangle(floors):
    """Number of floors in the triangle"""
    for floor in range(floors):
        print(' ' * (floors - floor - 1) + '*' * (2 * floor + 1))


# Execution
star_floors = 10
build_triangle(star_floors)
