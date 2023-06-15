===============
Before We Start
===============

At this point most books on programming leap right on in and start on the code. This is fine, but it means that sometimes people who are new around here can get lost, because they don't really understand the basic ideas. So in this chapter we'll look a few basic ideas that underpin the whole business of programming. These are mostly familiar ideas, that you've probably met many times before, but we need to think about them in a programming way.

True and False
==============

.. highlight:: none

Some statements are always True, and this can never change::

    Alan Turing proposed the Turing Test for Artificial Intelligence in 1950.

Some statements, on the other hand, are always False, and this will never change::

    Alan Turing was the first man to climb Mount Everest.

More often, statements are either True or False, depending on something that can be tested. So this statement is true as I type this::

    It is Tuesday today.

It could be True as you read this, or it could be False. I have no way of knowing right now. In order to determine whether it is currently True or False, you would need to test it, maybe by checking your phone. Programming revolves around these two values. A statement is True, or it is False. Perhaps it is True that a program's user has clicked a button in the interface, and so the program better respond in some useful way.

True and False are called **Boolean** values, named after `George Boole <https://en.wikipedia.org/wiki/George_Boole>`_, who in 1847 first applied mathematical ideas to logic [#bool]_. The word Boolean is usually written with a capital B for this reason.

Boole also showed how True and False can be combined using what are now known as Boolean (or logic) operators. For example, if there are two statements, **and** both are True, we can agree that a combined statement is True::

    Alan Turing is a famous Computer Scientist.
    Alan Turing proposed the Turing Test.

    Alan Turing is a famous Computer Scientist, who proposed the Turing Test.

There are a whole bunch of logic operators, but most of them are only really useful when working with electronics or hardware. For programming purposes, three are usually enough. ``AND`` and ``OR`` combine two logic values (let's call them ``A`` and ``B``, like this:

=====  =====  =======  ======
  A      B    A and B  A or B
=====  =====  =======  ======
False  False  False    False
True   False  False    True
False  True   False    True
True   True   True     True
=====  =====  =======  ======

The third useful operator, ``NOT`` just flips the value. So a True becomes False, and vice versa:

===== =====
  A   not A
===== =====
False True
True  False
===== =====

How Computers Work
==================

This is not the time or place to go deeply into the inner workings of a modern computer, but it *really* does help to understand programming if you have some idea of what's going on inside the box. After all, that's what a program is for; it's to make the computer do something useful.

.. note::

   What follows is very imprecise, but is mostly accurate, at least from a programmer's point of view. This is not a book about hardware!

Inside a computer is some memory. The memory stores all the programs that are running, along with the data they are using. It's usually called RAM. The memory is volatile (which means that everything in it is lost when the computer is powered off), so there is usually also some less volatile storage, like a disk drive. There is usually a lot more non-volatile storage available, mostly because it's a lot cheaper. In either case, data is stored in binary, as 1s and 0s, and binary is used to represent all the different kinds of data that a program might use.

The heart of a computer is the CPU. This is the chip that can carry out operations on data. Usually it only has a very few operations it can do, like adding two numbers, or comparing two, but my combining them we can write complex programs. The CPU can only work with programs and data that are in the volatile memory. To allow for this the CPU has a small amount of memory internally, and any data needed is copied into that so it can be processed.

So, when a program runs, it is first loaded into the memory. If the program requires some data (say a user has to type in a value), that data is also stored in memory. When the CPU needs it, it is copied into the CPU's memory, where is can be processed. Once done, the result is copied back into the main RAM, and the program carries on.

It is, obviously, much more complicated than that, with a modern CPU having many cores to allow it to process many things at the same time. But hold on to this idea of data being stored in memory, copied to the CPU, and written back. It's important.

.. rubric:: Footnotes

.. [#bool] This is a rare case in computing of an idea being named after a person (eponymy). Bonus credit if you can find more.

