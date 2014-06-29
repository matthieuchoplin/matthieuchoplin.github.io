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

Website generation using a Python framework: Nikola
===================================================

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

To deploy to Github, change the file conf.py such as:

.. code:: bash
 
  GITHUB_DEPLOY_BRANCH = 'master'


Once you are happy with it, you can deploy to Github with the command:

.. code:: bash

  nikola github_deploy

Posts written using reStructuredText
====================================

Useful cheatsheet for the basics: http://github.com/ralsina/rst-cheatsheet/raw/master/rst-cheatsheet.pdf

This is also a way to learn how to use Vim. Since Nikola 7.0.1, you can use the -e option when creating a new post.
But before, you need to set up a default editor.
If you want to use vim, you can first locate it:

.. code:: bash

  which vim

Then you can use it in the export variable:

.. code:: bash

  export EDITOR=/usr/bin/vim

Download a pre-built template from bootswatch
=============================================

.. code:: bash

  nikola bootswatch_theme -n custom_theme -s spruce -p bootstrap3

Upgrading Nikola
================

Since Nikola can be installed with Pip, you can use the following command:

.. code:: bash

  pip install -U nikola

As a reminder, pip is installed using setuptools and easyinstall:

.. code:: bash

  sudo easy install pip

To upgrade pip:

.. code:: bash

  sudo easy_install -U pip

To downgrade pip to a previous version:

.. code:: bash

  sudo easy_install pip==1.2.1

|

Add your own domain
===================

Log in to your domain provider website and change the forwarding value to the website url provided by Github-pages e.g.
username.github.io

