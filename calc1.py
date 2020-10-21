#creating a simple calculator to figure out area or perimeter
def area(length,width):
    ShapeArea = length * width
    print("Area =", ShapeArea)

def perimeter(length,width):
    ShapePerimeter = length*2 + width*2
    print("Perimeter = ", ShapePerimeter)

response = None
while response not in ("a","p"):
    response = input("Would you like to calculate area or perimeter? Enter a or p. >")
    response = response.lower()

if response == "a":
    length = int(input("Enter the length of the rectangle. >"))
    width = int(input("Enter the width of the rectangle. >"))
    area(length, width)

elif response == "p":
    length = int(input("Enter the length of the rectangle. >"))
    width = int(input("Enter the width of the rectangle. >"))
    perimeter(length, width)
