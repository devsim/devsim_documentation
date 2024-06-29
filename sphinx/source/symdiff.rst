.. include:: macros.rst

.. _ch__symdiff:

*******
SYMDIFF
*******

Overview
========

|symdiff|  is a tool capable of evaluating derivatives of symbolic expressions.  Using a natural syntax, it is possible to manipulate symbolic equations in order to aid derivation of equations for a variety of applications.  It has been tailored for use within |devsim|.

Syntax
======

Variables and numbers
---------------------
Variables and numbers are the basic building blocks for expressions.  A variable is defined as any sequence of characters beginning with a letter and followed by letters, integer digits, and the ``_`` character.  Note that the letters are case sensitive so that ``a`` and {A} are not the same variable.  Any other characters are considered to be either mathematical operators or invalid, even if there is no space between the character and the rest of the variable name.

Examples of valid variable names are:

  ``a, dog, var1, var_2``

Numbers can be integer or floating point.  Scientific notation is accepted as a valid syntax.  For example:

  ``1.0, 1.0e-2, 3.4E-4``


Basic expressions
-----------------

.. _symdiff__operators:

.. table:: Basic expressions involving unary, binary, and logical operators

  +-------------------+--------------------------------------+
  | Expression        |   Description                        |
  +===================+======================================+
  | ``(exp1)``        |   Parenthesis for changing precedence|
  +-------------------+--------------------------------------+
  +-------------------+--------------------------------------+
  | ``+exp1``         |   Unary Plus                         |
  +-------------------+--------------------------------------+
  | ``-exp1``         |   Unary Minus                        |
  +-------------------+--------------------------------------+
  | ``!exp1``         |   Logical Not                        |
  +-------------------+--------------------------------------+
  +-------------------+--------------------------------------+
  | ``exp1 ^ exp2``   |   Exponentiation                     |
  +-------------------+--------------------------------------+
  +-------------------+--------------------------------------+
  | ``exp1 * exp2``   |   Multiplication                     |
  +-------------------+--------------------------------------+
  | ``exp1 / exp2``   |   Division                           |
  +-------------------+--------------------------------------+
  +-------------------+--------------------------------------+
  | ``exp1 + exp2``   |   Addition                           |
  +-------------------+--------------------------------------+
  | ``exp1 - exp2``   |   Subtraction                        |
  +-------------------+--------------------------------------+
  +-------------------+--------------------------------------+
  | ``exp1 < exp2``   |   Test Less                          |
  +-------------------+--------------------------------------+
  | ``exp1 <= exp2``  |   Test Less Equal                    |
  +-------------------+--------------------------------------+
  | ``exp1 > exp2``   |   Test Greater                       |
  +-------------------+--------------------------------------+
  | ``exp1 >= exp2``  |   Test Greater Equal                 |
  +-------------------+--------------------------------------+
  +-------------------+--------------------------------------+
  | ``exp1 == exp2``  |   Test Equality                      |
  +-------------------+--------------------------------------+
  | ``exp1 != exp2``  |   Test Inequality                    |
  +-------------------+--------------------------------------+
  +-------------------+--------------------------------------+
  | ``exp1 && exp2``  |   Logical And                        |
  +-------------------+--------------------------------------+
  +-------------------+--------------------------------------+
  | ``exp1 || exp2``  |   Logical Or                         |
  +-------------------+--------------------------------------+
  +-------------------+--------------------------------------+
  | ``variable``      |   Independent Variable               |
  +-------------------+--------------------------------------+
  | ``number``        |   Integer or decimal number          |
  +-------------------+--------------------------------------+

In :ref:`symdiff__operators`, the basic syntax for the language is presented.  An expression may be composed
of variables and numbers tied together with mathematical operations.  Order of operations is from bottom to top in order of increasing precedence.  Operators with the same level of precedence are contained within horizontal lines.

In the expression ``a + b * c``, the multiplication will be performed before the addition.  In order to override this precedence, parenthesis may be used.  For example, in ``(a + b) * c``, the addition operation is performed before the multiplication.

The logical operators are based on non zero values being true and zero values being false.  The test operators evaluate the numerical values and result in ``0`` for false and ``1`` for true.

  *It is important to note since values are based on double precision arithmetic, testing for equality with values other than 0.0 may yield unexpected results.*

Functions
---------


.. _symdiff__functions:

.. list-table:: Predefined functions
    :widths: 20 30
    :header-rows: 1

    * - Function
      - Description
    * - ``acosh(exp1)``
      - Inverse Hyperbolic Cosine
    * - ``asinh(exp1)``
      - Inverse Hyperbolic Sine
    * - ``atanh(exp1)``
      - Inverse Hyperbolic Tangent
    * - ``cosh(exp1)``
      - Hyperbolic Cosine
    * - ``sinh(exp1)``
      - Hyperbolic Sine
    * - ``tanh(exp1)``
      - Hyperbolic Tangent
    * - ``B(exp1)``
      - Bernoulli Function
    * - ``dBdx(exp1)``
      - derivative of Bernoulli function
    * - ``dot2d(exp1x, exp1y, exp2x, exp2y)``
      - ``exp1x*exp2x+exp1y*exp2y``
    * - ``exp(exp1)``
      - exponent
    * - ``ifelse(test, exp1, exp2)``
      - if test is true, then evaluate exp1, otherwise exp2
    * - ``if(test, exp)``
      - if test is true, then evaluate exp, otherwise 0
    * - ``log(exp1)``
      - natural log
    * - ``max(exp1, exp2)``
      - maximum of the two arguments
    * - ``min(exp1, exp2)``
      - minimum of the two arguments
    * - ``pow(exp1, exp2)``
      - take exp1 to the power of exp2
    * - ``sgn(exp1)``
      - sign function
    * - ``step(exp1)``
      - unit step function
    * - ``kahan3(exp1, exp2, exp3)``
      - Extended precision addition of arguments
    * - ``kahan4(exp1, exp2, exp3, exp4)``
      - Extended precision addition of arguments
    * - ``vec_max``
      - maximum of all the values over the entire region or interface
    * - ``vec_min``
      - minimum of all the values over the entire region or interface
    * - ``vec_sum``
      - sum of all the values over the entire region or interface

.. _error__functions:

.. list-table:: Error functions
    :widths: 20 30
    :header-rows: 1

    * - Function
      -   Description
    * - ``erfc(exp1)``
      - complementary error function
    * - ``derfcdx(exp1)``
      - derivative of complementary error function
    * - ``erfc_inv(exp1)``
      - inverse complementary error function
    * - ``derfc_invdx(exp1)``
      - derivative of inverse complementary error function
    * - ``erf(exp1)``
      - error function
    * - ``derfdx(exp1)``
      - derivative error function
    * - ``erf_inv(exp1)``
      - inverse error function
    * - ``derf_invdx(exp1)``
      - derivative of inverse error function


.. _fermi__functions:

.. list-table:: Fermi Integral functions
    :widths: 20 30
    :header-rows: 1

    * - Function
      -   Description
    * - ``Fermi(exp1)``
      - Fermi Integral
    * - ``dFermidx(exp1)``
      - derivative of Fermi Integral
    * - ``InvFermi(exp1)``
      - inverse of the Fermi Integral
    * - ``dInvFermidx(exp1)``
      - derivative of InvFermi Integral

.. _gaussfermi__functions:

.. list-table:: Gauss-Fermi Integral functions
    :widths: 20 30
    :header-rows: 1

    * - ``gfi(exp1, exp2)``
      - Gauss-Fermi Integral
    * - ``dgfidx(exp1, exp2)``
      - Derivative of Gauss-Fermi Integral with respect to first argument
    * - ``igfi(exp1, exp2)``
      - Inverse Gauss-Fermi Integral
    * - ``digfidx(exp1, exp2)``
      - Derivative of Inverse Gauss-Fermi Integral with respect to first argument




In :ref:`symdiff__functions` are the built in functions of |symdiff|.  Note that the ``pow`` function uses the ``,`` operator to separate arguments.  In addition an expression like ``pow(a,b+y)`` is equivalent to an expression like ``a^(b+y)``.  Both ``exp`` and ``log`` are provided since many derivative expressions can be expressed in terms of these two functions.  It is possible to nest expressions within functions and vice-versa.  :ref:`error__functions` lists the error functions, derivatives, and inverses.  :ref:`fermi__functions` lists the Fermi functions, and are based on the Joyce-Dixon Approximation :cite:`joycedixon`. The Gauss-Fermi functions are listed in :ref:`gaussfermi__functions`, based on :cite:`paasch:2010`.

Commands
--------

.. _symdiff__commands:

.. table:: Commands

  +---------------------------------------+---------------------------------------------------------------+
  | Command                               |   Description                                                 |
  +=======================================+===============================================================+
  | ``diff(obj1, var)``                   | Take derivative  of ``obj1`` with respect to variable ``var`` |
  +---------------------------------------+---------------------------------------------------------------+
  | ``expand(obj)``	                  | Expand out all multiplications into a sum of products         |
  +---------------------------------------+---------------------------------------------------------------+
  | ``help``                              | Print description of commands                                 |
  +---------------------------------------+---------------------------------------------------------------+
  | ``scale(obj)``                        | Get constant factor                                           |
  +---------------------------------------+---------------------------------------------------------------+
  | ``sign(obj)``                         | Get sign as ``1`` or ``-1``                                   |
  +---------------------------------------+---------------------------------------------------------------+
  | ``simplify(obj)``                     | Simplify as much as possible                                  |
  +---------------------------------------+---------------------------------------------------------------+
  | ``subst(obj1,obj2,obj3)``             | substitute ``obj3`` for ``obj2`` into ``obj1``                |
  +---------------------------------------+---------------------------------------------------------------+
  | ``unscaledval(obj)``                  | Get value without constant scaling                            |
  +---------------------------------------+---------------------------------------------------------------+
  | ``unsignedval(obj)``                  | Get unsigned value                                            |
  +---------------------------------------+---------------------------------------------------------------+

Commands are shown in :ref:`symdiff__commands`.  While they appear to have the same form as functions, they are special in the sense that they manipulate expressions and are never present in the expression which results.  For example, note the result of the following command


.. code-block:: python

  > diff(a*b, b)
  a

User functions
--------------
.. _symdiff__userfunccommands:

.. table:: Commands for user functions

  +----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
  | Command                                            |   Description                                                                                                             |
  +====================================================+===========================================================================================================================+
  | ``clear(name)``                                    | Clears the name of a user function                                                                                        |
  +----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
  | ``declare(name(arg1, arg2, ...))``                 | declare function name taking dummy arguments ``arg1``, ``arg2``, . . . . Derivatives assumed to be ``0``                  |
  +----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
  | ``define(name(arg1, arg2, ...), obj1, obj2, ...)`` | declare function name taking arguments ``arg1``, ``arg2``, . . . having corresponding derivatives ``obj1``, ``obj2``, ... |
  +----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+


Commands for specifying and manipulating user functions are listed in :ref:`symdiff__userfunccommands`.  They are used in order to define new user function, as well as the derivatives of the functions with respect to the user variables.  For example, the following expression defines a function named ``f`` which takes one argument.

.. code-block:: none

  > define(f(x), 0.5*x)

The list after the function protoype is used to define the derivatives with respect to each of the independent variables.  Once defined, the function may be used in any other expression.  In additions the any expression can be used as an arguments.  For example:

.. code-block:: none

  > diff(f(x*y),x)
  ((0.5 * (x * y)) * y)
  > simplify((0.5 * (x * y)) * y)
  (0.5 * x * (y^2))

The chain rule is applied to ensure that the derivative is correct.  This can be expressed as

.. math::

  \frac{\partial}{\partial x} f \left( u, v, \ldots \right)
    = \frac{\partial u}{\partial x} \cdot \frac{\partial}{\partial u} f \left( u, v, \ldots \right)
    + \frac{\partial v}{\partial x} \cdot \frac{\partial}{\partial v} f \left( u, v, \ldots \right)
    + \ldots

The ``declare`` command is required when the derivatives of two user functions are based on one another.  For example:

.. code-block:: none

  > declare(cos(x))
  cos(x)
  > define(sin(x),cos(x))
  sin(x)
  > define(cos(x),-sin(x))
  cos(x)

When declared, a functions derivatives are set to 0, unless specified with a define command.  It is now possible to use these expressions as desired.

.. code-block:: none

  > diff(sin(cos(x)),x)
  (cos(cos(x)) * (-sin(x)))
  > simplify(cos(cos(x)) * (-sin(x)))
  (-cos(cos(x)) * sin(x))

Macro assignment
----------------

The use of macro assignment allows the substitution of expressions into new expressions.  Every time a command is successfully used, the resulting expression is assigned to a special macro definition, ``$_``.

In this example, the result of the each command is substituted into the next.

.. code-block:: none

  > a+b
  (a + b)
  > $_-b
  ((a + b) - b)
  > simplify($_)
  a

In addition to the default macro definition, it is possible to specify a variable identifier by using the ``$`` character followed by an alphanumeric string beginning with a letter.  In addition to letters and numbers, a ``_`` character may be used as well.  A macro which has not previously assigned will implicitly use ``0`` as its value.

This example demonstrates the use of macro assignment.

.. code-block:: none

  > $a1 = a + b
  (a + b)
  > $a2 = a - b
  (a - b)
  > simplify($a1+$a2)
  (2 * a)

Invoking SYMDIFF from DEVSIM
============================

Equation parser
---------------

The :meth:`devsim.symdiff` should be used when defining new functions to the parser.  Since you do not specify regions or interfaces, it considers all strings as being independent variables, as opposed to models.  :ref:`ModelCommands` presents commands which have the concepts of models. A ``;`` should be used to separate each statement.

This is a sample invocation from |devsim|

.. code-block:: python

  % symdiff(expr="subst(dog * cat, dog, bear)")
  (bear * cat)

Evaluating external math
------------------------

The :meth:`devsim.register_function` is used to evaluate functions declared or defined within |symdiff|.  A |python| procedure may then be used taking the same number of arguments.  For example:

.. code-block:: python

  from math import cos
  from math import sin
  symdiff(expr="declare(sin(x))")
  symdiff(expr="define(cos(x), -sin(x))")
  symdiff(expr="define(sin(x),  cos(x))")
  register_function(name="cos", nargs=1)
  register_function(name="sin", nargs=1)

The ``cos`` and ``sin`` function may then be used for model evaluation.  For improved efficiency, it is possible to create procedures written in C or C++ and load them into |python|.

Models
------

When used withing the model commands discussed in :ref:`ModelCommands`, |devsim| has been extended to recognize model names in the expressions.  In this situation, the derivative of a model named, ``model``, with respect to another model, ``variable``, is then ``model:variable``.

During the element assembly process, |devsim| evaluates all models of an equation together.  While the expressions in models and their derivatives are independent, the software uses a caching scheme to ensure that redundant calculations are not performed.  It is recommended, however, that users developing their own models investigate creating intermediate models in order to improve their understanding of the equations that they wish to be assembled.

