import sys
import unittest

from apply import apply


def func(foo=None, bar=None):
    return foo, bar


class ApplyTests(unittest.TestCase):

    def test_noargs(self):
        self.assertEqual(apply(func), (None, None))

    def test_args(self):
        self.assertEqual(apply(func, args=(1,)), (1, None))

    def test_kwargs(self):
        self.assertEqual(apply(func, kwargs={'bar': 2}), (None, 2))

    def test_apply(self):
        self.assertEqual(apply(func, (1,), {'bar': 2}), (1, 2))
