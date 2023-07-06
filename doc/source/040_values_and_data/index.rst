===============
Values and Data
===============

At the most basic level every program does the same thing.

#. It reads some data.
#. It processes that data in some way.
#. (Usually) it writes the data back.

There are obviously many variations here. The data could be read from a file, or from a keyboard. It could be processed in many different ways. It could be written back to the same place, a different place, or just displayed on a screen or printed out. But all programs do basically the same thing.

* A word processor reads a file containing a document, allows the user to edit it, and then saves the new version.
* A game reads a file containing the user's profile and a level description, allows the user to play the game, and then stores the new saved state.
* A utility to store WiFi settings on a smartphone reads the connection information as the user types, uses it to test and make a connection, and then saves it to a file so that the phone can connect automatically next time.

All these store data, so this seems a good place to start. We already know that data is stored in a binary format, and that it can be on disk or in memory. It's time to see how Python does this.

Creating Values
===============

A data item needs a name so that it can be referenced. In Python, a new data item is created simply by giving a value to a name, like this:

.. sidebar:: Try It!

    You can copy the commands in this section and run them at your own Python interpreter. On the web, hover the pointer over the code, and a little button will appear.

.. code-block::

   >>> eggs = 3

This looks like a very simple line of code, which indeed it is. But, behind the scenes, several things have happened:

* Python is aware that there is a "thing" called ``eggs``, and has added this to its list of names (its "namespace").
* By looking at the value assigned to it, Python has determined that ``eggs`` is an integer.
* The value ``3`` has been stored in memory.
* An entry has been made in a lookup table to allow Python to find the current value of ``eggs``.

It works much like this. The next time we access the value of ``eggs``.=, maybe we just want to ``print`` it:

.. code-block::

    >>> print(eggs)

Python checks the namespace. It sees something called ``eggs`` there, so goes to the lookup table to see where this is in memory. Finally it accesses the memory location to (in this case) print the value out.

So, every time a new value is created, an entry is made in the lookup table. And every time that value is needed, the process above is used to extract it from memory.

.. note::

    This description is another that is deliberately not precise, but will hopefully give you an idea of what is going on.

Values and Types
================

The value stored in ``eggs`` above is an integer, a whole number. Python determines the type of the value by examining the value assigned to it. The type of the value determines a number of things, not least how much memory is needed to store it. A floating-point value (a number where the decimal part is important) is created like so:

.. code-block::

    >>> swallow_speed = 12.5

This value requires more memory to store the decimal part, but the rest works the same as before.

Boolean values (which are basically integers in disguise) work like this:

.. code-block::

    >>> brave = False
    >>> run_away = True

Finally, strings are sequences of characters. Usually they have some meaning, like a name, but they could contain anything, including encrypted text:

.. code-block::

    >>> name = 'Sir Robin'

.. hint::

    Strings have quotation marks around them. You can use single or double quotes, but it is best to stay consistent. Boolean values do *not* have quotes.

Python is a *dynamically typed* language, which means that the types of values are determined when they are first used. It also means that the type associated with a name can change, but this is usually very confusing, and is best avoided!

In summary, Python provides these four built in types. They are called the *primitive* types.

int
    An integer, a whole number. Positive or negative with, effectively, no upper limit.
float
    A number with a decimal part.
str
    A string of characters. Effectively any length.
bool
    A True or False value.

A built-in command called ``type`` can be used to find out what type is currently stored in a value. It will get some use in the next sections.

Investigating Integers
**********************

Integers are probably the most common data type. Some programming languages offer many different types for whole number values, the choice depending on the range needed, whether they can be negative, and the like. Python offers just the one:

.. code-block::

    >>> eggs = 3
    >>> type(eggs)
    <class 'int'>

Let's see what we can do with some ``int`` s.

Doing the Maths
---------------

Integers are numbers, and so all the usual mathematical operators are available. It is quite possible to use the Python interpreter as a handy calculator, which will also show the four mathematical operations. Here we have addition, subtraction, multiplication (the symbol is ``*``) and divison (``/``).

.. code-block::

    >>> 2 + 2
    4
    >>> 8 - 6
    2
    >>> 3 * 4
    12
    >>> 8 / 2
    4.0

.. important::

    Take a close look at the last operation above. ``4.0`` is a floating-point value. So if we divide an integer by another integer, the result is a floating-point number, even if the decimal part is zero. Hmm.

There are three different kinds of division. Above is what we might call "normal" division, where the result is am floating-point number. This is usually what is needed. It is possible to require that the result is an integer, effectively ignoring any decimal part:

.. code-block::

    >>> 8 // 2
    4
    >>> 7 // 2
    3

Obviously this sometimes "loses" something, but this is sometimes the result wanted. It is also possible to find the number that are "left over" after a division (called the "modulus"):

.. code-block::

    >>> 8 // 2
    0
    >>> 7 // 2
    1

.. hint::

    A very common use case for the modulus operator (``%``) is to deermine whether an integer value is odd or even. An even value "modulus 2" is 0, an odd value is 1.

.. admonition:: Use Case

    Suppose we were dividing eggs into boxes of six. We need to divide the total number of eggs we have by six, but a floating-pont answer would not be useful. We can't put 6.33 eggs in a box! So here we would require integer division, and we could use the modulus operator to find out how many eggs would be left over.

Finally, there is also an operator to raise a number to a power.

.. code-block::

    >>> 2 ** 4
    16

Precedence
----------

If there is more than one operator in an expression the usual mathemtical rules of precedence reply. You might remember them from maths courses as BEDMAS or BODMAS.

    | *B* rackets.
    | *E* xponents (powers).
    | *D* ivision.
    | *M* ultiplication.
    | *A* ddition.
    | *S* ubtraction.

This can sometimes give unexpected results to the unwary when the operators in an expression are not applied left-to-right, as in:

.. code-block::

    >>> 2 + 8 / 2
    6.0

The trick is to use brackets to change the order:

.. code-block::

    >>> (2 + 8) / 2
    5.0

In general, even when the "BEDMAS" order gives the result required it is a good idea to add brackets to clearly show the intended order.

Focus on Floats
***************

In some applications, integers are sufficient for numeric data, but in general we are interested in numbers that have a floating-point (decimal) part. Floating-point decimal numbers are tricky to represent accurately in binary in much the same way as some fractions (like one third) are impossible to represent as decimal numbers. As before, some programming languages offer many different data types for floating-point numbers, depending on the accuracy needed, but Python offers just the one:

.. code-block::

    >>> speed = 3.0
    >>> type(speed)
    <class 'float'>

.. important::

    See here that ``3.0`` is a floating-point value, even though the number after the decimal point is zero. ``3`` is an integer value representing the same amount, but they are different data types.

Since they are also numeric values, floating-point numbers behave in a very similar way to integers. Behind the scenes things are more complicated, as floating-point values are more complex to store accurately in binary, but happily that is mostly hidden. So all the usual mathematical operators work as before:

.. code-block::

    >>> 2.5 + 3.2
    5.7
    >>> 2.5 - 1.45
    1.05
    >>> 2.5 * 3.5
    8.75
    >>> 5.6 / 3.2
    1.7499999999999998

.. tip::

    Check that last result above. This is what you see when the result of an expression can't be represented exactly. The answer is, obviously, 1.75, but that value can't be represented precisely in binary. (If you try the same expression on your calculator, you will probably get 1.75). This can make working with floating-point values tricky!

Floating-point values can also be combined with integers, where this makes sense to do so. Arithmetic operations work as you'd expect. The type of the result is determined by the types of the values. So an integer added to an integer is another integer, while an integer added to a float is a float:

.. code-block::

    >>> 3 + 3
    6
    >>> 3 + 3.5
    6.5

The usual rules of the order of operators also apply here.

String Theory
*************

A string is a sequence of characters. Usually it represents something interesting like a name or an identity number, or some other data that has been input. Python has many useful features that allow strings to be manipulated.

.. sidebar:: Languages

    There are many programming languages, and many programmers would say they have a favourite. The thing is that languages have strengths and weaknesses, and some are more suited to different tasks than others. The trick is often to pick the most suitable language for a given task.

Strings are denoted by quotation marks. Single or double quotes are fine, and are equivalent. The only time the choice becomes important is if the string itself includes a string. So these are all fine:

.. code-block::

    >>> 'Sir Robin'
    'Sir Robin'
    >>> "King Arthur"
    'King Arthur'
    >>> "Galahad's Sword"
    "Galahad's Sword"
    >>>

The simplest way (and probably most common) way to process a string is to extract certain characters. Characters in the string are given index numbers, from left to right. So the first character is at index ``0``, and the last has an index of the length of the string less one. This last is a bit complicated, and is a common this to want, so the last character also has index ``-1``. Indexes work from either end of the string, like so:

.. code-block::

    >>> 'Sir Robin'[0]
    'S'
    >>> 'Sir Robin'[2]
    'r'
    >>> 'Sir Robin'[-1]
    'n'
    >>> 'Sir Robin'[-3]
    'b'

It is also possible to extract ranges of characters from a string, by providing two indexes, a start and an end. If one is missed off, it defaults to the end of the string.

.. code-block::

    >>> 'Sir Robin'[0:3]
    'Sir'
    >>> 'Sir Robin'[4:]
    'Robin'
    >>> 'Sir Robin'[:-1]
    'Sir Robi'

This "slicing" seems a simple idea, but is incredibly powerful and useful in many applications.  There are many, many, more built-in operations for string wrangling, which we will meet later on.

Using Variables
===============

The correct name for a value in a program is a *variable*. A variable has a type, and a value. Usually the value changes as the program runs. In Python a variable is created just by giving it a value:

.. code-block::

    >>> foo = 3

It is important to pick a name for the variable (correctly, that's called the *identifier*) that explains its purpose. The example above is meaningless, so it is much better to pick an identifier that explains what the value is:

.. code-block::

    >>> number_of_knights = 3

There is a balance to hit between names that are too long and names that are too short and cryptic. These are both bad choices, for reasons that should be obvious:

.. code-block::

    >>> nok = 3
    >>> the_number_of_knights_seeking_the_holy_grail = 3

A further downside to long identifiers is that errors in spelling them can lead to errors in programs that are very, very hard to find.

By convention, variable identifiers in Python are written in ``lower_snake_case``. With words separated by underscores, and everything in lower case.

.. important::

    Conventions like this are important. They may seem pointless now, but if your programs don't follow them you will confuse experienced programmers if you ask for help. In a work setting, if you didn't follow them you would just be told to go away and rewrite the code "properly"!

Input and Output
================

Armed with varaibles, there are two more things needed before we can write a useful program. First, we need to be able to take some values as *input*, and then we need to *output* the results. The simplest cases here are to take input that the user types on the keyboard, and to display the results on the screen. More realistic programs read or write files, or use graphical interfaces, but the simple "screen and keyboard" approach will do for now.

For the moment we will also assume that the user behaves as expected, and enters values that make sense in the current program. Obviously in real life users do not behave that way, but assuming they do will simplify the problem for now!

Getting Input
*************

To get some input from a user we need to display a helpful prompt, and then wait while they type. Usually, their input will be ended when they hit "Enter" or "Return". Once we have the input we need to store it away in a suitable variable. There is a lot going on here, but Python provides a single command to do the job.

The ``input`` command displays a prompt, and waits for the user to type. Once the user hits Enter, the value entered is *returned* and can be stored in a variable. The value is always read as a string, so sometimes there is a need to convert it to a required type. It is very unlikely that the user would be asked to enter a Boolean value, so the conversion is almost always to an integer or floating-point value. In these examples, see that entering the identifier of a variable at the Python prompt just displays the current value of that variable:

.. code-block::

    >>> name = input('What is your name? ')
    What is your name? Sir Robin
    >>> name
    'Sir Robin'

    >>> number_of_knights = int(input('How many knights follow the quest? '))
    How many knights follow the quest? 5
    >>> number_of_knights
    5

    >>> speed = float(input('Enter the average speed of an African Swallow: '))
    Enter the average speed of an African Swallow: 37.5
    >>> speed
    37.5

Take a close look at the brackets in the second example. There are two *functions* used - ``int`` and ``float`` - to convert the values. Your IDE should show an error if the brackets match incorrectly.

This will be enough, for now, to allow us to write programs that take input. In later episodes we will need to validate the input for its type, and possibly its value, but this will do for now.

Displaying Results
******************

The command to display a value on the screen is ``print``. It takes either a literal value, like this:

.. code-block::

    >>> print('Hello, World')
    Hello, World

Or it can take a variable identifier (notice there are no quote marks here):

    >>> message = 'Spam and Eggs'
    >>> print(message)
    Spam and Eggs

The ``print`` command can also print a collection of values. These are provided separated by commas, and by default are printed with spaces between.

    >>> print('There are', swallow_count, 'swallows.')
    There are 3 swallows.

There are other options, but as with ``input``, this will do for now.

.. tip::

    Those spaces can be annoying, and are not always wanted. The quick fix at this point is to add an optional "separator" to the ``print`` command, like this:

    .. code-block::

        >>> print('Spam', 'Eggs', 'Spam')
        Spam Eggs Spam
        >>> print('Spam', 'Eggs', 'Spam', sep='')
        SpamEggsSpam
