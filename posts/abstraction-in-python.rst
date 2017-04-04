.. title: Abstraction in python
.. slug: abstraction-in-python
.. date: 2017-04-04 12:43:16 UTC+01:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text


Abstraction in python
=====================

For example, when copying files:

.. code:: python

  import shutil
  shutil.copy('file.txt', 'copy.txt')


It is much more abstract (and simpler) to use the *shutil* library than:

.. code:: python

  with open(src, 'rb') as fsrc:
      with open(dst, 'wb') as fdst:
          while True:
              buf = fsrc.read(buf_size)
              if not buf:
                  break
              fdst.write(buf)
      
