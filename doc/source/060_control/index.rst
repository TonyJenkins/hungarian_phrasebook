==================
Staying in Control
==================

Previously we have looked at *exceptions* and how they can be used to catch some error situations.

These have been errors that mean that Python cannot carry on because it makes no sense to process the values it is given. But what about the case where the values do make sense (in that they are the correct type), but are invalid for some other reason.

.. important::

    Remember that the Python interpreter has no concept of what the data it is processing represents. It just sees a bunch of numbers, strings, and so on. It is the programmer that understands what these mean, and knows how to determine if they are invalid. A programmer might call a variable ``age``, but the interpreter just sees a number. It has no idea that a negative value (or a value over 130 for that matter) is invalid.

Let's see how to deal with these errors. We might say that we are dealing with values that are *legal*, but invalid. We'll start with a simple example, and then look at some more complex ones.

Values in Range
===============

Remember the example of allocating students to buses. There was an error when the capacity of a bus was entered as ``0`` (it provoked a ``ZeroDivisionError``), but what about if ``-10`` had been entered? This is also clearly nonsense but the Python interpreter (which has no knowledge of buses) would happily carry on, producing potentially confusing results.

.. code-block::

    >>> students = 100
    >>> bus_capacity = -10
    >>> buses_needed = students // bus_capacity
    >>> buses_needed
    -10

To stop this we need to apply a small amount of logic to stop the calculation if the values entered are outside the known possible range. Usually, but not always, there will be an upper and a lower range. Let's jump in and fix the program so that the number of students has to be greater then 1. For clarity, we'll leave off the code that handled the exceptions for the moment, and go back to the bus size being set as a constant.

.. literalinclude:: /../../src/06/school_bus.py
   :language: python
   :emphasize-lines: 9
   :caption: ``school_bus.py``

The program is now providing a *condition*, and showing that some statements should be executed only if the condition turns out to be ``True``. The statements affected by this are *indented across*. So now if an incorrect value was entered the program would produce no output at all.

This is fine, but as it stands the user, looking at a program generating no output at all, might be a little baffled about what's going on. It would be better to provide them with some sort of useful error message. Or we could point them in the direction of how to use the program properly. To do this, we need to say what should happen if the condition is ``False``. It looks like this:

.. literalinclude:: /../../src/06/school_bus_else.py
   :language: python
   :emphasize-lines: 15-16
   :caption: ``school_bus.py``

The ``else`` states what happens when the condition at the ``if`` is ``False``. It is indented so that it is directly below its matching ``if``, so there is no need for the condition to be repeated.

.. important::

    This works because a Boolean condition is always one of ``True`` or ``False``. The condition in a statement like this can be anything that evaluates to a Boolean value.

The Boolean condition, being ``True`` or ``False`` (and having no other possible values) means that one of the ``if`` or ``else`` will always be executed, but never, of course, both.

That's enough for simple cases. Before looking at more elaborate ones, let's consider what's going on here.

Flow of Control
===============

The example above introduced a *conditional statement*. This is a statement that allows us to control the *flow of execution* in a program. Unless we specify otherwise, a program will flow from the top to the bottom, with the interpreter executing each statement in order. This is rarely what is needed, because we want to handle errors, deal with different user input, and so on.

.. tip::

    A *Conditional Statement* in a programming language is often referred to as the **If Statement**, just because of the word that introduces it in most languages. Either term is fine.

A conditional statement allows a programmer to mark that some statements should be executed only if some condition is true. Optionally, there may also be statements that are an alternative, to be executed only of the same condition is falase. Since any Boolean statement is either true or false, one or the other sets of statements will always be executed.

.. important::

    There does not need to be an alternative. So, in Python, the ``else`` part is optional.

.. tip::

    If you think about it, it is always possible to write a conditional statement in two ways, with true and false either way round. It rarely matters, but the best plan is always to pick the one that gives the most natural-looing code.

Python indicates which statements are affected by a control statement using indentation. The statements affected are all indented by a certain number of spaces, directly under the control ststement. When statements are "un-indented" they are no longer affected. Indentation also shows which ``else`` matches which ``if`` - the ``else`` is indented so that it is directly below the corresponding ``if``.

So here the first ``print`` is affected by (or "inside") the ``if``, but the second isn't:

.. code-block::

    if number == 1:
        print('Inside the if!')
    print('Outside the if!')

And here, the ``else`` is aligned with its ``if``:

.. code-block::

    if number == 1:
        print('Inside the if!')
    else:
        print('Inside the else!')

This alignment is important, because there can be a conditional statement inside another, liks so:

.. code-block::

    if number == 1:
        print('Inside the if!')

        if another_number == 2:
            print('Inside both the ifs!')
    else:
        print('Belongs to the first if!')

Spaces are usually used for indentation. TAB characters can be used\ [#tabs]_, but most IDEs will silently turn them into spaces. Any number of spaces can be used, but the PEP-8 standard calls for 4, and this is what most IDEs will do.

More Choices
************

The examples so far have allowed for two possibilities, based around a single condition. Sometimes this is all that is needed, like when a user enters a value that needs to be tested for a range, but in others it is not enough. Maybe we need to test a value, and carry out different actions depending on several possibilities. Here's an example:

.. topic:: Exam Grades

    A student takes an exam, and gets a mark on a scale of 0 to 100. The pass mark is 40. Any mark of 70 or over is recorded as a *Distinction*. A program needs to read the exam mark and print the corresponding result - *Pass*, *Fail*, *Distinction*.

So here we need to test whether the grade and test it twice. This could be done several ways, but the neatest way is probably to check for a Distinction, and then for a Pass, like this:

.. index:: single: Programs; exam_result.py
.. literalinclude:: /../../src/06/exam_result_1.py
   :language: python
   :caption: ``exam_result.py``

Three things to notice about the code here:

* ``elif`` allows for other choices to be tested. The complete statement will execute the first condition that turns out to be true.
* ``else`` serves as a "catch all" if not of the tested conditions are true.
* The final condition can be a catch-all because if the mark is not a Distiction or a Pass it *must* be a Fail, so there is no need for an explicit check.

And also:

* The string used for the inout prompt includes a single quote (an apostrophe), so the string itself is in double quotes.
* There are be any number of ``elif`` lines, but the order matters in that the first ``True`` is executed (all the others are passed over).
* There does not have to be a catch-all ``else``\ [#else]_.

Nesting
*******

As it stands, the exam result program is fine, but if we look back at the earlier programs in this chapter we might reflect that there is no attempt to check that the mark entered is valid! We should surely check that it is between 0 and 100, and provide an error if not. There are two ways to do this. One would be to add the checks to the existing tests, but that might obscure what as going on. And, anyway, we have most of what we need from the earlier program\ [#abstract]_ so we might as well reuse it.

The trick will be to put one conditional inside another. This is usually called *nesting*, and is where the indentation will really come in handy to show what's going on. Here it is:

.. index:: single: Programs; exam_result.py
.. literalinclude:: /../../src/06/exam_result_2.py
   :language: python
   :caption: ``exam_result.py``

As before, the first test could be written several ways. It all comes down to what "feels" best. Here we have used the way that is closest to how the test would be said ("The mark must be greater than or equal to zero and less than or equal to 100.") Notice how the indentation clearly shows which ``else`` belongs with which ``if``.

.. note::

    If you are typing along, your IDE might have taken exception to the first ``if`` line, and might be prompting you to rewrite it. This is because Python provides a shorthand, so this:

    .. code-block::

        if mark >= 0 and mark <= 100:

    can be shortened to:

    .. code-block::

        if 0 <= mark <= 100:

    Which you use going forward is up to you.

When Not to Test
****************

Finally, there is one remaining source of errors in this program. What happens if the user enters something other than an integer? If you try this you will see that the program crashes. Obviously it would be preferable to inform the user if their mistake. This will not be much work, because *we did just this in the previous chapter*. There we checked that the number of pupils getting on a bus was an integer, so we can reuse that idea here.

.. important::

    Remember that we prefer to use EAFP programming rather than LBYL. So we will *not* examine what the user types in to see if it really is an integer. We will just carry on trying to use the value input and, if it turns out not to be an integer, we will pick up the pieces when an error is thrown.

Looking back, we see that the *exception* generated when the user enters something invalid will be a ``ValueError``, so all we need to do is provide some quick error-handling to deal with this.

.. index:: single: Programs; exam_result.py
.. literalinclude:: /../../src/06/exam_result_3.py
   :language: python
   :emphasize-lines: 5,20-21
   :caption: ``exam_result.py``

Check out that indentation, and how it shows the program structure.

.. tip::

    In this example, the programmer has also left a few blank lines. This is a hopeful attempt to make the structure of the program more obvious to someone reading it. Python just ignores these lines, but they can help a reader.

    Remember that a program is read by a person more often than it it run!

Non-Linear Programs
===================

This is all fine, and the program we have here should cover all the possibilities. But it would be preferable if the user was given the chance to re-enter a value if they make a mistake. It might also be handy to be able to run it for a bunch of students.

In summary, we are now able to write programs that run top-to-bottom, and can skip over some lines depending on some conditions. The missing piece\ [#left]_ is to be able to go back up in the program, or to return to some previous place in the code. Let's do that next!

Repeating Yourself
==================

We often find ourselves repeating tasks. We might look through a drawer of socks *until* we find a matching pair. Or we might look through that box of festive chocolates, avoiding the toffee ones, *until* we find one we like. Or maybe we are asked to boil six eggs for breakfast, one at a time.

These kinds of *repetition* also occur in programming, where they are usually called *loops*. There are two, well, really three, types. To start with the two:

Determinate Loops
    This is where it can be known, before the first time the task repeats, how many times it will be done. It might be different each time the program runs, but it is always known. It's the eggs in the examples above - that will always happen exactly six times, no more, no less.

Indeterminate Loops
    This is where it is now known, and cannot be known, how many times the task will be done before it starts. The number of times depends on something that it unknown. This is the socks in the examples above - you might get lucky and find a pair in the first two, or you might need to look at a lot more.

The "three" comes in because there are two subtly different types of indeterminate loop. Sometimes it can be shown that the loop will always execute at least once, and sometimes it might never execute at all. To use the other example above, if we know that the tub of chocolates is full, we will always check at least one sweet one our way to finding one that is not toffee (so the checking for toffee will always happen at least once). Or, if the tub is open and could be empty, we might not check any sweets at all, so no check for toffee at all.

To implement these in a program there is only really a need for one new programming control statement, to give a loop. But it is convenient to have at least two, one for determinate loops, and one for indeterminate loops. Some languages provide three, with two for the indeterminates. Python goes with two, but a particularly Pythonic way of handling indeterminate loops is usually used. We'll look at these three now.

Determinate Loops
*****************

This is the case where it is known, in advance, how many times some statements need to be run. These loops are often referred to as ``for`` loops, because this is the keyword used to introduce them in many languages. Let's jump in with a simple example. Suppose we want to generate a table converting Fahrenheit temperatures into Celsius. A quick Google and some experimenting at the Python Interpreter would let us work out how to do the conversion:

.. code-block::

    >>> f = 80
    >>> c = (f - 32) * 5 / 9
    >>> c
    26.666666666666668

This is easy to put in a program that allows our user to enter the value to convert\ [#float]_:

.. index:: single: Programs; f2c.py
.. literalinclude:: /../../src/06/f2c_user.py
   :language: python
   :caption: ``f2c.py`` (with User Input)

.. note::

    The ``sep`` in the ``print`` statement simply stops Python printing a space between each part of the output. It's just there for neatness.

This is fine, but we wanted to generate a table. As it stands the user would have to run the program over and over, recording the results to generate such a table. It would be much neater do just display the table for a *range* of values.

Happily, Python provides a ``range`` function that will generate these values. Let's start by displaying the results for Fahrenheit values from 0 to 10. This is not very sensible if this was part of a weather app, but we'll fix that later on. To achieve a table, we need to remove the user input, and just run the conversion on a range of values. We'll start with zero to 10:

.. index:: single: Programs; f2c.py
.. literalinclude:: /../../src/06/f2c_1.py
   :language: python
   :caption: ``f2c.py``

If you run this program you will see that all the *indented* lines after the ``for`` line are repeated. They are executed 10 times, with the value of ``fahrenheit`` ranging from 0 to 10. Some notes:

* The count starts at zero. As we have seen before, everything in programming starts at zero.
* This means that the value in the ``range`` must be the number of lines to print, not the highest value. We wanted all the values from 0 to 10 here, so that's 11 lines.
* And that ``print`` statement is getting messy. We'll add a fix for that next chapter.

You might have noticed that 0F is really very cold, and that our table does not yet reach normal temperatures that might be seen in a weather app. We can tweak the program to display temperatures from, say, 25F to 80F, easily:

.. index:: single: Programs; f2c.py
.. literalinclude:: /../../src/06/f2c_2.py
   :language: python
   :emphasize-lines: 5
   :caption: ``f2c.py``

So now we provide the start point and the end point, remembering that the end must be one more than the final line we require.

.. important::

    Fiddly details like the final value needing to be one more than you might think are hard to remember. Never be afraid to just run the program and see what happens. If it doesn't work quite as planned, just go back and change it.

Finally, we might decide that the table is a bit too detailed, and that it will be enough to give the equivalents in increments of 5. This sounds tricky, but turns out to be simple as ``range`` allows us to specify the increments.

.. index:: single: Programs; f2c.py
.. literalinclude:: /../../src/06/f2c_3.py
   :language: python
   :emphasize-lines: 5
   :caption: ``f2c.py``

See that ``range`` allows us to specify the start, end, and increment. If there is only one value it assumes that the start is zero and the increment is 1, as this is the most common. Two numbers are taken to be a start and an end with an increment of 1. Three numbers, and you're in full control.

The increment can be negative if there is a need to count down; in this case the end must be less than the start! (This is always mentioned in programming books at this point, but practical uses are rare, so you might want to forget it now).

The version of the program above has all the values coded in. So we can look at the program now, and know how many times the loop will execute. That's what makes it determinate. But the values could be entered by a user, like this:

.. index:: single: Programs; f2c.py
.. literalinclude:: /../../src/06/f2c_user_2.py
   :language: python
   :caption: ``f2c.py`` (with User Input)

The loop here is still determinate, and we can still use ``for`` and ``range``. We can't tell from the program now how many lines it would print, but just before the loop starts that number would be known (we could print it out if we wanted to). So it's still a determinate loop, even if the number of times it will run will vary.

.. note::

    Before we move on, look again at that program. It really would need some checks that the values entered were integers, and that the start vakue was less than the end. And that the increment would eventually get us from the one to the other. So much of a program is devoted to handling what the user might do!

Indeterminate Loops
*******************

These are loops where the number of executions cannot be forecast in advance (that is, before the first execution). This is usually because they are required to run *until* something happens, or *while* something is true. Most languages use the keyword ``while`` to introduce these, so they are often just called *while loops*.

.. note::

    Remember there are two possibilities: the loop might always execute at least once, or the loop might never execute at all. Some languages offer different ways of writing each one, Python does not. One of Python's design philosophies is that there should be one way of doing something.

A *while loop* causes statements to execute as long as ("while") some condition is true. The statements affected are indented, as usual. Here's an example.

.. code-block::

    sweet = ''

    while sweet != 'caramel':
        sweet = input('What sweet did you find? ')
        if sweet != 'caramel':
            print('Ugh! Try again!')

    print('Yay! Found one!')

This snippet will repeat the prompt until the user enters ``caramel``. The final ``print`` statement is not indented, so only gets executed once the loop has finished.

That is all there is to it. Some things to bear in mind:

* If the loop condition is ``False`` initially, the statements inside the loop will never execute.
* Something inside the loop must potentially change the value of the condition, else the loop will never exit. This is an *infinite loop*, and is usually a problem!
* The loop can contain other statements, including other loops.
* After the last statement inside the loop (shown by the indentation) the statements start over. There is no need to include anything to make this happen.

Now, an idea that we will return to later is that an important aspect of good programming is not to repeat yourself. Spot the repetition in that example loop? Let's fix it.

More Cunning Loops
------------------

.. important::

    What follows in this section is in many ways specific to Python, and the way Python is usually used. If this book was about, say, Java, this section would not be here! An important part of using any language is to use it in the accepted way that has been developed by its community.

    In the Python community, we say that we aim to be *Pythonic*.

The loop up above contains duplication. Or, if you prefer, it includes information about our problem twice. Or, to put it another way, if we wanted to change one thing we would have to make two changes to the code. Suppose for some mad reason we wanted ``toffee`` instead of ``caramel`` - we would have to make two changes. That's bad.

The Pythonic way around this works as follows. It makes use of an infinite loop, and an explicit statement to exit the loop. It gives neater code, possibly at the cost of making the loop's condition harder to find. Done this way, the example above would look like this:

.. code-block::

    while True:
        sweet = input('What sweet did you find? ')
        if sweet != 'caramel':
            print('Ugh! Try again!')
        else:
            print('Yay! Found one!')
            break

The advantages of this version are:

* The condition is in the code just the once. So if we change it we change one thing.
* The initial value of the variable ``sweet`` is irrelevant.
* The entire logic of this code is not all together (*encapsulated* is the word).

The main downside is that we have to burrow into the code inside the loop to find out how the loop will terminate.

.. note::

    Anything that is always ``True`` can be used in loops like this. We have seen that Boolean ``True`` is really just `1` in disguise, so some programmers save a bit of typing by writing ``while 1``. Something like ``while 1 == 1`` is not unknown!

Unless you have been told not to, for some very good reason, this is the way to write while loops in Python.

Pulling It Together
===================

Let's finish this section by using the new ideas here to create a complete program. This example is not the most interesting, but it will use all the ideas from this chapter:

.. topic:: Times Tables

    Write a program that prints a "times table". The program should prompt the user to enter an integer between 0 and 12 (inclusive) and should display the "times table" for that value, from "0 times" to "12 times".

While small, this is going to be the most complex program we have written so far. It is unlikely that we would be able to sit down and type the whole thing in without errors, so the trick is to break it down. We'll define a useful first version, and then add in features\ [#savework]_. Let's go like this:

#. Write a program to print a single table, the "7 Times Table", say.
#. Change it so the user enters the number, without worrying about invalid entries.
#. Reject numbers outside the range 0 to 12 inclusive.
#. Allow the user to enter again if their number is out of range.
#. Fix the possibility that the user will not enter an integer.

Hold on! There is a lot in that list! Where did it come from? In many ways, that list is the hard part of programming. The hard part is taking a complex problem and breaking it down into smaller problems. If you do this, and repeat as needed, eventually you get to problems that are so small they can be solved. And gluging all the solutions together should solve the bigger problem!

Anyway, let's start with the first stage. This is a *determinate* loop, because we know there will always be 13 lines. The maths is not difficult, and a bit of fiddling will get the layout looking reasonable. A first version:

.. index:: single: Programs; 7times.py
.. literalinclude:: /../../src/06/7times.py
   :language: python
   :caption: ``7times.py``

We should test this program, even though it is simple, just to be sure it works. Then we take a look to see if it's a good start. Remembering that we should never repeat anything, we might spot that the ``7`` is in there twice; it makes sense to fix this, as for one thing it will make the next version easier. So, for the moment, let's turn that ``7`` into a constant, like so:

.. index:: single: Programs; 7times.py
.. literalinclude:: /../../src/06/7times_constant.py
   :language: python
   :caption: ``7times.py``

Now, to print a different table all that needs to be changed if the value of that one constant. Again, we would test.

Once satisfied, we need to change it so that the user enters the number, *but we do not care at this point about validating the input*. This is now easy, because all we have to do is change the way the constant gets its value (and at the same time change its name so that it is a variable).

.. tip::

    No need to change the name of the constant in three places. Your IDE should have a feature to do this for you. Look for somehing called ``Refactor`` or similar.

The required change is just to the one line. This is the whole point of splitting the task like this! The new version:

.. index:: single: Programs; any_times.py
.. literalinclude:: /../../src/06/any_times.py
   :language: python
   :emphasize-lines: 5
   :caption: ``any_times.py``

See that we give the user a hint of the allowed values, but we are not yet checking them. Also, there is a space between the end of the prompt and where the user will type. There is no harm in keeping our simple dialogue neat.

Next we want to check that the number entered is between 0 and 12. For the moment, we will just display the error, and not worry about anything else. This is obviously a conditional statement after the ``input`` line. The condition could be written two ways (either to define what is accepted, or what is not accepted), but the most obvious seems to be to say what values are allowed, like so\ [#shorthand]_:

.. index:: single: Programs; any_times.py
.. literalinclude:: /../../src/06/any_times_2.py
   :language: python
   :caption: ``any_times_2.py``

So now the user knows of their error, and could just run the program again. Or we could offer them a chance to make good their error. This seems a better user experience, so we'll do that.

This is another loop. It's indeterminate, but will happen at least once. Instead of worrying about what the loop condition should be (and worrying that it would be the same as the condition in the conditional!) we'll be Pythonic. We'll put the whole program in an infinite loop, and jump out of the loop after successfully printing the table. There's not much to change; the only tricky bit is getting the indentation right:

.. index:: single: Programs; any_times.py
.. literalinclude:: /../../src/06/any_times_3.py
   :language: python
   :emphasize-lines: 5, 11
   :caption: ``any_times_3.py``

.. important::

    If you needed another argument for being Pythonic when using these loops, here it is!

So now we ``break`` out of the loop only if we printed a table. Otherwise, we ask for the input again. Take a close look at the indentation. For example, the ``break`` is indented so as to be outside the ``for`` so that the whole table is printed. If you're unsure, move it across to line up with the ``print`` and see what changes.

Finally, we want to make sure that the user really does enter an integer. We are in Pythonic mood here, so we will not examine the value that's entered (LBYL - Look Before You Leap), we will just pick up the pieces if there is an error (EAFP - Easier to Ask Forgiveness than Permission). Long ago, we saw that there would be an exception generated, and it would be a ``ValueError``, so we need to try that.

.. index:: single: Programs; any_times.py
.. literalinclude:: /../../src/06/any_times_4.py
   :language: python
   :emphasize-lines: 6, 15-16
   :caption: ``any_times_4.py``

See how working like this means that we hardly touch the parts of the program we know work. That's the trick of the thing!

We now have a working, we hope, program. It contains examples of everything we have used so far. Study it!

Takeaways
=========

There has been a lot in this chapter, but we have at least now completed a working program that does something useful. Here are the main ideas:

#. Boolean conditions allow us to control the order in which statements are executed, and/or which statements are executed. This is called the *flow of control*.
#. Conditional statements are introduced with the keyword ``if`` and allow for different statements to be executed. More possibilities can be covered using the optional ``elif`` and ``else`` keywords.
#. Determinate loops are written with the ``for`` keyword. The ``range`` function is a handy way to control the number of times loops execute.
#. Indeterminate loops use the ``while`` keyword. They can directly use a condition or, pythonically, be used as infinite loops in conjunction with the ``break`` instruction.
#. Indentation shows which statements are inside which loops and conditions.
#. There can be, and often are, loops within loops, and conditions inside conditions. And loops inside conditions, and so on.
#. The trick of programming is to split the big problem into smaller problems. And to then repeat, until the problems are small enougn to solve.

Our programs are now going to get complex, at least in the sense that they will be longer. So next we will look at ways to keep the amount of code we are working on to a manageable amount. Say 24 lines or so. Onward!

.. [#tabs] But their use is controversial, and best avoided unless you want to end up in arguments. It's like the dark/light theme in the IDE thing.
.. [#else] A common misconception among new programmers is, for some reason, that there has to be an ``else``. This is not the case. Really.
.. [#abstract] They were people getting on a bus in the first example, and it's an exam grade now, but the tests are the same. This is *abstraction* - spotting a pattern and reusing the solution.
.. [#left] As it happens, that is pretty much all that remains to do. There isn't much more to programming after that.
.. [#float] Note that this program allows the user to enter a floating-point value.
.. [#savework] In practice we would also save working versions of the program we we went. So that if we got into a mess adding a new feature we could always retreat to a known working state.
.. [#shorthand] We saw a shorthand for testing if a value is between two others, so we'll use that here.
