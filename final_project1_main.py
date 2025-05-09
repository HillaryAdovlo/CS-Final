import sys
from PyQt6  import QtWidgets
from final_project1_gui import Ui_VotingApp
from final_project1_logic import VoteCounter

def main():
    vote_manager = VoteCounter('votes.csv', 'final_project1.csv')
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_VotingApp(vote_manager)
    window.VotingApp.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
