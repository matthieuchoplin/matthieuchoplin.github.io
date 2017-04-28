.. title: Using pip with different python versions
.. slug: using-pip-with-different-python-versions
.. date: 2017-04-28 11:33:19 UTC+01:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text

Using pip with different python version
=======================================

Let us say that you have python2 and python3 installed.

Use pip for python2

.. code:: bash

    pip2.6 install otherpackage
    pip2.7 install mybarpackage

      
You can see which version of python pip is using by default with:

.. code:: bash

    pip -V
    
Source: http://stackoverflow.com/questions/6504810/how-to-install-lxml-on-ubuntu?answertab=votes#tab-top