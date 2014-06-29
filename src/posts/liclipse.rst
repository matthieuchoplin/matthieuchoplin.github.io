.. title: Liclipse as Python editor
.. slug: installing-eclipse-luna
.. date: 2014-06-28 13:31:05 UTC+01:00
.. tags:python, editor 
.. link: 
.. description: 
.. type: text

Installation
============

.. _liclipse: http://brainwy.github.io/liclipse/index.html

Liclipse seems to be the IDE to go for Python edition if you come from the Eclipse + pydev plugin world: Liclipse_ (Lightweight Eclipse)

It comes with pydev and gedit plugin already integrated.

On ubuntu 12.04, you need to install the following Java dependencies before being able to launch it.

.. code:: bash

  sudo add-apt-repository ppa:webupd8team/java
  sudo apt-get update
  sudo apt-get install oracle-java7-installer

It'll keep your java 7 installation up to date.

To automatically set up the Java 7 environment variables JAVA_HOME and PATH:

.. code:: bash

  sudo apt-get install oracle-java7-set-default


Source: http://stackoverflow.com/questions/16263556/installing-java-7-on-ubuntu

Importing a Git project
=======================

If the project is already cloned in your local environment, then click "File" | "Import"| Select "Git" | "Project from Git"| "Existing local Repository" and select the project you want.

Else, you can also clone the project from Liclipse by doing "File" | "Import"| Select "Git" | "Project from Git"| "Clone Uri".

Using eGit
==========

.. _documentation: http://wiki.eclipse.org/EGit/User_Guide

Egit enables you to do the same as what git already enables but in a much more friendly way.

Because egit is already integrated in Jiclipse, you already have all its features. I recommend the documentation_. Most of the egit features are available when you right click on a file and select "Team".

- Annotations: When you are editing a file, you can access it by right clicking the file, selecting "Team" and "Show annotations".

  Similar to:

.. code:: bash

  git blame

- History: When you are editing a file, you can access it by right clicking the file, selecting "Team" and "Show in History".

  Similar to:

.. code:: bash

  git log -p

Using Pydev
===========

.. _pydev: http://pydev.org/

pydev_ is the Python IDE in Eclipse.

The debugging mode is very easy to use:

- Place your breakpoints where you want by double clicking in the margin of the files.

- Edit the "Run configuration" according to your project settings.

- Click on "Run" | "Debug as" and select the configuration you created.

Alternatives
============

Development environments for Python are listed here: http://docs.python-guide.org/en/latest/dev/env/

As text Editors, Vim is also a good choice combined with the following plugins:

.. _indent: http://www.vim.org/scripts/script.php?script_id=974
.. _syntax: http://www.vim.org/scripts/script.php?script_id=790
.. _vim-pep8: https://github.com/nvie/vim-pep8
.. _vim-pyflakes: https://github.com/nvie/vim-pyflakes
.. _syntastic: https://github.com/scrooloose/syntastic
.. _python-mode: https://github.com/klen/python-mode
.. _supertab: http://www.vim.org/scripts/script.php?script_id=1643

- indent_
- syntax_
- vim-pep8_
- vim-pyflakes_
- syntastic_
- python-mode_
- supertab_

