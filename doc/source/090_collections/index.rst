==========
Collecting
==========

As we've already noted more than once, we have actually covered all we need to know in order to create programs. Modules and functions are really just a convenience that help keep the job simple, and allow for useful chunks of program to be reused. They're all about making things easy, and saving unnecessary work. The new idea we'll meet in this chapter is almost the same - we don't strictly need to be able to handle *collections* of related data items, but being able to will make certain tasks much easier.

So this chapter introduces the idea of *collections* of data items. All programming languages will provide features for this and, as usual, the names differ but the basic ideas are the same. In the earliest languages collections were called *arrays*, and that name is still found in some modern languages. Other names you'll see include lists, maps, sets, and more.

Python provides a few collections as standard, and the *collections* module in the standard library contains a whole lot more. In general, a collection:

* Stores a number of related data items.
* May or may not require that those data items are of the same time.
* May store the items in a particular order, or may not consider order to be important.
* May or may not allow duplicate items.

We'll look at four collection types here\ [#sets]_. These cover all the common use cases, and together form a complete toolbox to draw on. *Strictly* you only need one collection type to do anything, but some do allow for more elegant and neater solutions. Anyway, below we will describe:

Lists
    The Swiss Army Knife of collections. You can do anything with a list. A list stores data items, and maintains the order. Usually the items are all of the same time.
Tuple
    Think of this as being like a row in a database table. This is a collection of data that represents something. The data items do not have to be the same type. Order is not important.
Set
    Basically a list, with the handy extra property that items in it have to be unique. This type also supports the usual operations (difference, intersection, etc) from maths set theory.
Dictionary
    A key-value collection. It is used by looking up a key, and finding the corresponding value. It's just like looking up a definition in a paper dictionary.

A collection is simply a bunch of related values that it is convenient to treat as a single entity. They have a single name (identifier), so they can be passed into functions, and returned from functions. So a list or tuple or set contains a collection of related data items.

The various collections have slightly different properties. In a list, for example, order is maintained - new values are added at the end, or among the existing values, in which case the others "shuffle along". Sets, in contrast, have no concept of order. Lists are said to be *mutable*, which means they can be changed. Tuples are *immutable*, which implies the opposite. Knowing a few of these details helps with picking the best collection for a particular application.

We start with lists, as these are the most general. Remember, you can do anything with a list.

.. note::

    This chapter will not attempt to cover all the details of each of these collections. That is what the docs are for! The Python docs include `Tutorials <https://docs.python.org/3/tutorial/datastructures.html>`_ along with the `full gory details <https://docs.python.org/3/library/stdtypes.html>`_. Links to the relevant docs are included in each section below.

    And, as always, Google will lead you to more tutorial material and examples.

Looking at Lists
================

A list is a collection of values, where the order is assumed to be important (although it doesn't have to be). Let's use a list to explore the whole idea of a collection.

.. seealso::

    The `official docs <https://docs.python.org/3/library/stdtypes.html#lists>`_.

A value in a list is often called an *element*. Usually, all the elements in a list are of the same type, which is to say that lists are *homogeneous*\ [#listshomo]_. It is assumed that the order of the elements in a list has some importance, if only that the elements added most recently are at the end. This in turn means that a list can usually be *sorted* into ascending or descending order.

.. hint::

    So lists are a good choice if you have data that needs to be sorted, or where you need values like the highest or lowest.

    It follows that there must be a way to sort the elements, that they have a concept of order, which brings us back to the idea that all the elements should be of the same type.

Enough description. Let's do an example that shows the basics.

A List Example
**************

.. topic:: Test Marks

    A school pupil has taken four maths tests. Whether they pass or fail overall depends on the average of the four marks from the five tests.

    Write a program that takes the marks are finds the average.

There are four test marks here, all of which are going to be integers. So, without collections, we might think that something like this would work. (In a real program the values would be entered, but here we'll just assign the values here to keep the code short).

.. code-block::

    >>> mark_1 = 65
    >>> mark_2 = 55
    >>> mark_3 = 45
    >>> mark_4 = 60
    >>> average = (mark_1 + mark_2 + mark_3 + mark_4) / 4

This is fine. But what would happen if there were five tests? Or three? We would need to add or remove variables, and remember to tweak the division to find the average. These multiple changes mean that this not DRY code! Being able to handle *any* number of marks would be DRY and would give a promising chance of creating some reusable code. We can, of course, do just this with a list.

.. important::

    Yes, you say, but the spec said *four* marks, so why write code that can handle any more? The answer is that this is *generalisation*. It is not much extra effort, and we will end up with some code that could be useful in other applications.

    Suppose we wanted the average of 10 temperature readings. If we have general code we could reuse it. That's *abstraction*.

So, let's rework this code to use a list. A list is created in the same way as any other variable, by giving it a value. A list is denoted with square brackets, so to create an empty list:

.. code-block::

    >>> marks = []

Or to create it with some values already in it:

.. code-block::

    >>> marks = [50, 40, 30,]

.. note::

    That comma at the end might look odd, and indeed you'll find that you could leave it out. Many programmers prefer this style, though, because it makes adding new values easier. Your call\ [#tuplecomma]_.

The important new idea here is that the list ``marks`` is a single variable, that happens to contain multiple values. Being a list, order is maintained, so a new value can be added, and will be at the end:

.. code-block::

    >>> marks.append(20)
    >>> marks
    [50, 40, 30, 20]

We can start to see how this would be useful when we realise there are handy built-in functions to calculate useful values from the values in the list. Like their number (the length of the list) or their sum:

.. code-block::

    >>> len(marks)
    4
    >>> sum(foo)
    140

.. hint::

    There are other built-in functions too, like ``max`` and ``min`` to find the highest and lowest values. Always remember to check for built-ins before writing some new code.

    The key thing is to think "This *must* have been done before!".

Using a list, the program to find the average of the four marks could use code something like this:

    >>> marks = []
    >>> marks.append(65)
    >>> marks.append(55)
    >>> marks.append(45)
    >>> marks.append(60)

    >>> average = sum(marks) / len(marks)

There's not much gained so far, but what if there were a different number of marks? Or how about a program that could handle any number of marks. That sounds a like a loop. If we know in advance how many marks there would be, a ``for`` loop could work in a program something like this:

.. literalinclude:: /../../src/09/marks_for.py
   :language: python
   :caption: ``marks.py``

.. note::

    For clarity, the code to verify that the mark entered is a number (and presumably is also in some valid range) has been left out here.

Here the number of marks is defined as a constant, but it could just be entered by the user. So to make this program work for any number of marks, all that would be needed would be to change the value in ``NUMBER_OF_MARKS``.

We can improve the readability of this program a little by pausing to think that averages are something that must be worked out a lot. A look in the docs (or a Google) would reveal that there is no built-in way to find an average in the standard library, but that there is a ``statistics`` module containing all sorts of promising stuff. So we can use this to make things a little neater (and the program a little shorter).

And one final tweak will be to renamne to ``count`` variable in the ``for`` loop. There is a convention (yes, another one) that if the variable is not of any use other than to control the loop it is named ``_``. So:

.. literalinclude:: /../../src/09/marks_for_mean.py
   :language: python
   :emphasize-lines: 4, 12, 16
   :caption: ``marks.py``

For completeness, and for the sake of another example, it's a small change to this program to get to a general-purpose version that could handle any number of marks. The change is to the loop, which in a general solution is *indeterminate*, and we need to provide the user with a way of indicating that have finished. We'll have them enter ``-1`` now\ [#whilenot]_. The constant can obviously be removed, and we end up with a DRY solution.

.. literalinclude:: /../../src/09/marks_while_mean.py
   :language: python
   :caption: ``marks.py``

Another advantage of having all the marks data in a list is that we can do many other useful things with it. The ``max`` built-in function would give us the highest value, for example. And the ``statistics`` module is full of other possibly interesting values to calculate.

Working with Lists
******************

This is not the place for a full description of all the things you can do with lists. Instead we'll talk about some of the most common uses, along with examples. Lists are very flexible and powerful, and Python provides several useful ways of putting them to work.

Keep in mind the most important features of a list in Python:

* It is heterogeneous (all the elements in it are of the same type).
* Its order is maintained, and is probably important.

As we have seen in the example, a list is denoted by square brackets, and can be created with or without some initial values:

.. code-block::

    >>> speeds = []
    >>> speeds = [1, 2, 3,]

It can be cleared either by just recreating it, or by emptying it:

.. code-block::

    >>> speeds.empty()

.. note::

    Many of the operations carried out on lists use a *dot notation*, where the identifier of the list is joined to the name of the operation by a dot. The ``empty`` operation did so above, and we have seen it before as in:

    .. code-block::

        choices = ['spam', 'eggs',]
        choices.append('beans')

    The ``append`` is using this dot notation. These operations behave rather like the *functions* we have met before, but are correctly called *methods* because of this different syntax. So that is the name used here.

Let's start by looking at what the *order* of a list means.

List Order
----------

The order of a list is maintained, whether or not it is important. This compares with a string, which is a sequence of characters, where the order is usually important. New elements are usually added at the end of list using the ``append`` method, like so:

.. code-block::

    >>> choice = ['beans',]
    >>> choice.append('spam')
    >>> choice
    ['beans', 'spam']
    >>> choice.append('spam')
    >>> choice
    ['beans', 'spam', 'spam']

.. important::

    This example also neatly illustrates that there can be duplicate elements in a list.

In rare cases\ [#listinsert]_ new elements can be inserted at a specified position. Positions count from zero (again, just like a string), and existing elements "shuffle along":

.. code-block::

    >>> choice.insert(1, 'egg')
    >>> choice
    ['beans', 'egg', 'spam', 'spam']

The most common useful order is to have the elements sorted. The meaning of "sort" depends on the type of the elements, but usually it does the obvious thing. Very confusing things happen if a list containing several data types is sorted. To sort a list, we just use the ``sort`` method:

.. code-block::

    >>> speeds = [12, 8, 23, 17]
    >>> speeds.sort()
    >>> speeds
    [8, 12, 17, 23]

And to reverse the sort, just ``sort`` and the ``reverse`` the list:

.. code-block::

    >>> speeds.sort()
    >>> speeds.reverse()
    >>> speeds
    [23, 17, 12, 8]

If you need to maintain a list in order, the procedure is simple. No need to find the correct place, and insert the new element. Just add it on the end, and ``sort`` the result:

.. code-block::

    >>> speeds = [12, 8, 23, 17]
    >>> speeds.append(10)
    >>> speeds.sort()
    >>> speeds
    [8, 10, 12, 17, 23]

That's it!

List Slices
-----------

The examples above mentioned that lists behave rather like strings. This is intentional - they are both what Python calls an *iterable*. So it follows that string operations and slices work on lists. Individual elements can be found via their index, counting from ``0`` on the left or ``-1`` on the right:

.. code-block::

    >>> speeds
    [8, 10, 12, 17, 23]
    >>> speeds[0]
    8
    >>> speeds[-1]
    23
    >>> speeds[2]
    12
    >>> speeds[-3]
    12

The two ways of counting mean that there are always two index values to get any element. Using this index value, elements can be changed:

.. code-block::

    >>> speeds
    [8, 10, 12, 17, 23]
    >>> speeds[0]
    8
    >>> speeds[0] = 7
    >>> speeds
    [7, 12, 17, 23]

Slices work too:

.. code-block::

    >>> speeds
    [8, 10, 12, 17, 23]
    >>> speeds[:-1]
    [8, 10, 12, 17]
    >>> speeds[2:]
    [12, 17, 23]
    >>> speeds[::2]
    [8, 12, 23]

Slices can be assigned too, but that's a bit obscure. Try it and see!

Finding Elements
----------------

So you have a list containing some values, and you need to know whether a given value is there. That's a very vague and abstract description, but it's actually quite common. Suppose you are reading car number plates as they pass, but only want to record each one once. Or a user has entered a choice from a menu, and you want to check whether it's a valid choice. Both require that you check *membership* of your list or, if you prefer, whether a given value is there.

There are two ways to do this, but we are not breaking Python's "one way to do something" rule, because it depends on what exactly you want to do. Do you just need to check if a value is in a list, or do you want to do that, *and* find out where it is?

In the first case (you just want to check if a value is in a list) we can use the fact that lists and strings are both iterables, and use the ``in`` operator. It simply tells us whether a value is, ah, in the list:

.. code-block::

    >>> speeds = [12, 8, 23, 17]
    >>> 12 in speeds
    True
    >>> 14 in speeds
    False

Alternatively, if we need to know where in the list the value can be found, the ``index`` method is the one to reach for:

.. code-block::

    >>> speeds = [12, 8, 23, 17]
    >>> speeds.index(12)
    0
    >>> speeds.index(14)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: 14 is not in list

That exception if the value is not to be found means that ``index`` is often used after ``in`` has been used to check whether value is there.

Looping Lists
-------------

Often a program needs to do something with every element in a list. So it makes sense to allow ``for`` loops to iterate across a list. In fact, the ``range`` function that we met when first looking at ``for`` loops effectively generates a list behind the scenes\ [#range]_. So we could have:

.. code-block::

    knights = ['Robin', 'Galahad', 'Bedevere']
    for a_knight in knights:
        print('Bold Sir ', a_knight)

This is a very common operation when printing results, searching for a value, and so on.

Copying Lists
-------------

Copying lists is straightforward, but a bit of a "gotcha". To understand why, we need to think a little about how lists are stored. We can think of it this way:\ [#pointers]_ a list is a pointer to a memory location where the first value is stored. That value is stored along with a pointer to the next, and so on. Eventually a value is reached that has no pointer, so this must be the end of the list.

So if we have this:

.. code-block::

    speeds = [1, 2, 3, 4,]

there are four memory locations, sort of chained together. If we then have this:

.. code-block::

    speeds_copy = speeds

we actually have two versions of the same list. Both point to the same first element, which points to the second. So changing one list will change the other too. See:

.. code-block::

    >>> speeds = [1, 2, 3, 4,]
    >>> speeds_copy = speeds
    >>> speeds_copy.append(5)
    >>> speeds
    [1, 2, 3, 4, 5]

We added an element to the second list, but is also shows up in the first!

This is sometimes what you want, but admitedly not often. The trick is to use the ``copy`` method, which actually does create a copy (a "shallow" copy to give its proper name). This now works more intuitively:

.. code-block::

    >>> speeds = [1, 2, 3, 4,]
    >>> speeds_copy = speeds.copy()
    >>> speeds_copy.append(5)
    >>> speeds
    [1, 2, 3, 4]
    >>> speeds_copy
    [1, 2, 3, 4, 5]

Always use this method if you need a copy.

.. note::

    As you will see in the docs, this is often written as creating a slice of the complete list, like so:

    .. code-block::

        >>> speeds_copy = speeds[:]

    This is so commonly used, it's fine.

Leaving Lists
*************

Lists are a fine general-purpose collection. As we've noted, you only really needs lists. Some older languages do only provide one collection type - usually called an *array*, but most modern languages provide some more. Three of those that Python provides are widely used, and we'll go on to them now.

But keep in mind that you can do anything these types can do with a list (except that for a Dicionary you need two lists). For that reason we'll focus on the differences, and the specific use cases where tuples, sets, and dictionaries come in handy.

Trying Tuples
=============

At first sight, tuples seem very similar to lists, and you may wonder what they are for. So let's start with the two most important differences:

* Tuples are *immutable*, which means that once created, a tuple does not change.
* Tuples are usually *heterogeneous*, that is a tuple contains data of a range of different data types.

This contrasts with a list which, as we have seen, is *mutable* and usually *homogeneous*.
.. hint::

    If you have studied databases, you can think of a tuple as a row in a database table. And the database table could be represented by a list of tuples.

We have, in fact, used tuples before, without knowing it. If you have a function that returns more than one value, it is in fact returning a tuple\ [#tuplereturn]_. That code looked something like this:

.. code-block::

    def find_string_and_number():

        a_string = ...
        a_number = ...

        return a_string, a_number

So we returned two values, separated with a comma. That is actually a *tuple*.

A tuple is represented just like that, a number of values separated by commas. So this creates a tuple:

.. code-block::

    >>> details = 'Robin', 12, False
    >>> type(details)
    <class 'tuple'>
    >>> details
    ('Robin', 12, False)

Notice that when the interpreter displays the value of a tuple it adds parentheses. So it is usual to add these in anyway when a tuple is created (and this also allows tuples to contain tuples). As you probably expect, the elements inside the tuple can be accessed by an index number (just like lists) and slices work too:

.. code-block::

    >>> details[2]
    False
    >>> details[-1]
    False
    >>> details[:-1]
    ('Robin', 12)

But, as they are immutable, it is not possible to assign values to the elements once a tuple is created:

.. code-block::

    >>> details[2] = True
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'tuple' object does not support item assignment

Some final details. To create an empty tuple use empty round parentheses:

.. code-block::

    >>> empty_tuple = ()

To create a tuple with a single element, you *must* add a trailing comma, like this\ [#trailcomma]_. But the brackets are optional:

.. code-block::

    >>> new_tuple = 'Robin',

And the same will add an element to the end of a tuple:

.. code-block::

    >>> details += ('Brave',)
    >>> details
    ('Robin', 12, False, 'Brave')

But if you find yourself adding to the end of a tuple that could well be the problem's way of telling you that you should be using a list!

So, really tuples are best thought of as a handy way to handle several related data items as a single unit. Remember the two key ideas - tuples are *immutable* and usually *heterogeneous*.

Seeking Sets
============

Sets are probably the most obscure collection type, but they are worth mentioning because of one special property. The features of a set are:

* It is unordered.
* It can be heterogeneous.
* It does *not permit duplicate elements*.
* It supports all the usual operations associated with a mathematical set, such as intersection and difference.

The most commonly useful properly is the uniqueness. A set is created using curly parentheses:

.. code-block::

    >>> knights = {'Robin', 'Galahad', 'Bedevere',}
    >>> type(knights)
    <class 'set'>

The trailing comma is optional, as with tuples and lists.

Membership testing is possible:

.. code-block::

    >>> 'Robin' in knights
    True
    >>> 'Arthur' in knights
    False

Items can be added to a set using the ``add`` method, but this has no effect if the item is already there.

.. code-block::

    >>> knights.add('Robin')
    >>> knights
    {'Galahad', 'Robin', 'Bedevere'}
    >>> knights.add('Bors')
    >>> knights
    {'Galahad', 'Bors', 'Robin', 'Bedevere'}

.. note::

    The code above also illustrates that order is not defined for a set.

The set operations can be useful if, say, we have two collections and want to know what items are in the one, but not the other, or are in both:

.. code-block::

    >>> knights = {'Robin', 'Galahad', 'Bedevere',}
    >>> brave_knights = {'Galahad', 'Bors', 'Bedevere',}
    >>> knights - brave_knights
    {'Robin'}
    >>> knights & brave_knights
    {'Galahad', 'Bors', 'Bedevere'}

The two operations here are set difference (``-``) and intersection (``&``).

So this can be very useful if this sort of thing is common in your application.

Finally, a common example where sets can be very handy is where you have a list but you want to filter out duplicate items. The simple way to do this is to convert the list to a set, and then back again! Look:

.. code-block::

    >>> knights = ['Galahad', 'Bors', 'Robin', 'Robin', 'Bors', 'Lancelot', 'Bors',]
    >>> knights = list(set(knights))
    >>> knights
    ['Galahad', 'Bors', 'Robin', 'Lancelot']

Neat.

Discovering Dictionaries
========================

The final collection that's worthy of a mention is a dictionary. A dictionary is a *key-value* pair, sometimes called a map. As usual, most modern programming languages provide something like a dictionary, and many provide multiple subtle variations.

.. note::

    There are many more collections, including specific types of dictionary, available in the standard library. We are just limiting ourselves to the built-in collection types here.

Assuming you have used a paper dictionary, you already have the idea of what a Python dictionary will do. In a paper dictionary you take a word (that's the *key*) and find the definition (that's the *value*). It's important to realise straight away that this doesn't work the other way around - you don't take a definition and look through the dictionary until you find the right word\ [#reversedict]_.

So when using a dictionary we have a *key* and some corresponding *values*. For example:

* In a phone book, contact names would be the key (a string), and the phone number would be the value (also a string\ [#phone]_).
* In a login system, user names would be the key (string), and the password would be the value (an encrypted string).
* In an exam system, a student id would be the key (a string), and their results would be the value (a list of integers).

Specifically, a Python dictionary:

* Is a collection of key-value pairs.
* Has unique keys.
* Does not (reliably) maintain any concept of order. (The order will most likely be the order in which items are added, but it would be a brave programmer who decided to rely on this!)

Given this, a dictionary is clearly going to be useful where the data in a problem neatly fits the key-value idea.

.. note::

    The question of "order" in a dictionary is a tricky one. The dictionaries we are discussing here do not have order, although you can write cunning code to sort them. But if you have a problem that really needs a dictionary with order, you can reach for one of the other available types and ``import`` them - ``OrderedDict`` for example.

Let's see a dictionary in use. An empty one is created using curly parentheses:

.. code-block::

    >>> scores = {}

.. important::

    Curly brackets like this were also used with sets, above. To create an empty set, the code is:

    .. code-block::

        >>> empty_set = set()

    Presumably they ran out of brackets.

Then it is simply a case of adding values. We specify the key, and the corresponding value:

.. code-block::

    >>> scores = {}
    >>> type(scores)
    <class 'dict'>
    >>> scores['robin'] = 23
    >>> scores['bors'] = 76
    >>> scores['galahad'] = 40
    >>> scores
    {'robin': 23, 'bors': 76, 'galahad': 40}

And to extract values, just use the key:

.. code-block::

    >>> scores['robin']
    23

The same works to change a value. Obviously changing a key doesn't really make sense, and has to be done by deleting and inserting a new entry.

.. code-block::

    >>> scores['robin'] = 45
    >>> scores['robin']
    45
    >>> del (scores['bors'])
    >>> scores['sir bors'] = 76
    >>> scores
    {'robin': 45, 'galahad': 40, 'sir bors': 76}

Two methods are commonly used to work with dictionaries. They are ``keys`` and ``values``, which provide lists of what they say:

.. code-block::

    >>> scores.keys()
    dict_keys(['robin', 'galahad', 'sir bors'])
    >>> scores.values()
    dict_values([45, 40, 76])

And also, ``items`` gives a list of tuples representing the dictionary:

.. code-block::

    >>> scores.items()
    dict_items([('robin', 45), ('galahad', 40), ('sir bors', 76)])

To finish with an example of using a dictionary, let's consider the problem of finding the key value in the above dictionary that has the highest value. Here's a shorthand for creating a dictionary:

.. code-block::

    >>> scores = dict(robin = 45, galahad = 40, bors = 76, bedevere = 90)
    >>> scores
    {'robin': 45, 'galahad': 40, 'bors': 76, 'bedevere': 90}

How to find the key with the highest value? We need to use the handy methods that let us get at the insides of the dictionary. We can find the highest value easily:

.. code-block::

    >>> high_score = max(scores.values())
    >>> high_score
    90

We have no way to find a key from just the value, and anyway the value might correspond to more than one key. So the trick is to use ``items`` and loop across the dictionary elements. This looks a bit strange, but once you've seen it once ...

.. code-block::

    >>> for name, score in scores.items():
    ...     if score == high_score:
    ...         print (name)
    bedevere

The tricky thing about using a dictionary can simply be realising that it is the right tool for your problem!

Takeaways
=========

This chapter has introduced four of the most common collection data types. Using these is fundamental towriting DRY programs that will work in a range of situations. When picking a collection type it is worth remembering:

* You can do basically anything with lists. Even key-value pairs can be implemented with lists.
* Some collections maintain order, and can be sorted, some do not.
* Some allow duplicate values, some do not.
* Some are well suited for heterogeneous data, others work better with homogeneous data.
* Some operations, like iterating over a sequence, or testing membership with ``in`` are available for more than one collection. As usual, it is the ones where the operation makes sense!

Many programs involve structures built up of several collections - lists of lists, or dictionaries where the value is a tuple. The trick to arriving at an efficient solution can often be to design the right *data structures*. Applications handling huge amounts of data often require consideration of the best structures to allow for efficient searching too, but that is not likely to be your problem for a while!

As usual, this chapter introduced the basic ideas. Full details are in the docs, and in many online tutorials.

.. [#sets] This almost said three, but we'll include Sets so as to be complete, and because they do have some nifty uses now and again.
.. [#listshomo] Note this says *usually*. Lists can contain elements of different types, but this often breaks the point of having a list, and the concept of "order" becomes difficult. A tuple is often a better call in this case.
.. [#tuplecomma] As we will see, this style is more important with tuples. So a good argument for doing this with lists is that it's consistent with other collections.
.. [#whilenot] Probably not a good example of UX. Next chapter we'll include a way to do this neatly.
.. [#listinsert] So rare that this example might have been left out.
.. [#range] This is in fact pretty much what ``range`` did in older versions of Python. Now, for efficiency it does something slightly different but we can still think of it as generating a list.
.. [#pointers] Think of it this way because this is exactly how it works.
.. [#tuplereturn] So, in effect, the function is returning *one* value, which happens to be a tuple.
.. [#trailcomma] This is one reason why adding the trailing comma in lists is good form. Keeps it less confusing.
.. [#reversedict] You can obviously code this in Python, but is is the stuff of nightmares to do.
.. [#phone] A string? Yes. Phone numbers usually have spaces in them and are very rarely used in arithmetic!
