.. title: Unresponsive process
.. slug: unresponsive-process
.. date: 2014-06-20 10:08:44 UTC+01:00
.. tags: 
.. link: 
.. description: 
.. type: text


.. code:: bash

  pkill -9f process-name

Example:

.. code:: bash

  pkill -9f filezilla

If you have launch a command that you cannot directly stopped with usually *ctrl+c*, 
you can always put the process in the background with *ctrl+z* and then use the 
*jobs* command to list the job (command) that you have launched.
Then, you have the number of the job and you can kill it with the command 
*kill %<number_of_the_job>*.

Example:

.. code:: bash

  $ sleep 100
  ^Z
  [1]+  Stopped                 sleep 100
  $ jobs
  [1]+  Stopped                 sleep 100
  $ kill %1
  $ jobs
  [1]+  Terminated              sleep 100
  $ jobs
  $

