.. title: Psycopg2
.. slug: psycopg2
.. date: 07/19/2014 12:14:20 AM UTC+01:00
.. tags: 
.. link: 
.. description: 
.. type: text

Connect to your postgresql database with psycopg2
=================================================

.. code:: python

  import psycopg2
  conn = psycopg2.connect("dbname='template1' user='dbuser' host='localhost' password='dbpass'")
  cur = conn.cursor()

Once you have the cursor of the database, you can execute queries with:

.. code:: python

  cr.execute(your_query;) 

Source: https://wiki.postgresql.org/wiki/Psycopg2_Tutorial
