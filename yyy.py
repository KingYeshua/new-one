
family = []

question = input("Would you like to add a name to the Family ? (Yes or No)	")

while question.lower() == "yes":
	name = input("\nWhat name do you want to add to family ?	")
	family.append(name)
	question = input("\nWould you like to add another name to Family ? (Yes or No)	")

print("\nThere are {} family members.".format(len(family)))
print("\nThe names of the family are: {}".format(family))
