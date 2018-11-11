import sys,os

from PyQt5.QtWidgets import (QWidget, QMainWindow, QAction, 
            qApp, QApplication, QTextEdit, QVBoxLayout, QHBoxLayout, 
            QPushButton, QScrollArea, QFileDialog)
from PyQt5.QtGui import QIcon, QFont, QPixmap

sys.path.append("..")


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
    savefile = QFileDialog.getSaveFileName()
    print(savefile)


class mainwidget(QWidget):
    def __init__(self):
        super().__init__()
        self.textbox = []
        self.savefilename = ""
        self.initUI()
    def loadvideo(self):
        result = "\xe7\x9c\x8b\xe7\x9c\x8b\xe5\x91\x97\xe5\x87\xba\xe5\x8f\x91\xef\xbc\x8c\xe5\xb0\xb1\xe6\x98\xaf\xe8\xbf\x99\xe6\xa0\xb7\xef\xbc\x8c\xe6\x88\x91\xe4\xb8\x8d\xe6\x83\xb3\xe6\xaf\x8f\xe5\xa4\xa9\xe5\xb0\xb1\xe6\x98\xaf\xe5\xb7\xa5\xe4\xbd\x9c\xe5\x8d\x95\xe4\xbd\x8d\xe5\x88\xb0\xe5\xae\xb6\xef\xbc\x8c\xe7\x84\xb6\xe5\x90\x8e\xe5\xb0\xb1\xe3\x80\x82"
        result = result.encode("raw_unicode_escape")
        resultstr = result.decode()
        print(resultstr)
        t4 = QTextEdit()
        t4.setText(resultstr)
        t4.setFixedHeight(100)
        self.vbox.addWidget(t4)
        self.show()
        #with open(Output_path,"w") as f:
        #    f.writelines(result.decode())

    def savefile(self):
        if self.savefilename == "":
            self.savefilename = QFileDialog.getSaveFileName()
        print(self.savefilename)
        content = self.textbox[0].toPlainText()
        print("content of t1 is " , content)
    
    def saveas(self):
        self.savefilename = QFileDialog.getSaveFileName()
        savefile()
    
    def addatextbox(self):
        t4 = QTextEdit()
        t4.setText("hi t4")
        t4.setFixedHeight(100)
        t4 = QTextEdit()
        t4.setText("hi t4")
        t4.setFixedHeight(100)
        self.vbox.addWidget(t4)
        self.show()
    
    def initUI(self):
        self.vbox = QVBoxLayout()
        t1 = QTextEdit()
        t1.setText("hi t1")
        t1.setFixedHeight(100)
        #t1.setAutoFillBackground(True)
        self.vbox.addWidget(t1)
        self.textbox.append(t1)
        t2 = QTextEdit()
        t2.setText("hi t2")
        t2.setFixedHeight(100)
        self.vbox.addWidget(t2)
        t3 = QTextEdit()
        t3.setText("hi t3")
        t3.setFixedHeight(100)
        self.vbox.addWidget(t3)
        self.setLayout(self.vbox)
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

        mw = mainwidget()

        # File -> Load video 
        loadvideoAction = QAction('&Load video', self)
        loadvideoAction.setStatusTip('choose video file')
        loadvideoAction.triggered.connect(mw.loadvideo)
        
        # File -> Save file
        saveAction = QAction('&Save File', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save edit file to disk')
        saveAction.triggered.connect(mw.savefile)

        # File -> Save As
        saveAsAction = QAction('&Save As', self)
        saveAsAction.setStatusTip('Save file to a new document')
        saveAsAction.triggered.connect(mw.savefile)

        # File -> Exit
        exitAction = QAction('&Exit', self)       
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        testAction = QAction('&Addtextbox',self)
        testAction.triggered.connect(mw.addatextbox)

        # build menubar
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        # menubar -> File
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(loadvideoAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(saveAsAction)
        fileMenu.addAction(exitAction)
        fileMenu.addAction(testAction)
        # menubar -> analyze
        AnalyzeMenu = menubar.addMenu('Analyze')
        
        # menubar -> config
        ConfigMenu = menubar.addMenu('Configure')

        # menubar -> About
        AboutMenu = menubar.addMenu("About")

        self.statusBar()
        
        # textEdit = QTextEdit()
        # textEdit.setText("hellpo")
        # textEdit.setGeometry(100,100,100,100)
        # instance of mainwidget
       
        sc = QScrollArea()
        sc.setWidget(mw)
        sc.setAutoFillBackground(True)
        sc.setWidgetResizable(True)
        self.setCentralWidget(sc)
        self.setGeometry(500, 100, 800, 500)
        self.setFixedHeight(800)
        self.setWindowTitle('BehavioralcodingTools')    
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    #app.setWindowIcon(QIcon('./apple.ico'))
    
    ex = Example()
    sys.exit(app.exec_())