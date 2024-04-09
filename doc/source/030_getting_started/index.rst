===============
Getting Started
===============

Now to get serious and get programming.

There are three things to master here:

#. How to enter a program.
#. How to get it to run.
#. How to find the results.

It has been said\ [#KnR]_ that once a new programmer can do these three things, the rest is comparatively easy!

It is important not to skip over this part so as to get to the more useful and interesting programs. We are going slowly for a reason! It is vitally important to be able to work effectively with your IDE. You need to be able to efficiently enter programs, run them, and check the output. Most likely you will make mistakes entering the programs (everyone does), so you will also need to be able to find and fix these errors.

.. index::
    single: Errors
    single: Syntax Error
    single: Semantic Error
    single: Error; Syntax
    single: Error; Semantic

We will think more about errors later on, but for the moment let's agree that there are two types of error:

Syntax Errors.
    The program written does not conform to the rules of Python, so the Interpreter does not understand what it needs to do, and so the program fails. Usually, the IDE will spot most of these and highlight them in some way. This means that syntax errors are usually easy to spot and correct.
Semantic Errors.
    The program is correct Python, and so can be run, but does the wrong thing. This is discovered by comparing the results of running the program to the desired results should the program be running correctly. Since this can be a lengthy and somewhat tedious process, these errors are harder to spot and correct.

Do not panic if you get errors. Everyone does. What you need is experience in spotting them, and then fixing them. Once you've seen an error the first time you'll be able to fix it next.

.. index::
    single: IDE; Saving

.. tip::

    As you enter programs you may start looking around for a "Save" button to write the current file to the disk. There is probably no need for this, as IDEs tend to be setup to save as you type. This is the default for PyCharm, and can be turned on for VS Code. Obviously it can be set to your preference.

One way to learn some programming is simply to enter some programs, and run them\ [#Speccy]_. Gradually you come to understand what all the commands do. So let's start with three short programs, and try that. Remember that a program is just a text file. So you need to be able to create that file using your IDE. And you need to store the file *somewhere where you will be able to find it again*. That might seem obvious, but it often gets forgotten. Pay attention to where your IDE stores the file!

.. tip::
    You might find it easier at first to create the folder for your programming project, and even a file, using the usual operating system tools. The file can be created with a simple text editor, like Notepad. The folder can then be opened with the IDE.

First, let's meet some programs.

.. index:: Three Simple Programs

Three Programs
==============

Here are three programs. You should be able to see what they do just by reading them. If some detail isn't obvious at the moment, no need to worry. For the moment we are just interested in getting them to run.

Enter them, one at a time, in separate files, into your IDE\ [#copy]_. If you have syntax errors the IDE will probably spot them and highlight them in some way. How this looks depends on settings and colour schemes, but expect some sort of underlining as the IDE expresses its unhappiness. If they all look correct, you can then run them in whatever's the most convenient way. Remember the little green arrows in the two IDEs introduced before.

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

.. important::

    Indentation is important in Python. This refers to the amount of space at the start of each line. In these simple programs, there is only a little indentation, but it must be correct. So gthe first two lines **must** start in the left-most column, and all the following lines **must** be indented. If you don't copy this, it will be a syntax error.

If the programs fail to run and produce some useful output, take a close look to see that you have them exactly right. Notice how your IDE will add colours to the code; as you get used to this it will help you spot mistakes as you type. Some IDEs will also highlight errors in the code as you type, or make possibly helpful suggestions.

Remember that a *syntax* error is where there is a problem with the way the program is expressed, meaning that it cannot run. A *semantic* error, on the other hand, is where the program runs, but does not do what you want. The first is usually easy to spot, the second is not.

.. index::
    single: IDE; Customisation
    single: quotation marks

.. tip::

    You will see that some of the programs contain quotation marks, pairs of which have to match up. Some IDEs will insert a closing quote as soon as you enter an opening quote. This does save typing, but can be confusing at first. Of course, you can root around in the settings to turn the behaviour off.

Make sure you save the code somewhere, and that you know where this is! Ideally store your programs somewhere where you will always be able to find them.

.. index::
    single: first programs
    single: Programs; hello.py
    single: Programs; hello_name.py
    single: Programs; hello_age.py

These three programs are probably the first three that any new programmer creates. So what do these programs do?

``hello.py``
    ... is the traditional first program that anyone writes. It just prints a cheery greeting on the screen.
``hello_name.py``
    ... is the traditional second program. This time the program displays a prompt, the user enters their name, and a
    personalised cheery greeting is displayed. Behind the scenes, the user's name is encoded as binary, stored in the
    computer's memory, and then retrieved, but all this is invisible to the programmer.
``hello_age.py``
    ... displays a cheery greeting that includes the user's age, which is calculated. Again, values are entered, and will be encoded
    as binary. Python always takes ``input`` as a string of letters, so there is a small fix to show that the values entered are going to be
    integers, and will be used for a calculation. Again, a lot happens behind the scenes even in this small programmer, but
    Python is a high-level language, and the programmer doesn't need to worry about all this.

Before leaving these programs, make copies, and change a few things. The worst that can happen is that you change something and the program stops working. Spend time getting used to your development tools; this will save a lot of pain later on.

.. index::
    single: physical environment
    single: programmer, behaviour and habits of
    single: IDE; customisation
    single: IDE; settings
    single: IDE; colour schemes
    single: IDE; font size

Programming in a Good Place
===========================

Before carrying on to learn more, it really is worth taking some time to think about how you work best, and about which tools suit you best. You have started to work with an IDE. Maybe there were some things that were a bit annoying, or maybe you really don't like the colours it used for the programs. Or did you keep getting distracted? Or did your arms get tired with the typing?

There are two aspects to making sure you are programming in a good place. First, there are the software tools you use to create your programs, and second there is the question of the physical environment.

.. index::
    single: Programming; tools

Tools of the Trade
******************

You shouldn't be using tools just because you've been told to, or your friends do, or because you always have. You need to have the best tools for the job, and that's different for different people. If you have a choice of tools to use, get them all installed, and try each one. Maybe use the programs above. Enter and run those programs in different IDEs. See which IDE you prefer. There is no single choice that works for everyone.

A modern IDE is immensely powerful. And as a programmer you will spend most of your day looking at your IDE and working with it. So you should take time to learn how it works, and how to make it work for you. You probably only need a small fraction of what your IDE can do, but make sure you know what this small fraction is, and how to use it efficiently.

Modern IDEs are also extremely customisable. No-one uses an IDE with all its default settings. Take a look at the various colour schemes available, and pick one you like\ [#dark]_. Make the font bigger if you need to. Hide menus and tools you are not going to need, make those you always need available all the time. You will probably find that the IDE will allow you to create an online account to store settings so that you can sync them between your different computers. Seriously, take time to use the IDE, make it yours. You are going to be using it **a lot** over the next several years!

..index::
    single: Programming; craft

Programming is a *craft*. Craftspeople use tools, and they get the tools right.

.. index::
    single: Programming; physical environment
    single: programmer, behaviour and habits of

The Physical Side
*****************

And look around.

Over time, a programmer will learn about what makes the best environment for them when they work. They will change things so that they are working in the best place. Good employers will recognise this, and should encourage it.

There are probably two aspects to this, but they are connected. First there is the hardware - the PC, laptop, screen, and so on - and second there is the overall environment - heat, light, desks, ambience. Hardware even includes the keyboard and mouse. Environment covers furniture, noise, and more.

There is again no "one size fits all" here, but most programmers probably prefer to work from a laptop, which they carry with them everywhere. (This is even more common in these days of hybrid working). The laptop can be used wherever it is needed "on the road", or can be used in the office at a conventional desk. Usually, on a desk it will be hooked up to a second display for comfort and productivity. Docking stations can add ports and other connectivity.

Having multiple displays is very important. If you have never tried this, you should! This small change may not immediately occur to people, but having two (or even three) screens available can seriously improve productivity, and is healthier too as it keeps your eyes busy. And why are monitors always landscape, with the longer edges top and bottom? Have you tried a portrait monitor? It's a game-changer, especially for reaing long programs or documents.

.. hint::
    Getting the right setup is important. Think out of the box too. If you're going to work with long programs, how
    about having a second monitor in portrait orientation? That's another potential game-changer. Or if you're often on the road, how about a portable second monitor for the laptop? They can be no bigger than a tablet, and can usually be powered by the laptop.

Desktop PCs still have their place but, again, consider having more than one display. And that keyboard? Is it one you can happily type on all day? Are you good with where all the keys are? Is the mouse comfortable to use? Do you keep randomly hitting some key that has some annoying effect? If so, you can probably remap it.

.. index::
    single: coffee

And finally, think about the overall environment. A tidy desk is best. And a chair you can sit on for a while. Do you want somewhere to open books, or are you happy to prop up a Kindle, or read on one of your monitors? Natural light is ideal but, if not available, there should be plenty of light sources. Think about whether you work best with music playing, or without? Above all, make sure there is a ready supply of coffee to hand\ [#coffee]_!

.. important::

    Having said all that, it is also important to appreciate the need to take breaks away from a screen. This can sound a bit "Health and Safety Gone Mad", but there is a serious point to it.

Takeaways
=========

After this chapter you should:

* Be able to enter programs, run them, and see the output.
* Have familiarised yourself with your programming tools, and at least started to customise them to suit your own preferences.
* Have thought about the best physical environment for your programming work, and ideally arranged this.

Now we can move on to see how a program processes and stores values. After all, that's what computers are good at, and also if you think about it, what every program does!

.. [#KnR] It is said in *The C Programming Language* by Brian Kernighan and Dennis Richie, a book affectionately known as "K&R".
.. [#Speccy] Most programmers between the ages of, say, 50 and 60 learned programming this way, hacking away at programs on the home microcomputers of the 1980s. ZX Spectrum all the way.
.. [#copy] If you are looking at this as a web page, you will see that a handy button will appear when you hover the mouse over the program code. This allows you to copy the code, *but* you will learn more if you type it yourself.
.. [#dark] As long as it's a dark colour scheme. No-one uses light schemes. Seriously.
.. [#coffee] Other beverage choices are possible, but most programmers go with coffee. And not decaff.
