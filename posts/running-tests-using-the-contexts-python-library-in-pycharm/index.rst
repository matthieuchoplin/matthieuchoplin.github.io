.. title: Running tests using the Contexts python library in Pycharm
.. slug: running-tests-using-the-contexts-python-library-in-pycharm
.. date: 2019-06-07 10:34:06 UTC+01:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text

Using:

- Pycharm CE: https://www.jetbrains.com/pycharm/download/

- Contexts: https://github.com/benjamin-hodgson/Contexts

1) Create a new External Tool
-----------------------------

In Pycharm, go to: Settings/Tools/External Tools

Create a new Tool:

  - "Name": give a distinct name

  - "Program": give the path of where *run-contexts* is in the path where the python interpreter is located for the project (typically a virtual environment)

  - "Arguments": click on "Insert Macro" for this field and select "SelectedText"

  - "Working directory": Where the python project is

2) Create a new Keymap
----------------------

In Pycharm, go to: Settings/Keymap

Search for the "Name" you have defined in 1), select the "External Tool" that you have just created and double click to "Add Keyboard Shortcut", eg "Alt+r"

3) Run tests
------------

Now you can run the tests that you are currently on by pressing the Keymap you have defined in 2), eg "Alt+r" here

