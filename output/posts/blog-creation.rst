.. title: Blog creation
.. slug: blog-creation
.. date: 2014-05-25 09:30
.. tags: Nikola, blog
.. link: 
.. description: How this website is built
.. type: text

Website hosted from my Github Repository
========================================

It is using `Github Pages <https://pages.github.com/>`__.
Create a repository called *username.github.io*, where username is your username (or organization name) on GitHub and put your website files in there.

Website generation using a Python framework
===========================================

This website is using `Nikola <http://getnikola.com>`__ which is a Python static website generator.
Assuming that you have created a github repository called *username.github.io*, clone it with:

.. code:: bash

  git clone git@github.com:username/username.github.io.git

Then initialize your website with this command:

.. code:: bash

  nikola init username.github.io

where *username.github.io* is the repository you have just cloned.

cd in this directory and execute this command:

.. code:: bash

  nikola build && nikola serve -b

The website will open at the url http://127.0.0.1:8000.

Once you are happy with it, you can deploy to Github with the command:

.. code:: bash

  nikola github_deploy

Posts written using reStructuredText
====================================

Useful cheatsheet for the basics: http://docutils.sourceforge.net/docs/user/rst/cheatsheet.txt
