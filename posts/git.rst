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

NB: If you want to see a list of aliases set up on your linux box, just type *alias* at the prompt.

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

Stash current work
==================

.. code-block:: bash

  git stash save
  git stash pop

Push
====

To avoid doing all the time:

.. code-block::

  git push origin <your-feature-branch>

You can do:

.. code-block::

  git push origin <your-feature-branch> -u

You next, you will just have to do:

.. code-block::

  git push

Find which commit is breaking the test with 'git bisect'
========================================================

You may be in situation where you come back from holidays and find the tests that were passing before broken.

Git can help to find which commit produced the failure.

To start bisect, run:

.. code-block::

  git bisect start

You know that the tests are failing so you indicate it with:

.. code-block::

  git bisect bad

You checkout an earlier revision when you know that the tests were passing (git log can help):

.. code-block::

  git checkout <the_failing_revision>

Then run the tests, and if they are passing, indicate it:

.. code-block::

  git bisect good

Once you have indicated that once it was bad and once it was good. You can leave git bisect do the job automatically:

.. code-block::

  git bisect run <command_that_run_the_tests>

You can now grab a coffee and come back few minutes later to see what commit made the tests failed.

Sources: 

- first it was JB: http://tartley.com/

- http://git-scm.com/docs/git-bisect

- http://www.askbjoernhansen.com/2010/04/30/git_bisect_mini_tutorial.html

