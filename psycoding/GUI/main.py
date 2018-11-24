import sys, os, json, multiprocessing, collections

from PyQt5.QtWidgets import (QWidget, QMainWindow, QAction, 
            qApp, QApplication, QTextEdit, QVBoxLayout, QHBoxLayout, 
            QPushButton, QScrollArea, QFileDialog, QMessageBox)
from PyQt5.QtGui import QIcon, QFont, QPixmap
import jieba
sys.path.append(".")
from psycoding.ffmpeg.psy_ffmpeg import psy_ffmpeg
from psycoding.xunfei import xunfei

#from ffmpeg.psy_ffmpeg import psy_ffmpeg

# Global variable
# configcls manages the configure of the software.
# Now it manage
# 1. video path.
# 2. ffmpeg binary path.
class configcls:
    def __init__(self, configpath=None):
        self.__videopath = None
        self.__ffmpegbinpath = None
        # if configpath:
        #     with open(configpath,'r') as f:
        #         config_json = json.loads(f.read())
        # else:
        #     defaultconfigpath = os.path.join(os.getcwd(),'config.json')
        #     config_json = json.loads(defaultconfigpath)
        self.videopath = config_json['videopath']
        self.ffmpegbinpath = config_json['ffmpegbinpath']
        print(self.videopath, self.ffmpegbinpath)

    def set_videopath(self, videopath):
        self.__videopath = videopath
        
    def get_videopath(self, videopath):
        return self.__videopath
        
    def set_ffmpegbinpath(self, ffmpegbinpath):
        self.__ffmpegbinpath = ffmpegbinpath
        
    def get_ffmpegbinpath(self, ffmpegbinpath):
        return self.__ffmpegbinpath

"""
Init global class 
"""
# ffmpeg instance
ffins = psy_ffmpeg("config.json")
xfins = xunfei()
#cfgins = configcls()


#Configure Action


"""
Convert data
"""
audiodatapath = []

textdatapath = []

def getfilename():
    videopath = QFileDialog.getOpenFileName()

def savefile():
    savefile = QFileDialog.getSaveFileName()
    savedfilepath = savefile[0]
    

class mainwidget(QWidget):
    def __init__(self):
        super().__init__()
        self.textbox = []
        self.videopath = ""
        self.savefilename = ""
        self.__textbox = []
        self.__textboxindex = 0
        self.__wordset = set()
        self.initUI()

    def getfilename(self):
        self.videopath = QFileDialog.getOpenFileName()[0]
        assert(type(self.videopath) is str)

    def configffmpeg(self):
        ffmpegbinpath = QFileDialog.getOpenFileName()
        if ffins.checkffmpeg(ffmpegbinpath):
            self.videopath = ffmpegbinpath
        else:
            QMessageBox.warning(self,"Warning","invalid path.", QMessageBox.Ok)
        #self.setStatusTip("load ffmpeg successfully!")
    
    def configwordset(self):
        wordfilepath = QFileDialog.getOpenFileName()[0]
        if not wordfilepath:
            return 
        with open(wordfilepath, 'rb') as f:
            while 1:
                line = f.readline()
                if not line:
                    break
                self.__wordset.add(line.decode('utf8').strip())
        print(self.__wordset)
        

    def audio2text_fortestuse(self):
        inputstr = xfins.audio2text(0)
        print(inputstr)

    def loadvideo_launch(self):
        p = multiprocessing.process(target=self.loadvideo)
        p.start()

    def loadvideo(self):
        self.getfilename()
        if not ffins.ffmpegbinpath:
            QMessageBox.warning(self,"Warning","empty ffmpegpath, please set path of ffmpeg.", QMessageBox.Ok)
        #self.statusTip("starting converting video...")
        print(self.videopath)
        if not self.videopath:
            return 
        output_audio_list = ffins.VideoToAudio(self.videopath)
        print("video has been transferred to audio!")
        xfins.set_audio_path(output_audio_list)
        inputstr_list = xfins.generate_text()
        #inputstr = xfins.audio2text(0)
        linecnt = 0
        for i in range(len(inputstr_list)):
            inputstr_list[i] = str(linecnt)+" min-" + str(linecnt + 1) + " min: " + inputstr_list[i]
            linecnt += 1
        for inputstr in inputstr_list:
            self.addtextbox(inputstr)
        # write to textfile
        tmpout = "tmpdata.txt"
        linecnt = 0
        with open(tmpout, 'w') as f:
            for inputstr in inputstr_list:
                f.writelines(inputstr + "\n")

    def load_processed_data(self):
        self.__textboxindex = []
        self.__textboxindex = 0
        processed_data_path = QFileDialog.getOpenFileName()[0]
        if not processed_data_path:
            return 
        textfile_list = []
        with open(processed_data_path, 'r') as f:
            while 1:
                line = f.readline()
                if not line:
                    break
                textfile_list += [line]
        self.addtextboxlist(textfile_list)


    def savefile(self):
        if self.savefilename == "":
            self.savefilename = QFileDialog.getSaveFileName()[0]
        linecnt = 0
        with open(self.savefilename, 'w') as f:
            for i in range(len(self.__textbox)):
                content = self.__textbox[i].toPlainText()
                if not content.startswith("defaultdict"):
                    f.writelines(content + "\n")

    

    def saveas(self):
        self.savefilename = QFileDialog.getSaveFileName()
        savefile()

    def addtextboxlist(self, inputstrlist=None):
        self.__textboxindex += len(inputstrlist)
        for s in inputstrlist:
            tb = QTextEdit()
            if not s:
                tb.setText("no input")
            else:
                tb.setText(s)
            tb.setFixedHeight(100)
            
            self.vbox.addWidget(tb)
            self.__textbox += [tb]
        self.show()

    def addtextbox(self, inputstr=None):
        self.__textboxindex += 1
        tb = QTextEdit()
        if not inputstr:
            tb.setText("no input")
        else:
            tb.setText(inputstr)
        tb.setFixedHeight(100)
        
        self.vbox.addWidget(tb)
        self.__textbox += [tb]
        self.show()
    
    def initUI(self):
        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)
        #self.setAutoFillBackground(True)
        self.show()

    def matchwords(self):
        """
        Method of Analyze -> matchwords
        """
        for i in range(len(self.__textbox)):
            context = self.__textbox[i].toPlainText()
            resdict = collections.defaultdict(int)
            for t in self.__wordset:
                if t in context:
                    resdict[t] += 1
            if len(resdict.keys()) == 0:
                continue
            self.addtextbox(str(resdict) + context)

    def cutwords(self):
        pass

    def saanalysis(self):
        """
        sentimental analysis
        """
        pass

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

        # File -> Load processed data
        load_processed_dataAction = QAction('&Load processedfile', self)
        load_processed_dataAction.setStatusTip('choose processed file')
        load_processed_dataAction.triggered.connect(mw.load_processed_data)

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

        # Analyze -> matchwords
        matchwordsAction = QAction('&matchwords', self)       
        matchwordsAction.setStatusTip('matchwords')
        matchwordsAction.triggered.connect(mw.matchwords)
        
        # Analyze -> sentimental analysis
        saAction = QAction('&sentimental analysis', self)       
        saAction.setStatusTip('sentimental analysis')
        saAction.triggered.connect(mw.saanalysis)
        
        # Config -> wordset
        configwordsetAction = QAction('&wordsetfilepath',self)
        configwordsetAction.triggered.connect(mw.configwordset)

        # build menubar
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        
        # menubar -> File
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(loadvideoAction)
        fileMenu.addAction(load_processed_dataAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(saveAsAction)
        fileMenu.addAction(exitAction)

        # menubar -> analyze
        AnalyzeMenu = menubar.addMenu('Analyze')
        AnalyzeMenu.addAction(matchwordsAction)
        AnalyzeMenu.addAction(saAction)
        configffmpegAction = QAction("ffmpegpath",self)
        configffmpegAction.setStatusTip("config ffmpeg bin path")
        configffmpegAction.triggered.connect(mw.configffmpeg)
        
        # menubar -> config
        ConfigMenu = menubar.addMenu('Configure')
        ConfigMenu.addAction(configffmpegAction)
        ConfigMenu.addAction(configwordsetAction)

        # menubar -> About
        AboutMenu = menubar.addMenu("About")

        self.statusBar()
        
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
    # print(os.getcwd())
    # rootdir = os.path.join(os.getcwd(),'config.json')
    # with open(rootdir,'r') as f:
    #     jdata = json.loads(f.read())
    #     print(jdata)
    #     print(jdata['rootfile'])
        #print(f.read())
    #print(os.path.dirname(os.getcwd()))
    #testcls = configcls(configpath=r"C:\Users\hongy\Documents\work\cici\BehavioralCoding-cs410project\psycoding\GUI\main.py")
    app = QApplication(sys.argv)
    #app.setWindowIcon(QIcon('./apple.ico'))
    
    ins = Example()
    sys.exit(app.exec_())
    #ffmpegcls = psy_ffmpeg()
    #ffmpegcls.VideoToAudio(videofilefullpath = "C:\\Users\\hongy\\Documents\\work\\cici\\ffmpeg-4.0.2-win64\\bin\\codingexample.mov")
