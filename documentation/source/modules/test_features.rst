test_features.py
================

.. include:: /common/roles.inc

Overview
--------

As detailed in :doc:`details`, this module is used to populate the builtins module in order to fascilitate the custom execution of the test files. The exception is any key mentioned in the :python:`NO_EXPORT` variable and that variable itself. Currently this module defines a custom implementation of :python:`__build_class__` which is called to execute the class body of classes being defined. If :python:`Test` is a direct base of a class it will be handled by :python:`internals.run_test()` and in other cases the original :python:`__build_class__` will be called using a reference in :python:`state.original_builtins`.

This module also defines a custom :python:`print()` function that logs prints to the top most test on the test stack :python:`state.test_stack`. Prints that happens outside of a runnin test will be printed using the original print function.

The :python:`Test` class in here is used to identify tests as described above.

This module also defines a function to help with iterating through variables from the calling locals, :python:`IterVars`.

API
---

.. py:data:: NO_EXPORT
	:type: str

	List of variables as space separated string.

.. py:function:: __build_class__(func, name, *bases, metaclass=type, **kwds)

	:param func: Function defining class body
	:type func: callable

	:param name: Name of class
	:type name: str

	:param bases: Tuple of bases
	:type bases: tuple of type

	:param metaclass: Metaclass to use
	:type metaclass: type

	:param kwds: Additional keyword arguments (typically passed onto :python:`__init_subclass__`)
	:type kwds: dict

	:returns: New class
	:rtype: type


.. py:function:: print(*items)

	:param items: Items to print or log
	:type items: tuple
	:returns: None

.. py:class:: Test

	Base class for identifying tests.

.. py:function:: IterVars(name_list)

	:param name_list: Iterator of names that will be looked up in :python:`locals()` of the calling function.
	:type name_list: iterator of str
	:returns: generator of (name, ref) tuples
	:rtype: generator
