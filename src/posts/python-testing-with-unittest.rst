.. title: Python testing with doctest and unittest
.. slug: python-testing-with-unittest
.. date: 2014-11-12 16:02:45 UTC+01:00
.. tags: python, testing
.. link: 
.. description: 
.. type: text

The problem:
------------
We want to create a function that is able to determine whether a string is a palindrome.

A palindrome is a word that is read the same from front-to-back and from back-to-front.

For instance, the words "noon" and "racecar" are both palindromes.

Algorithm:
----------

Reverse the string.

Compare the reversed string to the original string.

Recipe for designing functions:
-------------------------------

.. _Narrative tests are lousy tests: http://bemusement.org/narrative-tests

.. _Tests are code and doctests are not: http://bemusement.org/doctests-arent-code


0. Give the function a name

1. Examples

2. Type Contract

3. Header

4. Description

5. Body

6. Test
   
First, we will see the python module *doctest* which is good for having an up to date documentation.

But using *doctest* is not recommended for testing a whole program. This is why we will see the python module *unittest* which is more relevant.

For more about the cons of using *doctest*: `Narrative tests are lousy tests`_ and `Tests are code and doctests are not`_.

Create the file *palindrome.py*:

.. code:: python

  #! /usr/bin/python2.7

  def is_palindrome(s):
      """(str) -> bool

      Return True if and only if s is a palindrome.

      >>> is_palindrome('noon')
      True
      >>> is_palindrome('racecar')
      True
      >>> is_palindrome('dented')
      False
      """
      return reverse(s) == s

  def reverse(s):
      """(str) -> str

      Return the reversed string.

      >>> reverse('hello')
      'olleh'
      >>> reverse('a')
      'a'
      """
      rev = ''
      # for each character in s, add the character at the beginning of rev.
      for char in s:
          rev = char + rev
      return rev

  import doctest
  doctest.testmod()



We want to separate the tests from the main program and use the python *unittest* module.

Create the file test_palindromes.py

.. code:: python

  #! /usr/bin/python2.7

  import unittest
  import palindromes


  class TestPalindrome(unittest.TestCase):

      def test_is_palindrome_true(self):
          value = palindromes.is_palindrome('racecar')
          self.assertEquals(value, True)

      def test_is_palindrome_false(self):
          value = palindromes.is_palindrome('dedent')
          self.assertEquals(value, False)

      def test_reverse_normal(self):
          value = palindromes.reverse('hello')
          self.assertEquals(value, 'olleh')

      def test_reverse_error(self):
          list_of_bad_value = [
          123,
          None,
          ]
          for bad_value in list_of_bad_value:
              self.assertRaises(
                  TypeError,
                  palindromes.reverse, 
                  bad_value 
              )

  if __name__ == '__main__':
      unittest.main()

Choosing test cases to test
---------------------------

- Size: For collections, test with an empty collection, a collection with 1 item, the smallest interesting case, and a
  collection with several items

- Dichotomies: Vowels/Non Vowels, even/odd, positive/negative, empty/full, and so on.

- Boundaries: If the function behaves differently for values near a particular threshold, test at that threshold.

- Order: If the function behaves differently when the values are in different orders, identify and test each of those
  orders.


Source: https://class.coursera.org/programming2-001
