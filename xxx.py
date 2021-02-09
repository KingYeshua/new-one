
players = []

question = input("Would you like to add players to the game? (yes or no) "	)

while question.lower() == 'yes':
	name_add = input("\nEnter the name of players to add to the team:	")
	players.append(name_add)
	question = input("Would you like to add another player ? (Yes or No)	")

print("\nThere are {} players on the team.".format(len(players)))