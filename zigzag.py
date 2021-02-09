import time, sys
indent = 0 								
indentIncreasing = True 				

try:
	while True:							
		print(' ' * indent, end='')
		print('Do not let Alexander play with my laptop while i am gone.')
		time.sleep(0.1)					

		if indentIncreasing:
			indent = indent + 1
			if indent == 20:
				# Change direction:
				indentIncreasing = False

		else:
			indent = indent - 1
			if indent == 0:
				indentIncreasing = True
except KeyboardInterrupt:
	sys.exit()
