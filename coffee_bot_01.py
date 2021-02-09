
def coffee_bot():
	print('Welcome to coffee bot.')
	name = input('What is your name?	')
	size = get_drink_size()
	drink_type = get_drink_type()
	temperature = temp()
	print('Ok we got a {} {} {} for {} coming right up! '.format(temperature, size, drink_type, name))


def get_drink_size():
	res = input('What size would you like? \n[a] Small \n[b] Medium \n[c] Large \n> ')
	if res == 'a':
		return 'Small'
	elif res == 'b':
		return 'Medium'
	elif res == 'c':
		return 'Large'
	else:
		print_message()
		return get_drink_size()

def get_drink_type():
	res = input('What kind of coffee would you like? \n[a] Latte \n[b] Brewed Coffee \n[c] Mocha \n> ')
	if res == 'a':
		return 'Latte'
	elif res == 'b':
		return 'Brewed Coffee'
	elif res == 'c':
		return 'Mocha'
	else:
		print_message()
		return get_drink_type()

def temp():
	res = input('Would you like it hot or iced ?')
	if res == 'hot':
		return 'hot'
	elif res == 'iced':
		return 'iced'
	else:
		print_message()
		return temp()


def print_message():
	print('Invalid entry, please put a valid response. ')

coffee_bot()