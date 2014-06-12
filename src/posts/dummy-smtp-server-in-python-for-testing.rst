.. title: Dummy smtp server in Python for testing
.. slug: dummy-smtp-server-in-python-for-testing
.. date: 2014-06-12 18:19:30 UTC+01:00
.. tags: python
.. link: 
.. description: 
.. type: text


.. code:: bash

    sudo python -m smtpd -n -c DebuggingServer localhost:25

The sudo is needed as you can’t bind to a port number lower than 1024 as a normal user.

Source: http://www.euperia.com/development/test-smtp-with-a-dummy-server-in-python/460
