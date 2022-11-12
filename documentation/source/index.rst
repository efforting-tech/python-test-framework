
Efforting.Tech Python Testing Framework
=======================================

Location
--------

https://github.com/efforting-tech/python-test-framework

Usage
-----

Assuming it is installed as the site module ``efforting.testing``.

.. code-block:: console

	$ python -m efforting.testing some_tests.test.py

In this case the tests are written in the file ``some_tests.test.py``.

.. tip::

	Your test files, not being python scripts that works standalone, could have the suffix ``.test.py`` in order to help distinguish them from other python files.

..
	todo: add link to quickstart/exampels

Development Installation
------------------------

Installing this module while also be able to work on it. This will keep the git repo in one place but symlink to it from the site packages.
When you upgrade python you will have to do this again. The assumption here is per user installation.

In this example we want this module to be accessible under ``efforting.testing`` so we need to put our symlink in a directory.
This assumes that the current working directory is the directory of the repository.

1. Get the path of the user site
	.. code-block:: console

		$ site=`python -m site --user-site`
		$ echo $site
		/home/devilholk/.local/lib/python3.10/site-packages

2. Create the target folder for our symlink
	.. code-block:: console

		$ mkdir -p $site/efforting

3. Symlink the library folder (note, this assumes that $site/efforting/testing does not exist)
	.. code-block:: console

		$ ln -s `pwd`/library $site/efforting/testing


4. Test installation
	.. code-block:: console

		$ python -m efforting.testing

	If all works, no output or errors should happen since we does not specify a test file.



Navigation
==========

.. toctree::
   :maxdepth: 2

   modules/index
   examples/index
   meta/index

   glossary



| :ref:`modindex`
| :ref:`genindex`
| :ref:`search`

