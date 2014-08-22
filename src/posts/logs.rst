.. title: Logs
.. slug: logs
.. date: 2014-08-22 11:29:21 UTC+01:00
.. tags: 
.. link: 
.. description: 
.. type: text

The configuration and especially right permissions will be done in /etc/rsyslog.conf

Bitmask is going to be used so use this doc
://www.cyberciti.biz/faq/unix-linux-bsd-chmod-numeric-permissions-notation-command/Write your post here.

It will be taken into account for the new log files only when we reload rsylog with this commend:

.. code:: bash

  /etc/init.d/rsyslog reload

The old files are still on the old configuration. So, you need to change the right access directly for them with chown and chmod.

Example for vagrant user:

.. code:: bash

  root@openerp-development:/var/log/openerp# chown vagrant:vagrant /var/log/openerp/ -R 
  root@openerp-development:/var/log/openerp# chmod a+r /var/log/openerp/ -R

|
