import pickle
import csv

from team_member import TeamMember
from team import Team
class LeagueDatabase:
    """A singleton class that stores leagues."""

    _sole_instance = None
    """A class variable for the only instance of the class."""

    _leagues = []
    """Read-only property of this class to store the leagues."""

    _last_oid = 0
    """Private variable to store the last id number for objects."""

    @classmethod
    def instance(cls):
        if cls._sole_instance is None:
            cls._sole_instance = cls()
        return cls._sole_instance
    @classmethod
    def load(cls, file_name):
        try:
            with open(file_name, mode="rb") as f:
                cls._sole_instance = pickle.load(f)
        except OSError:
            print("File not found or reading error.")
            try:
                file_name += ".backup"
                with open(file_name, mode="rb") as f2:
                    cls._sole_instance = pickle.load(f2)
                    print("Loaded backup.")
                raise
            except OSError:
                raise
    @property
    def leagues(self):
        return self._leagues
    def save(self, file_name):
        try:
            with open(file_name, mode="xb") as f:
                pickle.dump(self, f)
        except FileExistsError:
            file_name += ".backup"
            with open(file_name, mode="wb") as f:
                pickle.dump(self, f)
                print("Saved backup.")
                raise
    def add_league(self, league):
        if league is not None and league not in self._leagues:
            self._leagues.append(league)
    def remove_league(self, league):
        if league is not None and league in self._leagues:
            self._leagues.remove(league)
    def league_named(self, name):
        for league in self._leagues:
            if league.name == name:
                return league
        return None
    def next_oid(self):
        self._last_oid += 1
        return self._last_oid
    def import_leagues_teams(self, league, file_name):
        if league is not None or file_name is not None:
            try:
                with open(file_name, newline='', encoding="utf-8") as csvfile:
                    csvreader = csv.reader(csvfile, delimiter=',')
                    rowInt = 0
                    tmNames = []
                    tmAry = []
                    tmMbrs = []
                    i = 2
                    for row in csvreader:
                        if rowInt > 0:
                            if row[0] not in tmNames:
                                tmNames.append(row[0])
                                tmMbrs.append(row[0])
                            else:
                                tmMbr = TeamMember(self.next_oid(), row[1], row[2])
                                tmMbrs.append(tmMbr)
                                rowInt += 1
                                continue
                            if len(tmNames) > 1 and len(tmNames) == i:
                                tmMbrs.remove(row[0])
                                tmAry.append(tmMbrs)
                                tmMbrs = []
                                i += 1
                                tmMbrs.append(row[0])
                                tmMbr = TeamMember(self.next_oid(), row[1], row[2])
                                tmMbrs.append(tmMbr)
                            else:
                                tmMbr = TeamMember(self.next_oid(), row[1], row[2])
                                tmMbrs.append(tmMbr)
                        rowInt += 1
                    tmAry.append(tmMbrs)
                    for tme in tmAry:
                        colInt = 0
                        tm = Team(self.next_oid(), "")
                        for member in tme:
                            if colInt == 0:
                                tm.name = member
                            else:
                                tm.add_member(member)
                            colInt += 1
                        league.teams.append(tm)
            except Exception:
                print("CSV File not found or reading error.")
                raise
    def export_leagues_teams(self, league, file_name):
        if league is not None or file_name is not None:
            try:
                with open(file_name, mode='w', newline='', encoding="utf-8") as csvfile:
                    csvwriter = csv.writer(csvfile, delimiter=',')
                    csvwriter.writerow(['Team name', 'Member name', 'Member email'])
                    for team in league.teams:
                        for member in team.members:
                            csvwriter.writerow([f'{team.name}', f'{member.name}', f'{member.email}'])
            except Exception:
                print("Writing error.")
                raise

    def __getstate__(self):
        """Getting the state of the database being pickled"""
        state = {"_last_oid" : self._last_oid, "_leagues" : self._leagues, "_sole_instance" : self._sole_instance}
        return state

    def __setstate__(self, state):
        """Setting the state of the database being unpickled"""
        self.__dict__.update(state)

    def __str__(self):
        return f"League database has {len(self._leagues)} leagues."