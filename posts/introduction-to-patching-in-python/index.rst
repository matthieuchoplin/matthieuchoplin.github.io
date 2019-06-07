.. title: Introduction to patching in Python
.. slug: introduction-to-patching-in-python
.. date: 2014-09-18 16:36:00 UTC+01:00
.. tags: 
.. link: 
.. description: 
.. type: text


If you want to use it in a version earlier than python3.3, you need yo install it:

.. code:: bash

  sudo pip install mock

Simple example
==============

Code to test:

.. code-block:: python

  import time
  def do_something():
      if time.sleep(100):
          print 'ok'
      else:
          print 'ko'

Actual test:

.. code-block:: python

  from mock import patch
  @patch('time.sleep')
  def test_do_something1(mock_sleep):
      mock_sleep.return_value = True
      do_something()
  
  @patch('time.sleep')
  def test_do_something2(mock_sleep):
      mock_sleep.return_value = False
      do_something()

Results:

.. code:: bash

  >>> test_do_something1()
  ok
  >>> test_do_something2()
  ko

Source:

- https://pypi.python.org/pypi/mock
