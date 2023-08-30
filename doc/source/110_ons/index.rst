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

Passing
*******

This might seem a little odd, but there is a statement in Python that does nothing. Ever. Nothing, nada, zilch. It's needed because of Python's reliance on indentation to show what statements are in which block. Look at this line of code:

.. code-block::

    if number_entered == 1:

The syntax of Python *requires* that there is a statement on the following line. If there isn't, that is an error, and the program will fail to run. In some other languages you could just use an empty pair of brackets or some such to show that there's nothing there, but the indentation in Python means that this won't work.

So there is a need for a statement that does nothing! This might be because there is nothing to do aside from declaring something (see *Custom Exceptions*), oe because the programmer needs a placeholder, or because explicitly saying nothing needs to be done improves the readability of the code.

All of these are the job of the ``pass`` statement. So in the code above, we could have this, which is valid Python:

.. code-block::

    if number_entered == 1:
        pass

Another common use is when writing functions. Quite often you need to write the function header, and want to work on the code that uses it. You will write the function body later. So you use ``pass`` as a placeholder:

.. code-block::

    def useful_function():
        pass

This satisfies the syntax, and stops your IDE generating errors. The code will also run, although obviously it will do nothing.

Finally, a less common use is when you explicitly want to say that nothing should happen. This is obviously irrelevant to Python, but could help someone reading the code. For example, suppose some code wanted to ignore every value in a certain range. We could write this, reasoning that just to ignore the range would look odd:

.. code-block::

    if number_entered == 1:
        print('One')
    elif number_entered == 6:
        print('Six')
    else:
        pass

The score here is that we are *explicitly* ignoring other values.

.. hint::

    If you use your IDE to create template code for functions, you may well find that it adds a ``pass`` statement in to make the code valid.

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
