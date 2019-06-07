.. title: defaultdict of defaultdict, nested
.. slug: defaultdict-of-defaultdict-nested
.. date: 2017-08-09 16:38:01 UTC+01:00
.. tags: python, defaultdict
.. category: 
.. link: 
.. description: defaultdict nested
.. type: text

Creating arbitrary level of nested dictionaries using `defaultdict <https://docs.python.org/2/library/collections.html#collections.defaultdict>`__:

.. code:: python

    from collections import defaultdict

    def recursive_defaultdict():
        return defaultdict(recursive_defaultdict)

.. code:: python

    >>> x = recursive_defaultdict()
    >>> x['a']['b']['c']['d']
    defaultdict(<function recursive_defaultdict at 0x7fbf9b0496e0>, {})
    >>> import json
    >>> print json.dumps(x)
    {"a": {"b": {"c": {"d": {}}}}}
    

With a lambda:

.. code:: python
    
    recursive_defaultdict = lambda: defaultdict(rec_dd)


Source: https://stackoverflow.com/questions/19189274/defaultdict-of-defaultdict-nested
