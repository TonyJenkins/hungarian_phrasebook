===============
Before We Start
===============

At this point most books on programming leap right on in and start on the code. This is fine, but it means that sometimes people who are new around here can get lost, because they don't really understand the basic ideas. So in this chapter we'll look a few basic ideas that underpin the whole business of programming. These are mostly familiar ideas, that you've probably met many times before, but we need to think about them in a programming way.

Instructions
============

A computer program is just a set of instructions. The instructions tell [#tell]_ the computer how to carry out some task.

.. sidebar:: Try It!

    After reading this section, try it! Write some instructions that someone should be able to follow to carry out
    some everyday task. Making a coffee, boiling an egg, starting a laptop and opening a Word file ...

We are all used to following instructions. This might be to install some software, walk to a new location in a new town, or make a new and interesting soup. This idea is so common that most of us probably carry on without really thinking about what we're doing. In fact, in some cases we could follow some instructions without knowing what the end result is intended to be!

Some sets of instructions are presented in a formalised way according to some conventions. That soup recipe, for example, will start by telling us what the recipe makes, and how much, then list the ingredients, and then present the steps to take, one at a time, in the correct order. It would be very strange to find a recipe that gave the steps before listing the ingredients. Following a recipe also assumes that we understand basic cookery terms ("mix", "fry", "stir"), probably some abbreviations ("tsp" means "teaspoon"), and that we follow it with some intelligence ("fry until brown", "add enough to thicken the soup").

Any set of instructions contains the same elements. There is *choice* and there is *repetition*. While we usually follow instructions from the first to the last (or from the top to the bottom), this is very rarely done without one or the other of these. In general, instructions contain:

Statements
    A single instruction to do something: "Add the onions", "Cross the road", "Connect the USB cable".
Choice
    Do one of a number of things, depending on what is observed. "Add water if required", "Take the shortest path", "Connect the cable if an external monitor is used".
Repetition
    Do (a Statement) several times. "Add the flour until none remains", "Walk uphill until you reach the station", "Click to install each of the updates that will download".

These three are the three most basic building blocks that make up any set of instructions. They are also the basic building blocks of a computer program. When writing a program, a programmer supplies the computer with an ordered list of instructions, along with the choices and repetitions that are needed to achieve a successful result. The instructions are expressed in a programming language, like Python.

Values and Types
================

In many daily tasks we are involved with *values*.

Some of these are numbers, or numeric. We might have to pay a bus fare, buy a needed amount of something, or walk a certain distance. We are good at recognising these values and in carrying out tasks that involve them. Generally we think in units of tens, or fractions of tens, or multiples of 10. Multiples of 10 (powers) are handy for bigger numbers: 10\ :sup:`2` is 100, 10\ :sup:`3` is 1000 and so on. These numbers are all integers, or whole numbers.

Fractions of 10 are used for smaller numbers, and numbers less than 1. These are floating-point numbers. They can also be represented as powers: 10\ :sup:`-1` is 0.1, or a tenth; 10\ :sup:`-2` is 0.01, or a hundredth. Presumably our obsession with working in 10s like this comes from the usual number of fingers on our hands.

Other values we use every day are characters. These could be letters, digits, punctuation marks, of even emojis. Characters might represent a name or email address. They could also represent a phone number - in this case the characters are also digits, but they are characters unless we plan to add up phone numbers, which is unlikely. A single character can have meaning - a grade on a test, for example. A collection of characters can also have a meaning, sometimes only if they are read in a particular order.

So, we use *values*, and values have *types*. We carry out operations on values, and what operations we can do are determined by the types.

True and False
==============

.. highlight:: none

We also deal with the ideas of truth, and fakery. For example, some statements are always True, and this can never change::

    Alan Turing proposed the Turing Test for Artificial Intelligence.

Some statements, on the other hand, are always False, and this will never change::

    Alan Turing was the first man to climb Mount Everest.

More often, statements are either True or False, depending on something that can be tested. So this statement is true as I type this::

    It is Tuesday today.

It could be True as you read this, or it could be False. I have no way of knowing right now. In order to determine whether it is currently True or False, you would need to test it, maybe by checking your phone. Programming revolves around these two values. A statement is True, or it is False. Perhaps it is True that a program's user has clicked a button in the interface, and so the program better respond in some useful way.

True and False are called **Boolean** values, named after `George Boole <https://en.wikipedia.org/wiki/George_Boole>`_, who in 1847 first applied mathematical ideas to logic [#bool]_. The word Boolean is usually written with a capital B for this reason.

Boole also showed how True and False can be combined using what are now known as Boolean (or logic) operators. For example, if there are two statements, **and** both are True, we can agree that a combined statement is True::

    Alan Turing is a famous Computer Scientist.
    Alan Turing proposed the Turing Test.

    Alan Turing, the famous Computer Scientist, proposed the Turing Test.

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

Binary
======

So, how does a computer store the data it needs? Computers do not have 10 fingers, but they do have electrical current [#onoff]_. A current has two possible values; it can be "on", or it can be "off". So computers count in 2s, which is called *binary*.

Remember that humans count in 10s. We find 10s easy, probably because we are taught to use 10s from an early age. The origins of this are presumably that we have 10 fingers, and we can use these to count. Powers are important here. To handle larger numbers we give certain powers of 10 special names, so:

* 10 x 10 (or 10\ :sup:`2`) is a hundred.
* 10 x 10 x 10 ((or 10\ :sup:`3`) is a thousand.

and so on. This is called *base 10* or sometimes *denary* or (less accurately) *decimal*.

Computers do not have fingers! A computer is an electronic device. Electricity is something that is either "on" or "off". So if a sentient computer could count, it would count in 2s, in much the same way as humans use 10s. This is called *base 2*, or *binary*.

This means that every data value stored inside a computer is *encoded* in binary. The details are not important here, but an overview is.

* An integer can just be stored as its binary equivalent.
* Various cunning ways exist to store numbers with fractional parts[#float]_.
* Character data can be stored by using a table to convert between numberic values and the characters. The most common one
  is `Unicode <https://en.wikipedia.org/wiki/Unicode>`_.

If a computer could somehow write out an integer it would have just two symbols to work with, ``1`` and ``0``. It would also work in powers of 2: 2\ :sup:`2` is denary 4, 2\ :sup:`3` is denary 8, and so on.

.. hint::

    To avoid confusion it is usual to add a subscript to a number when different number bases are involved. So 8\ :sub:`10` means the number 8, in denary (base 10). Likewise, 1000\ :sub:`2` is a binary value. (The two happen to represent the same number).

.. important::

    Knowing and recognising the powers of 2 is a hugely important skill in computer science::

        1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048

    If you have ever bought a laptop, you will recognise those numbers from the system specs!

So how would a computer represent, say, 3\ :sub:`10`?

Easy. Look at the powers (it helps to see them in reverse order::

        2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1

3 is just 2 + 1. So, in binary 3 is 11\ :sub:`2`.

How about a bigger number? Calculate it like this. First find the powers of 2 that are needed::

    42 = 32 + 8 + 2


Add in the missing ones::

    42 = (1 x 32) + (0 x 16) + (1 x 8) + (0 x 4) + (1 x 2) + (0 x 1)

And read off the 1s and 0s. In this case 42\ :sub:`10` is 101010\ :sub:`2`.

Most of this will be hidden as we write programs, but it helps to understand that this is happening "behind the scenes".

How Computers Work
==================

This is not the time or place to go deeply into the inner workings of a modern computer, but it *really* does help to understand programming if you have some idea of what's going on inside the box. After all, that's what a program is for; it's to make the computer do something useful.

.. note::
   What follows is very imprecise, but is mostly accurate, at least from a programmer's point of view. This is not a book about hardware!

Inside a computer is some memory. The memory stores all the programs that are running, along with the data they are using. It's usually called RAM. The memory is volatile (which means that everything in it is lost when the computer is powered off), so there is usually also some less volatile storage, like a disk drive. There is usually a lot more non-volatile storage available, mostly because it's a lot cheaper. In either case, data is stored in binary, as 1s and 0s, and binary is used to represent all the different kinds of data that a program might use.

The heart of a computer is the CPU. This is the chip that can carry out operations on data. Usually it only has a very few operations it can do, like adding two numbers, or comparing two, but my combining them we can write complex programs. The CPU can only work with programs and data that are in the volatile memory. To allow for this the CPU has a small amount of memory internally, and any data needed is copied into that so it can be processed.

So, when a program runs, it is first loaded into the memory. If the program requires some data (say a user has to type in a value), that data is also stored in memory. When the CPU needs it, it is copied into the CPU's memory, where is can be processed. Once done, the result is copied back into the main RAM, and the program carries on.

It is, obviously, much more complicated than that, with a modern CPU having many cores to allow it to process many things at the same time. But hold on to this idea of data being stored in memory, copied to the CPU, and written back. It's important.

Text Files
==========

"Stuff" on a computer is organised into files (which are also stored in a binary format). A file might represent a document, an image, or anything else that might be useful. Often a particular application is needed in order to use a file, so we sometimes talk about "Word Files" or "Photoshop Files". Files for applications like these are usually stored in some format that makes them useful only with that application; you can't open a Word file with Photoshop, or vice versa. This is OK, but remember that the files are only useful for as long as the application is available. If Word is suddenly unavailable (or, more likely, is not installed) all those Word files are useless.

This is becoming an issue in general Computing. Files created with applications that have become obsolete are themselves obsolete, with the owners unable to get at the data within. This is a big problem for businesses that rely on this data, and often means that they have to spend a lot of money maintaining obsolete software. The format in which we store our data is important - we can access documents written on paper hundreds of years ago, but getting at a document written in Wordwise in 1985 is basically impossible [#cds]_.

One format that will always be used and will always be decipherable is *plain text*. In Windows, such files are often opened with the Notepad editor, but they can be opened with many, many tools. Programs are written in plain text files. This means that programs written decades ago can still be read and understood, even if the computers that could run them are long gone. It also means that *every* computer has a tool that can be used to edit programs in plain text files (assuming the computer has some sort of keyboard!).

.. important::
   There is no such thing as a "Python File". A Python program is a plain text file that happens to contain the instructions that make up a Python program. It can be created or changed with any tool that can work with plain text files.

A side effect of this is that there is a lot of choice when it comes to created Python programs (or programs in any other languages). Some tools are sophisticated, and offer features specific to Python. Others are more general purpose. Some are very basic, but at least allow you to get the job done. More on these later.

.. hint::
   If you have some valuable data, consider keeping it in a plain text file. So if you lose that beautiful Word CV, at least you have the data so you can rebuild it. And if you really want to store some data so it will be around for 50 years, print it out and put the paper somewhere safe.

.. rubric:: Footnotes

.. [#tell] The word "tell" is not a very good one here, because it suggests that the computer as some awareness, and knows what it is doing. Of course, this is not, yet, true. But as you start out in programming this can be a useful way of understanding what is going on - you have a problem, and you are telling the computer how to solve it.
.. [#bool] This is a rare case in computing of an idea being named after a person (eponymy). Bonus credit if you can find more.
.. [#float] This means that there are some decimal numbers that it is impossible to represent inside a computer. Different ways of representing numbers with decimal parts exist, and have different levels of accuracy, but this is not something you need to worry about in normal programming.
.. [#onoff] In early computers, "on" and "off" would have corresponded to two positions of an actual switch or button, of course.
.. [#cds] We're talking about the format of the data on the disk here, but the same applies to the physical format. Not so long ago, for example, every PC had a CD drive. Now, very few do. So what shall we do with all that data we archived to CD in the 1990s and 2000s? Let's hope none of it was important, eh?
