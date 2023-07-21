==================
Staying in Control
==================

Previously we have looked at *exceptions* and how they can be used to catch some error situations. These have been errors that mean that Python cannot carry on because the values it is trying to process don't make sense. But what about the case where the values do make sense (in that they are the correct type), but are invalid for some other reason.

Values in Range
===============

Remember the example of allocating students to buses. There was an error when the capacity of a bus was entered as ``0`` (it provoked a ``ZeroDivisionError``), but what about if ``-10`` had been entered? This is clearly nonsense but the Python interpreter (which has no knowledge of buses) would happily carry on.

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

This is fine, but as it stands the user might be a little baffled about what's going on. It would be better to provide them with some sort of useful error message. Or we could point them in the direction of how to use the program properly. To do this, we need to say what should happen if the condition is ``False``. It looks like this:

.. literalinclude:: /../../src/06/school_bus.py
   :language: python
   :emphasize-lines: 15-16
   :caption: ``school_bus.py``

The ``else`` states what happens when the condition at the ``if`` is ``False``. It is indented so that it is directly below its matching ``if``, so there is no need for the condition to be repeated.

.. important::

    This works because a Boolean condition is always one of ``True`` or ``False``. The condition in a statement like this can be anything that evaluates to a Boolean value.

That's enough for simple cases. Before looking at more elaborate ones, let's consider what's going on here.

Flow of Control
===============

The example above introduced a *conditional statement*. This is a statement that allows us to control the *flow of executioN* in a program. Unless we specify otherwise, a program will flow from the top to the bottom, with the interpreter executing each statement in order. This is rarely what is needed, because we want to handle errors, deal with different user input, and so on.

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


.. [#tabs] But their use is controversial, and best avoided unless you want to end up in arguments. It's like the dark/light theme in the IDE thing.
