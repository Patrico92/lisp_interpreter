import operator as op

Number = (int, float)


def produce_start_env():

	env = {}
	env['+'] = op.add
	env['-'] = op.sub
	env['*'] = op.mul
	env['/'] = op.truediv
	env['print'] = print

	return env
	


global_env = produce_start_env()


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


def eval(tree):

	#print(tree)

	if isinstance(tree, Number): # it's just integer or floar
		return tree
	elif isinstance(tree, str): # in this case return value of the variable
		return global_env[tree]
	elif tree[0] == "defvar":
		varname = tree[1]
		varval = eval(tree[2])
		global_env[varname] = varval
	elif tree[0] in global_env:
		fun = eval(tree[0]) # get the callable for the procedure
		args = [eval(arg) for arg in tree[1:]]
		return fun(*args)
	else:
		raise SyntaxError("Sth went wrong in evaluation phase. I don't know what " + str(tree) + " is.")



def do_the_thing(input):
	return eval(build_tree(convert_to_tokens(input)))