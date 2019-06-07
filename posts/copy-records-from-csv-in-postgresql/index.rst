.. title: Copy records from csv in postgresql
.. slug: copy-records-from-csv-in-postgresql
.. date: 2014-07-18 16:39:41 UTC+01:00
.. tags: postgresql, sql, copy
.. link: 
.. description: copy csv in sql table
.. type: text

.. code-block:: sql

  CREATE TEMPORARY TABLE original_table_name_temp(like original_table_name including all);
  COPY original_table_name_temp FROM 'path_of_your_csv';

Source: http://postgresql.1045698.n5.nabble.com/reverse-strpos-td1891709.html
