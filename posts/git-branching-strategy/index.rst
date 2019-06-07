.. title: Git branching strategy
.. slug: git-branching-strategy
.. date: 2014-07-13 12:44:49 UTC+01:00
.. tags: git
.. link: 
.. description: 
.. type: text

Git Branching strategy
======================

The git-flow strategy
---------------------



Very nice cheatsheet: http://danielkummer.github.io/git-flow-cheatsheet/

The centralized worklow
-----------------------

Like Subversion, the Centralized Workflow uses a central repository to serve as the single point-of-entry for all changes to the project. Instead of trunk, the default development branch is called master and all changes are committed into this branch. This workflow doesn’t require any other branches besides master.

Pros
~~~~

Developers are always working on the last version of the code. 

Cons
~~~~

If some code breaks something, the whole process is stuck, no release can be done.

Feature Branch Workflow
-----------------------

The core idea behind the Feature Branch Workflow is that all feature development should take place in a dedicated branch instead of the master branch. This encapsulation makes it easy for multiple developers to work on a particular feature without disturbing the main codebase. It also means the master branch will never contain broken code, which is a huge advantage for continuous integration environments.

Encapsulating feature development also makes it possible to leverage pull requests, which are a way to initiate discussions around a branch. They give other developers the opportunity to sign off on a feature before it gets integrated into the official project. Or, if you get stuck in the middle of a feature, you can open a pull request asking for suggestions from your colleagues. The point is, pull requests make it incredibly easy for your team to comment on each other’s work.

source: https://www.atlassian.com/git/workflows
