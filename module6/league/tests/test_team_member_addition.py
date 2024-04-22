import unittest
from league.team_member import TeamMember

class TeamMemberTestAddition(unittest.TestCase):

    def test_setters(self):
        team_member = TeamMember(1, "<NAME>", "<EMAIL>""")
        team_member2 = TeamMember(2, "<NAME2>", "<EMAIL2>")

        team_member.name = None
        team_member.email = None
        team_member2.name = "Shaun"
        team_member2.email = "shaun"

        self.assertEqual("<NAME>", team_member.name)
        self.assertEqual("<EMAIL>", team_member.email)
        self.assertEqual("Shaun", team_member2.name)
        self.assertEqual("shaun", team_member2.email)