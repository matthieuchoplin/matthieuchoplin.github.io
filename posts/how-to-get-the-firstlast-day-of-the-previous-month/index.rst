.. title: How to get the first/last day of the previous month?
.. slug: how-to-get-the-firstlast-day-of-the-previous-month
.. date: 2017-04-05 16:55:47 UTC+01:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text

How to get first/last day of the previous month?
================================================

.. code:: python

   >>> from datetime import date
   >>> from dateutil.relativedelta import relativedelta
   >>> today = date.today()
   >>> d = today - relativedelta(months=1)
   >>> date(d.year, d.month, 1)
   datetime.date(2008, 12, 1)
   >>> date(today.year, today.month, 1) - relativedelta(days=1)
   datetime.date(2008, 12, 31)
   >>>
