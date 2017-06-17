.. title: Skype with Python
.. slug: skype-with-python
.. date: 2017-06-17 10:28:07 UTC+01:00
.. tags: skype
.. category: api
.. link: 
.. description: use skype with python
.. type: text

Create the virtualenv
=====================

.. code:: bash

  virtualenv skype_venv -p /usr/bin/python2.7 --system-site-packages

Note that I am specyfying the python2 interpreter, and using the system site packages (`the python libraries already installed <https://virtualenv.pypa.io/en/stable/userguide/#the-system-site-packages-option/>`__).


Install the Skype4Py library
============================

You can install it with pip.

.. code:: bash

  source skype_venv/bin/activate
  pip install Skype4Py
  
Note that this library allows us to control Skype client application. It means that you will need to have a skype client installed with which you will interact using python.


Source: https://pypi.python.org/pypi/Skype4Py/


Use the library
===============

Open your skype client and launch a python prompt

.. code:: bash

  >>> import Skype4Py
  >>> skype = Skype4Py.Skype()
  >>> skype.Attach()
  
At this point, the Skype client will ask for authorization:

.. image:: http://imgur.com/gKj46yz.png
   :alt: Skype4Py authorisation
   :align: center
   :class: well-large

And now, you can for example get the list of all your contacts:

.. code:: bash

  >>> print 'Your full name:', skype.CurrentUser.FullName
  >>> print 'Your contacts:'
  >>> for user in skype.Friends:
          print '    ', user.FullName

To go further:

https://leakforums.net/thread-641974?tid=641974&&tid=641974&&pq=2

https://sinister.ly/Thread-Tutorial-Create-your-own-SkypeBOT

https://media.readthedocs.org/pdf/sevabot-skype-bot/latest/sevabot-skype-bot.pdf

