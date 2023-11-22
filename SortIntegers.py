print("Enter three integers:")
num1 = int(input())
num2 = int(input())
num3 = int(input())

# Sort the integers in non-decreasing order
if num1 > num2:
    num1, num2 = num2, num1
if num2 > num3:
    num2, num3 = num3, num2
if num1 > num2:
    num1, num2 = num2, num1

print("The integers in non-decreasing order are:", num1, num2, num3)
