.. include:: macros.rst

.. _ch__scripting:

**************
User interface
**************

Starting DEVSIM
===============

Refer to :ref:`sec__installation` for instructions on how to install |devsim|.  Once installed, |devsim| may be invoked using the following command


``devsim`` is loaded by calling

.. code-block:: python

  import devsim

from |python|.

Many of the examples in the distribution rely on the ``python_packages`` module, which is available by using:

.. code-block:: python

  import devsim.python_packages

Directory structure
===================

A |devsim| directory is created with the following sub directories listed in :ref:`installation__directories`.

.. _installation__directories:

.. table:: Directory structure for |devsim|

   ==============================  =======================================================
   ``devsim_data``                 contains project documentation files
   ``devsim_data/doc``             product documentation
   ``devsim_data/examples``        example scripts
   ``devsim_data/testing``         additional examples used for testing
   ==============================  =======================================================

This may be found using the virtual environment path specified in :numref:`python_distros`.

.. _sec__python:

|python| language
=================

Introduction
------------

|python| is the scripting language employed as the text interface to |devsim|.  Documentation and tutorials for the language are available from :cite:`python`.
A paper discussing the general benefits of using scripting languages may be found in :cite:`Ousterhout98scripting:higher`.

DEVSIM commands
---------------

All of commands are in the ``devsim`` namespace.  In order to invoke a command, the command should be prefixed with ``devsim.``, or the following may be placed at the beginning of the script:

.. code-block:: python

  from devsim import *

Unicode support
---------------

Internally, |devsim| uses UTF-8 encoding, and expects model equations and saved mesh files to be written using this encoding.  Care should be taken when using non-ASCII characters in names for visualization using the tools in :ref:`ch__visualization`, as this character set may not be supported in these third-party tools.

.. _errorHandling:

Error handling
==============

Exceptions
----------

When a syntax error occurs in a |python| script an exception may be thrown.  If it is uncaught, then |devsim| will terminate.  An exception that is thrown by |devsim| is of the type ``devsim.error``.  It may be caught, and a message may be extracted to determine the issue.


Fatal errors
------------

When |devsim| enters a state in which it may not recover.  The interpreter will throw a ``devsim.error`` exception with a message ``DEVSIM FATAL``.  At this point |devsim| may enter an inconsistent state, so it is suggested not to attempt to continue script execution if this occurs.

In rare situations, the program may behave in an erratic manner, print a message, such as ``UNEXPECTED`` or terminate abruptly.  Please report this using the contact information in :ref:`Contact`.

.. _sec_fpe:

Floating point exceptions
-------------------------

During model evaluation, |devsim| will attempt to detect floating point issues and return an error with some diagnostic information printed to the screen, such as the symbolic expression being evaluated.  Floating point errors may be characterized as invalid, division by zero, and numerical overflow.  This is considered to be a fatal error.

Solver errors
-------------

When using the :meth:`devsim.solve`, the solver may not converge and a message will be printed and an exception may be thrown.  The solution will be restored to its previous value before the simulation began.  This exception may be caught and the bias conditions may be changed so the simulation may be continued.



.. _python__verbosity:

Example
-------

More helpful exception information returned to |python| if the error is considered fatal.  This can be used to decide if the simulation can be restarted.  Note that if this occurs during a solve, it is necessary for the user to restore the previous circuit and device solutions if a restart is desired.  In addition, model evaluation is reset so that no false cyclic dependencies are reported after an error.

In this example code below, the previously ``DEVSIM FATAL`` error string will now provide the context that a floating point exception occurred and be handled in |python|.

.. code-block:: none

    try:
        self.solve()
    except error as msg:
        m = str(msg)
        if 'Convergence failure' in m:
            self.set_vapp(last_bias)
        elif'floating point exception' in m:
            self.set_vapp(last_bias)
            self.restore_callback(self.is_circuit)
        else:
            raise


Verbosity
=========

The :meth:`set_parameter` may be used to set the verbosity globally, per device, or per region.  Setting the ``debug_level`` parameter to ``info`` results in the default level of information to the screen.  Setting this option to ``verbose`` or any other name results in more information to the screen which may be useful for debugging.

The following example sets the default level of debugging for the entire simulation, except that the gate region will have additional debugging information.

.. code-block:: python

  devsim.set_parameter(name="debug_level", value="info")
  devsim.set_parameter(device="device" region="gate",
    name="debug_level", value="verbose")

.. _python__parallelization:

Command help
============

It is now possible to see the full list of |devsim| commands by typing

.. code-block:: python

  help(devsim.solve)


Parallelization
===============

Model evaluation
----------------

Routines for the evaluating of models are parallelized.  In order to select the number of threads to use

.. code-block:: python

  devsim.set_parameter(name="threads_available", value=2)

where the value specified is the number of threads to be used.  By default, |devsim| does not use threading.  For regions with a small number of elements, the time for switching threads is more than the time to evaluate in a single thread.  To set the minimum number of elements for a calculation, set the following parameter.

.. code-block:: python

  devsim.set_parameter(name="threads_task_size", value=1024)

The |intelmkl| is parallelized, the number of thread may be controlled by setting the ``MKL_NUM_THREADS`` environment variable.

Long operations
---------------

While running long operations, |devsim|, will yield to the |python| to allow it to perform other operations.

External math libraries
-----------------------

Please see the documentation for external solvers, such as BLAS/LAPACK or the |intelmklpardiso|, on how to control their threading behavior.


Reset simulator
===============

The :meth:`devsim.reset_devsim` command will clear all simulator data, so that a program restart is not necessary.

Array type input and output
===========================

In most circumstances, the software now returns numerical data using the |python| ``array`` class.  This is more efficient than using standard lists, as it encapsulates a contiguous block of memory.  More information about this class can be found at `https://docs.python.org/3/library/array.html <https://docs.python.org/3/library/array.html>`__.  The representation can be easily converted to lists and |numpy| arrays for efficient manipulation.

When accepting user input involving lists of homogenous data, such as :meth:`devsim.set_node_values` the user may enter data using either a list, string of bytes, or the ``array`` class.  It may also be used to input |numpy| arrays or any other class with a ``tobytes`` method.

