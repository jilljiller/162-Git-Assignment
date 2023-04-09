# CS 16X Git Assignment

# Project requires TWO functions:
# 1. rect_area (length, width) which will return the area of a rectangle
def rect_area(length, width):
    area = length * width
    return area


# 2. rect_solid_area (length, width, height) which will return the area of a solid rectangular object
def rect_solid_area(length, width, height):
    area = 2 * (rect_area(length, width) + rect_area(height, length) + rect_area(height, width))
    return area


# Request the dimension of a solid rectangular object
length = int(input("Enter the length of the the object as in integer: "))
width = int(input("Enter the width of the the object as in integer: "))
height = int(input("Enter the height of the the object as in integer: "))


# Find the surface area and store it into a variable surface_area
surface_area = rect_solid_area(length, width, height)


# Print final measurements
print("Length = ", length, "Width = ", width, "Height = ", height)
print("Total Surface Area = ", surface_area)


# End
