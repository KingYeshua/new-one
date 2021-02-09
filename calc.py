def calc():

	print("Welcome to the calculator program. ")
	

	op = input("Enter an operator		")
	num1 = int(input("Enter a number		"))
	num2 = int(input("Enter another number		"))

	if op == "+":
		print("{} + {} =  ".format(num1, num2))
		print(num1 + num2)
	elif op == "-":
		print("{} - {} =  ".format(num1, num2))
		print(num1 - num2)
	elif op == "*":
		print("{} * {} =  ".format(num1, num2))
		print(num1 * num2)
	elif op == "/":
		print("{} / {} =  ".format(num1, num2))
		print(num1 / num2)
	else:
		print("You fucked up, try to put a valid entry.")

calc()