===============
Before We Start
===============

At this point most books on programming leap right on in and start on the code. This is fine, for some folks. But it means that sometimes people who are new around here can get lost, because they don't really understand the basic ideas. Often there are a many assumptions being made about what you know before the coding start. And, guess what? If you don't know those things you very quickly get lost in a whole load of detail. You off to a bad start from the get-go.

So in this chapter we'll look a few basic ideas that underpin the whole business of programming. These are mostly familiar, that you've probably met many times before, but we need to think about them in a programming way. And these are all things that need to be kept in mind as we carry on.

.. tip::

    This chapter is short, but rather difficult to arrange in the best order. It might be an idea to read through it quickly once, then again, more slowly!

Let's start by thinking about what a computer program actually is.

.. index::
    single: computer program
    single: computer program; instructions

Instructions
============

A computer program is just a set of instructions. The instructions tell\ [#tell]_ the computer how to carry out some task.

.. sidebar:: Try It!

    After reading this section, try it! Write some instructions that someone should be able to follow to carry out
    some everyday task. Making a coffee, boiling an egg, starting a laptop and opening a Word file, walking from your place to the nearest corner shop ...

We are all used to following instructions. This might be to install some software, walk to a new location in a new town, or make a new and interesting soup. This idea is so common that most of us probably carry on without really thinking about what we're doing. In fact, in some cases we could follow some instructions without knowing what the end result is intended to be!

.. important::

    But remember that we are intelligent. Computers do not, yet, have intelligence. If a human were given instructions that do not make sense, or even placed them in peril, they would stop following them and seek corrections. Computers will just carry on following their program (instructions), regardless, with no *understanding* of what's going on.

Some sets of instructions are presented in a formalised way according to some conventions. That soup recipe, for example, will start by telling us what the recipe makes, and what quantity. It will then list the ingredients, and then present the steps to take, one at a time, in the correct order. It would be very strange to find a recipe that gave the steps before listing the ingredients; it would be very awkward to use. Following a recipe also assumes that we understand basic cookery terms ("mix", "fry", "stir"), probably some abbreviations ("tsp" means "teaspoon", "g" is "gram"), and that we follow it with some intelligence ("fry until browned", "add enough to thicken the soup"). Also, we would query anything that seemed obviously wrong; we would not add 10 *kilograms* of flour to thicken our soup, because that is clearly wrong (and probably a misprint for *grams*).

In general, any set of instructions contains the same elements. There is a *sequence* of steps. And there is *choice* and there is *repetition*. While we usually follow instructions from the first to the last (or from the top to the bottom), this is very rarely done without one or the other of *choice* or *repetition*. In general, instructions contain:

.. index::
        single: computer program; instructions
        single: sequence
        single: choice
        single: repetition

Statements
    A single instruction to do something: "Add the onions", "Cross the road", "Connect the USB cable".
Choice
    Do one of a number of things (Statements), depending on what is observed. "Add water if required", "Cross the road if it is safe to do so", "Connect the cable if an external monitor is to be used". What is done depends on whether something is observed to be *true* or *false*.
Repetition
    Do (a Statement) several times. "Add the flour until none remains", "Walk uphill until you reach the station", "Click to install each of the updates that will download".

These three are the three most basic building blocks that make up any set of instructions. They are also the basic building blocks of a computer program.

When writing a program, a programmer supplies the computer with an ordered list of instructions, along with the choices and repetitions that are needed to achieve a successful result. The instructions are expressed in a programming language, like Python.

What do these instructions do? They store and manipulate *values*. If you think about it, it's amazing that these simple ideas can get us to complex software programs such as modern games and office tools.

.. index::
    single: values
    single: types

Values and Types
================

In many daily tasks we are involved with using and manipulating *values*.

Some of these values are numbers, or *numeric*. We might have to pay a bus fare, buy a needed amount of something, or walk a certain distance. We are good at recognising these values and carrying out tasks that involve them.

Generally to do this we think in units of tens, or fractions of tens, or multiples of 10. Our currency is based on 10s, and we are used to working with 10s. While in the UK we hold on to measuring longer distances in miles, we are increasingly using the metric system, which is based on 10s.

.. index::
    single: powers
    single: floating-point numbers

Multiples of 10 (powers) are handy for bigger numbers: 10\ :sup:`2` is 100, 10\ :sup:`3` is 1000 and so on. These numbers are all integers, or whole numbers. This idea is at the heart of the metric system.

Fractions of 10 are used for more exact numbers, and numbers that represent part of a whole. These are *floating-point* numbers. They can also be represented as powers: 10\ :sup:`-1` is 0.1, or a tenth; 10\ :sup:`-2` is 0.01, or a hundredth.

It's often stated that our obsession with working in 10s like this comes from the usual number of fingers we observe on our hands. This could be true, or it could just be that this is something we are so used to doing, and something we are taught from an early age, that it's impossible to think of any other way.

Of course, we often use values that are not numbers. An example of another *type* of value we use every day is *characters*. These could be letters, digits, punctuation marks, or even emojis. A sequence of characters might represent a name or an email address. They could also represent a phone number - in this case the characters are also digits, but they are characters unless we plan to add up phone numbers, which is unlikely. A single character can have meaning - a grade on a test, for example. A collection of characters can also have a meaning, sometimes only if they are read in a particular order. We might call such a collection a *string*; the order of characters in a string is usually important.

So, we use *values*, and values have *types*. We carry out operations on values, and the operations we can do are determined by the types. For example, we often add up numeric values to work out how much to pay. We don't add up character values, but we often use a string of them to, say, send an email. We might also compare values, to see if they are the same, or if one is bigger than the other. We might also test to see if a value is in a particular range, or if it is a particular value. All these things, obviously, also go on inside a computer program.

.. index::
    single: Booleans
    single: True
    single: False

True and False
==============

.. highlight:: none

There is another type of value that is very important in Computing. It gets a separate section here because maybe it is a little less obvious, even if we do deal with it in everyday life. We deal with the ideas of truth, falsehood, and fakery. Take any statement, and we might say that it is *true* or it is *false*.

.. note::

    Arguably there is a third state, where we know that a statement is true or false but we do not know at present which.

Any statement can be tested, and from the test its "truth value" can be determined. That said, some statements are always true, and this can never change::

    Python is named after Monty Python's Flying Circus.

Some statements, on the other hand, are always false, and this will never change\ [#guido]_::

    Johnny Depp created the Python programming language.

Often, statements are either True or False, depending on something that can be tested. So this statement is true as I type this::

    It is Tuesday today.

It could be true as you read this, or it could be false. I have no way of knowing right now. I have just read it on a Monday, so now it is false. In order to determine whether it is currently true or false, you would need to test it, maybe by checking your phone.

Programming revolves around these two values, for reasons we will see in a moment. When it comes to making sure that a program works correctly, they are probably the most important values! A statement is true, or it is false. Perhaps it is true that a program's user has clicked a button in the interface, and so the program better respond in some useful way. Maybe it is false that the user has permission to access that part of the application. Maybe it is true that Mario just drove into a banana skin, and so the program better make him skid.

.. index::
    single: logic
    single: Boolean
    single: logic operators
    single: Boole, George

`True` and `False` are called **Boolean** values, named after `George Boole <https://en.wikipedia.org/wiki/George_Boole>`_, who in 1847 first applied mathematical ideas to logic\ [#bool]_. The word Boolean is usually written with a capital B for this reason.

.. index::
    Monty Python's Flying Circus: Parrot Sketch

Boole also showed how True and False can be combined using what are now known as Boolean (or logic) operators. For example, if there are two statements, **and** both are True, we can agree that a combined statement is True::

    John Cleese wrote the Parrot Sketch.
    The Parrot Sketch was in Monty Python's Flying Circus.

    John Cleese wrote a sketch that was in Monty Python's Flying Circus.

.. index::
    single: truth tables
    single: logical operators
    single: and (Boolean)
    single: or (Boolean)
    single: not (Boolean)

.. _truth-tables:

There are a whole bunch of *logic operators*, but most of them are only really useful when working with electronics or hardware. For programming purposes, three are usually enough. ``AND`` and ``OR`` combine two logic values (let's call them ``A`` and ``B``, like this:

=====  =====  =======  ======
  A      B    A and B  A or B
=====  =====  =======  ======
False  False  False    False
True   False  False    True
False  True   False    True
True   True   True     True
=====  =====  =======  ======

If you read it, the result is very much as you would expect if you just read it out loud::

    A is True.
    B is True.

    Therefore A and B is True.

    A is True.
    But B is False.

    Therefore A and B is False.

The third useful operator, ``NOT`` just flips the value. So a True becomes False, and vice versa:

===== =====
  A   not A
===== =====
False True
True  False
===== =====

Why is this important? Let's look at how computers (for the want of a better word) "count".

.. index::
    single: binary
    single: base 2
    single: denary
    single: octal
    single: hexadecimal
    single: Unicode

Binary
======

So, how does a computer store the data it needs? Computers do not have 10 fingers, but they do have electrical switches\ [#onoff]_. A switch has two possible values; it can be "on", or it can be "off", just like a light-switch at home.

So computers count in 2s, which is called *binary*.

Remember that humans count in 10s. We find 10s easy, probably because we are taught to use 10s from an early age. The origins of this are probably that we have 10 fingers, and we can use these to count. Children are still taught to count in 10s, and to use their fingers to help them.

Powers are important here. This is when a number is multiplied by itself. To handle larger numbers we give certain powers of 10 special names, so:

* 10 x 10 (or 10\ :sup:`2`) is a hundred.
* 10 x 10 x 10 ((or 10\ :sup:`3`) is a thousand.

and so on.

.. note::

    Counting in 10s like this is called *base 10* or sometimes *denary* or (less accurately) *decimal*. In Computing we also sometimes meet *Octal* (base 8) and *Hexadecimal* (base 16). See that those last two are powers of two. That's important. It's all to do with how computers store data, with the memory arranged into chunks of 8 bits (a *byte*). More on this later.

Computers do not have fingers! A computer is an electronic device, based around *switches*, where a current is either flowing, or not. So a switch is something that is either "on" or "off". So if a sentient computer could count, it would count in 2s, in much the same way as humans use 10s. This is called *base 2*, or *binary*.

This means that every data value stored inside a computer, either in memory or on a disk, is *encoded* in binary. The details are not important here, but an overview is. Basically:

* An integer can just be stored as its binary equivalent.
* Various cunning ways exist to store floating-point numbers with fractional parts\ [#float]_. Again, this usesd binary.
* Character data can be stored by using a table to convert between integer values and the characters. The most common one
  is `Unicode <https://en.wikipedia.org/wiki/Unicode>`_. You may also see references to Unicode's predecessor, `ASCII <https://en.wikipedia.org/wiki/ASCII>`_, which offers a smaller set of characters.

So if a computer could somehow write out an integer it would have just two symbols to work with, `1` and `0`. It would also work in powers of 2: 2\ :sup:`2` is denary 4, 2\ :sup:`3` is denary 8, and so on.

.. hint::

    To avoid confusion it is usual to add a subscript to a number when different number bases are involved. So 8\ :sub:`10` means the number 8, in denary (base 10). Likewise, 1000\ :sub:`2` is a binary value. (The two happen to represent the same number).

.. important::

    Knowing and recognising the powers of 2 is a hugely important skill in computer science::

        1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048

    If you have ever bought a laptop, you will recognise those numbers from the system specs! Currently, laptops tend to have either 8 or 16 GB of memory, and offer either 256 GB or 512 GB of storage. These are all powers of 2, and it all comes back to how computers store data.

So how would a computer represent, say, 3\ :sub:`10`?

Easy. Look at the powers (it helps to see them in reverse order::

        2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1

3 is just 2 + 1. So, in binary 3 is 11\ :sub:`2`.

How about a bigger number, like 42? Calculate it like this. First find the powers of 2 that are needed (it's just like giving change using the smallest number of coins possible)::

    42 = 32 + 8 + 2

Add in the missing ones::

    42 = (1 x 32) + (0 x 16) + (1 x 8) + (0 x 4) + (1 x 2) + (0 x 1)

And read off the 1s and 0s. In this case 42\ :sub:`10` is 101010\ :sub:`2`.

Most of this will be hidden as we write programs, but it helps to understand that this is happening "behind the scenes". Let's now think about how a computer stores and processes these values.

.. index::
    computer; how it works
    single: memory
    single: CPU
    single: RAM
    single: volatile
    single: non-volatile
    single: disk drive

How Computers Work
==================

This is not the time or place to go deeply into the inner workings of a modern computer, but it *really* does help to understand programming if you have some idea of what's going on inside the box. After all, that's what a program is for; it's to make the computer do something useful.

.. note::
   What follows is very imprecise, but is mostly accurate, at least from a programmer's point of view. This is not a book about hardware!

If this was a hardware book, you would learn that the main components of a computer are a *CPU* (Central Processing Unit), and some *memory*. The CPU is the part that carries out the instructions, and the memory is where the data is stored. There also needs to be some way to get data in, and get results out. Data being processed by the computer can either be volatile, or non-volatile. Volatile data is lost when the computer is powered off, and non-volatile data is not.

So, nside a computer is some memory. The memory stores all the programs that are running, along with the data they are using. It's usually called RAM. The memory is volatile (everything in it is lost when the computer is powered off), so there is usually also some less volatile storage, which these days still means a disk drive, or it could be "Cloud" storage. There is usually a lot more non-volatile storage available, simply because it's a lot cheaper.

In either case, data is stored in binary, as 1s and 0s, and binary is used to represent all the different kinds of data that a program might use. The computer spends a lot of time shuffling data between the volatile and the non-volatile storage, which can have a significant impact on the performance of a system.

The heart of a computer is the CPU. This is the chip that can carry out operations on data. Usually it only has a very few operations it can do, like adding two numbers, or comparing two numbers, but by combining them we can write complex programs. The CPU can only work with programs and data that are in the volatile memory. To allow for this the CPU has a small amount of memory internally, and any data needed is copied into there so it can be processed. (That's another performance bottleneck).

So, when a program runs, it is first loaded into the memory. If the program requires some data (say a user has to type in a value, or some file is needed off a disk), that data is also stored in memory. When the CPU needs it, it is copied into the CPU's memory, where it can be processed. Once done, the result is copied back into the main RAM, and the program carries on. These days this all happens very quickly, but it's still happening. It is still necessary to write programs that are efficient, and that don't waste time copying data around. That's why we need to understand what's going on

It is, obviously, much more complicated than that, with a modern CPU having multiple cores to allow it to process many things at the same time. But hold on to this idea of data being stored in memory, copied to the CPU, and written back. It's important.

We finish with a look at how data is stored in that non-volatile memory (usually a hard-drive of some sort).

.. index::
    single: file formats
    single: plain text
    single: text files

Text Files
==========

.. important::

    This section is very important. Modern operating systems, especially Windows, condition us to associate files with the applications that use them. We double-click a file and the appropriate application opens, as if by magic. This is fine (and undoubtedly convenient) for the user who sees their laptop as an appliance, but it gets in the way when we want to do serious work.

"Stuff" on a computer is organised into files (which are also stored in a binary format). A file might represent a document, an image, or anything else that might be useful. Often a particular application is needed in order to use a file, so we sometimes talk about "Word Files" or "Photoshop Files". Files for applications like these are usually stored in some format that makes them useful only with that application; you can't open a Word file with Photoshop, or vice versa. This is OK, but remember that the files are only useful for as long as the appropriate application is available. If Word is suddenly unavailable (or, more likely, is not installed on a particular computer) all those fine Word files are useless.

The simplest file is just a *plain text* file. It contains characters, encoded in binary, probably in turn using Unicode. The characters could represent anything - a shopping list, a Python program, a set of system specs. This format has been around for as long as modern computers have been. Should we find a plain text file from the 1960s or 1970s we would have a very good chance of accessing its contents in the 2020s.

The tight coupling of applications and files is becoming an issue in general Computing. Files created with applications that have become obsolete are themselves obsolete, with the owners unable to get at the data within. This is a big problem for businesses that rely on this data, and often means that they have to spend a lot of money maintaining obsolete software just so they can get at their historic data. The format in which we store our data is important - we can access documents written on paper hundreds of years ago, but getting at a document written in Wordwise of a home microcomputer in 1985 is basically impossible\ [#cds]_.

One format that will always be used and will always be decipherable is that good old *plain text*. In Windows, such files are often opened and modified with the Notepad editor, but they can be opened and modified with many, many tools. Programs are written in plain text files. This means that programs written decades ago can still be read and understood, even if the computers that could run them are long gone. It also means that *every* computer has a tool that can be used to edit programs in plain text files (assuming the computer has some sort of keyboard!).

A side effect of this is that there is a lot of choice when it comes to creating Python programs (or programs in any other languages). Some tools are sophisticated, and offer features specific to Python. Others are more general purpose. Some are very basic, but at least allow you to get the job done. More on these later.

.. hint::
   If you have some valuable data, consider keeping it in a plain text file. So if you lose that beautiful Word CV, at least you have the data so you can rebuild it. And if you really want to store some data so it will be around for 50 years, print it out and put the paper somewhere safe.

.. tip::

    This book applies this principle! The files that make up this book are plain text. A simple mark-up language called `reStructuredText <https://docutils.sourceforge.io/rst.html>`_ is used to mark sections, fonts and so on. Even if that language was no longer supported anyone could take the text files, and reasonably quickly extract all the content. The HTML or PDF that you are looking at is created from the plain text files by a bunch of Python programs (which are themselves plain text files, of course).

    A side issue is that the files that make up this book can be edited on basically any computer.

The practical upshot of all this is:

.. important::

    There is no such thing as a "Python File". A Python program is a plain text file that happens to contain the instructions that make up a Python program. It can be created or changed with any tool that can work with plain text files. As we will see, that tool could just be good old Notepad, or it could be something more sophisticated.

A second upshot is that this book can be neutral as regards the operating system, and overall toolset you choose to use for your programming. Any OS can handle plain text files, and there are many, many, great tools out there. This book will not be tied to any particular toolset, and will not assume that you have any particular tools, apart from Python, installed.

Takeaways
=========

The takeaways from this chapter are very simple. You need an understanding of each topic above. For example:

#. You need to understand (in everyday terms) instructions, sequence, choice, and repetition.
#. You should know that values have different types, and have some idea of how these are stored in a computer.
#. You should have a basic idea of how a computer stores and processes data.
#. You should understand that files have different formats, and why plain text is the one format to rule them all.

.. [#tell] The word "tell" is not a very good one here, because it suggests that the computer as some awareness, and knows what it is doing. Of course, this is not, yet, true. But as you start out in programming this can be a useful way of understanding what is going on - you have a problem, and you are telling the computer how to solve it.
.. [#guido] He didn't. See `Guido van Rossum <https://en.wikipedia.org/wiki/Guido_van_Rossum>`_.
.. [#bool] This is a rare case in computing of an idea being named after a person (eponymy). Bonus credit if you can find more.
.. [#float] This means that there are some decimal numbers that it is impossible to represent precisely inside a computer. Different ways of representing numbers with decimal parts exist, and have different levels of accuracy, but this is not something you need to worry about in normal programming.
.. [#onoff] In early computers, "on" and "off" would have corresponded to two positions of an actual switch or button, of course.
.. [#cds] We're talking about the format of the data on the disk here, but the same applies to the physical format. Not so long ago, for example, every PC had a CD drive. Now, very few do. So what shall we do with all that data we archived to CD in the 1990s and 2000s? Let's hope none of it was important, eh?
