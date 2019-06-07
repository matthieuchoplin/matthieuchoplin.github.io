.. title: Associate hostname with IP address
.. slug: associate-hostname-with-ip-address
.. date: 2014-09-24 10:37:55 UTC+01:00
.. tags: 
.. link: 
.. description: 
.. type: text

You can do that in the /etc/hosts file:

.. code:: bash

  127.0.0.1       localhost
  192.168.1.10    foo.mydomain.org       foo
  192.168.1.13    bar.mydomain.org       bar
  146.82.138.7    master.debian.org      master
  209.237.226.90  www.opensource.org

So, from the command line, you can do:

.. code:: bash

  ping foo.mydomain.org

Or:

.. code:: bash
  
  ssh user@foo

Source: http://linux.die.net/man/5/hosts
