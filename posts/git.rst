.. title: Git
.. slug: git
.. date: 06/06/2014 05:09:03 PM UTC+01:00
.. tags: git
.. link: 
.. description: 
.. type: text


Nice display of the current tree
================================


.. code-block:: bash

 git log --graph --all --format=format:"%x09%C(yellow)%h%C(reset) %C(green)%ai%x08%x08%x08%x08%x08%x08%C(reset) %C(bold
 white)%cn%C(reset)%C(green)%d%C(reset)%n%x09%C(white)%s%C(reset)" --abbrev-commit "$@"

An alternative:

.. code-block:: bash

  git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit

You can also make an alias. Copy and paste the line below on your terminal:

.. code-block:: bash

  git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

And every time you need to see your log, just type in

.. code-block:: bash

  git lg

Or, if you want to see the lines that changed

.. code-block:: bash

  git lg -p

Source: https://coderwall.com/p/euwpig

Simply add color to your git environment:

.. code-block:: bash

  git config --global color.ui auto

Source: http://git-scm.com/book/en/Customizing-Git-Git-Configuration

Tutorial
========

Learn git from your browser: https://try.github.io/levels/1/challenges/1

Delete current tag
==================

.. code-block:: bash

  git tag -d 12.15
  git push origin :refs/tags/12.15

