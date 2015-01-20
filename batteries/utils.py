class Enum(object):
    """ 
        Enum implementation for convenience usage in Django 
        Usage: inherit your enum class from this class and define uppercase attributes
        Example:
        class MyEnum(Enum):
            ATTR1, ATTR2, ATTR3 = 1, 2, 3
    """

    def choices(self):
        for k, v in self.__class__.__dict__.iteritems():
            if k.upper() == k:
                yield (k, v)
