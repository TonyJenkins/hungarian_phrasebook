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

Command-Line Arguments
**********************

Early on in this book, we introduced the *command line*. While many applications use graphical interfaces these days, there are still plenty of times where we need to just type a command into a terminal. For one thing, this is probably how many of the programs that we write will be run. You can run the program from inside your IDE, but you can't assume that your use will have the same IDE, or even any Pyton tool at all. So we fall back on the good old command-line.

.. tip::

    You may well find on Windows that double-clicking a Python program will run it, a terminal window will appear, and then vanish before you can see the results. Google will lead you to ways to preserve the output, but firing up a terminal and running it there really is the best way.

Running a program at the command line is a simple case of starting the Python interpreter with the name of the file containing the program (programs are just plain text files, remember). So on a Linux or Mac system:

.. code-block::

    $ python3 my_prog.py

does the job.

Windows is, as usual, a little more complicated, as typing ``python`` has a habit of opening the Windows Store. The simplest fix is to use:

.. code-block::

    C:\> py my_prog.py

making sure you are running in the same folder as contains the program. Better fixes are a Google away.

When running a program like this, it is often useful to have some input on the command line, along with the name of the program file. As an example, here is a simple program that counts the lines in a file (and uses an f-string!):

.. index:: single: Programs; wc.py
.. literalinclude:: /../../src/11/wc_input.py
   :language: python
   :caption: ``wc.py``

This is fine, and it would work, but wouldn't it be neater if the user just typed the name of the file they want to use as input *after* the program name? So instead of:

.. code-block::

    $ python3 wc.py
    Enter the file name: text_file.txt

the user could just:

.. code-block::

    $ python3 wc.py text_file.txt

This is obviously possible, and is a case where we have the program capture *command line arguments*. It works like this:

#. Import the ``sys`` module.
#. Then you have a list called ``sys.argv`` which contains everything from the command line. The first element is the name of the program, and then the remainder is anything that was typed after it.

So for this program is we ``import`` the ``sys`` module, and then run the program as so:

.. code-block::

    $ python3 wc.py text_file.txt

The list ``sys.argv`` will contain ``wc.py`` at index 0, and ``text_file.txt`` at index 1. With this knowledge, we can change the program:

.. index:: single: Programs; wc.py
.. literalinclude:: /../../src/11/wc_clas.py
   :language: python
   :caption: ``wc.py``

and it will work as expected.

Using the command line like this usually introduces the possibility of errors, often when the user misses off a required argument, or when the argument is invalid. So there is some common code that often gets added in. In this case, missing off the argument would give an ``IndexError`` when the program tries to access the argument. There could also be a ``FileNotFoundError`` if, ah, the file cannot be found. So a complete version of the program, with error-checking, would be:

.. index:: single: Programs; wc.py
.. literalinclude:: /../../src/11/wc.py
   :language: python
   :caption: ``wc.py``

Remember that ``sys.argv[0]`` contains the name of the program, so here we are making sure that the user knows what is generating the error.

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

This comes in useful when we want a user to enter some values, while giving them a way to indicate that they are finished. A while back we had a program where a user entered some marks, and we calculated the average. It looked like this:

.. literalinclude:: /../../src/09/marks_while_mean.py
   :language: python
   :caption: ``marks.py``

And we noted at the time that having them enter ``-1`` to show they were done was not the greated piece of user experience ever. A couple of small changes will allow the user to just press ``Enter`` to show they are done. We use the fact that this gives an empty string, and that ``not`` applied to an empty string gives ``True``. The only other change is that we need to move the ``int`` conversion so that we can test the possibly-emty string. The improved version is:

.. literalinclude:: /../../src/11/marks_while_mean.py
   :language: python
   :emphasize-lines: 11, 12, 15
   :caption: ``marks.py``

Much better UX!

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

Lists are a very powerful collection data type. In fact, to be honest, lists are the *only* collection type you really need to know. They tend to be used in similar ways in many programs, and often appear in similarly structured code. Typically there is a ``for`` loop, that does something to each item in a list, or adds values to a list depending on some condition. As an example, suppose we have a list of marks, and we want to build another list containing just the fails (less than 40, say). The code might be something along the lines of:

.. code-block::

    fail_marks = []

    for mark in all_marks:
        if mark < 40:
            fail_marks.append(mark)

Or suppose we have a name like ``Arthur James Wensleydale``, and want to extract the capital letters. These would represent the initials, and could be useful. We would code:

.. code-block::

    initials = ''

    for letter in full_name:
        if letter.isupper():
            initials += letter

This looks quite different, but is the same structure. Both these code samples initialise a variable, and then add to it as they examine each element of something else in turn. There are no lists in the second example, but there is what Python calls an *iterable*, and that means they are basically the same thing.

These are cases where *list comprehensions* come in useful. As with some of the other topics in this chapter there is never a case where you **must** use these, but they can lead to neater code.

.. important::

    Remember that good code values clarity over neat tricks. List comprehensions are close to being neat tricks, and can lead to temptation to try to create nifty one-liners.

    Always look at your code with an eye on readability and clarity!

A list comprehension takes one list, and produces another, based on some condition. Rather than describe the syntax, here is an example that would create a list of all even integers less than 20:

.. code-block::

    >>> evens = [x for x in range(20) if x % 2 == 0]
    >>> evens
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


We can read this as ``evens`` is a list including all values in ``range(20)`` where that value ``%`` 2 is 0 (so it is even).

Compare this with that same code written out "long hand", and you'll see the point:

.. code-block::

    evens = []
    for x in range(20):
        if x % 2 == 0:
            evens.append(x)

In fact, you can see the code for the comprehension in that sample.

That's all there is to it. We can rewrite our first example using a comprehension, so this:

.. code-block::

    fail_marks = []

    for mark in all_marks:
        if mark < 40:
            fail_marks.append(mark)

becomes the substantially neater:

.. code-block::

    fail_marks= [mark for marks in all_marks if mark < 40]

But what of that string example, where we were looking through a name? The trick here is to build a list of the initial letters, and then to convert that list back to a string. Seems over complicated, but the code is rather neat. First build the list:

.. code-block::

    initials = [letter for letter in full_name if letter.isupper()]

And then we can use the ``join`` function, that takes a list and joins the elements together with the given separator. Here the separator is nothing:

.. code-block::

    initials = ''.join([letter for letter in full_name if letter.isupper()])

Again, this is very neat.

Using list comprehensions like this is very common, and is seen as Pythonic. So although it might look like a neat trick it is safe to assume that any experienced programmer will understand. Try them in your next project!

Takeaways
*********

More than any other chapter in this book, this one is probably not complete!

There is really only one takeaway here, and that is that a programmer never stops learning. It is doubtful that there is anyone, anywhere, who knows *all* of Python, and can use it well. Modern programming languages are constantly developing and improving, and any developer needs to set time aside to keep up to date. Languages that are driven forward by a community of users, like Python, have a process where anyone can contribute, and the end results are achieved by consensus.

Much the same applies to any language you may come to use in the future. Languages like Java and PHP have communities and continue to develop too. Even languages with stronger ties to particular companies, like C# as an example, develop, even if they are guided in a somewhat different way.

So, take away that there is plenty more to learn. Look at code written by others, check the many tutorials available online, and, if you want to, keep up to date with new developments in Python.

.. [#none] This is *still* not strictly true. ``None`` isn't really a type, it's an object, and there is only one of them. See the docs if you really need to know!
