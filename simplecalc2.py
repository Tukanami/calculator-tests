def area(length, width):
    ShapeArea = length * width
    print("Area = ", ShapeArea)

response = None
while response not in ("Yes","No"):
    response = input("Would you like to calculcate the area of the rectangle? Enter Yes or No.")
    response = response.lower()

    if response == "yes":
        length = int(input("Enter the length of the rectangle."))
        width = int(input("Enter the width of the rectangle."))
        area(length, width)
        exit(0)

    elif response == "no":
        exit(0)
