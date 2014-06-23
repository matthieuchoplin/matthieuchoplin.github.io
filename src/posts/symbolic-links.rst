.. title: Symbolic links
.. slug: symbolic-links
.. date: 06/04/2014 10:38:08 PM UTC+01:00
.. tags: sysadmin 
.. link: 
.. description: Symbolic likns
.. type: text

Dealing with broken symbolic links
==================================

Find broken symlinks and delete them

.. code:: bash

  $find -L /path/to/check -type l -delete

List them

.. code:: bash

  $find -L /path -type l

If you want to delete them with confirmation first, do

.. code:: bash

  $find -L /path -type l -exec rm -i {} +


Creating symbolik links
=======================

First cd into your directory and then indicate where your symlinks will point

.. code:: bash

    $find /directory_where_yout_symlinks_are/ -maxdepth 1 -type d -exec ln -s  {} \;

If you want to update your existing symlinks, use the **-f** option such as:

.. code:: bash

    $find /home/matt/workspace/unified_repos/erp_core/modules/ -maxdepth 1 -type d -exec ln -sf  {} \;

|
