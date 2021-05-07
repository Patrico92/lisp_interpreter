import my_parser

print('Lisp intepreter. Write a Lisp list or call it quits... (q)')

while True:

	print('lisp-> ', end='')

	line = input()

	if line == 'q':

		print('Thanks for working with me!')
		break

	val = my_parser.eval(my_parser.build_tree(my_parser.convert_to_tokens(line)))
	
	if val is not None:
		print(val)
