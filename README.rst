####################
IS 210 Assignment 14
####################
******************
Synthesizing Tasks
******************

:College: CUNY School of Professional Studies
:Course-Name: Software Application Programming I
:Course-Code: IS 210

Overview
========

In additional to compactness, the generator (whether an object or a function)
has massive performance benefits for Python. In this set of tasks we'll revive
our old friend the Fibonacci sequence to watch the generator pattern in-action.

.. warning::

    It is possible to pass the unit tests without passing the assignment.
    Students are expected to follow directions and use the directed tools to
    achieve their objectives.

Instructions
============

The following tasks will either have you interacting with existing files in
the assignment repository or creating new ones on the fly. Don't forget to add
your interpreter directive, utf-8 encoding, and a short docstring with any new
files that you create!

.. important::

    In these exercises, you may, on occasion, come across a task that requres
    you to research or use a function or method not directly covered by the
    course text. Since Python is such a large language it would be impossible
    for the author to have included descriptions of each and every available
    function which would largely duplicate the offical Python documentation.

    A *vital* skill to successful programming is being comfortable searching
    for and using official language documentation sources like the
    `Python String Documentation`_ page. Throughout our coursework we will be
    practicing both the use of the language in practice and the search skills
    necessary to become functional programmers.

Synthesizing Tasks
==================

Task 01
-------

In this task you will create a new Fibonacci sequence generator. The generator
should be able to produce a variable number of Fibonacci numbers as specified
in the count parameter.

A version of your original Fibonacci sequencer has been included for reference
in ``oldfibo.py``.

Specifications
^^^^^^^^^^^^^^

#.  Create a module named ``task_01.py``

#.  Create a function named ``xfibo()`` that takes exactly one argument:

    #.  ``count`` (int), The number of Fibonacci numbers to return.

#.  Create a generator that will yield each number in a Fibonacci sequence
    starting with ``0``

#.  The generator should stop after it has returned the number of numbers
    specified in the ``count`` parameter


Examples
^^^^^^^^

.. code:: pycon

    >>> for i in xfibo(5):
    ...     print i
    0
    1
    1
    2
    3

The above demonstrates the basic function of the module. For a more interesting
challenge, try writing out a big number to a file, eg:

.. code:: pycon

    >>> fh = open('/tmp/numbers.txt', 'w')
    >>> for number in xfibo(50000):
    ...    fh.write('{}\n'.format(number))
    >>> fh.close()

This will create a file that is approximately 250MB in size. For comparison
you *could* try the following:

.. code:: pycon

    >>> fh = open('/tmp/numbers.txt', 'w')
    >>> for number in oldfibo(50000):
    ...    fh.write('{}\n'.format(number))
    >>> fh.close()

.. warning::

    Don't actually do this unless you want to crash your machine or you have
    a *ridiculous* amount of memory. Because it has to build all 50000 numbers
    in a list in memory before looping, all have to be captured in memory
    simultaneously.

Task 02
-------

Now that we've made a super-slick generator we're going to use a list
comprehension to wrap it in a list. This effectively complete the circle; where
a generator is more performant in cases where you only access each number at a
time there might be other cases where you still need a true list. In these
cases, the cheapest way to build the list is with a simple list comprehension.

Specifications
^^^^^^^^^^^^^^

#.  Create a module named ``task_02.py``

#.  Import ``task_01``

#.  In ``task_02.py``, create a function named ``fibo()`` that takes one
    argument:

    #.  count (int), The total number of Fibonacci numbers to return

#.  In the ``fibo()`` function, return a list comprehension that uses
    ``task_01.xfibo()`` to generate ``count`` Fibonacci numbers and return them
    all in a list.

Examples
^^^^^^^^

    >>> fibo(5)
    [0, 1, 1, 2, 3]

Executing Tests
===============

Code must be functional and pass tests before it will be eligible for credit.

Linting
-------

Lint tests check your code for syntactic or stylistic errors To execute lint
tests against a specific file, simply open a terminal in the same directory as
your code repository and type:

.. code:: console

    $ pylint filename.py

Where ``filename.py`` is the name of the file you wish to lint test.

Unit Tests
----------

Unit tests check that your code performs the tested objectives. Unit tests
may be executed individually by opening a terminal in the same directory as
your code repository and typing:

.. code:: console

    $ nosetests tests/name_of_test.py

Where ``name_of_test.py`` is the name of the testfile found in the ``tests``
directory of your source code.

Running All Tests
-----------------

All tests may be run simultaneously by executing the ``runtests.sh`` script
from the root of your assignment repository. To execute all tests, open a
terminal in the same directory as your code repository and type:

.. code:: console

    $ ./runtests.sh

Submission
==========

Code should be submitted to `GitHub`_ by means of opening a pull request.

As-of Lesson 02, each student will have a branch named after his or her
`GitHub`_ username. Pull requests should be made against the branch that
matches your `GitHub`_ username. Pull requests made against other branches will
be closed.  This work flow mimics the steps you took to open a pull request
against the ``pull`` branch in Week Two.

For a refresher on how to open a pull request, please see homework instructions
in Lesson 01. It is recommended that you run PyLint locally after each file
is edited in order to reduce the number of errors found in testing.

In order to receive full credit you must complete the assignment as-instructed
and without any violations (reported in the build status). There will be
automated tests for this assignment to provide early feedback on program code.

When you have completed this assignment, please post the link to your
pull request in the body of the assignment on Blackboard in order to receive
credit.

.. _GitHub: https://github.com/
.. _Python String Documentation: https://docs.python.org/2/library/stdtypes.html
