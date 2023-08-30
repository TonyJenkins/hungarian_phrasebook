====================
Those Little Details
====================

As we know, one of Python's design features is that should be one, and preferably only one, way of doing something. Right at the start if this book we set out that we would explain and, and preferably only one, way of doing something in Python. That has probably worked, until now.

Programming languages change and evolve, and Python is no exception. It's been around for many years now, and new ideas and feedback from the community lead to changes in the language. This is one of the joys of working with open source languages and projects - everyone can have an input into how somnething develops.

This section includes some features that have been added into Python over the years. Along with these are a few details that we passed over so as to keep things simple. The sections below are in no special order, and will probably be added to over time!

F-Strings
*********

It is more than likely that you have found it difficult (or at least fiddly) to generate neat output from some of your programs. This has not been helped by the way that we have always used the ``print`` statement, along with a collection of arguments, and optionally the ``sep`` argument to add or remove spacing. There is, not surprisingly a much neater way to do all this, and to provide neatly formatted strings.

.. important::

    The "best" way to achieve this has changed in Python over the years, so the usual Google and StackOverflow searches may well lead to different solutions. These are fine, but also fiddly.

Currently, the best way for formatting strings is formatted strings, or *f-strings*. The full reasons for their introduction were debated backn in 2016, and are documented in `PEP 498 <https://peps.python.org/pep-0498/>`_. The basic idea is to *interpolate* (that is, include) code inside strings. This is not as tricky as it sounds. A simple example:

.. code-block::

    >>> name = 'Robin'
    >>> print(f'Greetings, Sir {name}!)
    Greetings, Sir Robin!

So the idea is that whatever is inside the curly brackets is executed as Python code, and the result is printed. Here the contents of the curly brackets is just the name of a variable, so the value is printed.

There is nothing here that couldn't be done with conditional statements, string concatenation (adding), and so on, but this is *much neater*.

Here is an example of the brackets containing code. Suppose we have a test mark, the pass is 40, and we want to print the result. Traditionally we would write:

.. code-block::

    if mark >= 40:
        print('Your mark was', mark, '. You have passed!', sep='')
    else:
        print('Your mark was', mark, '. You have failed', sep='')

This is OK, but is fiddly to get the spacing right. Compare with the f-string version:

.. code-block::

    print(f'Your mark is {mark}. You have {"passed" if mark >= 40 else "failed"}!')

The code is now a one-liner. It is easy to read, and the message is not duplicated, making it a DRY solution.

.. hint::

    In code like this, remember that we need to use double-quotes inside single-quotes, else it will not be obvious where the first string ends. (You could use single inside double, it matters not, as long as you are consistent.)

It is the magic ``f`` before the string that is making this happen.

There is more. These f-strings also allow the output to be formatted. The full details are `in the docs <https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals>`_ (but you may be better off Googling for some examples). The sort of formatting available includes padding a string with spaces (before, after, or to centre it), displaying a floating-point value to a number of decimal places, and more.

Some examples of formatting a string for output, using ``***`` to show what's going on:

.. code-block::

    >>> name = 'Robin'
    >>> print(f'***{name:<20}***')
    ***Robin               ***
    >>> print(f'***{name:>20}***')
    ***               Robin***
    >>> print(f'***{name:^20}***')
    ***       Robin        ***

This is handy for a neat table of results.

And an example of controlling the number of decimal places in a result:

.. code-block::

    >>> eggs_ratio = 31/7
    >>> 31/7
    4.428571428571429
    >>> print(f'{eggs_ratio:.2f}')
    4.43

Note that the value is rounded, not just truncated.

There are many more options, but these two are really the most common. Check the docs for more!

Finally, a quick note on a common programming task:

.. topic:: Binary

    Write a program that accepts an integer as input and displays the equivalent in binary.

Now, to do this, you might start thinking about loops, calculating powers of two, using remainders and modulus, and so on. And you would come up with a program that was maybe 20 lines long, and you would be very proud.

But here is that, with the conversion done in one line, courtesy of an f-string ...

.. index:: single: Programs; binary.py
.. literalinclude:: /../../src/11/binary.py
   :language: python
   :caption: ``binary.py``

Sorry.

None
****

Any book on programming will at some point provide a list of the built-in *primitive* data types available. As we know, the list varies between languages but usually includes:

* Whole numbers, called integers.
* Numbers with a fractional part, called floating-point numbers.
* Strings, with a single character string possibly being a special case.

Modern languages usually also include a Boolean type, while older languages might just use integers for that. Some languages offer more specific types, for example integers that cannot be negative, or integers that occupy a specific amount of memory.

Python keeps it simple, so way back, we said that these were the four types in Python:

* ``int``, an integer.
* ``float``, a number with a fractional part.
* ``str``, a string, which can have any number of characters,
* ``bool``, a Boolean.

This was not strictly true. There is a fifth type. It's called ``None`` or more accurately ``NoneType``\ [#none]_.

The need for this arises from a particular problem. Python determines a variable's type from the value it is given when it is created, but *what happens if we want a variable that has no initial value*? Such a variable has no value, so no type, so it can be given ``NoneType``.

It can be assigned deliberately, like this:

.. code-block::

    >>> spam = None
    >>> type(spam)
    <class 'NoneType'>

And we can test whether the variable currently has an interesting value:

.. code-block::

    >>> not spam
    True

So at the moment ``spam`` has no useful value. Let's give it one:

.. code-block::

    >>> spam = 1
    >>> not(spam)
    False

This all seems a bit abstract, so let's have an example where this might be useful. Suppose we have a function that finds a value in a list. It takes two parameters, the list and a number to search for, and returns where the number is in the list. There is a built-in function called ``index`` that will do most of the heavy lifting, so we get something like:

.. code-block::

    def find_number(list_of_numbers, number):
        return list_of_numbers.index(number)

This is fine and we could use it like this to look for a number, say ``12``:

.. code-block::

    position = find_number(all_numbers, 12)

But what happens if the number cannot be found? The ``index`` function will throw an exception. This could be handled in the program using the function, but it *can be neater* to return ``None`` to say the value was not found. The function becomes:

.. code-block::

    def find_number(list_of_numbers, number):
        try:
            return list_of_numbers.index(number)
        except ValueError:
            return None

This is neater because this function now *always returns a value*, so there is no need to worry about exceptions when using it. So the code using the function can simply be:

.. code-block::

    position = find_number(all_numbers, 12)
    if position:
        print('Value Found')
    else:
        print('Value not found')

This is a neatness, but it does often improve the readability of code.

.. note::

    Somewhat related to this is a common structure in Python where we need to check if, say, a list is empty, or a string variable contains no characters. The Boolean ``not`` comes in handy:

    .. code-block::

        >>> s = ''
        >>> not s
        True
        >>> l = []
        >>> not l
        True

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

.. [#none] This is *still* not strictly true. ``None`` isn't really a type, it's an object, and there is only one of them. See the docs if you really need to know!
