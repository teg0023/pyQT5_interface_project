import unittest
import datetime

from league.competition import Competition
from league.team import Team
from league.team_member import TeamMember
from league.fake_emailer import FakeEmailer

class CompetitionTestsAddition(unittest.TestCase):
    def test_competition_send_email(self):
        t1 = Team(1, "Team 1")
        t2 = Team(2, "Team 2")
        t3 = Team(3, "Team 3")

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

        fe = FakeEmailer()
        c1.send_email(fe, "S", "M")
        self.assertIn("fred", fe.recipients)
        self.assertIn("barney", fe.recipients)
        self.assertEqual(5, len(fe.recipients))
        self.assertEqual("S", fe.subject)
        self.assertEqual("M", fe.message)

        fe2 = FakeEmailer()

        c2.send_email(fe2, "Prep", "Practice")
        self.assertIn("wilma", fe2.recipients)
        self.assertIn("dino", fe2.recipients)
        self.assertEqual(7, len(fe2.recipients))
        self.assertEqual("Prep", fe2.subject)
        self.assertEqual("Practice", fe2.message)

    def test_str(self):
        t1 = Team(1, "Team 1")
        t2 = Team(2, "Team 2")
        t3 = Team(3, "Team 3")
        dte = datetime.datetime(2020, 5, 24, 12, 30)
        c1 = Competition(1, [t1, t2], "A", None)
        c2 = Competition(2, [t2, t3], "B", dte)

        self.assertEqual("Competition at A with 2 teams", str(c1))
        self.assertEqual("Competition at B on 05/24/2020 12:30 with 2 teams", str(c2))

    def test_setters(self):
        dte = datetime.datetime(2020, 5, 24, 12, 30)
        c1 = Competition(1, [Team(1, "Team"), Team(2, "Teamfd")], "Loc")
        c2 = Competition(2, [Team(3, "ER"), Team(4, "ERr")], "DAT", dte)

        c1.location = None
        c1.date_time = datetime.datetime(2012, 3, 15, 10,20)

        c2.location = "New Location"
        c2.date_time = None

        self.assertEqual("Loc", c1.location)
        self.assertEqual(datetime.datetime(2012, 3, 15, 10,20), c1.date_time)
        self.assertEqual("New Location", c2.location)
        self.assertEqual(None, c2.date_time)
