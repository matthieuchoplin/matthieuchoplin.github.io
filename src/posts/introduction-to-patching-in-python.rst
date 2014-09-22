.. title: Introduction to patching in Python
.. slug: introduction-to-patching-in-python
.. date: 2014-09-18 16:36:00 UTC+01:00
.. tags: 
.. link: 
.. description: 
.. type: text

Simple example
==============


.. code-block:: python

    @patch('time.sleep')

    def test_do_something(mock_sleep):
       mock_sleep.return_value = True
       do_something()
 
    test_do_something()
    ok
    from mock import patch
    import time
    def do_something():
        if time.sleep(100):
            print 'ok'
        else:
            print 'ko'
   
    @patch('time.sleep')
    def test_do_something(mock_sleep):
        mock_sleep.return_value = True
        do_something()
   
    @patch('time.sleep')
    def test_do_something(mock_sleep):
        mock_sleep.return_value = False
        do_something()
   
    test_do_something()
    ko
