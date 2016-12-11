.. title: Sorting list with two criteria
.. slug: sorting-list-with-two-criteria
.. date: 2016-12-11 10:26:07 UTC
.. tags: python
.. category: 
.. link: 
.. description: 
.. type: text

We want to sort a list of elements with the first element in ascending order and the second element in descending order.

Using the lambda function:
--------------------------


.. code-block:: python

    occurences = {'bat': 2, 'mat': 1, 'cat': 3}
    sorted(occurences.items(), key=lambda x: (-x[1], x[0]))

The -x[1] is for the reversed sort.

By order of priority, we first sort with the 2nd element (x[1]), then with the 1st element (x[0])
