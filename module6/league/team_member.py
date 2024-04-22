from identified_object import IdentifiedObject
class TeamMember(IdentifiedObject):
    """This class represents a team member in any league's team."""

    def __init__(self, oid, name, email):
        super().__init__(oid)
        self._name = name
        self._email = email

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @name.setter
    def name(self, name):
        if name is not None:
            self._name = name

    @email.setter
    def email(self, email):
        if email is not None:
            self._email = email

    def send_email(self, emailer, subject, message):
        lst = []
        if self.email is not None:
            lst.append(self.email)
            emailer.send_plain_email(lst, subject, message)

    def __str__(self):
        return f"{self.name}<{self.email}>"

