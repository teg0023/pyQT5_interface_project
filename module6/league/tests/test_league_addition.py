import unittest

from league.competition import Competition
from league.league import League
from league.team import Team
from league.team_member import TeamMember

class LeagueTestsAddition(unittest.TestCase):

    def test_teams_for_member(self):
        league = League(1, "Some league")
        t1 = Team(1, "t1")
        t2 = Team(2, "t2")
        t3 = Team(3, "t3")
        all_teams = [t1, t2, t3]
        league.add_team(t1)
        league.add_team(t2)
        league.add_team(t3)
        tm1 = TeamMember(1, "Fred", "fred")
        tm2 = TeamMember(2, "Barney", "barney")
        tm3 = TeamMember(3, "Wilma", "wilma")
        tm4 = TeamMember(4, "Betty", "betty")
        tm5 = TeamMember(5, "Pebbles", "pebbles")
        tm6 = TeamMember(6, "Bamm-Bamm", "bam-bam")
        tm7 = TeamMember(7, "Dino", "dino")
        tm8 = TeamMember(8, "Mr. Slate", "mrslate")
        t1.add_member(tm1)
        t1.add_member(tm2)
        t2.add_member(tm3)
        t2.add_member(tm4)
        t2.add_member(tm5)
        t3.add_member(tm6)
        t3.add_member(tm7)
        t3.add_member(tm8)
        # every team plays every other team twice
        oid = 1
        for c in [Competition(oid := oid + 1, [team1, team2], team1.name + " vs " + team2.name, None)
                  for team1 in all_teams
                  for team2 in all_teams
                  if team1 != team2]:
            league.add_competition(c)

        er = league.teams_for_member(tm1)
        self.assertEqual(er, [t1])

        er = league.teams_for_member(tm4)
        self.assertEqual(er, [t2])

    def test_competitions_for_team(self):
        league = League(1, "Some league")
        t1 = Team(1, "Team 1")
        t2 = Team(2, "Team 2")
        t3 = Team(3, "Team 3")

        league.add_team(t1)
        league.add_team(t2)
        league.add_team(t3)
        tm1 = TeamMember(1, "Fred", "fred")
        tm2 = TeamMember(2, "Barney", "barney")
        tm3 = TeamMember(3, "Wilma", "wilma")
        tm4 = TeamMember(4, "Betty", "betty")
        tm5 = TeamMember(5, "Pebbles", "pebbles")
        tm6 = TeamMember(6, "Bamm-Bamm", "bam-bam")
        tm7 = TeamMember(7, "Dino", "dino")
        tm8 = TeamMember(8, "Mr. Slate", "mrslate")
        t1.add_member(tm1)
        t1.add_member(tm2)
        t2.add_member(tm3)
        t2.add_member(tm4)
        t2.add_member(tm5)
        t3.add_member(tm6)
        t3.add_member(tm7)
        t3.add_member(tm8)

        c1 = Competition(1, [t1, t2], "Here", None)
        c2 = Competition(2, [t2, t3], "There")
        league.add_competition(c1)
        league.add_competition(c2)

        er = league.competitions_for_team(t1)
        et = league.competitions_for_team(t2)
        rt = league.competitions_for_team(t3)
        nt = league.competitions_for_team(None)

        self.assertEqual(er, [c1])
        self.assertEqual(et, [c1, c2])
        self.assertEqual(rt, [c2])
        self.assertEqual(nt, [])


    def test_competitions_for_member(self):
        league = League(1, "Some league")
        t1 = Team(1, "Team 1")
        t2 = Team(2, "Team 2")
        t3 = Team(3, "Team 3")

        league.add_team(t1)
        league.add_team(t2)
        league.add_team(t3)
        tm1 = TeamMember(1, "Fred", "fred")
        tm2 = TeamMember(2, "Barney", "barney")
        tm3 = TeamMember(3, "Wilma", "wilma")
        tm4 = TeamMember(4, "Betty", "betty")
        tm5 = TeamMember(5, "Pebbles", "pebbles")
        tm6 = TeamMember(6, "Bamm-Bamm", "bam-bam")
        tm7 = TeamMember(7, "Dino", "dino")
        tm8 = TeamMember(8, "Mr. Slate", "mrslate")
        t1.add_member(tm1)
        t1.add_member(tm2)
        t2.add_member(tm3)
        t2.add_member(tm2)
        t2.add_member(tm4)
        t2.add_member(tm5)
        t3.add_member(tm6)
        t3.add_member(tm7)
        t3.add_member(tm8)

        c1 = Competition(1, [t1, t2], "Here", None)
        c2 = Competition(2, [t2, t3], "There")
        league.add_competition(c1)
        league.add_competition(c2)

        er = league.competitions_for_member(tm2)
        et = league.competitions_for_member(tm1)
        rt = league.competitions_for_member(tm6)
        nt = league.competitions_for_team(None)

        self.assertEqual(er, [c1, c2])
        self.assertEqual(et, [c1])
        self.assertEqual(rt, [c2])
        self.assertEqual(nt, [])

    def test_modified_add_competitions(self):
        league = League(1, "Some league")
        t1 = Team(1, "Team 1")
        t2 = Team(2, "Team 2")
        t3 = Team(3, "Team 3")

        league.add_team(t1)
        league.add_team(t2)
        league.add_team(t3)
        league.add_team(None)
        tm1 = TeamMember(1, "Fred", "fred")
        tm2 = TeamMember(2, "Barney", "barney")
        tm3 = TeamMember(3, "Wilma", "wilma")
        tm4 = TeamMember(4, "Betty", "betty")
        tm5 = TeamMember(5, "Pebbles", "pebbles")
        tm6 = TeamMember(6, "Bamm-Bamm", "bam-bam")
        tm7 = TeamMember(7, "Dino", "dino")
        tm8 = TeamMember(8, "Mr. Slate", "mrslate")
        t1.add_member(tm1)
        t1.add_member(tm2)
        t1.add_member(None)
        t2.add_member(tm3)
        t2.add_member(tm2)
        t2.add_member(tm4)
        t2.add_member(tm5)
        t2.add_member(None)
        t3.add_member(tm6)
        t3.add_member(tm7)
        t3.add_member(tm8)
        t3.add_member(None)

        c1 = Competition(1, [t1, t2], "Here", None)
        c2 = Competition(2, [t2, t3], "There")
        league.add_competition(c1)
        league.add_competition(c2)

        league.add_competition(None)

        self.assertEqual(league.competitions, [c1, c2])

    def test_str(self):
        league = League(1, "Nothing")
        league2 = League(2, "Something")

        t1 = Team(1, "Team 1")
        t2 = Team(2, "Team 2")

        league2.add_team(t1)
        league2.add_team(t2)

        c1 = Competition(1, [t1, t2], "S Cup")
        league2.add_competition(c1)

        self.assertEqual("Nothing: 0 teams, 0 competitions", str(league))
        self.assertEqual("Something: 2 teams, 1 competitions", str(league2))

    def test_setters(self):
        league = League(1, "ABC Cup")
        league2 = League(2, "Dans")

        league.name = None
        league2.name = "Cup Zero"

        self.assertEqual("ABC Cup", league.name)
        self.assertEqual("Cup Zero", league2.name)

    def test_modified_add_team_exception(self):
        league = League(1, "wer")

        t1 = Team(1, "Team 1")
        t2 = Team(2, "Team 2")

        league.add_team(t1)
        league.add_team(t2)

        with self.assertRaises(Exception):
            league.add_team(t1)
        with self.assertRaises(Exception):
            league.add_team(t2)

    def test_modified_remove_team(self):
        league = League(1, "wer")

        t1 = Team(1, "Team 1")
        t2 = Team(2, "Team 2")
        t3 = Team(3, "Team 3")

        league.add_team(t1)
        league.add_team(t2)
        league.add_team(t3)
        c1 = Competition(1, [t1, t2], "S Cup")
        league.add_competition(c1)

        league.remove_team(t3)

        self.assertEqual([t1, t2], league.teams)

    def test_modified_remove_team_value_error(self):
        league = League(1, "wer")

        t1 = Team(1, "Team 1")
        t2 = Team(2, "Team 2")

        league.add_team(t1)
        league.add_team(t2)
        c1 = Competition(1, [t1, t2], "S Cup")
        league.add_competition(c1)

        with self.assertRaises(ValueError):
            league.remove_team(t1)
        with self.assertRaises(ValueError):
            league.remove_team(t2)

    def test_modified_add_competition_value_error(self):
        league = League(1, "wer")

        t1 = Team(1, "Team 1")
        t2 = Team(2, "Team 2")
        t3 = Team(3, "Team 3")
        t4 = Team(4, "Team 4")

        league.add_team(t1)
        league.add_team(t2)
        c1 = Competition(1, [t1, t2], "S Cup")
        c2 = Competition(2, [t3, t4], "")
        c3 = Competition(3, [t1, t3], "Ball Cup")
        league.add_competition(c1)

        with self.assertRaises(ValueError):
            league.add_competition(c2)
        with self.assertRaises(ValueError):
            league.add_competition(c3)

