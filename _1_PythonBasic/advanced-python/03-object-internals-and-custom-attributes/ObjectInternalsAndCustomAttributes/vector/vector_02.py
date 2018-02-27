"""Demonstrate object implementation and custom attributes using a simple 2D vector.
"""


class Vector:

    def __init__(self, **coords):
        self.__dict__.update(coords)

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__,
                               ', '.join("{k}={v}".format(k=k, v=self.__dict__[k]) for k in sorted(self.__dict__.keys())))
