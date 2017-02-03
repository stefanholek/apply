=====
apply
=====
------------------------------------
An apply function for Python 2 and 3
------------------------------------

Package Contents
================

apply(object, args=None, kwargs=None)
    Call object with args and kwargs; return its results.

Overview
========

Python 3 has no apply. We like apply.
I you like apply as well, have no fear. This version of apply works
across all versions of Python.

Examples
========

apply allows to create read/write properties in a very compact way::

    from apply import apply

    class X509:

        def __init__(self, store):
            self.store = store

        @apply
        def CN():
            doc = 'The common name attribute'
            def get(self):
                return self.store.get('CN')
            def set(self, value):
                self.store.put('CN', value)
            return property(get, set, doc=doc)

    record = X509(LDAP())
    record.CN = 'Slate Rock and Gravel Company'

