import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog
from league.league_database import LeagueDatabase
from league.league import League
from main_ui.edit_league_dialog import EditLeagueDialog

Ui_MainWindow, QtBaseClass = uic.loadUiType("main_window.ui")

class MainWindow(QtBaseClass, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.actionLoad.triggered.connect(self.load_file)
        self.actionSave.triggered.connect(self.save_file)
        self.loadFileButton.clicked.connect(self.load_file)
        self.saveFileButton.clicked.connect(self.save_file)
        self.deleteLeagueButton.clicked.connect(self.delete_league)
        self.addLeagueButton.clicked.connect(self.add_league)
        self.editLeagueButton.clicked.connect(self.edit_league)
        self._cls = LeagueDatabase()
        self.update()
    def load_file(self):
        fileName = QFileDialog().getOpenFileName(filter="DAT or Backup Files (*.dat *.backup)")
        if fileName[0] != "":
            self._cls.load(fileName[0])
            self._cls = self._cls.instance()
        self.update()
    def save_file(self):
        fileName = QFileDialog().getSaveFileName(filter="DAT or Backup Files (*.dat *.backup)")
        if fileName[0] != "":
            self._cls.save(fileName[0])
        self.update()
    def delete_league(self):
        lst_row = self.league_list_selected_row()
        if lst_row != -1:
            league = self._cls.leagues[lst_row]
            self._cls.remove_league(league)
        self.update()
    def add_league(self):
        new_league_name = self.lineLeagueName.text()
        new_league = League(self._cls.next_oid(), new_league_name)
        self._cls.add_league(new_league)
        self.update()
    def edit_league(self):
        lst_row = self.league_list_selected_row()
        if lst_row != -1:
            league = self._cls.leagues[lst_row]
            dialog = EditLeagueDialog(self._cls, league)
            dialog.exec_()
        self.update()
    def update(self):
        self.listLeaguesView.clear()
        for league in self._cls.leagues:
           self.listLeaguesView.addItem(str(league))
    def league_list_selected_row(self):
        selection = self.listLeaguesView.selectedItems()
        if len(selection) == 0:
            return -1
        assert len(selection) == 1
        selected_item = selection[0]
        try:
            return [str(l) for l in self._cls.leagues].index(selected_item.text())
        except ValueError:
            pass
        return -1

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())