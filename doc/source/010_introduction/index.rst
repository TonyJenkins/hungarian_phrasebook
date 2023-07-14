==========
Greetings!
==========

This is a book about programming. Well, this is a book that is sort of about programming.

Let's start by considering what this book is, what it is not, and why it is like that.

.. only:: html

    This book is also available as a PDF. The content is the same. :download:`Get it here <../../build/latex/yetanotherpythonbook.pdf>`.

.. only:: latex

    This book is also available online. The content should be the same. Go here: `<https://www.tony-jenkins.org.uk>`_.

About this Book
===============

This is a book about the Python programming language. Sort of.

This is more a book that introduces the main ideas of programming, and uses Python as the language that illustrates the main ideas.

To be very clear from the outset:

.. important::

    You do not learn to program by reading a book.

Seriously. Programming is a skill, and it is a skill that takes many years to master properly. The purpose of this book is to put you in a position where you understand enough that you can start on that journey.

Suppose you wanted to learn to ride a bicycle, juggle, or repair lawnmowers. You would not expect to be able learn to do any of these things well just by reading a book. (And there are very few books teaching you how to do these things anyway, which is probably significant.) To take just the first - if you wanted to learn to juggle you would first try to get the basics. You might watch some YouTube videos, or get help from someone who already had the skill. Then you would practice, and practice some more. Eventually, you would get to the point where you felt you were a competent juggler.

Programming is like that. Every programmer is constantly learning. Even after 30 years or more experience, programmers are still learning. This book is aimed at getting you to the point that you can start this learning.

This chapter sets the scene for the book, and hopefully convinces you that you are in the right place.

Design Decisions
================

There are usually many ways to write a computer program. Some are just as good as others, but sometimes an experienced programmer will have some sort of instinct that one is best. Or it could just come down to experience. Likewise, there are many to write a book about computer programming. Let's start by going over the design decisions behind this book.

This book is the result of many years watching (and sometimes even helping) people learn to program. The key design ideas, in roughly their order of importance, are:

Dynamic
    Paper books (pbooks), in the tech world at least, are dead. Tech moves so fast that it is virtually impossible to produce a traditional pbook that covers current versions of tools and current ideas in methods. This book isn't actually a book in the traditional sense of what that means. It is a set of web pages, generated from a bunch of text files. The content can be changed in minutes, and a new version can be deployed in seconds. Pressing another button can cause a PDF or e-reader version to pop into existence.

Just Enough
    This book does not cover all the small details of a programming language. There is documentation for that. When a new programmer starts there is no need to worry about all those fiddly little details that only come into play now and again. So, some things are deliberately missed out (although there may be pointers to where the gory details can be found).

Pythonic
    The programming language used here is Python. Python is currently one of the most popular languages around, and is the only really sensible choice for a first language to learn. The aim, though, is to use Python as Python was intended. To be Pythonic, as it were. This means that at various times we will talk about Pythonic things that might not exist (or be as important) in other languages.

One Way
    An important aspect of the original design of Python was that there should always be one, and just one, way to do something. That has maybe slipped in recent versions, but this book will stick to presenting one way to do something. If there happen to be more, you'll find them later. There might again be pointers.

Free, as in Beer
    Finally, this book is free, as in beer. You are welcome to use it for anything you want to. The text files can be found on GitHub, and all the tools needed to build the HTML and PDF are free.

This book will also be, in places, somewhat opinionated. No apologies are made for this, because the opinions are correct.

Programming
===========

Above all, this book is about *programming*, and the things that programmers do. A popular image is that programming is a very solitary occupation, with a programmer involved in some sort of late night mortal combat, trying to bend a computer to their will. Well, it does feel like that sometimes, but more often programming is a social occupation, working with others to produce something cool. So this book will occasionally step away from the details of Python to go into **what programmers do**.

Let's be clear about this. Programmers use Google. They use StackOverflow. They wander across the office to ask a colleague to take a look at their code. They use version control tools. They chat on Slack or Teams. They explain programming problems to small plastic ducks\ [#duck]_. All of these, and there are more, make them more productive. While the details are probably beyond the scope of this book, it is so important to know they are there, and that they are basic parts of the way programmers work. Very often, when a new programmer sees a Senior Developer fix a problem all that Senior knew was what to Google. Really.

To put it another way, what experienced programmers have is, ah, *experience*. This means that they have seen most of the problems before, and know how to solve them. In the trade, this is called *abstraction* - the ability to take a solution to a problem you have seen before, recognise that a "new" problem is actually the same one, and map the solution over. This experience comes with time, and comes from working with other programmers. Another reason why programming is often a social process.

.. important::

    If you know experienced programmers, learn from them. You might have to buy them a coffee, but that will be a good investment in the long run.

Assumptions
===========

So, how to get this experience? To make sure that we are starting from a good place, this book will make some assumptions. Specifically, we want to concentrate on writing programs here. We don't want to be fighting the computer. We therefore need to be able to carry out some basic tasks that an PC user should be able to do.

.. note::

    We are *operating system agnostic* here. Python works just fine on any modern operating system, so we are not going to tie ourselves to anything. More on this later.

This book assumes that you have a PC or laptop available. It doesn't matter what operating system it uses (and we will not worry about OS issues much), and it does not have to be especially powerful. But you need to be able to use it. Specifically, we will assume that:

* You understand how files are organised.
* You can create a sensible structure of folders (directories) to store your files, and know why this is important.
* You can carry out basic file operations, such as renaming, deleting, and so on.
* You can find files if you have forgotten where they are stored.
* You are comfortable installing software, and have the permissions to do so.
* You have an Internet connection, so that you can download the software you need.
* You understand that backups are important, and have access to some solution that will keep your files safe!

It would also be good to assume that you have some experience of the *command line*. This is likely if you are using Linux, possible if you have a Mac, but unlikely if you have Windows. Some of the details will be covered later, just in case.

This needs to be set out because the ways in which we use PCs and laptops have changed hugely in the last few years. The arrival of PCs in the home has meant that to many people a computer is just an appliance. It's like a fridge, and you can use a fridge without any idea of how it actually works. This is fine as long as all you want to do on the PC is write a letter, read the news, or play a game. If you want to be able to program that computer to do something new, you need to understand something about how it works. Or, at this point, you need to be willing to learn about how it works.

YouTube is full of videos explaining these things if you need a refresher.

Programming Languages
=====================

To write a program, we need a programming language. There have been many programming languages over the years. Some have had their time and fallen into obscurity, others are just beginning to gain traction and users. Deep down, though, they are all basically the same. A programmer who learned, say `ALGOL <https://en.wikipedia.org/wiki/ALGOL>`_ in the 1970s could easily be working happily with `Java <https://en.wikipedia.org/wiki/Java_(programming_language)>`_ today, and also looking to upskill to `Golang <https://en.wikipedia.org/wiki/Go_(programming_language)>`_ in the next few months. Some languages have a habit of clinging on to life even when past their prime, with programmers always needed to support business-critical systems. Some languages, sadly, never really find their niche and just fade away.

This is not to say that all programming languages are equal. There are some fundamentally different designs out there. But the underlying concepts *are* basically the same, and those are the concepts that concern us here. Armed with a good knowledge of the basic ideas it should be possible to pick up any programming language, even the ones that haven't been designed yet.

.. note::

    If you like analogies, we could say that all cars are basically the same. But a small Kia is different to a mid-range Audi is different to a Bugatti. They all have their uses. Some are more popular than others. Some have falled into misuse. New ones are always interesting. Get the idea?

Many programming languages do have a sense of style and idiom. This relates to how the language is used (or how programs are expressed using it). There are also conventions that determine how programmers structure their code, and how they use the language in other ways. It is important to understand these, and to try to work within each languages's conventions. This is similar to learning any foreign language - it would be possible to translate, say, French into English word-for-word, and the result would be understandable, but would probably seem very strange. A much better translation could be achieved by understanding English, its idioms, and its use. That is why we bother to learn foreign languages!

.. important::

    This book will follow the standard conventions for Python, which are set out in a document called `PEP-8 <https://peps.python.org/pep-0008/>`_. Very different conventions would apply if we were using Java.

There are many surveys of the current popularity of programming languages\ [#lang]_. This is all a bit artificial, because some languages are more suited to certain applications, and some applications are more widespread than others. The top five languages in these surveys, though, are usually fairly consistent, although the order changes. **Alphabetically**, they are:

* C++
* C#
* Java
* JavaScript
* Python

All these languages are available free, and there are extensive free tools, tutorials, and other docs. Now, when picking a first language to use or learn, we can reason as follows.

#. JavaScript is tightly tied to the Web, and requires knowledge of HTML and CSS. It is also usually used with higher level frameworks, which change rapidly. For both these reasons it is not a good choice for a first language.
#. C# and Java are basically the same language, and share much with C++. All are object-oriented, and are good all-rounders. There are a lot of object-oriented concepts that need to be understood before they can be used effectively. For that reason alone, they are not a good choice.
#. Python is object-oriented but, unlike Java, can be used sensibly without objects. It is a scripting language, suitable for rapid development. It is possible to write useful programs using a small amount of code. It is therefore the best choice.

There has been much debate over the years over the first language to learn. Wars have probably been fought over less. But at the moment, Python is the best choice.

Python
******

The language used in this book is Python. Python is a well-established language, having been around for over 30 years now. It is very widely used in a wide range of applications. A solid all-rounder. As noted above, it is currently one of the most popular programming languages, and therefore one of the most in-demands skills.

Python has many features that make it the best choice for our first language.

It is multi-paradigm.
    Which means that it can be used in a bunch of different ways. This might not seem important, but contrast this with other languages that support only one way of working. In essence, it means we can start simple, and work up.
It is scripting language.
    Which means that programs are just plain text files containing a sequence of instructions. A tool called the *Python Interpreter* takes these instructions, and executes them. Simple.
It can be interactive.
    Which means that the Python Interpreter can be used as an interactive tool to try things out, check out ideas, and test programming snippets before using them for real.
It is relatively small.
    Which means that Python has a relatively small core, so we can hope to cover most of it. But it also has an architecture that allows it to be extended with external modules. Modules exist to do all sorts of cool stuff. It is massively extensible.
It has a simple straightforward syntax.
    Which means that it is usually obvious what a program does. Quite often simply reading a Python program out loud can explain what is going on.

Of course, it is not all good news. Python programs can be inefficient, and Python is not the best language if you want to develop something that will run lightning fast in an embedded system. But that's not the point, and it's not what Python is for.

Python is also intended to be fun. Its name is a nod to `Monty Python's Flying Circus <https://en.wikipedia.org/wiki/Monty_Python>`_. Many examples and tutorials draw from the Python canon. `PyPi <https://pypi.org/>`_, the standard repository of Python packages is sometimes affectionately called `The Cheese Shop <https://www.youtube.com/watch?v=Hz1JWzyvv8A>`_. You might notice the name of the GitHub repository where this book resides.

Python is completely free. And is also kind of cool.

Takeaways
=========

Every chapter of this book will end with a sort summary of where you should be now. After this section:

#. You should understand what this book is, and why it is like that.
#. You should have got hold of a suitable PC or laptop.
#. You should have the basic PC skills to manage files and folders.
#. You should understand why there are different programming languages.
#. You should know why the language we will use from now on is Python.

Right. Now to get this setup. We are starting slowly here. The plan is to head off any problems that might get in the way once we start the serious programming work.

.. [#duck] Seriously. It's called `Rubber Duck Debugging <https://en.wikipedia.org/wiki/Rubber_duck_debugging>`_ and is a very useful technique. It works with penguins, elephants, and bears too.
.. [#lang] Amusingly (or depressingly, depending on your point of view), these lists often include things that aren't programming languages, such as HTML, CSS, or SQL.
