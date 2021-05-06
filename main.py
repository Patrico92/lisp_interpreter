import my_parser 

print('Lisp intepreter. Write a Lisp list or call it quits... (q)')

while True:

	print('lisp-> ', end='')

	line = input()

	if line == 'q':

		print('Thanks for working with me!')
		break
