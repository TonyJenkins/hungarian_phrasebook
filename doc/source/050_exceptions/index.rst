====================
When Things Go Wrong
====================

Many programming books carry on at this point with writing some programs. They tell the new programmer not to worry about what happens if the user does something unexpected, or if something else goes wrong. That is all a bit artificial, because users do often do awkward things. So here we will extend our programming by looking at some basic error situations.

A Simple Error
==============

Here's a problem:

.. topic:: Buses for Students

    A school is running a trip to a local theme park. Buses have been hired. Each bus can seat 46 students. A program is required that reads the number of students who have applied to join the trip, and will determine how many buses are needed, and how many students will be left behind.

We can sketch out a solution along these lines:

#. Set the number of students on each bus as a constant, so we can easily see what happens if we get bigger or smaller buses.
#. Display a prompt.
#. Read the number of students, as an integer.
#. Calculate the number of buses needed using integer division (we cannot have half a bus).
#. Use the modulus (remainder) operator to find how many students will be left.
#. Print the results.

And this matches neatly to a program, which might look something like this:

.. index:: single: Programs; school_bus.py
.. literalinclude:: /../../src/05/school_bus.py
   :language: python
   :caption: ``school_bus.py``

Running the program, the results would look promising:

.. code-block::

    How many students are there? 62
    Buses Needed:  1
    Students Left: 16

The first line is where the user has entered a value. The results look right.

Now, look closely at this line of the program:

.. literalinclude:: /../../src/05/school_bus.py
   :language: python
   :emphasize-lines: 7
   :caption: ``school_bus.py``

It does quite a lot. It displays a prompt, reads the user's input, converts the string entered to an integer (``input`` always reads a string), and assigns the result to a variable. All good, but what would happen if the user entered a value that could not be converted into an integer? The quickest thing to do it to try it and see by entering ``lots`` instead of a number:

.. code-block::

    How many students are there? lots
    Traceback (most recent call last):
      File "school_bus.py", line 7, in <module>
        number_of_students = int(input('How many students are there? '))
    ValueError: invalid literal for int() with base 10: 'lots'

Eek! This message tells us that the program has failed. It tells us which line this was (line 7), and displays the offending line. There is also a clue to the error ("invalid literal"), and a name for it (``ValueError``). Obviously we would rather the program ended rather more elegantly, and ideally gave the user more of a clue as to what went wrong. Lets's see how to do that.

Handling an Exception
=====================

This error is correctly called an *Exception*, because it represents an exception to what should have happened. Python is unable to continue with the program but, before all is lost, it is giving us two things:

#. An exception type, that indicates in general terms what has happened. Here is is ``ValueError``.
#. A message that contains a hint of what Python believes has gone wrong. Here, the literal value entered is invalid.

There are to approaches to tackling this error:

#. We could examine the string entered, determine whether it will convert to an integer, and carry on if it looks fine.
#. We could convert the string entered, whatever it is, and deal with any error that might happen.

The first of these is called **Look Before You Leap** (LBYL) and is a common approach in many older languages. It can lead to complex programs, where it can be difficult to see what is *supposed* to happen.

The second is EAFP, or **Easier to Ask Forgiveness than Permission**. This is a more modern approach, and is common in most newer languages. It tends to keep code that deals with errors all in one place, leaving what should happen alone.

.. important::

    Python prefers EAFP. A lot.

    We aim to be *Pythonic* here, so EAFP is what we will use.

Provided we know what exception might happen, it is easy to amend the code. In this example we are concerned about a ``ValueError``. So all we need to do is tell Python what to do if such an error happens. It looks like this (changes are highlighted):

.. literalinclude:: /../../src/05/school_bus_exception.py
   :language: python
   :emphasize-lines: 7, 16-17
   :caption: ``school_bus.py``

So we ``try`` to do what is expected (see that this is now indented so it is "inside" the ``try``). If there is a ``ValueError`` the program jumps straight down to the ``except`` and does what it says there. So now:

.. code-block::

    How many students are there? lots
    Please enter an integer.

And after any changes it is always important to check that the program still works as before:

.. code-block::

    How many students are there? 58
    Buses Needed:  1
    Students Left: 12

Looks good! This approach is much easier than trying to examine a string to see if it could represent an integer, and has the extra benefit of leaving the original program untouched.

Let's extend this to make the program a little more useful. Maybe we have the option for different sizes of bus.

Another Exception
=================

To modify the program to deal with different bus sizes, we are going to need to ask the user to enter the number of students who will fit on one bus. So the bus capacity is no longer a constant, but a variable. So the first attempt is to change the constant ``STUDENTS_PER_BUS`` to a variable that is entered (and to remember to change its identifier to lower-case as it is no longer constant).

.. hint::

    Renaming a variable or constant is common. Don't be tempted to use some sort of search-and-replace to do this, as al sorts of unexpected things could happen if the name exists elsewhere. You will find that your IDE has an intelligent way to do this (look for options called *Refactor*).

So now we have:

.. literalinclude:: /../../src/05/school_bus_exception.py
   :language: python
   :caption: ``school_bus.py``

This is fine, and if we tried it we would find that all still worked. But could anything else now go wrong? If we thought about it we might realise that the user could enter zero for the bus capacity. This is nonsense, but is an integer, so the program would carry on to try to divide the number of students by zero. Dividing by zero is an error, so what would happen? We expect an *exception*, but what would it be called?

The quickest way to find out is to fire up the Python Interpreter and find out.

.. hint::

    You can access the interpreter from inside your IDE. No need to change windows!

.. code-block::

    >>> 2 / 0
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ZeroDivisionError: division by zero

The information we want is in the last line. The exception is a ``ZeroDivisionError``. Good name for it. To catch this error, all we need to do is add it to the program. The changes are isolated at the bottom, with the other handling of the exceptions - this is why EAFP usually gives neater programs.

.. literalinclude:: /../../src/05/school_bus_final.py
   :language: python
   :emphasize-lines: 17-18
   :caption: ``school_bus.py``

Exceptions are Good
===================

Suppose we look again for more errors. We might wonder what would happen if the user entered nothing at all. That is obviously an error, but what happens when Python attempts to convert nothing into an integer?

A quick experiment would show that what Python does in this case is generate a ``ValueError``! So as it turns out we have already caught that possible error. The worst case is that we will have to rewrite the error message.

EAFP is based around the idea that most of the time the user will do what they are expected to do. So if they do something else that is an *exception* to the normal, and should be handled as such. It is much easier to write programs that assume all will be well, but to include code to show that something has gone wrong. LBYL in contrast often involves a lot of code to handle situations that will very rarely occur.

.. note::

    Sometimes an error situation is considered so unlikely that there is no point in adding code to handle it. The most common example of this is the `Blue Screen of Death` <https://en.wikipedia.org/wiki/Blue_screen_of_death>`_ in Windows.

It's worth noting that many new programmers instinctively go for LBYL approaches, and start writing insanely complex code when a simple bit of LBYL would solve the problem. That is why we have discussed EAFP and exceptions here *before* getting to the ideas needed to write LBYL! But the rule remains, to **always prefer EAFP** if at all possible.

More Errors
===========

So what errors remain here> There are still things that could go wrong with this program. The most obvious is that the user could enter a negative integer for either of the required values. This is obviously nonsense. The program would display results because it has no reason not to. But there should be some way to stop that - this is coming up next!

And arguably there could be some *sanity checks* on the input. Is a bus with a capacity of 3000 likely? In practice there would only be a small number of capacities available, and we might pick from a list. And a really good program would take the number of students, and work out the best collection of bus sizes to arrange.

Next section we'll look at ways to approach these kinds of problem.

Takeaways
=========

Exceptions are important. There are a basic part of Python, and handling them is fundamental.

#. You should now understand what an Exception is, and how to spot one.
#. You should be able to trap an Exception in a program, and display an error message.
#. You should be able to use the Python Interpreter to investigate the types of Exception that are generated in certain cases.
#. You should understand LBYL and EAFP approaches, and particularly why EAFP is preferred in Python!

There is surprisingly little left to cover before we can say we've done the basics of programming. Let's get on with it!
