====================
Those Little Details
====================

As we know, one of Python's design features is that should be one, and preferably only one, way of doing something. Right at the start if this book we set out that we would explain and, and preferably only one, way of doing something in Python. That has probably worked, until now.

Programming languages change and evolve, and Python is no exception. It's been around for many years now, and new ideas and feedback from the community lead to changes in the language. This is one of the joys of working with open source languages and projects - everyone can have an input into how somnething develops.

This section includes some features that have been added into Python over the years. Along with these are a few details that we passed over so as to keep things simple. The sections below are in no special order, and will probably be added to over time!

F-Strings
*********

..
    TODO

None
****

..
    TODO

Custom Exceptions
*****************

Exceptions, and programming with them, are very important in Python. This is especially true if we adopt the preferred *easier to ask forgiveness than permission (EAFP)* approach to dealing with errors. We have written programs that have caught and dealt with exceptions, as well as programs that have generated their own.

Up to know we have been content to use the built-in exceptions. Usually it has been possible to find one where the name meets the facts of the case of what is going wrong. But these are by their very nature quite generic; ``ValueError`` tells us nothing except that a value is wrong, for example. It is often useful to be able to create our own exceptions, and to use those. So if there is a problem with a password, we could generate a ``PasswordError``, for example.

.. hint::

    There is a full list of the standard exceptions, as well as plenty of details on how to use them, in the `Python Docs <https://docs.python.org/3/library/exceptions.html#concrete-exceptions>`_.

Defining a new exception uses *Classes*, which is a feature of Python we have been using all along, since everything is a class. Look:

.. code-block::

    >>> type(1)
    <class 'int'>

Integers are a class of *objects*. So when we define a new exception we are going to add a new object to the class of exceptions. The code to do this is simple, and makes use the ``pass`` statement! To create an exception to indicate a password problem:

.. code-block::

    class PasswordError(Exception):
        pass

That's it! Assuming this is defined at the top of a program (or, better, in an imported module) we could have some code that generated a meaningful error. Something like:

.. code-block::

    if password != confirmation_password:
        raise PasswordError('Password mismatch')

That's all there is to it. Remember that the name of the exception provides a general idea of where the problem is, and the message includes more details.

List Comprehensions
*******************

..
    TODO

Takeaways
*********

..
    TODO
