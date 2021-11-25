.. include:: macros.txt

.. _ch__scripting:

User Interface
--------------

Starting DEVSIM
~~~~~~~~~~~~~~~

Refer to :ref:`sec__installation` for instructions on how to install |devsim|.  Once installed, |devsim| may be invoked using the following command


It is necessary to first ``PYTHONPATH`` variable to the ``lib`` directory in the |devsim| distribution.  As an alternative, an experimental installation script is available to make the process easier.  Please see :ref:`sec__installation_script` for more information.

``devsim`` is loaded by calling

.. code-block:: python

  import devsim

from |python|.

Many of the examples in the distribution rely on the ``python_packages`` module, which is available by using:

.. code-block:: python

  import devsim.python_packages

The supported versions of |python| for use in scripts is 3.6 or higher.

.. _sec__python:

Python Language
~~~~~~~~~~~~~~~

Introduction
^^^^^^^^^^^^

|python| is the scripting language employed as the text interface to |devsim|.  Documentation and tutorials for the language are available from :cite:`python`.
A paper discussing the general benefits of using scripting languages may be found in :cite:`Ousterhout98scripting:higher`.

DEVSIM commands
^^^^^^^^^^^^^^^

All of commands are in the ``devsim`` namespace.  In order to invoke a command, the command should be prefixed with ``devsim.``, or the following may be placed at the beginning of the script:

.. code-block:: python

  from devsim import *

For details concerning error handling, please see :ref:`errorHandling`.

..
  _sec__pythonpath:

.. 
  Other packages
  ~~~~~~~~~~~~~~

..
  |devsim| is able to load |python| packages.  It is important to note that binary extensions loaded into |devsim| must be compatible with the operating system which it was compiled for.  To load an extension, it is first necessary to provide the path as an environment variable, or at program run time.

..
  For example, if the |python| packages on your system are available in ``/usr/share/tcltk``, it is necessary to set the environment variable in ``csh`` as

..
  .. code-block:: python

..
    setenv PYTHONPATH /usr/share/tcltk
..
  or in ``bash``

..
  .. code-block:: python

..
    export PYTHONPATH=/usr/share/tcltk

..
  In the |python| script, this may be done using using the appropriate paths for your system

..
  .. code-block:: python

..
    import sys
..
    sys.path.append("/usr/share/tcltk")

..
  Please see :ref:`additional__python` for more information on obtaining a copy of |python| for your computer's operating system.

Advanced usage
^^^^^^^^^^^^^^

In this manual, more advanced usage of the |python| language may be used.  The reader is encouraged to use a suitable reference to clarify the proper use of the scripting language constructs, such as control structures.

Unicode Support
^^^^^^^^^^^^^^^

Internally, |devsim| uses UTF-8 encoding, and expects model equations and saved mesh files to be written using this encoding.  Users are encouraged to use the standard ASCII character set if they do not wish to use this feature.  Python 3 interpreters handle UTF-8 encoding well.

..
  For the deprecated Python 2 interpreter, it is necessary to put the following line at the beginning of the python script.

..
  .. code-block:: none

    # -*- coding: utf-8 -*-


..
  When reading a ``unicode`` encoded script, the built in |python| interpreter should be made aware of the encoding of the source encoding using this on the first or second line of the script

..
  This option is only required on systems, such as |mswindows|, which do not default to this encoding.

On some systems, such as |mswindows|, it may be necessary to set the following environment variable before running a script containing UTF-8 characters.

.. code-block:: none

  SET PYTHONIOENCODING=utf-8


Care should be taken when using UTF-8 characters in names for visualization using the tools in :ref:`ch__visualization`, as this character set may not be supported.

.. _errorHandling:

Error handling
~~~~~~~~~~~~~~

Python errors
^^^^^^^^^^^^^

When a syntax error occurs in a |python| script an exception may be thrown.  If it is uncaught, then |devsim| will terminate.  More details may be found in an appropriate reference.  An exception that is thrown by |devsim| is of the type ``devsim.error``.  It may be caught.

Fatal errors
^^^^^^^^^^^^

When |devsim| enters a state in which it may not recover.  The interpreter should throw a |python| exception with a message ``DEVSIM FATAL``.  At this point |devsim| may enter an inconsistent state, so it is suggested not to attempt to continue script execution if this occurs.

In rare situations, the program may behave in an erratic manner, print a message, such as ``UNEXPECTED`` or terminate abruptly.  Please report this using the contact information in :ref:`Contact`.

Floating point exceptions
^^^^^^^^^^^^^^^^^^^^^^^^^

During model evaluation, |devsim| will attempt to detect floating point issues and return an error with some diagnostic information printed to the screen, such as the symbolic expression being evaluated.  Floating point errors may be characterized as invalid, division by zero, and numerical overflow.  This is considered to be a fatal error.

Solver errors
^^^^^^^^^^^^^

When using the :meth:`devsim.solve`, the solver may not converge and a message will be printed and an exception may be thrown.  The solution will be restored to its previous value before the simulation began.  This exception may be caught and the bias conditions may be changed so the simulation may be continued.  For example:

.. code-block:: python

  try:
    solve(type="dc", absolute_error=abs_error,
      relative_error=rel_error, maximum_iterations=max_iter)
  except devsim.error as msg:
    if msg[0].find("Convergence failure") != 0:
      raise
    #### put code to modify step here.

.. _python__verbosity:

Verbosity
^^^^^^^^^

The :meth:`set_parameter` may be used to set the verbosity globally, per device, or per region.  Setting the ``debug_level`` parameter to ``info`` results in the default level of information to the screen.  Setting this option to ``verbose`` or any other name results in more information to the screen which may be useful for debugging.

The following example sets the default level of debugging for the entire simulation, except that the gate region will have additional debugging information.

.. code-block:: python

  devsim.set_parameter(name="debug_level", value="info")
  devsim.set_parameter(device="device" region="gate",
    name="debug_level", value="verbose")

.. _python__parallelization:

Parallelization
^^^^^^^^^^^^^^^

Routines for the evaluating of models have been parallelized.  In order to select the number of threads to use

.. code-block:: python

  devsim.set_parameter(name="threads_available", value=2)

where the value specified is the number of threads to be used.  By default, |devsim| does not use threading.  For regions with a small number of elements, the time for switching threads is more than the time to evaluate in a single thread.  To set the minimum number of elements for a calculation, set the following parameter.

.. code-block:: python

  devsim.set_parameter(name="threads_task_size", value=1024)

The |intelmkl| is parallelized, the number of thread may be controlled by setting the ``MKL_NUM_THREADS`` environment variable.



