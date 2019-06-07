.. title: Tipue search
.. slug: tipue-search
.. date: 07/19/2014 01:05:20 PM UTC+01:00
.. tags: Nikola
.. link: 
.. description: Introducing Tipue search
.. type: text

As the number of posts is growing, I think that having a search engine within the website is now relevant. This post only shows what I am using for that.

Instead of using an external search engine such as Google or DuckDuckGo, you have a plugin in Nikola than enables searching on the client side by using jQuery.

Assuming you have installed Nikola > v7.0, you can install the plugin like this:

.. code-block:: python

  nikola plugin -i localsearch

It will give you a configuration sample to paste in your config.py file.

Source: http://plugins.getnikola.com/#localsearch
