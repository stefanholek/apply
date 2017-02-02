.. apply documentation master file, created by
   sphinx-quickstart on Thu May 10 17:11:01 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

===============================================
apply |version| -- Cross-Python apply
===============================================

.. toctree::
   :maxdepth: 2

.. module:: apply

The :mod:`apply` module provides an :func:`~apply.apply` function for
Python 2 and 3.
It preserves the functionality of the :func:`apply() <py:apply>` builtin,
which has been deprecated and removed from Python.

API Documentation
=================

.. function:: apply(object, args=None, kwargs=None)

    Call a callable object with positional arguments taken from the optional
    tuple `args`, and keyword arguments taken from the optional dictionary
    `kwargs`; return its results.

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

