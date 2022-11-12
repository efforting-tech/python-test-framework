__main__.py
===========

.. include:: /common/roles.inc

Overview
--------

..
	todo: Make proper references to things we talk about
	See: https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#cross-referencing-python-objects


This is the ingress point of this package. When the package is executed, all arguments will be interpreted as filenames of tests to run. After each test is run using :python:`load_and_run_test()` a summary will be printed using :python:`print_summary()`.

.. note::

	The current behavior is likely to change in the future as argument parsing is added. This is not yet planned out.


API
---

.. py:function:: load_and_run_test(filename)

	:param filename: Path to the filename with the test definitions
	:type filename: str or ~pathlib.PurePath
	:returns: None

	Loads and runs tests defined in ``filename``.
	View implementation details :doc:`here <details>`.

	..
		todo: the ref to details should be to an anchor

.. py:function:: print_summary(exit_process=False)

	:param exit_process: Exit process after print
	:type exit_process: bool
	:returns: None

	Prints out a summary of all executed registered tests (:python:`state.registered_tests`).

	If ``exit_process`` is set to :python:`True`, the process will exit with returncode :python:`0` if all executed tests succeeds or :python:`1` if any of them fails.



Navigation
----------


.. toctree::

	details