==============
Fun with Files
==============

Many pages ago we noted that all programs to basically the same thing. They take some data, they do some processing, and then they write out the changed data. But up to now all our programs have processed data that we have had a user enter from a keyboard. This is sometimes enough, but only works for very small amounts of data, or simple answers to prompts. In general we need to be able to handle data that is read from files.

This will mean that programs can handle a lot more data, but so long as we make sure we are writing DRY programs, the programs themselves will not get much longer or more complex. Some other issues will emergem, though, such as:

- A program may try to access a file that does not exist.
- A program may try to access a file that does exist, but for which there are no permissions (if it is owned by a different user, or requires some admin privilege, say).
- A program may be able to find and open a file, which then turns out to be in an unexpected format.
- A program may try to write a file to a location that requires permissions which are not available. Or which would overwrite an ecisting file.

This list looks a bit daunting, but the simple thing to remember is that any of these error cases will generate an exception. So the only real issue is identifying and trapping these in the same ways as we have done previously. This means that the three new programming ideas needed to work with files are:

#. How to find if a file exists.
#. How to read data from a file into some convenient data structure, like a string or list.
#. How to write data back to a file.

.. important::

    Programs should, as far as is possible, be *platform-independent*. They should run on any operating system. OSs differ in how they name files, and in how folders are added into file names - notably Windows uses ``\`` to separate folders in a hierarchy but Unix-like systems use ``/``.

    We will get round these issues here by just looking for files in the same folder (directory) as the program. There are plenty of useful functions in modules like ``os`` and ``sys`` for handling file names so as to make sure that code is portable.

The actual processing of the data should use the same ideas as we have seen before. So let's work through the basics of working with a file.

Finding Files
=============

This is a good opportunity to revise the two different approaches to checking for error conditions. The issue we need to overcome is that we are going to create a program that uses a file; we need to check whether that files exists, and is available for us to read. The two approaches are:

- To examine the files available, generate a list somehow, and see if the file we need is in that list. And then proceed if it looks to be there. *This is Look Before You Leap - LBYL*.
- Process the file regardless, and deal with any errors that arise if the file cannot be found. *This is EAFP: Easier to Ask Forgiveness than Permission*.

Remember that in Python, we prefer the second (EAFP), even though the first - LBYL - might seem to be the obvious way to go about it!

In this simple example, we will create a program that checks whether a file exists and is accessible in the current folder (that is, the same folder as contains the program). The program on its own won't be very useful, but it will illustrate some important points.

Following EAFP, the strategy will be simply to ``open`` the file we are interested in, and to see whether or not any errors occur when we do! In this simple example we'll have the user enter the file name, and we won't bother with any validation on that. As before, we could look up what error will happen if the file cannot be opened, or we could just try it and see. The command to open a file in a Python program is just:

.. code-block::

    >>> open('spam.txt')

Trying that with a file that we know *does not* exist will show what the exception we are looking for will be.

.. code-block::

    >>> open('spam.txt')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    FileNotFoundError: [Errno 2] No such file or directory: 'spam.txt'

To be safe we should probably check what happens if the file does exist. On Linux (or Mac), the ``touch`` command creates an empty file, so:

.. code-block::

    $ touch eggs.txt
    $ python3
    Python 3.10.12 (main, Jun 11 2023, 05:26:28) [GCC 11.4.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> open('eggs.txt')
    <_io.TextIOWrapper name='eggs.txt' mode='r' encoding='UTF-8'>

The output is maybe a little mysterious for now, but it is definitely not an error.

So let's craft a program. First, we assume that the file *does* exist (and that the program will crash if we try to open a file that does not exist):

.. literalinclude:: /../../src/10/file_exists.py
   :language: python
   :caption: ``file_exists.py``

It is obviously much neater to trap that exception thrown if the file cannot be opened. We know from the experiment above that it is a ``FileNotFoundError``, so the code is easy.

This simple example gives us the *boilerplate* code that will be needed every time we come to access a file. Remember they key idea, though: we assume that the file exists, and that all will be well, and pick up the pieces if this turns out not to be the case.

So, there are two, or arguably three things we need to be able to do with a file once we have assured ourselves that it can be opened. The first is that our program will *read* the contents. The second and third are very similar - the program might need to *write* a new version of the file, or it might *append* to the existing content.

.. important::

    In our spirit of keeping things simple, we are going to just deal with *text files* here. You can think of this as meaning files of data that make sense if you display them on the screen. Python can also handle *binary files* - such as MP3s or images - in a similar way to that described below. But remember that if you have a program that needs to open, say, music files, there is probably something in PyPi that will do a lot of the hard work for you.

Many programs obviously read a file, do something with the data, and then write the results. So we start with reading.

Reading Files
=============

Reading from a file is easy. First, the file is opened (along with the checks above), and then there are methods (functions) that can read the contents. The command to open a file is, ah, ``open``, as we have seen, and for reading we also specify the mode. So that the file can be referenced, the result of the ``open`` command is saved in a variable, which most programmers would call a *file pointer* or maybe *file reference*. So opening a file called ``spam.txt`` to read from it looks like this:

.. code-block::

    >>> f = open('spam.txt', 'r')

Reading (denoted by ``r``) is the default, so this can be left out, but it is good form to keep it in. There are then three usual options (remember that we are limiting ourselves to text files here). Assuming the file is opened as above, with a file pointer ``f``:

``f.read()``
    Will read the whole file into a string.
``d.readline()``
    Will read the next line of the file into a string.
``d.readlines()``
    Will read the whole file into a list of strings.

Once the file contents are in these variables, they can be processed using all the Python we have seen before.

Let's do a simple example.

.. topic:: Counting Lines

    Write a program that takes the name of a text file, and prints the number of lines in the file.

This program is straightforward when we remember that we can read the file into a list, which each element being one line, and that we can easily find the length of a list. A first attempt, where we assume the file exists could be:

.. literalinclude:: /../../src/10/word_count.py
   :language: python
   :caption: ``word_count.py``

Once we have finished with a file, it is good practice to explicitly ``close`` it. This is not strictly needed (it will be closed when the program exits), but it is tidy, and it indicates clearly that the program has finished with the file.

So:

.. literalinclude:: /../../src/10/word_count_2.py
   :language: python
   :emphasize-lines: 10
   :caption: ``word_count.py``

And the program can be completed by adding in the usual code to deal with a possibly missing file.

.. literalinclude:: /../../src/10/word_count_3.py
   :language: python
   :emphasize-lines: 7,15-16
   :caption: ``word_count.py``

That's done. There is probably one more small detail to mention.

Newlines
--------

If you look at the data that is read from a file, you will see that every string is terminated with ``\n``. This symbol represents the "new line" character at the end of each line. Obviously we don't see that character, but it is how the file marks the end of lines, and therefore why there is a line break when we view the file in an IDE, or Notepad.

.. note::

    As well as ``\n`` you may also see ``\t``, which represents a TAB character. There are others (they are called *escape sequences*, but these two are the most common.

So, suppose we want to count the number of characters in a file, as well as the lines. In that case we probably wouldn't count the end of line characters. Such a program is actually a very common "recipe", where we do something with every line of file. Example coming up!

Line-by-line
------------

Processing every line in a file is easy when we remember that the ``readlines`` method gives a list. We can just loop over that list with a good old ``for``. Let's use this technique to extend our line-counting program to count characters.

All we need to do is set a running counter to zero, and then add the length of each line in turn. To get the answer that most would consider correct, we also need to knock one off each line's length for the newline character\ [#lines]_.

We also need to do a little *refactor* here so that the list containing the file contents is stored in a variable. Deep breath ...

.. literalinclude:: /../../src/10/word_count_4.py
   :language: python
   :caption: ``word_count.py``

This structure, where a file is processed line-by-line is very common, so this code is worth studying.

Now we can read files, we can try writing!

Writing Files
=============

.. note::

    TODO

Takeaways
=========

.. note::

    TODO

.. [#lines] Alternatively, and quite cunningly, we could just take the complete length and then at the end, subtract the total number of lines.
