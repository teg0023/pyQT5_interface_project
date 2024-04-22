Terence Goosby - CPSC 4970 - Module 6 - Final Project

PyQt5 Interface

Description:

This project contains classes with methods of a Curling League Manager, unit tests, and a pyqt5 interface that uses 
these classes and methods.

Instructions:

To execute the user interface, run main_window_exec.py in the main_ui package (which is inside the module6 package) to run the main window.

    module6
        main_ui
            main_window_exec.py
The main window contains buttons, a list, file load/save menu items, and an input line:

    Main Window
        File Menu Items:
            Load - load a selected DAT or Backup file
            Save - save a new DAT or Backup file
        List - displays leagues in the database
        Buttons:
            Delete - delete a league selected from the list
            Edit - edit a selected league in a dialog box
            Add - add a new league typed from the input line
            Load - laod a selected file
            Save - save a new file
        Input Line - enter a league name
The edit dialog for a selected league contains some similar buttons and an input line, plus to new buttons:
    
    Edit League Dialog
        List - displays teams in the selected league
        Buttons:
            Delete - delete a team selected from the list
            Edit - edit a selected team in a dialog box
            Add - add a new team typed from the input line
            Import - import the teams and their members from a csv file
            Export - export the teams and their members in a new csv file
        Input Line - enter a team name

Finally, the edit dialog for a selected team contains the following elements:

    Edit Team Dialog
        List - displays members in the selected team
        Buttons:
            Delete - delete a member selected from the list
            Edit - edit a selected member's name and email from the name and email input lines
            Add - add a new member typed from the name and email input lines
        Input Lines:
            Name Line: enter a member name
            Email Line: enter a member email