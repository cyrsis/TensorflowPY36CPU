
class OneShotDict(dict):

    def __init__(self, existing=None):
        super().__init__()
        if existing is not None:
            for k, v in existing:
                self[k] = v

    def __setitem__(self, key, value):
        if key in self:
            raise ValueError("Cannot assign to existing key {!r}".format(key))
        super().__setitem__(key, value)


class OneShotClassNamespace(dict):

    def __init__(self, name, existing=None):
        super().__init__()
        self._name = name
        if existing is not None:
            for k, v in existing:
                self[k] = v

    def __setitem__(self, key, value):
        if key in self:
            raise TypeError("Cannot reassign existing class attribute {!r} of {!r}".format(key, self._name))
        super().__setitem__(key, value)


class ProhibitDuplicatesMeta(type):

    @classmethod
    def __prepare__(mcs, name, bases):
        return OneShotClassNamespace(name)


class Dodgy(metaclass=ProhibitDuplicatesMeta):

    def method(self):
        return "first definition"

    def method(self):
        return "second definition"







