.. title: Control the screen brightness in Ubuntu
.. slug: control-the-screen-brightness-in-ubuntu
.. date: 2016-06-23 23:07:34 UTC+01:00
.. tags: ubuntu
.. link: 
.. description: screen brigthness not working from the keyboard 
.. type: text

Controlling the brightness of your screen not working after installing Ubuntu on a laptop equipped with an Intel graphics card?

You can solve that through the Xorg configuration.

First, look at your PCI bus, in order to identify your card:

.. code:: bash

  $ lspci | grep -i vga

  00:02.0 VGA compatible controller: Intel Corporation 2nd Generation Core Processor Family Integrated Graphics Controller (rev 09)

That's how it looks on my machine. I am interested in the Intel card, so I need to remember its bus id *00:02.0*.

Next you need to create the config file:

.. code:: bash

  $ sudo nano /usr/share/X11/xorg.conf.d/20-intel.conf

and put the following content in, which will tell the xorg driver to use intel_backlight: 

.. code:: bash

  Section "Device"  
          Identifier      "card0"
          Driver          "intel"
          Option          "Backlight" "intel_backlight"
          BusID           "PCI:0:2:0"
  EndSection

Please note that the BusID should match.

Save, restart your Xorg:

- find which display manager your ubuntu is having with following command:

.. code:: bash

  $ cat /etc/X11/default-display-manager

- and, for Ubuntu with LightDM:

.. code:: bash

  $ sudo restart lightdm 


It should then work.

Source: 
- https://float-middle.com/screen-brightness-on-intel-ubuntu-14-04/
- http://askubuntu.com/questions/1220/how-to-restart-x-window-server-from-command-line
