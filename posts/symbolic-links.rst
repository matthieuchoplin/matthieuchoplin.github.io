.. title: Symbolic links
.. slug: symbolic-links
.. date: 06/04/2014 10:38:08 PM UTC+01:00
.. tags: sysadmin 
.. link: 
.. description: Symbolic likns
.. type: text


Find broken symlinks and delete them

.. code:: bash

  $find -L /path/to/check -type l -delete

List them

.. code:: bash

  $find -L /path -type l

If you want to delete them with confirmation first, do

.. code:: bash

  find -L /path -type l -exec rm -i {} +


