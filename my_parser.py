import operator as op

Number = (int, float)


def produce_start_env():

	env = {}
	env['+'] = op.add
	env['-'] = op.sub
	env['*'] = op.mul
	env['/'] = op.truediv
	env['print'] = print

	# conditional operations

	env['equal'] = op.eq
	env['>'] = op.gt
	env['>='] = op.ge
	env['<'] = op.lt
	env['<='] = op.le

	#list creation and maniuplation
	env['list'] = lambda *x: list(x)
	env['getl'] = lambda x, y: x[y]
	env['append'] = lambda x,y: x.append(y)
	env['setl'] = lambda x,y,z: x[0:y] + [z] + x[y+1:]
	env['cdr'] = lambda x: x[1:]

	return env

global_env = produce_start_env()
user_defined_functions = {}


def convert_to_tokens(program):
	"""The function is used to convert lisp list to tokens for futher processing"""

	return program.replace('(', ' ( ').replace(')', ' ) ').split()

def build_tree(tokens):
	"""Given a list of tokens this recursive function builds a tree for the later evaluation"""

	if len(tokens) == 0:
		raise SyntaxError("Sth went wrong...")

	token = tokens.pop(0)

	if token == '(':

		t = []

		while tokens[0] != ')':
			t.append(build_tree(tokens))

		tokens.pop(0)
		return t

	else:

		try:
			x = int(token)
			return x
		except ValueError:
			try:
				x = float(token)
				return x
			except ValueError:
				if token == ')':
					raise SyntaxError('Sth went wrong while building the tree - unexpected closing')
				else:
					return token


def eval(tree, extra_env=None):
	"""This function takes the syntax tree and tries to evaluate"""

	if isinstance(tree, Number): # it's just integer or float
		return tree

	elif isinstance(tree, str): # in this case return value of the variable
		if tree in global_env:
			return global_env[tree]
		else:
			raise SyntaxError(tree + "? I don't know this symbol... Sorry :(")

	elif tree[0] == 'set':
		
		var = tree[1]
		value = eval(tree[2])

		global_env[var] = value	

	elif tree[0] == 'if':
		if eval(tree[1]):
			return eval(tree[2])
		else:
			return eval(tree[3])

	elif tree[0] == "defvar":

		if tree[1] in global_env:
			raise SyntaxError('Variable ' + tree[1] + " is already defined...")

		varname = tree[1]
		varval = eval(tree[2])
		global_env[varname] = varval

	elif tree[0] == "deffun":
		# (deffun funname (args) (body) )
		user_defined_functions[tree[1]] = (tree[2], tree[3])

	elif tree[0] in global_env:
		fun = eval(tree[0]) # get the callable for the procedure
		args = [eval(arg) for arg in tree[1:]]
		return fun(*args)

	elif tree[0] in user_defined_functions:

		func = user_defined_functions[tree[0]] # get params and function definition
		arguments_passed = tree[1]
		arguments = func[0]

		#change global arguments during function execution

		storage = {}

		for i in range(len(arguments)):

			arg = arguments[i]

			if arg in global_env:
				storage[arg] = global_env[arg]

			global_env[arg] = eval(arguments_passed[i])


		body = func[1]

		result = eval(body)

		# return to previous state

		for arg in arguments:
			del global_env[arg]

		global_env.update(storage)

		return result


	else:
		raise SyntaxError("Sth went wrong in evaluation phase. I don't know what " + str(tree) + " is.")



def do_the_thing(input):
	"""Just a shortcut function to perform parsing (tokenization) + evaluation at once"""
	return eval(build_tree(convert_to_tokens(input)))