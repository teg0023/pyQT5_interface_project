import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog
from main_ui.edit_team_dialog import EditTeamDialog
from league.team import Team
Ui_MainWindow, QtBaseClass = uic.loadUiType("edit_league_dialog.ui")

class EditLeagueDialog(QtBaseClass, Ui_MainWindow):
    def __init__(self, cls=None, league=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        if cls:
            self._cls = cls
        if league:
            self._league = league
        self.deleteTeamButton.clicked.connect(self.delete_team)
        self.editTeamButton.clicked.connect(self.edit_team)
        self.addTeamButton.clicked.connect(self.add_team)
        self.importButton.clicked.connect(self.import_teams)
        self.exportButton.clicked.connect(self.export_teams)
        self.update_league()

    def delete_team(self):
        lst_row = self.team_list_selected_row()
        if lst_row != -1:
            team = self._league.teams[lst_row]
            self._league.remove_team(team)
        self.update_league()

    def add_team(self):
        new_team_name = self.lineTeamName.text()
        new_team = Team(self._cls.next_oid(), new_team_name)
        self._league.add_team(new_team)
        self.update_league()

    def edit_team(self):
        lst_row = self.team_list_selected_row()
        if lst_row != -1:
            team = self._league.teams[lst_row]
            dialog = EditTeamDialog(self._cls, team)
            dialog.exec_()
        self.update_league()
    def import_teams(self):
        fileName = QFileDialog().getOpenFileName(filter="Comma Separated Values Files (*.csv)")
        if fileName[0] != "":
            self._cls.import_leagues_teams(self._league, fileName[0])
        self.update_league()
    def export_teams(self):
        fileName = QFileDialog().getSaveFileName(filter="Comma Separated Values Files (*.csv)")
        if fileName[0] != "":
            self._cls.export_leagues_teams(self._league, fileName[0])
        self.update_league()
    def update_league(self):
        self.listWidgetTeam.clear()
        for team in self._league.teams:
            self.listWidgetTeam.addItem(str(team))

    def team_list_selected_row(self):
        selection = self.listWidgetTeam.selectedItems()
        if len(selection) == 0:
            return -1
        assert len(selection) == 1
        selected_item = selection[0]
        try:
            return [str(t) for t in self._league.teams].index(selected_item.text())
        except ValueError:
            pass
        return -1

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = EditLeagueDialog()
    window.show()
    sys.exit(app.exec())