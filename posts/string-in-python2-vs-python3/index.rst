.. title: String in python2 vs python3
.. slug: string-in-python2-vs-python3
.. date: 2017-08-17 12:35:28 UTC+01:00
.. tags: python
.. category: python
.. link: 
.. description: Difference between basestring and str in python 
.. type: text

Difference between *basestring* and *str* in python 
===================================================

In Python versions prior to 3.0 there are two kinds of strings "plain strings" and "unicode strings". Plain strings (str) cannot represent characters outside of the Latin alphabet (ignoring details of code pages for simplicity). Unicode strings (unicode) can represent characters from any alphabet including some fictional ones like Klingon.

So why have two kinds of strings, would it not be better to just have Unicode since that would cover all the cases? Well it is better to have only Unicode but Python was created before Unicode was the preferred method for representing strings. It takes time to transition the string type in a language with many users, in Python 3.0 it is finally the case that all strings are Unicode.

The inheritance hierarchy of Python strings pre-3.0 is:

.. code:: bash

          object
             |
             |
         basestring
            / \
           /   \
         str  unicode
         
'basestring' introduced in Python 2.3 can be thought of as a step in the direction of string unification as it can be used to check whether an object is an instance of str or unicode

.. code:: python

    >>> string1 = "I am a plain string"
    >>> string2 = u"I am a unicode string"
    >>> isinstance(string1, str)
    True
    >>> isinstance(string2, str)
    False
    >>> isinstance(string1, unicode)
    False
    >>> isinstance(string2, unicode)
    True
    >>> isinstance(string1, basestring)
    True
    >>> isinstance(string2, basestring)
    True
    
Source: https://stackoverflow.com/questions/1979004/what-is-the-difference-between-isinstanceaaa-basestring-and-isinstanceaaa