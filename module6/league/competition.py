from identified_object import IdentifiedObject
class Competition(IdentifiedObject):
    """This class represents a competition."""

    def __init__(self, oid, teams, location, datetime=None):
        super().__init__(oid)
        self._teams_competing = teams
        self._location = location
        self._date_time = datetime

    @property
    def teams_competing(self):
        return self._teams_competing

    @property
    def date_time(self):
        return self._date_time

    @property
    def location(self):
        return self._location

    @date_time.setter
    def date_time(self, datetime):
        self._date_time = datetime

    @location.setter
    def location(self, location):
        if location is not None:
            self._location = location

    def send_email(self, emailer, subject, message):
        lst = []
        counter = 0
        mem_List = []
        for team in self.teams_competing:
            for mem in team.members:
                if counter < 1 and mem.email is not None:
                    mem_List.append(mem.email)
                    lst.append(mem.email)
                elif mem.email is not None and mem.email not in mem_List:
                    lst.append(mem.email)
            counter += 1
        emailer.send_plain_email(lst, subject, message)


    def __str__(self):
        if self.date_time is None:
            return f"Competition at {self.location} with {len(self.teams_competing)} teams"
        else:
            return (f"Competition at {self.location} on {self.date_time.strftime("%m/%d/%Y %H:%M")} "
                    f"with {len(self.teams_competing)} teams")

