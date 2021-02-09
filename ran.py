
import random

ran = random.randint(1000, 3000)

def order(num1, num2, num3):
	if num1 >= num2 and num3:
		print(num1)
	elif num2 >= num1 and num3:
		print(num2)
	elif num3 >= num1 and num2:
		print(num3)


order(ran, ran, ran)
order.sort()
print(sort(order()))


#code above works for one but i want all three ordered


