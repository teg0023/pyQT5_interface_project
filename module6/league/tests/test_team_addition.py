from league.team import Team
from league.team_member import TeamMember
import unittest

class TeamTestAddition(unittest.TestCase):

    def test_str(self):
        team = Team(1,"Team")
        team2 = Team(2,"Team2")
        tm1 = TeamMember(1, "TeamMember", "teammember")
        tm2 = TeamMember(2, "TeamMember2", "teammember2")

        team2.add_member(tm1)
        team2.add_member(tm2)

        self.assertEqual("Team: 0 members", str(team))
        self.assertEqual("Team2: 2 members", str(team2))

    def test_setters(self):
        team = Team(1,"Team")
        team2 = Team(2,"Team2")
        team.name = None
        team2.name = "RB"

        self.assertEqual("Team", team.name)
        self.assertEqual("RB", team2.name)

    def test_modified_add_member_exception(self):
        team = Team(1,"Team")
        tm1 = TeamMember(1, "TeamMember", "teammember")
        tm2 = TeamMember(2, "TeamMember2", "TeamMembeR")
        tm3 = TeamMember(1, "TeamMember3", "merm3")

        team.add_member(tm1)

        with self.assertRaises(Exception):
            team.add_member(tm3)
        with self.assertRaises(Exception):
            team.add_member(tm2)


