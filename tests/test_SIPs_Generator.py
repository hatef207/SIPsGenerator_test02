#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_SIPs_Generator
----------------------------------

Tests for `SIPs_Generator` module.
"""

import unittest

import SIPs_Generator


class TestSips_generator(unittest.TestCase):

    def setUp(self):
        #pass
        self.hello_message = "HEllo MEhdi"

    def test_something(self):
       # output = SIPs_Generator.hello()
       # assert(output == self.hello_message)
        assert(SIPs_Generator.__version__)

    def tearDown(self):
        pass
