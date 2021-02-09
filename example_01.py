import random, sys


while True:
	print("Welcome to the Oracle. ")

	while True:
		userIn = input("Enter quit to exit or ask to continue.		")

		if userIn == "quit":
			sys.exit()
		elif userIn == "ask":
			break

	name = input("What is your name ?		")
	quest = input("What is the question you want to ask the Oracle ?		")

	print(name + " would like to know " + quest)

	rando = random.randint(1, 3)

	if rando == 1:
		print("Yes")
	elif rando == 2:
		print("No")
	elif rando == 3:
		print("Check back later.")



