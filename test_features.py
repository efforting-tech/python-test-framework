import sys
from . import state


def __build_class__(func, name, *bases, metaclass=type, **kwds):

	frame = sys._getframe(1)

	if Test in bases:
		from . import internals
		internals.run_test(func, name, frame, **kwds)

	else:
		return state.original_builtins['__build_class__'](func, name, *bases, metaclass=metaclass, **kwds)


def print(*items):
	printed_items = state.test_stack[-1]
	printed_items.append(items)

class Test:
	pass

def IterVars(name_list):
	calling_frame = sys._getframe(1)

	for name in name_list:
		yield name, calling_frame.f_locals[name]