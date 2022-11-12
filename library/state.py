#This is used to hold a global state when running tests, such as statistics, and original builtins

from collections import deque

registered_tests = dict()
test_stack = deque()


def enter_test_definition(test_name, description):
	#test_name_stack.append(name)
	#test_name = '.'.join(test_name_stack)
	assert test_name not in registered_tests, f'Test {test_name!r} was already registered'
	registered_tests[test_name] = None
	return test_name

def exit_test_definition(name):
	pass
	#assert test_name_stack.pop() == name

def register_success(name):
	registered_tests[name] = True

def register_failure(name):
	registered_tests[name] = False

