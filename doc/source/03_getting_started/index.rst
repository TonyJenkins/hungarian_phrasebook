===============
Getting Started
===============

Now to get programming. There are actually three things to master here:

#. How to enter a program.
#. How to get it to run.
#. How to find the results.

It has been said [#KnR]_ that once a new programmer can do these three things, the rest is compararively easy!

Remember that a program is just a text file. So you need to be able to create that file using your editor or IDE. And you need to store the file *somewhere where you will be able to find it again*. (That might seem obvious, but it often gets forgotten).

One way to learn some programming is simply to enter some programs, and run then [#Speccy]_. Gradually you come to understand what all the commands do. So let's start with three short programs, and try that.

Three Programs
==============

Here are three programs. Enter them into your computer (make sure you know where they're stored!), and then run them in whatever's the most convenient way [#copy]_.

.. caution::
   Take care when copying programs from a book. Long lines can get split in awkward places. You should see a symbol at the
   start of any line where this has happened.

.. index:: single: Programs; hello.py
.. literalinclude:: /../../src/03/hello.py
   :language: python
   :caption: ``hello.py``

.. index:: single: Programs; hello_name.py
.. literalinclude:: /../../src/03/hello_name.py
   :language: python
   :caption: ``hello_name.py``

.. index:: single: Programs; hello_age.py
.. literalinclude:: /../../src/03/hello_age.py
   :language: python
   :caption: ``hello_age.py``

If the programs fail to run, take a close look to see that you have them exactly right. Notice how your text editor (or IDE) will add colours to the code; as you get used to this it will help you spot mistakes. Some IDEs will also highlight errors in the code as you type.

Make sure you save the code somewhere, and that you know where this is! Ideally store your programs somewhere where you will always be able to find them.

So what do these programs do?

``hello.py``
    ... is the traditional first program that anyone writes. It just prints a cheery greeting on the screen.
``hello_name.py``
    ... is the tradtional second program. This time the program displays a prompt, the user enters their name, and a
    personalised cheery greeting is displated. Behind the scenes, the user's name is encoded as binary, stored in the
    computer's memory, and then retrieved, but all this is invsible to the programmer.
``hello_age.py``
    ... displays a cheery greeting include the user's age, which is calculated. Again, values are entered, and will be encoded
    as binary. Python always takes ``input`` as a string of letters, so there is a small fix to show that the values entered are
    integers, and will be used for a calculation. Again, a lot happens behind the scenes even in this small programmer, but
    Python is a high-level language, and the programmer doesn't need to worry.

Before leaving these programs, make copies, and change a few things. The worst that can happen is that you change something and the program stops working. Spend time getting used to your development tools; this will save a lot of pain later on.

Programming in a Good Place
===========================

Before carrying on to learn more, it really is worth taking some time to think about how you work best, and about which tools suit you best. There are two aspects to this. First, there are the software tools you use to create your programs, and second there is the question of the physical environment.

Tools of the Trade
******************

You shouldn't be using tools just because you've been told to, or your friends do, or because you always have. You need to have the best tools for the job, and that's different for different people. If you have a choice of tools to use, get them all installed, and try each one. Maybe use the programs above. See which you prefer. There is no single choice that works for everyone.

A modern IDE is immensely powerful. And as a programmer you will spend most of your day looking at it. So you should take time to learn how it works, and how to make it work for you. You probably only need a small fraction of what your IDE can do, but make sure you know what this small fraction is.

Modern IDEs are also extremely customisable. Take a look at the various colour schemes available, and pick one you like [#dark]_. Make the font bigger if you need to. Hide tools you are not going to need, make those you always need available all the time. You will probably find that the IDE will store settings so that you can sync them between your different computers. Seriously, take time to use the IDE, make it yours. If you follow this path you are going to be using it **a lot** over the next several years!

The Physical Side
*****************

Over time, a programmer will learn about what makes the best environment for them when they work. There are probably two aspects to this, but they are connected. First there is the hardware - the PC, laptop, screen, and so on - and second there is the overall environment - heat, light, desks, ambience.

There is no "one size fits all" here, but most programmers probably prefer to work from a laptop, which they carry with them everywhere. (This is even more common in these days of hybrid working). The laptop can be used wherever it is needed "on the road", or can be used in the office at a conventional desk. Usually, on a desk it will be hooked up to a second display for comfort and productivity. This small change may not immediately occur to people, but having two (or even three) screens available can seriously improve productivity, and is also healthier too.

.. hint::
    Getting the right setup is important. Think out of the box too. If you're going to work with long programs, how
    about having a second monitor in portrait orientation? That's anothe potential game-changer.

Desktop PCs still have their place but, again, consider having more than one monitor. And that keyboard? Is it one you can happily type on all day? Are you good with where all the keys are? Is the mouse comfortable to use?

And finally, think about the overall environment. A tidy desk is best. Do you want somewhere to open books, or are you happy to prop up a Kindle? Natural light is ideal but, if not available, there should be plenty of light sources. Think about whether you work best with music playing, or without? Above all, make sure there is a ready supply of coffee to hand [#coffee]_!

Takeaways
=========

After this chapter you should:

* Be able to enter programs, run them, and see the output.
* Have familiarised yourself with your programming tools, and at least started to customise them to suit your own preferences.
* Have thought about the best physical environment for your programming work, and probably arranged this.

Now we can move on to see how a program processes and stores values. After all, that's what computers are good at, and also if you think about it, what every program does!

.. rubric:: Footnotes

.. [#KnR] It is said in *The C Programming Language* by Brian Kernighan and Dennis Richie, a book affectionately known as "K&R".
.. [#Speccy] Most programmers between the ages of, say, 50 and 60 learned programming this way, hacking away at programs on the home microcomputers of the 1980s. ZX Spectrum all the way.
.. [#copy] If you are looking at this as a web page, you will see that a handy button will appear when you hover the mouse over the program code. This allows you to copy the code, *but* you will learn more if you type it yourself.
.. [#dark] As long as it's a dark colour scheme. No-one uses light schemes. Seriously.
.. [#coffee] Other beverage choices are possible, but most programmers go with coffee.
