
.. include:: macros.txt

.. _sec__installation:

Installation
------------

Availability
~~~~~~~~~~~~
Information about the open source version of |devsim| is available from |devsimorg|.  This site contains up-to-date information about where to obtain compiled and source code versions of this software.  It also contains information about how to get support and participate in the development of this project.

.. _sec__supportedplatforms:

Supported platforms
~~~~~~~~~~~~~~~~~~~

|devsim| is compiled and tested on the platforms in :numref:`installation__platforms`.  If you require a version on a different software platform, please contact us.

.. _installation__platforms:

.. csv-table:: Current platforms for |devsim|.
  :header: "Platform", "Bits", "OS Version"
  :widths: 10, 10, 10

  "|mswindows|", "32, 64", "|mswindowsseven|, |mswindowsten|"
  "|linux|", "64", "|ubuntutrusty|, |ubuntuxenial|, |rhelsix| (|centossix| compatible)"
  "|macosx|", "64", "|macosxhighsierra|"


Binary availability
~~~~~~~~~~~~~~~~~~~

Compiled packages for the the platforms in :numref:`installation__platforms` are currently available from |devsimgithubrelease|.  The prerequisites on each platform are described in the ``linux.txt``, ``macos.txt``, and ``windows.txt``.

Source code availability
~~~~~~~~~~~~~~~~~~~~~~~~

|devsim| is also available in source code form from |devsimgithub|.

Directory Structure
~~~~~~~~~~~~~~~~~~~

A |devsim| directory is created with the following sub directories listed in :numref:`installation__directories`.

.. _installation__directories:

.. table:: Directory structure for |devsim|.

   ==============================  =======================================================
   ``bin``                         contains the devsim tcl binary
   ``lib/devsim``                  contains the devsim interpreter modules
   ``lib/devsim/python_packages``  contains runtime libraries
   ``doc``                         contains product documentation
   ``examples``                    contains example scripts
   ``testing``                     contains additional examples used for testing
   ==============================  =======================================================

Running DEVSIM
~~~~~~~~~~~~~~

See :ref:`ch__scripting` for instructions on how to invoke |devsim|.

