.. title: The watch command
.. slug: the-watch-command
.. date: 06/05/2014 03:59:51 PM UTC+01:00
.. tags: 
.. link: 
.. description: 
.. type: text

.. code:: bash

  watch -n1 ' ps aux | grep what_you_want'


Something interesting when combined with svc:

.. code:: bash

  watch svstat *

It will monitor every 2 seconds the state of your service.


