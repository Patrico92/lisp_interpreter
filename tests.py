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


	def test_eval_addition(self):


		lisp_program = '( + 1 2 )'

		tree = my_parser.build_tree(my_parser.convert_to_tokens(lisp_program))
		self.assertEquals(my_parser.eval(tree), 3)

	def test_eval_nested_addition(self):


		lisp_program = '( + 1 ( - 2 5))'

		tree = my_parser.build_tree(my_parser.convert_to_tokens(lisp_program))
		self.assertEquals(my_parser.eval(tree), -2)

	def test_create_var_and_do_sth_with_it(self):


		lisp_program = ['(defvar a 10)', '(* a 2)', '(/ a 4)', '(defvar b 3)', '(- b a)']

		result = my_parser.do_the_thing(lisp_program[0])
		
		self.assertIn('a', my_parser.global_env)

		result = my_parser.do_the_thing(lisp_program[1])

		self.assertEquals(result, 20)

		result = my_parser.do_the_thing(lisp_program[2])

		self.assertEquals(result, 5)

		result = my_parser.do_the_thing(lisp_program[3])

		self.assertIn('b', my_parser.global_env)

		result = my_parser.do_the_thing(lisp_program[4])

		self.assertEquals(result, -2)

	def test_set





if __name__ == '__main__':
	unittest.main()