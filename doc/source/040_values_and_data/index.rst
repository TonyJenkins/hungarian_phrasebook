==================
Somewhere to Start
==================

The time has come to create a program, and also to understand how it works. So in this chapter we will look at the three building blocks we need:

#. Data.
#. Input.
#. Output.

We have actually seen all these in the programs in the previous chapter. so shopefully you have some idea of what is to come.

.. tip::

    Remember that a good way to learn to program is just to read programs, and understand them. This is easier than writing new programs, but an excellent place to start. It's the same with any language; people who learn a foreign language can usually read and understand it well before they are able to write an essay in it.

Right. At the most basic level every program does the same thing.

#. It takes some data.
#. It transforms that data in some way.
#. It does something with the new data.

There are obviously many variations here. The data could be read from a file, or from a keyboard. It could be processed in many different ways. It could be written back to the same place, a different place, or just displayed on a screen or printed out. But all programs do basically the same thing.

* A word processor reads a file containing a document, allows the user to edit it, and then saves the new version.
* A game reads a file containing the user's profile and a level description, allows the user to play the game, and then stores the new saved state.
* A utility to store WiFi settings on a smartphone reads the connection information as the user types, uses it to test and make a connection, and then saves it to a file so that the phone can connect automatically next time.

It really is that simple. If you edit a document using Word, you are just using a program to change the file that represents the document. If you play a race in Mario Kart you are really just using a program to change the file that represents your saved state in the game.

Any program needs to store data, so this seems a good place to start. We already know that data is stored in a binary format, and that it can be on disk or in memory. It's time to see how Python does this. Happily, as we will see, Python's high-level approach means that a lot of the details are hidden from us.

Creating Values
===============

If a program is going to store data, a programmer needs to be able to refer to that data. Every data item processed in a program is going to need a unique name, and the computer will then keep track of what value is currently associated with what name. So our simple model for how a program works becomes:

#. Read the data, giving each item a unique name.
#. Process or transform the data.
#. Output the data, using the names to make sure that everything ends up in the right place.

So, every data item needs a unique name so that it can be referenced. In Python, the simplesy way new data item is created is simply by giving a value to a name. So, let's create a data item called ``eggs`` and give it the value ``3``.

.. sidebar:: Try It!

    You can copy the commands in this section and run them at your own Python interpreter. On the web, hover the pointer over the code, and a little button will appear to allow you to copy the code.

    Remember that ``>>>`` represents the prompt of the interpreter, and should not be copied. In fact, on the web you shouldn't be abe to!

.. code-block::

   >>> eggs = 3

This looks like a very simple line of code, which indeed it is. But, behind the scenes, several things have happened:

* Python is aware that there is a "thing" called ``eggs``, and has added this to its list of known names (its "namespace").
* By looking at the value assigned to it, Python has determined that ``eggs`` is an integer.
* The value ``3`` has been stored at a particular location in memory, using the correct amount of memory for an integer.
* An entry has been made in a lookup table to allow Python to find the current value of ``eggs``. The table stores the name, and the memory location where the value can be found.

To give things their proper names, we have now created a *variable* with the *identifier* ``eggs`` that has been *assigned* the value ``3``. From now on we'll try to use the proper terms.

So, what happens the next time we access the value stored in the variable with identifier ``eggs``? Maybe we just want to ``print`` it:

.. code-block::

    >>> print(eggs)

Python checks the namespace. It sees something called ``eggs`` there, so goes to the lookup table to see where this is stored in memory. It then accesses the memory location to (in this case) print the value out.

So, every time a new value is created, an entry is made in the lookup table. And every time that value is needed, the process above is used to extract it from memory. Obviously all this happens "behind the scenes". In the olden days programmers had to do much of this work themselves, but high-level languages like Python remove all that pain. But it still pays to understand that this is happening.

.. note::

    This description is another that is deliberately not precise, but will hopefully give you an idea of what is going on.

    You need the ideas of creating a variable (value), and Python then maintaining a table of where each variable is currently held in memory.

Values and Types
================

The value stored in ``eggs`` above is an integer, a whole number. The type of a variable is important, as it determines what operations can be carried out on. We can use an integer in artihmetic, for example. It might not make sense to do arithmetic on other data types. Let's see.

Python determines the type of the variable by examining the value assigned to it. As well as the operations that are valid on it, the type of the value determines a number of things, not least how much memory is needed to store it. A floating-point value (a number where the decimal part is important) is created like so:

.. code-block::

    >>> swallow_speed = 12.5

This value requires more memory to store the decimal part, but the rest works the same as before. And all the details of how a floating-point number is stored inside the computer memory are, thankfully, hidden.

Boolean values work like this:

.. code-block::

    >>> brave = False
    >>> run_away = True

.. warning::

    Boolean values are basically integers in disguise. Be careful using them, and never ask a user to enter one.

Finally, strings are sequences of characters. Usually they have some meaning, like a name, but they could contain anything, including encrypted text:

.. code-block::

    >>> name = 'Sir Robin'

.. hint::

    Strings have quotation marks around them. You can use single or double quotes, but it is best to stay consistent\ [#quotes]_. Boolean values do *not* have quotes.

Python is a *dynamically typed* language, which means that the types of variables are determined when they are first used, inferred from the value given. It also means that the type associated with a name can change, but this is usually very confusing, and is best avoided!

In summary, Python provides these four built in types\ [#none]_. They are called the *primitive* types.

int
    An integer, a whole number. Positive or negative with, effectively, no upper limit.
float
    A number with a decimal part.
str
    A string of characters. Effectively any length.
bool
    A True or False value.

A built-in command called ``type`` can be used to find out what type is currently stored in a value. It will get some use in the next sections as we work at the interpreter, but it is rarely used in programs. As we will see in the next chapter, Python's philosophy is to run a program, and deal with any errors caused by types as they arise. So very rarely does a program need to check a variable's type.

Investigating Integers
**********************

Integers are probably the most common data type, so we'll start with those. Some programming languages offer many different types for whole number values, the choice depending on the range needed, whether they can be negative, and the like. Python keeps things simple and offers just the one\ [#oneway]_:

.. code-block::

    >>> eggs = 3
    >>> type(eggs)
    <class 'int'>

Let's see what we can do with some ``int`` s.

Doing the Maths
---------------

Integers are numbers, and the most common uses fo them obviously involve all the things we do with numbers. All the usual arithmetic operators are available. It is quite possible to use the Python interpreter as a handy calculator, which will also show the four mathematical operations. Here we have addition, subtraction, multiplication (the symbol is ``*``) and divison (``/``).

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

    Take a close look at the last operation above. ``4.0`` is a floating-point value. So if we divide an integer by another integer, the result is a floating-point number, even if the decimal part is zero. Why so? Because *in general* the result of dividing two integers will have a floating-point part, so it makes sense to always return a ``float`` as the result.

This all looks straightforwarde, but there is one detail to cover. There are three different kinds of division. Above is what we might call "normal" division, where the result is a floating-point number. This is usually what is needed, so it is what happens by default. However, sometimes *integer division* is needed. So, it is possible to require that the result is an integer, effectively ignoring any decimal part:

.. code-block::

    >>> 8 // 2
    4
    >>> 7 // 2
    3

Obviously this sometimes "loses" something, but this is sometimes the result wanted. As something is lost, it is also possible to find the number that are "left over" after a division (called the "modulus"):

.. code-block::

    >>> 8 // 2
    0
    >>> 7 // 2
    1

.. hint::

    A very common use case for the modulus operator (``%``) is to deermine whether an integer value is odd or even. An even value "modulus 2" is 0, an odd value is 1.

.. admonition:: Use Case

    Suppose we were dividing eggs into boxes of six. We need to divide the total number of eggs we have by six, but a floating-pont answer would not be useful. We can't put 6.33 eggs in a box! So here we would require integer division to tell us how many boxes will be full, and we could use the modulus operator to find out how many eggs would be left over.

Finally, there is also an operator to raise a number to a power.

.. code-block::

    >>> 2 ** 4
    16

There are many other mathematical operators, useful in scientific applications. But these are not included in strandard Python. It is easy to make them available, though, as we will see later.

Precedence
----------

These operators can be chained together to make more complex *expressions*. For example:

.. code-block::

    >>> 2 + 2 - 3
    1

In expressions like this the question arises of what order the operators are applied. In the above example it makes no difference to the result, but in an expression like:

.. code-block::

    >>> 2 + 2 * 3
    8

the order matters. You can probbly work out that in this expression the multiplication has been applied before the addition. How so?

The rule is that if there is more than one operator in an expression the usual mathematical rules of precedence reply. You might remember them from maths courses, where they are usually remembered as as *BEDMAS* or *BODMAS*.

    | *B* rackets.
    | *E* xponents (powers).
    | *D* ivision.
    | *M* ultiplication.
    | *A* ddition.
    | *S* ubtraction.

This explains why the multiplicattion happened first above; it has a higher precedence. This can sometimes give unexpected results to the unwary when the operators in an expression are not applied left-to-right, as in:

.. code-block::

    >>> 2 + 8 / 2
    6.0

Here division happens first, and this also means that the result is a ``float``. The trick is to use brackets to change the order. So if left-to-right was needed hwre we could write:

.. code-block::

    >>> (2 + 8) / 2
    5.0

In general, even when the *BEDMAS* order gives the result required it is a good idea to add brackets to clearly show the intended order. So our first example here is best written like this, even though the brackets actually have no effect.

.. code-block::

    >>> 2 + (8 / 2)
    6.0

This is a small detail, and Python probably does what you would expect, but it's always worth checking if the result of an expression isn't quite what you expect.

More Operators
--------------

As well as the arithmetic operators, there are a few that get commonly used. They are shorthands for common needs. For example, suppose we want to add one to the value of variable. We could program like so:

.. code-block::

    >>> eggs = 3
    >>> print(eggs)
    3
    >>> eggs = eggs + 1
    >>> print(eggs)
    4

This might seem odd at first, but the thing to remember is that the right-hand side is evaluated first, and the result is assigned to the variable on the left.

.. tip::

    A common source of confusion is the use of ``=`` in expressions like this, which is different to the way that it is usually used in maths. This operation is called *assignment*, and some languages use a different symbol for it. But Python sticks with one ``=`` for assignment.

    Assignment is different to *equality*. See later for that.

This operation (called *incrementing*) is so common that there is a shorthand:

.. code-block::

    >>> eggs = 3
    >>> print(eggs)
    3
    >>> eggs += 1
    >>> print(eggs)
    4

This increments the valure by 1, but any value can go there. So we could *decrement* a value by, say, 2:

.. code-block::

    >>> eggs = 3
    >>> print(eggs)
    3
    >>> eggs -= 2
    >>> print(eggs)
    1

Multiplying and dividing also work like this, but are probably less common. Here are two examples. See again that the division produces a ``float``.

.. code-block::

    >>> eggs = 3
    >>> eggs *= 2
    >>> print(eggs)
    6
    >>> eggs /= 3
    >>> print(eggs)
    2.0

Focus on Floats
***************

In some applications, integers are sufficient for numeric data, but in general we are interested in numbers that have a floating-point (decimal) part. This is especially true in scientific applications, but also true in simpler problems that involve working out, for example, averages.

Floating-point decimal numbers are tricky to represent accurately in binary in much the same way as some fractions (like one third) are impossible to represent as decimal numbers. As before, some programming languages offer many different data types for floating-point numbers, depending on the accuracy needed, but Python offers just the one:

.. code-block::

    >>> speed = 3.0
    >>> type(speed)
    <class 'float'>

.. important::

    See here that ``3.0`` is a floating-point value, even though the number after the decimal point is zero. ``3`` is an integer value representing the same amount, but they are different data types.

    .. code-block::

        >>> european_speed = 3.0
        >>> type(speed)
        <class 'float'>
        >>> african_speed = 3
        >>> type(speed)
        <class 'int'>

    A slightly interesting question is whether these two values are equal. What do you think? We'll check later.

Since they are also numeric values, floating-point numbers behave in a very similar way to integers. Behind the scenes things are more complicated, as floating-point values are more complex to store accurately in binary, but happily that is mostly hidden. So all the usual mathematical operators work as before:

.. code-block::

    >>> 2.5 + 3.2
    5.7
    >>> 2.5 - 1.45
    1.05
    >>> 2.5 * 3.5
    8.75
    >>> 3.5 ** 2
    12.25
    >>> 5.6 / 3.2
    1.7499999999999998

.. tip::

    Check that last result above. This is what you see when the result of an expression can't be represented exactly. The answer is, obviously, 1.75, but that value can't be represented precisely in binary. (If you try the same expression on your calculator, you will probably get 1.75 because the calculator will do some rounding). This can make working with floating-point values tricky!

Floating-point values can also be combined with integers, where this makes sense to do so. They are both numbers, after all. Arithmetic operations work as you'd expect. The type of the result is determined by the types of the values. So an integer added to an integer is another integer, while an integer added to a float is a float:

.. code-block::

    >>> 3 + 3
    6
    >>> 3 + 3.5
    6.5

This is what you'd expect as any other result would lose the decimal part.

The usual rules of the order of operators also apply here.

Conversions
-----------

Since ``int`` and ``float`` values are both numeric it is useful to be able to convert between them. Converting a floating-point value to an integer will lose something, of course, but sometimes that doesn't matter. An integer is easily converted to a floating-point, with all that really changes being the internal representation.

Conversions can be done just using the name of the required types. Like this:

.. code-block::

    >>> speed = 3
    >>> speed_float = float(speed)
    >>> print(speed_float)
    3.0
    >>> type(speed_float)
    <class 'float'>
    >>> speed_float = 3.5
    >>> speed = int(speed_float)
    >>> print(speed)
    3

This code creates and integer, and then converts it to a ``float`` (see the ``.0``). This floating-point value is than changed, and the value is then converted back to an ``int``. This loses the decimal part, effectively rounding down.

.. tip::

    A quick hack to convert an integer to a float goes like this. You might see it in some example code and wonder what's going on.

    .. code-block::

        >>> speed = 3
        >>> new_speed = speed * 1.0
        type(new_speed)
        <class 'float'>

    Multiplying by ``1.0`` (a ``float``) gives a ``float`` as the result.

String Theory
*************

A string is a sequence of characters. Usually it represents something interesting like a name or an identity number, or some other data that has been input by the user or read from a file. Python has many useful features that allow strings to be manipulated, and this is often quoted as a strength of the language. Python is very well suited for any application that involves much processing of strings.

.. sidebar:: Languages

    There are many programming languages, and many programmers would say they have a favourite. The thing is that languages have strengths and weaknesses, and some are more suited to different tasks than others. The trick is often to pick the most suitable language for a given task.

Strings are denoted by quotation marks. Single ``'`` or double quotes ``"`` are fine, and are equivalent (but pairs must match). The only time the choice becomes important is if the string itself includes a quotation mark. So these are all fine:

.. code-block::

    >>> 'Sir Robin'
    'Sir Robin'
    >>> "King Arthur"
    'King Arthur'
    >>> "Galahad's Sword"
    "Galahad's Sword"

.. tip::

    If you type a value at the Python interpreter it will just print (echo) the value back, like this.

The simplest way (and probably most common) way to process a string is to extract certain characters. Characters in the string are given index numbers, from left to right. So the first character is at index ``0``, the second at index ``1``, and the last has an index of the length of the string less one [#zero]_.

This last is a bit complicated, and it is surprisingly common to want to find the final character of a string, so the last character also has index ``-1``. Indexes work from either end of the string, like so:

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

Arithmetic can also work for string, where it makes sense. It makes sense to add two strings:

.. code-block::

    >>> 'Eggs ' + 'Spam'
    'Eggs Spam'

but it makes no sense to subtract one string from another. Similarly, it makes no sense to multiply or divide strings, but it *does* make sense to multiply a string by an integer. See what it does:

.. code-block::

    >>> 'Spam! ' * 4
    'Spam! Spam! Spam! Spam! '

We will return to strings later. But, just one last time, handling strings like this is one of the main strengths of Python. So it will ge tthe attention it deserves later on.

Boolean News
************

.. index::
    Booleans; basics

A Boolean value is one that is either ``True`` or ``False``. These values have been :ref:`discussed before <020_important_ideas/index:true and false>` because they are so fundamental. A value of this type is created in the usual way:

.. code-block::

    >>> brave_sir_robin = False
    >>> type(brave_sir_robin)
    <class 'bool'>

Arithmetic operations make no sense with Boolean values but logic operations clearly do. Check :ref:`back here <truth-tables>` for a reminder of these.

First ``not`` takes one Boolean and "flips" it, so True becomes ``False``, and ``False`` becomes ``True``.

.. code-block::

    >>> brave_sir_robin = False
    >>> run_away = not brave_sir_robin
    >>> run_away
    True

This will seem rather abstract at the moment, but we will use this a lot later on! The other two operators, ``and`` and ``or`` combine two values as expected.

.. code-block::

    >>> eggs = True
    >>> spam = False
    >>> eggs and spam
    False
    >>> eggs or spam
    True
    >>> spam = True
    >>> eggs and spam
    True

The use of Booleans is maybe not obvious at the moment, but they will be crucial later when we need to control the order in which statements are executed. Before that, let's see how values can be combined and compared into *Boolean Expressions*.

Boolean Expressions
-------------------

A Boolean variable holds either the value ``True`` or ``False``. Similarly, a *Boolean Expression* is an expression that is either ``True`` or ``False``. As with the truth of some statements we met before, some expressions are self-evidently ``True``:

.. code-block::

    >>> 1 == 1
    True

.. important::

    Heads up! We have used the single equals sign before, for value *assignment*. Two equals signs, as above, is used for *comparison*. So this expression is testing, ah, whether ``1`` equals ``1``, which obviously it does.

More usefully, we can test whether a variable holds a certain value:

.. code-block::

    >>> eggs = 6
    >>> eggs == 6
    True

Boolean operators allow for comparing values like this. Look again at the overloading of what an equals sign does! Here are the more common ones:

======== =====================          ============ ==============
Operator Meaning                        True Example False Example
======== =====================          ============ ==============
``==``   Is equal to                    1 == 1       3 == 2
``!=``   Not equal to                   1 != 0       1 != 1
``>``    Greater than                   3 > 1        1 > 0
``<``    Less than                      1 < 3        0 < 2
``>=``   Greater or equal to            2 >= 1       2 >= 3
``<=``   Less than or equal to          1 <= 1       2 <- 0
======== =====================          ============ ==============

These examples all use integers. The same operators will work with floating-point numbers, in the obvious way. Integers and floating-point numbers can be compared, but care is needed because of the difficulty of storing floating-point values exactly.

.. tip::

    In practice, avoid using ``==`` with floating-point values. The results are not always what you would expect because sometimes storing the value loses some precision.

We did wonder whether ``1`` (the integer) was equal to ``1.0`` (the floating-point). Turns out they are:

.. code-block::

    >>> 1 == 1.0
    True

A similar experiment will also reveal that, just maybe, Booleans are integers in disguise!\ [#bools]_

.. code-block::

    >>> 1 == True
    True
    >>> 0 == False
    True

And finally, comparison operators also work with strings. The meaning of "less than" and friends is based on the internal (numeric) way strings are stored, but is effectively alphabetical.

These operators can be combined with the Boolean operators to give complex expressions. Suppose we were interested in checking that a number was between 0 and 100 inclusive. That involves three operators:

.. code-block::

    >>> mark = 65
    >>> mark >= 0 and mark <= 100
    True
    >>> mark = 150
    >>> mark >= 0 and mark <= 100
    False

Building up expressions like this will become very important later on.

A final operator is worth a mention here. The ``in`` operator gives a Boolean value depending on whether or not one value is contain inside another. This is often used with strings:

.. code-block::

    >>> 's' in 'spam'
    True
    >>> 's' in 'eggs'
    True
    >>> 'spam' in 'fritters'
    False

This is really just a shorthand for a whole bunch of ``and`` tests together, but it can be useful. It also has the happy side-effect of making code more readable.

Now, let's try and formalise what this chapter has discussed.

Values and Variables
====================

To call it what it should be called, a value in a program is a *variable*. A variable has a type, and a value. Usually the value changes as the program runs. In Python a variable is created just by giving it a value:

.. code-block::

    >>> foo = 3

This creates a variable named ``foo`` with the value ``3`` . As we have seen before ``foo`` is given a type of ``int``, which is inferred from the initial value.

.. tip::

    Remember that ``3`` is an integer but, ``3.0`` is a floating-point. And if it comes to that ``'3'`` is the string that represents the digit three.

It is important to pick a name for the variable (correctly, this is called its *identifier*) that describes its purpose. The example above is meaningless, so it is much better to pick an identifier that explains what the value is:

.. code-block::

    >>> number_of_knights = 3

So now we can see that this value is presumably going to be used to store the number of knights that have done something, or otherwise become interesting in some way.

Meaningful identifiers are good. But there is a balance to hit between names that are too long and names that are too short and cryptic. These are both bad choices, for reasons that should be obvious:

.. code-block::

    >>> nok = 3
    >>> the_number_of_knights_seeking_the_holy_grail = 3

A further downside to long identifiers is that errors in spelling them can lead to errors in programs that are very, very hard to find\ [#spelling]_.

.. index:: Conventions; variable identifiers

By convention, variable identifiers in Python are written in ``lower_snake_case``. With words separated by underscores, and everything in lower case. Programs in this book will stick with this convention, as should you.

.. important::

    Conventions like this are important. They may seem pointless now, but if your programs don't follow them you will confuse experienced programmers if you ask for help. In a work setting, if you didn't follow them you would just be told to go away and rewrite the code "properly"!

    The thing to remember is that most programs are developed and maintained by teams. It makes a lot of sense if all the members of the team use conventions like this to ensure that their code is consistent and understandable.

.. index:: Conventions; constant identifiers

Another example of a convention is when a program needs to handle a *constant* value. This is a variable that will be used in the program, but the value will always be the same. A variable that will not vary, if you like. By convention, the identifiers of these values are witten in ``UPPER_SNAKE_CASE``. This is irrelevant to Python, but very useful to someone reading a program. So when a programmer sees:

.. code-block::

    >>> KNIGHTS_IN_HORSE = 4

It is clear that this is a value that is used in the program, but which will never change.

.. important::

    This might seem a bit odd, but the idea is to define the constant value in one place, and then potentially use it in many places. If it needs to be changed, it changes in just the definition, so is just changed the once.

Using constants like this also improves the readability of programs. It is oftem said that programs are read much more often than they are written!

Input and Output
================

Armed with variables, there are two more things needed before we can write a useful program. First, we need to be able to take some values as *input*, and then we need to *output* the results. The simplest cases here are to take input that the user types on the keyboard, and to display the results on the screen. More realistic programs read or write files, or use graphical interfaces, but the simple "screen and keyboard" approach will do for now.

For the moment we will also assume that the user behaves as expected, and enters values that make sense in the current program. Obviously in real life users do not behave that way, but assuming they do will simplify the problem for now!

Getting Input
*************

.. index::
    input statement
    Statements; input

To get some input from a user we need to display a helpful prompt, and then wait while they type. Usually, their input will be ended when they hit "Enter" or "Return". Once we have the input we need to store it away in a suitable variable. There is a lot going on here, but Python provides a single command to do the job.

The ``input`` command displays a prompt, and waits for the user to type. Once the user hits Enter, the value entered is *returned* and can be stored in a variable. The value is always returned as a string, so sometimes there is a need to convert it to a required type. It is very unlikely that the user would be asked to enter a Boolean value, so the conversion is almost always to an integer or floating-point value.

We briefly met the way to convert values between types earlier in this chapter. In these examples, remember that entering the identifier of a variable at the Python prompt just displays the current value of that variable:

.. index::
    Input; reading a string
    Input; reading an integer
    Input; reading a float
    input statement

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

Take a close look at the brackets in the second and third examples. There are two *functions* used - ``int`` and ``float`` - to convert the values. The brackets need to match up, as shown. Your IDE should show an error if the brackets match incorrectly.

This will be enough, for now, to allow us to write programs that take input. In later episodes we will need to validate the input for its type, and possibly its value, but this will do for now. Specifically, in the next chapter we will see how to cope if the user enters values of the wrong type, or at least data that cannot be converted to the correct type.

Displaying Results
******************

.. index::
    Statements; print
    print statement

The command to display a value on the screen is ``print``. We saw it earlier, but passed over it. It takes either a literal value, like this:

.. code-block::

    >>> print('Hello, World')
    Hello, World

Or it can take a variable identifier (notice there are no quote marks in the ``print`` here):

    >>> message = 'Spam and Eggs'
    >>> print(message)
    Spam and Eggs

The ``print`` command can also print a collection of values. The easiest way to do this is to make sure they are provided separated by commas, and by default they are printed with spaces between.

    >>> swallow_count = 3
    >>> print('There are', swallow_count, 'swallows.')
    There are 3 swallows.

There are other options, but as with ``input``, this will do for now. Keep it simple!

.. tip::

    Those spaces can be annoying, and are not always wanted. The quick fix at this point is to add an optional "separator" to the ``print`` command, like this:

    .. code-block::

        >>> print('Spam', 'Eggs', 'Spam')
        Spam Eggs Spam
        >>> print('Spam', 'Eggs', 'Spam', sep='')
        SpamEggsSpam

Takeaways
=========

There is a lot in this (rather long) chapter. But programming really is all about reading some values, storing them, processing them, and then making the results available. By now you should:

#. Understand that values have different *types*. And know which basic (*primitive*) types Python provides.
#. Be able to create values at the Python Interpreter, and carry out operation on them.
#. Know how to prompt a user to enter some values, and how to convert that to a required type.
#. Know how to display results on the screen.

We can actually write some reasonably useful programs now. The main gap is how to do different things depending on what the user enters. We'll look at that in a while, but first we'll think about what to do if the user doesn't behave as expected. Users are like that ...

.. [#quotes] The style in this book is to use single quotes unless double-quotes are essential, for example if the string itself contains single quotes. You could copy that, or go your own way. Just be consistent.
.. [#none] This is not true. Sorry. There is another type, ``NoneType``. This means that a variable exists, but has no value, and therefore no type. We'll need it later, so just hold the thought for now.
.. [#oneway] As we know, Python is intended to have one, and just one, way to do anything. So why have a whole bunch of different types for whole numbers, when one will do? Looking at you, Java.
.. [#zero] Computer Scientists start counting at zero.
.. [#spelling] Although obviously your IDE should quickly flag up such spelling issues.
.. [#bools] Which is fine and, if you think about it, the obvious way of doing it!
