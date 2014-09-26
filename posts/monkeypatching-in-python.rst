.. title: Monkeypatching in python
.. slug: monkeypatching-in-python
.. date: 2014-09-26 10:55:04 UTC+01:00
.. tags: 
.. link: 
.. description: 
.. type: text

A MonkeyPatch is a piece of Python code which extends or modifies other code at runtime (typically at startup). MonkeyPatching? would be the practice of writing, or running, a monkeypatch.

A simple example looks like this:

.. code:: python

  from SomeOtherProduct.SomeModule import SomeClass
  def speak(self):
      return "ook ook eee eee eee!" 

  SomeClass.speak = speak 


In this example, if *SomeClass* did not already have a *speak()* method, it does now :-) If it had a speak() method before, **the new code has replaced the old method definition**.

Source: https://web.archive.org/web/20120730014107/http://wiki.zope.org/zope2/MonkeyPatch
