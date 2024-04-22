class IdentifiedObject:
    """This is an abstract class of an identified object."""
    def __init__(self, oid):
        self._oid = oid

    @property
    def oid(self):
        return self._oid

    def __eq__(self, other):
        if type(other) is self.__class__ and self._oid == other.oid:
            return True
        return False

    def __hash__(self):
        return hash(self._oid)