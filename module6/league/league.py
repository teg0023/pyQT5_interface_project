from identified_object import IdentifiedObject
from custom_exceptions import DuplicateOid

class League(IdentifiedObject):
    """This class represents a league."""

    def __init__(self, oid, name):
        super().__init__(oid)
        self._name = name
        self._teams = []
        self._competitions = []

    @property
    def name(self):
        return self._name

    @property
    def teams(self):
        return self._teams

    @property
    def competitions(self):
        return self._competitions

    @name.setter
    def name(self, name):
        if name is not None:
            self._name = name

    def add_team(self, team):
        if team is not None:
            for tm in self._teams:
                if tm.oid == team.oid:
                    raise DuplicateOid("This team oid is already in the collection.", team.oid)
            self._teams.append(team)

    def remove_team(self, team):
        if team is not None:
            for cm in self._competitions:
                if team in cm.teams_competing:
                    raise ValueError("This team is already in a competition.")
        self._teams.remove(team)

    def team_named(self, team_name):
        if team_name is None:
            return None
        for tm in self.teams:
            if tm.name == team_name:
                return tm
        return None

    def add_competition(self, competition):
        if competition is not None:
            for tm in competition.teams_competing:
                if tm not in self._teams:
                    raise ValueError("This competition's teams are not in the league")
            self._competitions.append(competition)

    def teams_for_member(self, member):
        team_List = []
        for tm in self.teams:
            for t_member in tm.members:
                if t_member.name == member.name:
                    team_List.append(tm)
        return team_List

    def competitions_for_team(self, team):
        comp_List = []
        for cmp in self.competitions:
            for tm in cmp.teams_competing:
                if team == tm:
                    comp_List.append(cmp)
        return comp_List
    def competitions_for_member(self, member):
        comp_List = []
        for cmp in self.competitions:
            preMark = 0
            for tm in cmp.teams_competing:
                for mbr in tm.members:
                    if mbr == member:
                        preMark += 1
                        if preMark == 1:
                            comp_List.append(cmp)
        return comp_List

    def __str__(self):
        return f"{self.name}: {len(self.teams)} teams, {len(self.competitions)} competitions"

