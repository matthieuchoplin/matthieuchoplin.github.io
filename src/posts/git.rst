.. title: Git
.. slug: git
.. date: 06/06/2014 05:09:03 PM UTC+01:00
.. tags: git
.. link: 
.. description: 
.. type: text


Nice display of the current tree
================================

.. code:: bash

  git log --graph --all --format=format:"%x09%C(yellow)%h%C(reset) %C(green)%ai%x08%x08%x08%x08%x08%x08%C(reset) %C(bold
  white)%cn%C(reset)%C(magenta)%d%C(reset)%n%x09%C(white)%s%C(reset)" --abbrev-commit "$@"