import sys
import unittest

from apply import apply


class TestCase(unittest.TestCase):

    def test_apply(self):

        def func(foo=None, bar=None):
            return foo, bar

        self.assertEqual(apply(func, 1, bar=2), (1, 2))
