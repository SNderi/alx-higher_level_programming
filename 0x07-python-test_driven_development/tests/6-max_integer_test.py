#!/usr/bin/python3
'''Unittest for 6-max_integer module'''


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''Tests for max_integer function'''
    def test_norm(self):
        '''Using a normal list of integers'''
        list0 = [23, 45, 7, 12, 49]
        self.assertEqual(max_integer(list0), 49)

    def test_rep(self):
        '''Using a list of repeated values'''
        list00 = [6, 6, 6, 6, 6, 6]
        self.assertEqual(max_integer(list00), 6)

    def test_neg(self):
        '''Using a list of negative integers'''
        list1 = [-4, -2, -3, -1, -5]
        self.assertEqual(max_integer(list1), -1)

    def test_empty(self):
        '''Using an empty list'''
        list2 = []
        self.assertEqual(max_integer(list2), None)

    def test_one(self):
        '''Using list with one element'''
        self.assertEqual(max_integer([0]), 0)

    def test_char(self):
        '''Using list with characters'''
        list3 = ['a', 'b', 'c', 'd', 'e']
        self.assertEqual(max_integer(list3), 'e')

    def test_str(self):
        '''Using a list of strings'''
        list4 = ['Hello', 'Welcome', 'To', 'Python']
        self.assertEqual(max_integer(list4), 'Welcome')

    def test_mix(self):
        '''Using a list of mixed types'''
        list5 = [23, 3.5, 'qwerty']
        self.assertRaises(TypeError, max_integer, list5)
        list6 = [4, [4, 6, 7]]
        self.assertRaises(TypeError, max_integer, list6)

    def test_float(self):
        '''Using a list with floats'''
        list7 = [2.6, 8.64, 5.32, 4.67532, 9.872]
        self.assertEqual(max_integer(list7), 9.872)
        list8 = [1, 2.45, 9, 10.76]
        self.assertEqual(max_integer(list8), 10.76)

    def test_not(self):
        '''Using a non-list'''
        # using int
        self.assertRaises(TypeError, max_integer, 5)
        # using tuple
        tup = (2, 3, 4, 5)
        self.assertEqual(max_integer(tup), 5)
        # using a string
        self.assertEqual(max_integer('qwerty'), 'y')

    def test_none(self):
        '''Using none as argument'''
        self.assertRaises(TypeError, max_integer, None)
