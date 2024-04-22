import unittest

from league.competition import Competition
from league.team import Team
from league.team_member import TeamMember
from league.league import League

class TestMultipleClass(unittest.TestCase):

    def test_not_equality(self):
        team1 = Team(1,"")
        tm1 = TeamMember(1, "<NAME>", team1)
        comp1 = Competition(1, [], "")
        league1 = League(1, "er")

        self.assertNotEqual(tm1, team1)
        self.assertNotEqual(tm1, comp1)
        self.assertNotEqual(tm1, league1)
        self.assertNotEqual(team1, comp1)
        self.assertNotEqual(team1, league1)
        self.assertNotEqual(comp1, league1)

    def test_equality(self):
        team1 = Team(1, "")
        team2 = Team(1, "<NAME>")
        tm2 = TeamMember(1, "<NAME2>", "team2")
        tm1 = TeamMember(1, "<NAME>", "team1")
        comp1 = Competition(1, [], "")
        comp2 = Competition(1, [], "sd")
        league1 = League(1, "er")
        league2 = League(1, "")

        self.assertEqual(tm1, tm2)
        self.assertEqual(team1, team2)
        self.assertEqual(comp1, comp2)
        self.assertEqual(league1, league2)