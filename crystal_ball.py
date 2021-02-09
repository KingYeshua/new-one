
import random 

def crystal_ball():
	print("\nWelcome to the Crystal Ball. \nAsk any question you wish.")

	quest = input("\nPlease Enter your question. >	")

	my_list = [ "Sometimes we overlook that which is right in front of our eyes. Learn to see, don't just look." "What is meant to be, will be. " "Everything will be alright." "I would encourage you to look within", "What you seek is what you shall find. Stay positive in your mind, at all times!", "Your future is cloudy even for my crystal ball", "Yes", "Absolutely.", "Your deepest desires will soon become your greatest strength!"]

	print("I see....I see....\nAhhh there it is.\n")


	print(random.choice(my_list))

crystal_ball()