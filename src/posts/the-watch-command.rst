.. title: The watch command
.. slug: the-watch-command
.. date: 06/05/2014 03:59:51 PM UTC+01:00
.. tags: 
.. link: 
.. description: 
.. type: text

.. code:: bash

  watch -n1 ' ps aux | grep what_you_want'


Something interesting when combined with svc:

.. code:: bash

  cd /etc/service # or wherever svc (supervise) is installed
  watch svstat *

It will monitor every 2 seconds the state of your service.

Monitor the queries being run in real time:

.. code:: bash

 watch -n 1 'sudo -u postgres psql --tuples-only --command "SELECT datname, procpid, date_trunc(\$\$second\$\$, age(current_timestamp, xact_start)), current_query FROM pg_stat_activity;"'

Source: http://kevin.deldycke.com/2011/10/postgresql-commands/
