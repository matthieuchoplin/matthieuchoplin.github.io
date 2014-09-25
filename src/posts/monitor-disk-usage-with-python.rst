.. title: Monitor disk usage with python
.. slug: monitor-disk-usage-with-python
.. date: 2014-09-25 11:41:03 UTC+01:00
.. tags: 
.. link: 
.. description: 
.. type: text

The module to use in python2 is *statvfs* imported from *os*

.. code:: python

  import os
  statvfs = os.statvfs('/')
  statvfs.f_frsize * statvfs.f_blocks     # Size of filesystem in bytes
  statvfs.f_frsize * statvfs.f_bfree      # Actual number of free bytes
  statvfs.f_frsize * statvfs.f_bavail     # Number of free bytes that ordinary users

NB: it is deprecated in python3, the module to use will be `fstat`_ os.fstat

.. _fstat:
   https://docs.python.org/3.3/library/os.html#os.fstat

Source:

- http://stackoverflow.com/questions/4260116/find-size-and-free-space-of-the-filesystem-containing-a-given-file

Better usage:

- http://blog.projectfondue.com/archives/2010/01/21/getting-an-early-warning-of-low-disk-space
