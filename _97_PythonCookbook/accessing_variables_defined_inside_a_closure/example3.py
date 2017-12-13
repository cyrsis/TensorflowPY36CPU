# Example of a normal class

# Example use
import sys


class Stack2:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)

class ClosureInstance:
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals

        # Update instance dictionary with callables
        self.__dict__.update((key,value) for key, value in locals.items()
                             if callable(value) )
    # Redirect special methods
    def __len__(self):
        return self.__dict__['__len__']()


if __name__ == '__main__':
    # import example2
    from timeit import timeit

    print('Using a class')
    s = Stack2()
    print(timeit('s.push(1); s.pop()', 'from __main__ import s'))
    print('Using a closure')

    s2 = ClosureInstance()
    print(timeit('s.push(1); s.pop()', 'from __main__ import s'))
