.. title: Context Manager in Python
.. slug: context-manager-in-python
.. date: 2014-10-11 13:50:58 UTC+01:00
.. tags: python
.. link: 
.. description: 
.. type: text

The keyword *with*
==================

The context manager is going to be used with the keyword *with* such as:

.. code:: python

  with MyContextManager as context_var:
      # here the statement is going to evaluate the methods
      # __enter__ and __exit__ of the class MyContextManager.
      # The value returned by __enter__ is going to be assigned
      # to the variable "context_var".


The context manager can be defined as a class
=============================================

Two essential methods are required for making the class a context manager:

- *__enter__(self)*
  
  Defines what the context manager should do at the **beginning of the block** created by the with statement.
  Note that the return value of __enter__ is bound to the target of the with statement, or the name after the as.

- *__exit__(self, exception_type, exception_value, traceback)*
  
  Defines what the context manager should do **after its block has been executed (or terminates)**. 
  It can be used to handle exceptions, perform cleanup, or do something always done immediately after the action in the block. 
  If the block executes successfully, exception_type, exception_value, and traceback will be None. Otherwise, you can choose to handle the   exception or let the user handle it; if you want to handle it, make sure __exit__ returns True after all is said and done. 
  If you don't want the exception to be handled by the context manager, just let it happen.

Example
=======

.. code:: python

  class MyContextManager(object):
      def __enter__(self):
          print '__enter__()'
          return self
      def __exit__(self, exception_type, exception_value, traceback):
          print '__exit__()'

  with MyContextManager() as context_var:
      print 'Doing work in the context'

Where the output is:

.. code:: bash

  __enter__()
  Doing work in the context
  __exit__()

The Context Manager can also be defined as a Generator
======================================================

Here, we use the contextlib library and the module contextmanager.

The equivalent of the example above would be:

.. code:: python

  import contextlib

  @contextlib.contextmanager
  def mycontextmanager():
      print "__enter__"
      try:
          yield
      finally:      
          print "__exit__"

  with mycontextmanager() as context_var:
      print 'Doing work in the context'

First we use the decorator *@contextmanager* to indicate to Python that the function will be a context manager.

Then, we do a *try/finally* (it is not automatic like with __enter__ and __exit__).

The word *yield* split the code in two parts: 

- everything that is before  *yield* is similar to what we had above in  *__enter__*

- everything that is after is similar to *__exit__*

The content (the returned value) of *yield* is taken in the variable 'context_var' here defined with the key word *as*.
