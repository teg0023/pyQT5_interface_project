import os

from league_database import LeagueDatabase
from league.league import League
from team import Team
from team_member import TeamMember
import unittest

class TestLeagueDatabase(unittest.TestCase):

    def test_add_league(self):
        league_database = LeagueDatabase()
        league_1 = League(1, "League1")
        league_2 = League(2, "League2")

        league_database.add_league(league_1)
        league_database.add_league(league_2)
        league_database.add_league(None)

        self.assertEqual([league_1, league_2], league_database.leagues)

    def test_remove_league(self):

        league_database = LeagueDatabase()
        league_1 = League(1, "League1")
        league_2 = League(2, "League2")

        league_database.add_league(league_1)
        league_database.add_league(league_2)
        league_database.add_league(None)
        league_database.remove_league(None)
        league_database.remove_league(league_1)

        self.assertEqual([league_2], league_database.leagues)

    def test_league_named(self):
        league_database = LeagueDatabase()
        league_1 = League(1, "League1")
        league_2 = League(2, "League2")

        league_database.add_league(league_1)
        league_database.add_league(league_2)

        self.assertEqual(league_1, league_database.league_named("League1"))
        self.assertEqual(None, league_database.league_named(""))
        self.assertEqual(None, league_database.league_named(None))

    def test_load_and_save(self):
        league_database = LeagueDatabase()
        league_1 = League(1, "League1")
        league_2 = League(2, "League2")
        file_name = "test_league_database.dat"

        league_database.add_league(league_1)
        league_database.add_league(league_2)
        league_database.save(file_name)
        self.assertTrue(os.path.exists(file_name))

        league_database.load(file_name)

        """Modified version of testing the LeagueDatabase load class method"""
        self.assertEqual(str(league_database.instance()), str(league_database))

    def test_load_exception(self):
        league_database = LeagueDatabase()

        with self.assertRaises(OSError):
            league_database.load("test_no_file.dat")

    def test_save_exception_file_exists(self):
        league_database = LeagueDatabase()
        file_name = "test_file_exist.dat"
        league_database.save(file_name)

        with self.assertRaises(FileExistsError):
            league_database.save(file_name)

    def test_import_league_teams(self):
        league_database = LeagueDatabase()
        file_name = "Teams.csv"
        league_1 = League(1, "League 1")

        league_database.import_leagues_teams(league_1, file_name)

        self.assertEqual(4, len(league_1.teams))

    def test_import_league_teams_exception(self):
        league_database = LeagueDatabase()
        file_name = "nofile.csv"
        league_1 = League(1, "League 1")

        with self.assertRaises(Exception):
            league_database.import_leagues_teams(league_1, file_name)

    def test_export_league_teams(self):
        league_database = LeagueDatabase()
        file_name = "testTeams.csv"
        league_1 = League(1, "League 1")
        tm1 = Team(1, "Team A")
        tmbr = TeamMember(1, "Allan Jones", "alJones")
        tmbr2 = TeamMember(2, "Byron Hill", "bhill@teamA.org")
        tmbr3 = TeamMember(3, "George Hill", "hill@")
        tm1.add_member(tmbr)
        tm1.add_member(tmbr2)
        tm1.add_member(tmbr3)
        tm2 = Team(2, "Team B")
        tmbr4 = TeamMember(4, "Billy Williams", "bily@teamB.org")
        tmbr5 = TeamMember(5, "Aaron Johnson", "aaron@teamB.org")
        tmbr6 = TeamMember(6, "Tim Hawk", "timHawk@teamB.org")
        tm2.add_member(tmbr4)
        tm2.add_member(tmbr5)
        tm2.add_member(tmbr6)

        league_1.add_team(tm1)
        league_1.add_team(tm2)

        league_database.export_leagues_teams(league_1, file_name)
        self.assertTrue(os.path.exists(file_name))

    def test_export_leagues_teams_exception(self):
        league_database = LeagueDatabase()
        file_name = "nofile2.csv"
        tm = Team(1, "Team 1")

        with self.assertRaises(Exception):
            league_database.export_leagues_teams(tm, file_name)