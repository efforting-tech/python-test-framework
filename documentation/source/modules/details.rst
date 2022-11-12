Details
=======

.. include:: /common/roles.inc

load_and_run_test
-----------------
..
	todo - add links to python concepts discussed here
	Also add references to other parts of the project we refer to.

1.
	Copy the original :python:`builtins.__dict__` to :python:`state.original_builtins`.

2.
	Extract the :python:`test_features.NO_EXPORT` data and make a local set named :python:`NO_EXPORT`.

3.
	Update :python:`builtins.__dict__` with everything in :python:`test_features.__dict__` **unless** the key is present in :python:`NO_EXPORT`.

4.
	Assign :python:`filename`, :python:`module_name`, :python:`spec` and :python:`module` using utilities in :python:`importlib.util`.

5.
	Execute the loaded module.

6.
	Clear :python:`builtins` and restore using `state.original_builtins`.


..
	todo - write about the run_test function