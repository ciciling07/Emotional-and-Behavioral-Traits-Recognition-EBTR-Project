import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
from PyQt5.QtGui import QIcon

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100,100,300,300)
        self.setWindowTitle("Icon")
        self.setWindowIcon(QIcon('C:\\Users\\hongy\\Documents\\work\\cici\\BehavioralCoding-cs410project\\psycoding\\GUI\\icon.png'))
        
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())