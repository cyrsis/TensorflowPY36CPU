
class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "{}({}, {})".format(self.__class__.__name__, self.x, self.y)
