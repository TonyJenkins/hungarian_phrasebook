==========
Collecting
==========

As we've already noted more than once, we have actually covered all we need to know in order to create programs. Modules and functions are really just a convenience that help keep the job simple, and allow for useful chunks of program to be reused. They're all about making things easy, and saving unnecessary work. The new idea we'll meet in this chapter is almost the same - we don't strictly need to be able to handle *collections* of related data items, but being able to will make certain tasks much easier.

So this chapter introduces the idea of *collections* of data items. All programming languages will provide features for this and, as usual, the names differ but the basic ideas are the same. In the earliest languages collections were called *arrays*, and that name is still found in some modern languages. Other names you'll see include lists, maps, sets, and more.

Python provides a few collections as standard, and the *collections* module in the standard library contains a whole lot more. In general, a collection:

* Stores a number of related data items.
* May or may not require that those data items are of the same time.
* May store the items in a particular order, or may not consider order to be important.
* May or may not allow duplicate items.

We'll look at four collection types here\ [#sets]_. These cover all the common use cases, and together form a complete toolbox to draw on. *Strictly* you only need one collection type to do anything, but some do allow for more elegant and neater solutions. Anyway, below we will describe:

Lists
    The Swiss Army Knife of collections. You can do anything with a list. A list stores data items, and maintains the order. Usually the items are all of the same time.
Tuple
    Think of this as being like a row in a database table. This is a collection of data that represents something. The data items do not have to be the same type. Order is not important.
Set
    Basically a list, with the handy extra property that items in it have to be unique. This type also supports the usual operations (difference, intersection, etc) from maths set theory.
Dictionary
    A key-value collection. It is used by looking up a key, and finding the corresponding value. It's just like looking up a definition in a paper dictionary.

We start with lists, as these are the most general. Remember, you can do anything with a list.

Looking at Lists
================

A list is a collection of values, where the order is assumed to be important (although it doesn't have to be). Let's use a list to explore the whole idea of a collection.

A collection is simply a bunch of related values that it is convenient to treat as a single entity. They have a single name (identifier), so they can be passed into functions, and returned from functions. So a list contains a collection of related data items. In a list, order is maintained - new values are added at the end, or among the existing values, in which case the others "shuffle along".

Let's do an example that shows the basics.

A List Example
**************

Suppose we wanted to store the marks of a child on some tests. We need to find the average, say. Something like this would work (we'll just assign the values here to keep the code simple).

.. code-block::

    >>> mark_1 = 65
    >>> mark_2 = 55
    >>> mark_3 = 45
    >>> mark_4 = 60
    >>> average = (mark_1 + mark_2 + mark_3 + mark_4) / 4

This is fine. But what would happen if there were five tests? Or three? We would need to add or remove variables, and remember to tweak the division to find the mean. Being able to handle *any* number of marks would be DRY and would give a promising chance of creating some reusable code. We can, of course, do just this with a list.

A list is created in the same way as any other variable, by giving it a value. A list is denoted with square brackets, so to create an empty list:

.. code-block::

    >>> marks = []

Or to create it with some values already in it:

.. code-block::

    >>> marks = [50, 40, 30]

The important new idea here is that the list ``marks`` is a single variable, that happens to contain multiple values. Being a list, order is maintained, so a new value can be added, and will be at the end:

.. code-block::

    >>> marks.append(20)
    >>> marks
    [50, 40, 30, 20]

We can start to see how this would be useful when we realise there are handy built-in functions to calculate useful values from the values in the list. Like their number (the length of the list) or their sum:

.. code-block::

    >>> len(marks)
    4
    >>> sum(foo)
    140

.. hint::

    There are other built-in functions too, like ``max`` and ``min`` to find the highest and lowest values. Always remember to check for built-ins before writing some new code.

    The key thing is to think "This *must* have been done before!".

Using a list, the program to find the average of the four marks could use code something like this:

    >>> marks = []
    >>> marks.append(65)
    >>> marks.append(55)
    >>> marks.append(45)
    >>> marks.append(60)

    >>> average = sum(marks) / len(marks)

There's not much gained so far, but what if there were a different number of marks? Or how about a program that could handle any number of marks. That sounds a like a loop. If we know in advance how many marks there would be, a ``for`` loop could work in a program something like this:

.. literalinclude:: /../../src/09/marks_for.py
   :language: python
   :caption: ``marks.py``

.. note::

    For clarity, the code to verify that the mark entered is a number (and presumably is also in some valie range) has been left out here.

Here the number of marks is defined as a constant, but it could just be entered by the user. So to make this program work for any number of marks, all that would be needed would be to change the value in ``NUMBER_OF_MARKS``.

We can improve the readability of this program a little by pausing to think that averages are something that must be worked out a lot. A look in the docs (or a Google) would reveal that there is no built-in way to find an average, but that there is a ``statistics`` module containing all sorts of promising stuff. So we can use this to make things a little neater (and the program a little shorter):

.. literalinclude:: /../../src/09/marks_for_mean.py
   :language: python
   :emphasize-lines: 4, 16
   :caption: ``marks.py``

For completeness, and for the sake of another example, it's a small change to this program to get to a version that could handle any number of marks. The change is to the loop, which is now *indeterminate*, and we need to provide the user with a way of indicating that have finished. We'll have them enter ``-1`` now\ [#whilenot]_. The constant can obviously be removed, and we end up with a general-purpose solution.

.. literalinclude:: /../../src/09/marks_while_mean.py
   :language: python
   :caption: ``marks.py``

Another advantage of having all the marks data in a list is that we can do many other useful things with it. The ``max`` built-in function would give us the highest value, for example. And the ``statistics`` module is full of other possibly interesting values to calculate.

List Order
**********

..
    TODO

List Slices
***********

..
    TODO

Trying Tuples
=============

..
    TODO

Discovering Dictionaries
========================

..
    TODO

Seeking Sets
============

..
    TODO

Takeaways
=========

..
    TODO

.. [#sets] This almost said three, but we'll include Sets so as to be complete, and because they do have some nifty uses now and again.
.. [#whilenot] Probably not a good example of UX. Next chapter we'll include a way to do this neatly.
