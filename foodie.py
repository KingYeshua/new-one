
import random, sys

while True:
	print("Welcome to the food picker.")

	while True:
		print("Enter quit to quit or choose to choose")
		userIn = input()

		if userIn == "quit":
			sys.exit()
		elif userIn == "choose":
			break
			

	rando = random.randint(1, 6)

	if rando == 1:
		print("Steak")
	elif rando == 2:
		print("Lobster")
	elif rando == 3:
		print("Salad")
	elif rando == 4:
		print("Spagetti")
	elif rando == 5:
		print("Pho")
	elif rando == 6:
		print("Quesadilla")