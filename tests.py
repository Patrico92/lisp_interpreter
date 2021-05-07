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
		self.assertEqual(my_parser.eval(tree), 3)

	def test_eval_nested_addition(self):


		lisp_program = '( + 1 ( - 2 5))'

		tree = my_parser.build_tree(my_parser.convert_to_tokens(lisp_program))
		self.assertEqual(my_parser.eval(tree), -2)

	def test_create_var_and_do_sth_with_it(self):


		lisp_program = ['(defvar a 10)', '(* a 2)', '(/ a 4)', '(defvar b 3)', '(- b a)']

		result = my_parser.do_the_thing(lisp_program[0])
		
		self.assertIn('a', my_parser.global_env)

		result = my_parser.do_the_thing(lisp_program[1])

		self.assertEqual(result, 20)

		result = my_parser.do_the_thing(lisp_program[2])

		self.assertEqual(result, 2.5)

		result = my_parser.do_the_thing(lisp_program[3])

		self.assertIn('b', my_parser.global_env)

		result = my_parser.do_the_thing(lisp_program[4])

		self.assertEqual(result, -7)

	def test_equality(self):

		prog = '(equal 1 2)'
		self.assertFalse(my_parser.do_the_thing(prog))

		prog = '(equal 2 2)'
		self.assertTrue(my_parser.do_the_thing(prog))

	def test_simply_if(self):

		my_parser.do_the_thing('(defvar x 20)')

		prog = '(if (equal x 10) (+ x 2) (+ x 1) )'

		res = my_parser.do_the_thing(prog)

		self.assertEqual(res, 21)

	def test_define_function(self):

		my_parser.do_the_thing('(deffun sum_till_0 (x) (  if (> x 0) (+ x (sum_till_0 ((- x 1))) ) 0 ))')

		prog = '(sum_till_0 (6) )'

		res = my_parser.do_the_thing(prog)

		self.assertEqual(res, 21)


if __name__ == '__main__':
	unittest.main()