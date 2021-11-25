import unittest

import numpy as np

import sample.sample_script as scr

# pylint: disable=no-self-use
class TestSampleScript(unittest.TestCase):
    def test_get_zeros(self):
        np.testing.assert_array_equal(scr.get_zeros(np.zeros((2, 2))), np.zeros((2, 2)))

    def test_get_ones(self):
        np.testing.assert_array_equal(scr.get_ones(np.zeros((2, 2))), np.ones((2, 2)))

    def test_get_n(self):
        np.testing.assert_array_equal(scr.get_n(np.zeros((2, 2)), 5), np.ones((2, 2)) * 5)
