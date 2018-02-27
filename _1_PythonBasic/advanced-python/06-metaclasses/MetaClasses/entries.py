
class EntriesMeta(type):

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        print("Entries.__prepare__(name, bases, **kwargs)")
        print("  mcs =", mcs)
        print("  name =", name)
        print("  bases =", bases)
        print("  kwargs =", kwargs)
        namespace = super().__prepare__(name, bases, **kwargs)
        print("<-- namespace =", namespace)
        print()
        return namespace

    def __new__(mcs, name, bases, namespace, num_entries, **kwargs):
        print("Entries.__new__(mcs, name, bases, namespace, **kwargs)")
        print("  mcs =", mcs)
        print("  name =", name)
        print("  bases =", bases)
        print("  namespace =", namespace)
        print("  kwargs =", kwargs)
        print("  num_entries =", num_entries)
        namespace.update({chr(i): i for i in range(ord('a'), ord('a')+num_entries)})
        cls = super().__new__(mcs, name, bases, namespace)
        print("<-- cls =", cls)
        print()
        return cls

    def __init__(cls, name, bases, namespace, **kwargs):
        print("Entries.__init__(cls, name, bases, namespace, **kwargs)")
        print("  cls =", cls)
        print("  name =", name)
        print("  bases =", bases)
        print("  namespace =", namespace)
        print("  kwargs =", kwargs)
        super().__init__(name, bases, namespace)
        print()

