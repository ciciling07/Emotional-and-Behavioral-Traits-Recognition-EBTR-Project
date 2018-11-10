import sys
from PyQt5.QtWidgets import (QWidget, QMainWindow, QAction, 
            qApp, QApplication, QTextEdit, QVBoxLayout, QHBoxLayout, 
            QPushButton, QScrollArea, QFileDialog)
from PyQt5.QtGui import QIcon, QFont, QPixmap


"""
Global variable

"""
videopath = ""

def getfilename():
    # get video path
    videopath = QFileDialog.getOpenFileName()
    
    # processing video
    #return fname
    #print(fname)

def savefile():
    print('you got it')


class mainwidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        vbox = QVBoxLayout()
        t1 = QTextEdit()
        t1.setText("hi t1")
        t1.setFixedHeight(600)
        #t1.setAutoFillBackground(True)
        vbox.addWidget(t1)
        t2 = QTextEdit()
        t2.setText("hi t2")
        t2.setFixedHeight(600)
        vbox.addWidget(t2)
        t3 = QTextEdit()
        t3.setText("hi t3")
        t3.setFixedHeight(600)
        vbox.addWidget(t3)
        self.setLayout(vbox)
        #self.setAutoFillBackground(True)
        self.show()

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # QToolTip.setFont(QFont('SansSerif', 10))
        # self.setToolTip('This is a <b>QWidget</b> widget')
        # btn = QPushButton('Button', self)
        # btn.setToolTip('This is a <b>QPushButton</b> widget')
        # btn.resize(btn.sizeHint())
        # #btn.clicked.connect(QCoreApplication.instance().quit)
        # btn.move(50,50)
        # self.setGeometry(100,100,300,300)
        # self.setWindowTitle("Icon")
        # #self.setWindowIcon(QIcon('C:\\Users\\hongy\\Documents\\work\\cici\\BehavioralCoding-cs410project\\psycoding\\GUI\\icon.png'))
        # self.setWindowIcon(QIcon('/Users/yuxi/work/cici/BehavioralCoding-cs410project/psycoding/GUI/icon.jpg'))
        # self.show()

        # File -> Load video 
        loadvideoAction = QAction('&Load video', self)
        loadvideoAction.setStatusTip('choose video file')
        loadvideoAction.triggered.connect(getfilename)
        # File -> Save file
        saveAction = QAction('&Save File', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save edit file to disk')
        saveAction.triggered.connect(savefile)

        # File -> Exit
        exitAction = QAction('&Exit', self)       
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)


        # build menubar
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        # menubar -> File
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(loadvideoAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(exitAction)
        self.statusBar()
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')   
        self.show()
        

        # textEdit = QTextEdit()
        # textEdit.setText("hellpo")
        # textEdit.setGeometry(100,100,100,100)
        sc = QScrollArea()
        sc.setWidget(mainwidget())
        sc.setAutoFillBackground(True)
        sc.setWidgetResizable(True)
        self.setCentralWidget(sc)
        self.setGeometry(500, 100, 800, 500)
        self.setFixedHeight(800)
        self.setWindowTitle('Buttons')    
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    #app.setWindowIcon(QIcon('./apple.ico'))
    
    ex = Example()
    sys.exit(app.exec_())