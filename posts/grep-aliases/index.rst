.. title: Grep aliases
.. slug: grep-aliases
.. date: 2014-10-10 10:31:27 UTC+01:00
.. tags: grep, bash
.. link: 
.. description: 
.. type: text

In .bashrc

.. code:: bash

  # recursive search in files

  function grp {

      GREP_OPTIONS="-rI --color --exclude-dir=\.bzr --exclude-dir=\.git --exclude-dir=\.hg --exclude-dir=\.svn --exclude=tags $GREP_OPTIONS" grep "$@"

  }



  # recursive search in Python source

  function grpy {

    GREP_OPTIONS="--exclude-dir=build --exclude-dir=dist --include=*.py $GREP_OPTIONS" grp "$@"

  }

Use:

.. code:: bash

  $ grp WORD .

Or 

.. code:: bash

  $ grpy to just search in python files


Then reload bashrc with:

.. code:: bash

  $ . ~/.bashrc

Thank you JB!! (http://tartley.com/)
