number1 = int(input('Enter first: '))
number2 = int(input('Enter second: '))
number3 = int(input('Enter third: '))
number4 = int(input('Enter fourth: '))

if number1 > number2 and number1 > number3 and number1 > number4:
	print(number1)

if number2 > number1 and number2 > number3 and number2 > number4:
	print(number2)

if number3 > number2 and number3 > number1 and number3 > number4:
	print(number3)

if number4 > number2 and number4 > number1 and number4 > number3:
	print(number4)