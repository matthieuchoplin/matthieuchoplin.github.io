.. title: Extract list of installed packages
.. slug: extract-list-of-installed-packages
.. date: 06/05/2014 03:03:35 PM UTC+01:00
.. tags: 
.. link: 
.. description: 
.. type: text

.. code:: bash
  
  dpkg-query -l | awk '{print $2 $3}'

Notice the combinatin of dpkg-query and awk!
