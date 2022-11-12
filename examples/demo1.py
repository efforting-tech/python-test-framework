'''
	Assuming we are in the top level directory of the repository we can run this demo as follows

	#Regular run
	python -m efforting.testing examples/demo1.py

	#Run with modified environment to demonstrate how we can make use of the environment
	RUN_THING=1 python -m efforting.testing examples/demo1.py


'''

class basic_tests(Test):
	'This just demonstrates that tests can be grouped'

	class success(Test):
		'This is the first test demonstration and it will succeed'

		print("This test prints a thing and succeeds")


	class failure(Test, should_fail=True):
		'This test will fail, and that is expected'

		1 / 0	#Division with zero

class skipped_group(Test, skip=True):
	'This entire group will be skipped, note that this will just count as one skipped test since the sub tests are never even defined'

	class success(Test):
		'This is the first test demonstration and it will succeed'

		print("This test prints a thing and succeeds")


	class failure(Test, should_fail=True):
		'This test will fail, and that is expected'

		1 / 0	#Division with zero

import os
class environ_based(Test, skip=not os.environ.get('RUN_THING')):
	'This test is only executed if RUN_THING is set in the environment'

class iter_var(Test):
	'Demonstrates how one could use IterVar to perform multiple tests'

	test, thing, hello, world = 1, 2, 3, 4

	#IterVars is added by the test framework and makes it easier to iterate over variables by name
	for name, ref in IterVars('test thing hello world'.split()):

		#Note that we use index here because we can't define more than one test with the same name, index should be something that gets a unique value as repr(index), such as a number or string
		#But you could also use the id of objects such as index=id(ref) if you are going through a bunch of objects that doesn't have unique names
		class var_test(Test, index=name, title=f'Testing if {name!r} is within allowed range'):
			assert ref >= 2, f'Oh noes, {name!r} ({ref}) was outside of the allowed range'
