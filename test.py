#!/bin/env python


import unittest

from bookland import *

class Test_rgbtocmyk(unittest.TestCase):
    '''RGB to CMYK conversion. This only tests the formula,
       not the actual color conversion, which can be device dependent.'''
    def test_00(self):
        self.assertEqual(rgbtocmyk((0,0,0)),(0,  0,  0,  1.))
    def test_01(self):
        self.assertEqual(rgbtocmyk((0,0,1)),(1., 1., 0,  0))
    def test_02(self):
        self.assertEqual(rgbtocmyk((0,1,0)),(1., 0,  1., 0))
    def test_03(self):
        self.assertEqual(rgbtocmyk((0,1,1)),(1., 0,  0,  0))
    def test_04(self):
        self.assertEqual(rgbtocmyk((1,0,0)),(0,  1., 1., 0))
    def test_05(self):
        self.assertEqual(rgbtocmyk((1,0,1)),(0,  1., 0,  0))
    def test_06(self):
        self.assertEqual(rgbtocmyk((1,1,0)),(0,  0,  1., 0))
    def test_07(self):
        self.assertEqual(rgbtocmyk((1,1,1)),(0,  0,  0,  0))

class Test_colorValOK(unittest.TestCase):
    'Not much to look at here'
    def test_00(self):
        t = (2,0,0)
        self.assertFalse(colorValOK(t))
    def test_01(self):
        t = (-1,0,0)
        self.assertFalse(colorValOK(t))
    def test_02(self):
        t = (2,0,0,0)
        self.assertFalse(colorValOK(t))
    def test_03(self):
        t = (-1,0,0,0)
        self.assertFalse(colorValOK(t))
    def test_04(self):
        t = (1,0,0)
        self.assertTrue(colorValOK(t))
    def test_05(self):
        t = (0,0,0)
        self.assertTrue(colorValOK(t))
    def test_06(self):
        t = (1,0,0,0)
        self.assertTrue(colorValOK(t))
    def test_07(self):
        t = (0,0,0,0)
        self.assertTrue(colorValOK(t))

class Test_setfont(unittest.TestCase):
    pass


unittest.main()
