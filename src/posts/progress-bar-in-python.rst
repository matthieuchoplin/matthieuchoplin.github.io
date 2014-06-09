.. title: Progress bar in python
.. slug: progress-bar-in-python
.. date: 06/05/2014 09:25:49 AM UTC+01:00
.. tags: python
.. link: 
.. description: 
.. type: text

Writing '\r' will move the cursor back to the beginning of the line.

This displays a percentage counter:

.. code:: python

    import time,sys
    for i in range(100):
        time.sleep(1)
        sys.stdout.write("\r%d%%" %i)
        sys.stdout.flush()

Sourcce: http://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
