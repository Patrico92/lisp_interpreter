import unittest
import my_parser

class TestParser(unittest.TestCase):

	def test_simple_addition(self):

		lisp_program = '( + 1 2 )'

		self.assertEqual(my_parser.convert_to_tokens(lisp_program), ['(', '+', '1', '2', ')'])

	def test_build_tree_simple_addition(self):

		lisp_program = '( + 1 2 )'

		tree = my_parser.build_tree(my_parser.convert_to_tokens(lisp_program))

		self.assertEqual(tree, ['+', 1, 2])


	def test_build_tree(self):

		lisp_program = '(list 1 2 (quote foo))'
		tree = my_parser.build_tree(my_parser.convert_to_tokens(lisp_program))

		self.assertEqual(tree, ['list', 1, 2, ['quote', 'foo']])





if __name__ == '__main__':
	unittest.main()