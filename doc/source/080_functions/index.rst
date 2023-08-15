=================
Keeping it Simple
=================

Right at the start of the book we went through some basic ideas that, together, formed what you need to know to start programming. If you look back, you will see that we have now covered everything. Sure, there are some things that will make our programming lives easier, and some features of Python that need a mention, but everything is very much there.

We could use what we have learned to write complex programs. But there would be a problem. These programs would quickly become very long, and the whole process would be unsustainable. How would we cope if a small change in a program at line 11 caused an expected error at line 276? Or even line 102982? Complex systems are made up of tens of thousands of lines of program code, often more. No-one can cope with that complexity, so there needs to be some way to keep the day-to-day programming tasks to something we can comprehend.

So, how many lines of program should a developer be working on? A reasonable rule these days would be an *absolute maximum* of 50, but ideally far fewer. The guideline used to be around 20, going back to the days when programming was done on a single-screen dumb terminal.

.. image:: ../_images/vt100.png
    :width: 400
    :align: right
    :alt: A VT100 Terminal

The guideline really is that a programmer should be able to see *all* the code they are working on, without scrolling up and down. In the olden days, this was about 20 lines. Now it's a few more, but not by much.

The ideas in this section are all about keeping the amount of code a programmer works on down to a reasonable limit. But first, some more to convince you that this really is a good idea.

Code is Crafted
===============

A common saying these days is that programming is a *craft*. This means many things, but essentially it tells us that programming is all about producing good, elegant solutions, that can be maintained and repaired, and that will work for a long time. It is not enough for a program to work - it must work well. Or, if you prefer, it should be *crafted*.

Think about a craftsperson making a chair. A chair can be made by nailing a few pieces of wood together, and screwing some legs on. But that would not produce a good chair. A good chair simply looks good. It is well made, and we will be happy to have it in our homes. We would expect a good chair to be used for a long time, and we would expect to be able to repair it.

Here are some ideas that help us think about what makes code good, or indeed *crafted*.

Code is Read
************

Code is read much more than it is written. Good code should be readable, so that a programmer who is not the original author can quickly and easily see what it does, and how it does it. This means that good code:

* Follows all the conventions of programming in that language.
* Uses meaningful identifiers for all variables and constants.
* Does not rely on "neat tricks" or anything that obfuscates what is going on.

Remember also that the programmer reading the code might still be the original author, a few years down the line!

Programming is a Team Effort
****************************

Anything other than the simplest programs is developed by teams of programmers. So there needs to be a way to split the work. If a program is held in one single monolithic file, it is impossible for several programmers to work on it together. So splitting the work up is vital.

.. important::

    This short statement introduces the need for *source code control*. More on this at the end of the book.

Multi-tasking is Difficult
**************************

Do you find it difficult to do 7 things at once? Probably.

A program that does 7 things is difficult to write, for the same reason. It is difficult to keep track of what should be doing what, and how that affects other things.

Splitting the program into smaller chunks can remove this problem. The key idea is that each "chunk" does exactly one thing. This means:

* That the code to be worked on will be shorter.
* Programmers can work on one chunk each, and later combine them.
* If the code has to do one thing, the chances are it will do that thing!
* If the code turns out to be incorrect, it is obvious where the fix needs to be.

This idea leads up to the most important concept here - DRY Code (and WET Code).

Don't Repeat Yourself
*********************

Once you have some program code that solves a problem it makes sense to keep using it wherever it can be used. This is, of course, the basic idea of *abstraction*, or taking a solution to one problem and using it elsewhere. For example, if a program requires a user to enter an integer value ten times, why write the code for that out ten times? Why not write it the once, and then "call" it whenever needed?

This idea exists in many areas of Computing. Do something once, or save a data item once, and that becomes the definitive version. Once you have this version, use it wherever needed. The score is that you have recorded this one aspect of the system once, and in one place. It would need to change it for some reason, just change it once.

.. seealso::

    An important idea in databases is to store everything about the problem once. Then if you need to change it, you change one thing. You *represent everything in the real world once*.

This gives us the idea of DRY code, which is good code.

.. important::

    DRY is *Don't Repeat Yourself*.

    Do it once, and reuse it.  DRY is good.

The alternative to DRY code is, obviously WET code.

.. warning::

    WET is Write Everything Twice.

    WET is Waste Everyone's Time.

    WET is We Enjoy Typing.

You should always aim for DRY Code. DRY Code is good for teams, good for keeping things simple, and good for crafting code.

Code Reuse
==========

Let's jump in with an example. In the chapter on Modules, we had this program.

.. literalinclude:: /../../src/07/pythagoras.py
   :language: python
   :caption: ``pythagoras.py``

And we noted that the two ``input`` lines really need some sort of validation to make sure that the numbers entered are greater than zero. In fact, if the user's experience is to make sense, we really shouldn't be asking for the second number until the first has been entered correctly. It would also be best to allow the user to reenter their value if an error is detected.

The code to validate one number is straightforward, not least because we have seen it before! We simply stick the ``input`` inside the usual infinite loop, and ``break`` out once the number is acceptable. It looks something like this:

.. code-block::

    while True:
        side = int(input('Enter a length: '))

        if side > 0:
            break
        else:
            print('Value out of range. Try again.')

To fix the program, we could just use this code twice. *But we would be repeating ourselves!*. We need to way to put this "chunk" of program somewhere, so that we can use it more than once. That turns out to be easy, but defining a *function*. To do this, we basically just give this code a name, and *def*ine it at the start of the program. And then we can use it twice. The amended program looks like this:

.. literalinclude:: /../../src/08/pythagoras.py
   :language: python
   :caption: ``pythagoras.py``

A lot going on here! Things to note:

* The function is defined *below* the ``import`` and above the main program.
* The function contains the usual code to read an integer, and has a name that explains what it does.
* The function is used (called, or "invoked") (twice) from the the main program.
* When it has finished, the function has a ``return`` line that sends a value back the main program.

.. hint::

    By convention there are *two* blank lines above and below the function.

.. important::

    There is actually very little new here. Using this function is exactly the same as using any of the built-in functions we have used before. The only real difference is that we wrote the function, and we can see its code.

This is fine, and we are being DRY, but let's make it a little better. At the moment, the prompt displayed when the user enters a value is always the same. In the original program it was different. We can change the way the function works by sending it some values. These values, called *parameters* work like this:

.. literalinclude:: /../../src/08/pythagoras_2.py
   :language: python
   :caption: ``pythagoras.py``

So now (run it and see!) the program will display two different prompts. The string provided where the function is called passes into the function, and matches up with the ``prompt`` variable that is used in the ``input`` line.

Finally, the killer! We have forgotten to check that the value entered is an integer. We know that an exception will be thrown if the value is something else, and we know the code to catch this. Now we are using a function, though, we need to enter this new code just the once. And it will work in both places where it is used. DRY!

.. literalinclude:: /../../src/08/pythagoras_3.py
   :language: python
   :caption: ``pythagoras.py``

In Python, the technique we are using here is called a *function*. Every programming language provides something similar although, as usual, the names may change. "Function" is common, but you may encounter *procedure*. In some languages the correct term is *method*, although these are subtly different. For the moment "function" is what they will be called.

Now, let's step back and look a bit more at what is going on here.

Functions Explained
===================

We have already seen how to use the functions that come as part of Python's Standard Library, and also those that can be imported from modules. What is new now is that we are going to write our own functions.

Just like the built-in functions, our functions should be tried and tested units of code that:

* Do exactly one thing (and therefore do it well).
* Are less than about, say, 25 lines of code.
* May take input values ("parameters") that affect what they do (like the value passed to ``math.sqrt``.
* Usually\ [#return]_ ``return`` some value once they have completed.

Ideally, functions also have the potential to be used in other programs, but this may not always be possible. Even then, using functions splits up the program into smaller chunks that are easier to write and manage.

Functions are defined at the top of a program, below any ``import`` line and before the main program starts. They are checked by Python, but the lines in them are not executed. And by convention functions are separated by *two* blank lines.

.. important::

    It may seem that functions are complicating the issue. After all, you can write a program without them. But this is to miss the point. Functions make writing the program easier, by breaking down the task. Sure, you can write a 100 line program without functions, but try writing a 100,000,000 line system in one file!

Functions are called from the main program just like the built-in functions. Functions can, and often do, call other functions.

Let's look at some examples.

.. topic:: Example Function

    Write a function to determine if a number is even.

The maths here is easy - we simply need to divide a number by 2, and see if the result is an integer. Or, and probably easier, we could use the modulus operator (``%``) and see if the result is zero. The function will need to receive the number to be tested as a parameter, and will return ``True`` if it is an even number, or ``False`` otherwise. And for a name ``is_even`` sounds like a good call\ [#names]_.

Now to write the code for the function. The first line defines the name, and optionally, the names of any parameters. It can be useful if the identifier of the parameter gives a hint of the purpose of the value. So:

.. code-block::

    def is_even(number):

Then the rest of the function (called the *body* goes below. With a ``return`` to send the result back to whatever is using the function. There can be more than one ``return`` - whichever is reached first will terminate the function. So we can write:

.. code-block::

    def is_even(number):
        if number % 2 == 0:
            return True
        else:
            return False

That's it.

Of course, the function should be tested. This is often done just by writing a short program that tests the function with a variety of input values. So we could quickly print all the even numbers in a range:

.. literalinclude:: /../../src/08/even_tester.py
   :language: python
   :caption: ``even_tester.py``

And that should convince us that all is well with the function.

All is well, but the function doesn't do any error checking. If the value passed to the function is something other than an integer, there will be an error (an exception). *This is fine!* The exception should go back to whatever called the function, and we should expect that to deal with it.

.. note::

    Functions can also generate their own exceptions. We'll do an example shortly.

This function had just the one parameter, but in general functions can have any number. In this case, they need to be supplied in the expected order. To illustrate this, let's *generalise* our function for reading an integer. We'll create a version that takes three parameters:

#. The lowest allowed value.
#. The highest allowed value.
#. The message to display when the user is prompted to enter the value.

So we have there an integer, another integer, and a string. And there is an additional rule that the first integer must be lower than the second. We have most of the code itself from our previous example.

The first line of the function again defines it, and names the parameters:

.. code-block::

    def read_int_with_limits(lower_limit, upper_limit, prompt):

As usual, we try to use identifiers that show what is going on. In the main body of the function we just need the usual loop, with a check that the value is between the limits. We'll take the chance to *refactor* the code slightly to remove the ``break``; we can just ``return`` at this point\ [#refactor]_.

.. code-block::

    def read_int_with_limits(lower_limit, upper_limit, prompt):

        while True:
            try:
                number_entered = int(input(prompt))

                if lower_limit <= number_entered <= upper_limit:
                    return number_entered
                else:
                    print('Value out of range!')
            except ValueError:
                print('Please enter an integer!')

This function can be called from anywhere else, with the call providing two integers, and a string, in that order:

.. code-block::

    sides = read_int_with_limits(1, 100, 'Enter the number of sides: ')
    players = read_int_with_limits(1, 6, 'How many players? ')

Finally, we have a problem if there is an error when the function is called, and the second number is lower than the first. The function would fall into an infinite loop, because there is no value between the two. What to do?

There is *absolutely no point* printing out an error. It does not help to tell the program's user that the *programmer* has made an error. The correct thing to do is to ``raise`` an exception to indicate to whatever is calling the function that some dreadful has happened, and the function cannot do its work. In fact, we can simply use an existing exception - ``ValueError`` looks a good one - and throw this back.

.. code-block::

    def read_int_with_limits(lower_limit, upper_limit, prompt):

        if lower_limit > upper_limit:
            raise ValueError('Invalid limits')

        while True:
            try:
                number_entered = int(input(prompt))

                if lower_limit <= number_entered <= upper_limit:
                    return number_entered
                else:
                    print('Value out of range!')
            except ValueError:
                print('Please enter an integer!')

Here ``raise`` terminates the function and passes everything back to the caller. There should be code there that handles the exception, and does something sensible.

Let's finish this chapter with an example program that makes serious use of functions.

A Simple Game
=============

.. topic:: The Rules

    A game is played on a 20x20 grid. There is some buried treasure at a random location. The player starts at the bottom left, and can move north, south, east, or west. After every move, they are told how far they are from the treasure.

    The game is simply for the player to move to the treasure in as few moves as possible.

There are many ways to implement this simple game. What follows is just one example. It has been chosen so that it covers all the ideas from this chapter. (And it would also be easier if we could use some of the ideas in the next, but we are where we are\ [#tuples]_.)

Let's go.

Thinking It Through
-------------------

Programming works like this. We have a problem, so now we start breaking the problem down into smaller problems. We can immediately see some of the problems we will have to crack:

* We will need to know the player's current position.
* We will need to randomly generate a location for the treasure.
* We will need to work out the distance between the two.
* The program will need to ask for the player's move, and terminate once they are at the treasure.

We cam see that it will be possible to detect that the player is at the treasure because the distance from it will be zero.

Thinking more about the problem we might spot a couple of issues that will complicate things:

#. A player should not be able to move off the 20x20 grid.
#. The treasure location should not be the same as the player's starting position.

We are going to need to fix these, sure, but they are fine examples of the sort of issue we might (and will) decide to ignore for the moment. We will get a basic version working, and come back to these details later. Our basic version can just track the player around the grid, not worrying about limits.

The grid for the game is 20x20, so we'll follow the usual X and Y axis model. The X-axis goes from 0 to 19 across, and the Y from 0 to 19 up. Remember that we should count from 0! For this first version, we can now think:

* We need two integers for the player's position, one for the X position (across) and one for Y (up).
* The user needs to enter their move (N/S/E/W will do). That needs to be validated.
* Once we have a valid move, we can change the player's position.
* The whole thing can loop forever. Eventually it will end when the player reaches the treasure.

We *could* write all this in one program, but it will be easier to write some functions. This is especially so as the function to get and validate the move does seem rather like the function we already have to validate the entry of an integer.

.. [#return] "Usually", because a function could just be a bunch of ``print`` statements. Even if a function just does some action (like opening a network connection, say) it usually returns a value to indicate whether or not it was successful.
.. [#names] Choosing function names carefully can often mean that lines of program can be read, and that reading them explains what they do. This can eliminate the need for any other tedious way of explaining or documenting the code.
.. [#refactor] Either way to write this is fine. Some programmers prefer to always have the ``return`` as the last line. Some go further and say there should only ever be one ``return``. We take the view here that anything is fine, as long as it is used consistently, and as long as the resulting code is clear.
.. [#tuples] There is only one place where this really becomes a pain. See if you can spot it.
