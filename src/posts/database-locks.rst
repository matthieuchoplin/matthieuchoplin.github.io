.. title: Database locks
.. slug: database-locks
.. date: 07/19/2014 12:27:04 AM UTC+01:00
.. tags: postgresql, lock
.. link: 
.. description: 
.. type: text

To find a lock in the DB:
=========================

.. code-block:: postgresql

  select * from pg_stat_activity where waiting='t';

Fix the lock:

.. code-block:: postgresql

  select pg_cancel_backend(pid int)

Where "pid int" is the pid you find with pg_stat_activity
Sources: 
- http://www.postgresql.org/docs/9.2/static/functions-admin.html
- http://wiki.postgresql.org/wiki/Lock_Monitoring
- http://chrismiles.info/systemsadmin/databases/articles/viewing-current-postgresql-queries/
