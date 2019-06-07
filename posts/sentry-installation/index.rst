.. title: Sentry installation
.. slug: sentry-installation
.. date: 2014-09-24 22:03:47 UTC+01:00
.. tags: 
.. link: 
.. description: 
.. type: text


Create a directory called sentry:

.. code:: bash

  # mkdir /opt/sentry && cd /opt/sentry

Create a virtual environment and activate it:

.. code:: bash

  # virtualenv sentry && source /opt/sentry/sentry/bin/activate

Install Sentry:

.. code:: bash

  # easy_install -UZ sentry[postgres]
  # easy_install -UZ sentry

Initialize the conifguration

.. code:: bash

  # sentry init /opt/sentry/sentry.conf.py

In the configuration file /opt/sentry/sentry.conf.py, you are going to change:

- the database configuration such as:

.. code:: python

  DATABASES = {
    'default': {
                  'ENGINE': 'django.db.backends.postgresql_psycopg2',
                  'NAME': 'sentry',
                  'USER': 'sentry',
                  'PASSWORD': 'sentry',
                  'HOST': 'localhost',
                  'PORT': '',
               }
             }

- And the url:

.. code:: python

  SENTRY_URL_PREFIX = 'http://192.168.50.4:9000' # the ip address of the server


Install postgresql

.. code:: bash

  # apt-get install postgresql-9.3

Create a user for sentry:

.. code:: bash

  # sudo su postgres
  $ createuser sentry
  $ psql template1
  # alter role sentry with password 'sentry';

Create the database as postgres:

.. code:: bash

  # createdb -E utf-8 sentry

Create the initial schema using the upgrade command as root:

.. code:: bash

  # sentry --config=/opt/sentry/sentry.conf.py upgrade

If you did not create the user on the first run, you can correct this by doing the following:

.. code:: bash

  # sentry --config=/opt/sentry/sentry.conf.py createsuperuser
  # sentry --config=/opt/sentry/sentry.conf.py repair --owner=sentry

You can start Sentry with:

.. code:: bash

  # sentry --config=/opt/sentry/sentry.conf.py start


