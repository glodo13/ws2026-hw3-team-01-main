# IMporting the math module
import math

# Function for calculating the perimeter of a right triangle
def perimeter_right_triangle(c1, c2):
    return c1 + c2 + math.sqrt(c1**2 + c2**2)

# Function for calculating the area of a right triangle
def area_right_triangle(c1, c2):
    return (c1 * c2) / 2

# Function for calculating the perimeter of a circle
def perimeter_circle(r):
    return 2 * math.pi * r

# Function for calculating the area of a circle
def area_circle(r):
    return math.pi * r**2

# Function for calculating the surface area of a sphere
def surface_sphere(r):
    return 4 * math.pi * r**2

# Function for calculating the volume of a sphere
def volume_sphere(r):
    return (4 / 3) * math.pi * r**3

# Function for calculating the surface area of a cylinder
def surface_cylinder(r, h):
    return 2 * math.pi * r * (r + h)

# Function for calculating the volume of a cylinder
def volume_cylinder(r, h):
    return math.pi * r**2 * h

# Function for calculating the surface area of a cone
def surface_cone(r, h):
    return math.pi * r * (r + math.sqrt(r**2 + h**2))

# Function for calculating the volume of a cone
def volume_cone(r, h):
    return (1 / 3) * math.pi * r**2 * h