
# C = (F - 32) * 5/9
# F = (C * 9/5) + 32

def degree_conversion():

	print("Temperature Conversion Program")

	q = input("Would you like to convert ceslsius to fahrenheit or fahrenheit to celsius ?		")
	x = float(input("Ok, what temperature would you like to convert ?		"))

	if q == "celsius to fahrenheit":
		print((x * 9/5) + 32)
	elif q == "fahrenheit to celsius":
		print((x - 32) * 5/9)
	else:
		print("Invalid entry. Please answer the question and put a valid response.")

degree_conversion()
