.. title: Using enum in python
.. slug: using-enum-in-python
.. date: 2014-07-28 09:52:22 UTC+01:00
.. tags: 
.. link: 
.. description: 
.. type: text

Install enum module prior to python 3.4
=======================================

.. code-block:: bash

    pip install enum34

Example:
--------

.. code-block:: python

    from enum import Enum
    Animal = enum('Animal', 'ant bee cat dog')

or equivalently:

.. code-block:: python

    class Animals(Enum):
        ant = 1
        bee = 2
        cat = 3
        dog = 4

