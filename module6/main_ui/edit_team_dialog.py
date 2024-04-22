import sys

from PyQt5 import QtWidgets, uic
from league.team_member import TeamMember
Ui_MainWindow, QtBaseClass = uic.loadUiType("edit_team_dialog.ui")

class EditTeamDialog(QtBaseClass, Ui_MainWindow):
    def __init__(self, cls=None, team=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        if cls:
            self._cls = cls
        if team:
            self._team = team
        self.deleteMemberButton.clicked.connect(self.delete_member)
        self.editMemberButton.clicked.connect(self.edit_member)
        self.addMemberButton.clicked.connect(self.add_member)
        self.update_team()

    def delete_member(self):
        lst_row = self.member_list_selected_row()
        if lst_row != -1:
            member = self._team.members[lst_row]
            self._team.remove_member(member)
        self.update_team()

    def add_member(self):
        new_name = self.lineName.text()
        new_email = self.lineEmail.text()
        new_team_member = TeamMember(self._cls.next_oid(), new_name, new_email)
        self._team.add_member(new_team_member)
        self.update_team()

    def edit_member(self):
        lst_row = self.member_list_selected_row()
        if lst_row != -1:
            member = self._team.members[lst_row]
            changed_name = self.lineName.text()
            changed_email = self.lineEmail.text()
            member.name = changed_name
            member.email = changed_email
        self.update_team()

    def update_team(self):
        self.listWidgetMember.clear()
        for member in self._team.members:
            self.listWidgetMember.addItem(str(member))

    def member_list_selected_row(self):
        selection = self.listWidgetMember.selectedItems()
        if len(selection) == 0:
            return -1
        assert len(selection) == 1
        selected_item = selection[0]
        try:
            return [str(m) for m in self._team.members].index(selected_item.text())
        except ValueError:
            pass
        return -1

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = EditTeamDialog()
    window.show()
    sys.exit(app.exec())