.. title: VIM
.. slug: vim
.. date: 06/04/2014 10:51:32 PM UTC+01:00
.. tags: 
.. link: 
.. description: 
.. type: text



VIM basics
==========

The built in tutorial of Vim is very useful to know the basics. To launch it simply type the following in your terminal:

.. code:: bash
  
  $vimtutor

It will launch some lessons with an approach 'learning by doing'.

Configuration
=============

The ~/.vimrc file provides Vim's default configuration

vim memento
===========

Simple vimrc
------------

.. code:: bash

  set textwidth=79  " lines longer than 79 columns will be broken
  set shiftwidth=4  " operation >> indents 4 columns; << unindents 4 columns
  set tabstop=4     " a hard TAB displays as 4 columns
  set expandtab     " insert spaces when hitting TABs
  set softtabstop=4 " insert/delete 4 spaces when hitting a TAB/BACKSPACE
  set shiftround    " round indent to multiple of 'shiftwidth'
  set autoindent    " align the new line indent with the previous line

Jump to function definition:
----------------------------

.. code:: bash

  g + *

Highlight variable under cursor:
--------------------------------

.. code:: bash

  :autocmd CursorMoved * exe printf('match IncSearch /\V\<%s\>/', escape(expand('<cword>'), '/\'))

Move cursor to its last position:
---------------------------------

The quickest way is to hit either:

.. code:: bash

  ''

(two apostrophes) or:

.. code:: bash

  ``

(two backticks). Note that the difference is that the backtick goes to the same location on the line, whereas the apostrophe goes to the start of the line. On a UK keyboard, the apostrophe is more accessible, so I tend to use that one. There are loads of useful marks like this, see :help mark-motions.
For some other motions (not 2j I think), there's also the jump-list that lets you navigate back and forth among a number of motions.  Ctrl-O and Ctrl-I do this navigation, but see :help jump-motions for more information.

Line numbers
------------

To display line numbers along the left side of a window, type any one of the following command while using text editor:

.. code:: bash

  :set number

Go to line
----------

.. code:: bash

  :42

where 42 is the number of line you want to go

Split the screen
----------------

.. code:: bash

  :vsp

Paste from another application into vim
---------------------------------------

To avoid indentation issue:

.. code:: bash

  :set paste

