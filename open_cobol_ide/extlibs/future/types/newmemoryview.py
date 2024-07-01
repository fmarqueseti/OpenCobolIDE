"""
A pretty lame implementation of a memoryview object for Python 2.6.
"""

from collections.abc import Iterable
from numbers import Integral
import string

from future.utils import istext, isbytes, PY3, with_metaclass
from future.types import no, issubset


# class BaseNewBytes(type):
#     def __instancecheck__(cls, instance):
#         return isinstance(instance, _builtin_bytes)


class newmemoryview(object):   # with_metaclass(BaseNewBytes, _builtin_bytes)):
    """
    A pretty lame backport of the Python 2.7 and Python 3.x
    memoryviewview object to Py2.6.
    """
    def __init__(self, obj):
        return obj


__all__ = ['newmemoryview']
