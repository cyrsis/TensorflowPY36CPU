"""Demonstrate object implementation and custom attributes using a simple 2D vector.
"""


class Vector:

    def __init__(self, **coords):
        private_coords = {'_' + k: v for k, v in coords.items()}
        self.__dict__.update(private_coords)

    def __getattr__(self, name):
        print(name)

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__,
                               ', '.join("{k}={v}".format(k=k[1:], v=self.__dict__[k])
                                         for k in sorted(self.__dict__.keys())))
