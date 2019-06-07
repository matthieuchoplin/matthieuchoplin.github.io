.. title: Introspection in python
.. slug: introspection-in-python
.. date: 2017-04-25 12:43:16 UTC+01:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text


Introspection in python
=======================

Imagine that you are debugging and that you want to know the methods that you can call on an object, this pseudo code can be helpful. Here "some_object" is any python object:

.. code:: python

  [method for method in dir(some_object) if callable(getattr(some_object, method))]


              
Source: http://www.diveintopython.net/power_of_introspection/index.html