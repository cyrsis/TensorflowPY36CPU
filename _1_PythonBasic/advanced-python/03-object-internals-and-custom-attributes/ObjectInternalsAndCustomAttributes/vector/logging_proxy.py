class LoggingProxy:

    def __init__(self, target):
        super().__setattr__('target', target)

    def __getattribute__(self, name):
        target = super().__getattribute__('target')

        try:
            value = getattr(target, name)
        except AttributeError as e:
            raise AttributeError("{} could not forward request {} to {}".format(
                super().__getattribute__('__class__').__name__,
                name,
                target)) from e
        else:
            print("Retrieved attribute {!r} = {!r} from {!r}".format(name, value, target))
            return value

    def __setattr__(self, name, value):
        target = super().__getattribute__('target')

        try:
            setattr(target, name, value)
        except AttributeError as e:
            raise AttributeError("{} could not forward request {} to {}".format(
                super().__getattribute__('__class__').__name__,
                name,
                target))
        else:
            print("Set attribute {!r} = {!r} on {!r}".format(name, value, target))

