print("Enter value for 1st side:")
side1 = int(input())

print("Enter value for 2nd side:")
side2 = int(input())

print("Enter value for 3rd side:")
side3 = int(input())

if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    print("Valid!!")
    perimeter = side1 + side2 + side3
    print("Perimeter of the triangle is:", perimeter)
else:
    print("Invalid! The sides do not form a triangle.")
