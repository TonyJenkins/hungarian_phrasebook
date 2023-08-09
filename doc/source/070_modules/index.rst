==========================
The Wheel. Do Not Reinvent
==========================

Python is quite a small language. We have already looked at most of the more important features, and will spend the next few chapters filling in some more details. For a moment we will pause, though, and look at some of the ways in which we can use useful *modules* of program code that come with Python. And in passing we'll mention some of the many other ways in which Python can be extended.

In many ways, modern programming is case a case of bringing together "stuff" from many sources into a whole that solves some new problem. A modern app might use a database, a framework for web applications, a toolkit for developing front-end websites, and more. Even with just a programming language there are many extensions and handy collections of code that can make our lives easier.

And using them is not cheating! Using them is just what professional programmers do. Not using them is just making more work for yourself.

Moreover, Python exists in the open source world, so many of these extensions are developed, tested, and used by huge communities across the world. Any bugs are quickly found and dealt with, and packages are extended and new versions released regularly. This means that you can be confident that the extensions you are using are tried and tested, and maybe you will be able to contribute to the community yourself one day.

Let's illustrate this with a simple programming task:

.. note::

    Validate a user's input to ensure that the first character of a string they enter is an uppercase letter, and the last is a period (full stop).

We could start thinking about this problem along these lines::

    Hmm. We can get the first character of a string at index ``0``, and we
    can somehow write an ``if`` statement. Maybe we can see if it's
    between ``A`` and ``Z`` or something. The last character will be index ``-1``,
    and testing that will be easy.

This is wrong! Looking for uppercase letters, and checking how a string ends sound like they might be common things to need to do. They are. And so *there is a built-in way to quickly and easily do either*. This is always the way do think - does what I am trying to do seem like something that has been done many, many times before?

For the record, there is a built-in function in Python called ``isupper`` that will tell us if a character is an upper case letter. There is another for testing how a string ends, imaginatively named ``endswith``. So to validate the string as required it's just a case if gluing these two together:

.. index:: single: Programs; f2c.py
.. literalinclude:: /../../src/07/string_check.py
   :language: python
   :caption: ``string_check.py``

.. tip::

    Another advantage of using built-in functions like this is that the resulting code when "read aloud" can often do a very good job of saying what the program is doing.

Of course, we do not know how ``isupper`` and ``endswith`` work. Nor do we want to know, or need to know. We just know what they do, and how we use them. We trust that they have been tested thousands of times, and are trusted.

.. tip::

    As you enter a program, your IDE may well pop-up helpful hints about what you might want to type next. Look at these, and you will see possible functions that might come in handy later on.
