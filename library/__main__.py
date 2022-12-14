import sys
import importlib.util
from pathlib import Path
from . import test_features, state
import builtins

#TODO - when a test has sub tests it should only be considered succeeded if all sub tests as also succeeding.
#TODO - maybe keep track of when importing other tests so we can group them nicer

def load_and_run_test(filename):
	try:

		state.original_builtins = dict(builtins.__dict__)
		NO_EXPORT = set(test_features.NO_EXPORT.split())
		builtins.__dict__.update({k: v for k, v in test_features.__dict__.items() if k not in NO_EXPORT})

		filename = Path(filename)	#Upgrade to Path

		module_name = filename.stem
		spec = importlib.util.spec_from_file_location(module_name, filename)
		module = importlib.util.module_from_spec(spec)
		#sys.modules[module_name] = module		# We do not necessarily want to put this in the loaded modules dict
		spec.loader.exec_module(module)


		builtins.__dict__.clear()
		builtins.__dict__.update(state.original_builtins)

	except Exception as reason:
		raise Exception('Could not load test script') from reason


def print_summary(exit_process=False):
	all_tests = state.registered_tests
	executed = tuple(n for n, s in state.registered_tests.items() if s in (True, False))
	succeeded = tuple(n for n, s in state.registered_tests.items() if s == True)
	failed = tuple(n for n, s in state.registered_tests.items() if s == False)
	print('Test summary:')
	print(f'    Total: {len(all_tests)}, Skipped: {len(all_tests) - len(executed)}, Succeeded: {len(succeeded)}, Failed: {len(failed)}')

	if exit_process:
		if failed:
			exit(1)
		else:
			exit(0)

for filename in sys.argv[1:]:
	load_and_run_test(filename)
	print_summary(exit_process=True)