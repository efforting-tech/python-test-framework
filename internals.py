import traceback, textwrap
from collections import deque
from . import state


#TODO - later we may want to store the information in a test representation so that we can print info later instead/also.
def run_test(function, name, local_frame, index=None, skip=False, export=None, should_fail=False):
	print = state.original_builtins['print']

	#Note - we may still get a description if second const happens to be a string, we would have to actually disassemble the function to know for sure and we will not do this right now

	if len(function.__code__.co_consts) >= 2:
		class_name, class_doc = function.__code__.co_consts[:2]
		if not isinstance(class_doc, str):
			class_doc = None
	else:
		class_name, class_doc = function.__code__.co_consts[0], None


	#NOTE- export was not needed with this current implementation

	#todo - allow export to be tuple, list, dict or string
	if isinstance(export, str):
		export_map = {k: k for k in export.split()}
	elif isinstance(export, (tuple, list)):
		export_map = {k: k for k in export}
	elif isinstance(export, dict):
		export_map = export
	else:
		export_map = None

	if index is not None:
		class_name = f'{class_name}[{index}]'

	#Note - class_name will be qualified name which works great for nested tests
	test_name = state.enter_test_definition(class_name, class_doc)

	if not skip:

		#function_scope = dict()
		printed_items = deque()
		state.test_stack.append(printed_items)
		state.printed_items = printed_items

		try:
			function()
		except Exception as e:
			if should_fail:
				state.register_success(class_name)
				was_successful = True
			else:
				state.register_failure(class_name)
				was_successful = False
				last_exception = e
		else:
			if should_fail:
				state.register_failure(class_name)
				was_successful = False
				last_exception = None
			else:
				state.register_success(class_name)
				was_successful = True


			# #Here we assume export is just the one string
			# if export_map:
			# 	parent_frame = local_frame.f_back
			# 	for target, source in export_map.items():
			# 		parent_frame.f_locals[target] = local_frame.f_locals[source]

		state.printed_items = state.test_stack.pop()


	state.exit_test_definition(class_name)


	if not skip:

		print(f'Test: {test_name}')
		if class_doc:
			print(f'    Description: {class_doc}')

		if was_successful:
			print('    Status: Success')
		else:
			print('    Status: Failure')
			print()
			if last_exception is None:
				print('        Test did not fail as it should')
			else:
				#Note - we skip the first entry of the traceback since that is calling this function we are currently in
				print(textwrap.indent(''.join(traceback.format_exception(last_exception, value=last_exception, tb=last_exception.__traceback__.tb_next)).rstrip('\n'), '        '))

		if printed_items:
			print()
			print('    Output:')
			for item in printed_items:
				print('       ', *item)


		print()

