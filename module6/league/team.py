from identified_object import IdentifiedObject
from custom_exceptions import DuplicateOid
from custom_exceptions import DuplicateEmail

class Team(IdentifiedObject):
    """This class represents a team."""

    def __init__(self, oid, name):
        super().__init__(oid)
        self._name = name
        self._members = []

    @property
    def name(self):
        return self._name

    @property
    def members(self):
        return self._members

    @name.setter
    def name(self, name):
        if name is not None:
            self._name = name

    def add_member(self, member):
        if member is not None:
            for memberIn in self._members:
                if memberIn.oid == member.oid:
                    raise DuplicateOid("This team member oid is already in the collection.", member.oid)
                if memberIn.email.lower() == member.email.lower():
                    raise DuplicateEmail("This team member email is already in the collection.", member.email)
            self._members.append(member)

    def member_named(self, s):
        if s is None:
            return None
        for mem in self.members:
            if mem.name == s:
                return mem
        return None

    def remove_member(self, member):
        if member is not None and member in self._members:
            self._members.remove(member)

    def send_email(self, emailer, subject, message):
        lst = []
        for mem in self.members:
            if mem.email is not None:
                lst.append(mem.email)
        emailer.send_plain_email(lst, subject, message)

    def __str__(self):
        return f"{self.name}: {len(self.members)} members"


