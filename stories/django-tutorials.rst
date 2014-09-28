.. title: Django tutorials
.. slug: django-tutorials
.. date: 2014-09-28 12:51:00 UTC+01:00
.. tags: 
.. link: 
.. description: 
.. type: text

We are going to create a django project that will be version controlled with **git**.

Create a git repository
=======================

Make sure that git is installed with:

.. code:: bash

  $ sudo apt-get install git

Then you can initialise the git repository

.. code:: bash

  $ mkdir myproject
  $ cd myproject
  $ git init


Create a virtual environment
============================

To do that you can use virtualenv

.. code:: bash

  $ sudo apt-get install virtualenv

virtualenv is a tool to create isolated Python environments.

Source: http://virtualenv.readthedocs.org/

Within *myproject* created above, you can create the virtual environment with:

.. code:: bash

  $ virtualenv venv

The directory structure within myproject should look like:

.. code:: bash

  .
  └── venv
      ├── bin
      ├── include
      ├── lib
      └── local

NB: you can easily view the directory structure with the command *tree* (sudo apt-get install tree).

Then, we want to activate the virtual environment:

.. code:: bash

  $ source venv/bin/activate

NB: to quit the virtual environment, use *deactivate*

Configure the virtual environment
=================================

This environment will be used only for this project, we are going to install the dependancies within this environment so that we can easily reinstall them with pip and a requirement.txt file.

If you do a *pip freeze*, you will see all the libraries installed.

If you install a new library, you will see that it has been added if you do a *pip freeze* again.

For instance, we want to install south, django-registration and stripe:

.. code:: bash

  $ pip install django==1.5.1 south django-registration stripe
  $ pip freeze
  $ pip freeze
  Django==1.5.1
  South==1.0
  argparse==1.2.1
  django-registration==1.0
  requests==2.4.1
  stripe==1.19.0
  wsgiref==0.1.2

NB: you can precize the version you want. Here, we want to use django with the version 1.5.1

We are going to keep the output of *git freeze* in a requirements.txt file:

.. code:: bash

  $ pip freeze > requirement.txt

That way, we can recreate the virtual environment easily with:

.. code:: bash

  $ pip install -r requirement.txt

The virtual environment is going to take a lot of place in the git repository, so we are going to untrack it.

To do that, we are going to create a *.gitignore* file.

.. code:: bash

  $ cat .gitignore
  venv

Create your django project
==========================

.. code:: bash

  $ django-admin.py startproject myproject

Check that it is installed correctly by running the server:

.. code:: bash

  $ python manage.py runserver

and in your browser, go to the url http://127.0.0.1:8000/


