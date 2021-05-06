

def convert_to_tokens(program):
	"""The function is used to convert lisp list to tokens for futher processing"""

	return program.replace('(', ' ( ').replace(')', ' ) ').split()

def build_tree(tokens):
	"""Given a list of tokens this recursive function builds a tree for later evaluation"""

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
		 





