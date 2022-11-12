internals.py
============

.. include:: /common/roles.inc

Overview
--------

This module currently only contains one function. This function will be detailed :doc:`here <details>` at a later time.

.. py:function:: run_test(function, name, local_frame, index=None, skip=False, export=None, should_fail=False)

	:param function: Class body function used as test
	:type func: callable

	:param name: Name of test
	:type name: str

	:param local_frame: Frame of test definition
	:type local_frame: frame

	:param index: Index or name to identify sub test
	:type index: str or int

	:param skip: Skips this test
	:type skip: bool

	:param export: Not used

	:param should_fail: Indicates this test is supposed to throw an exception.
	:type should_fail: bool

	This function executes the test in the :python:`function` parameter in accordance with the parameters above.


	.. note::

		The parameter :python:`export` will likely be removed soon.

	.. note::

		Later on we may add a feature to only accept a particular exception type or exception group for tests that should have an exception thrown so that we know if they failed the expected way or not.
