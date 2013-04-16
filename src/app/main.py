import sys
import des
import check
from PyQt4 import QtGui, QtCore

class qtui(QtGui.QMainWindow):
    
    def __init__(self):
        super(qtui, self).__init__()
        
        self.initUI()
    
    def initUI(self):

        self.fileinstr = ''
        self.fileoutstr = ''
        self.typestr = 'Encrypt'
        
        self.pbar = QtGui.QProgressBar(parent = self)
        self.pbar.setGeometry(65, 130, 265, 20)
        self.pbar.setValue(0)
        
        self.combo = QtGui.QComboBox(self)
        self.combo.resize(80, 20)
        self.combo.addItem("Encrypt")
        self.combo.addItem("Unencrypt")
        self.combo.addItem("Check")
        
        self.combo.activated[str].connect(self.onActivated)

        self.report = QtGui.QTextEdit(parent = self)
        self.report.resize(380, 80)
        
        buttonfin = QtGui.QPushButton(u'Open File', parent = self)
        buttonfin.resize(80, 20)
        buttonfout = QtGui.QPushButton(u'Open File', parent = self)
        buttonfout.resize(80, 20)
        buttonstart = QtGui.QPushButton(u'Start', parent = self)
        buttonstart.resize(80, 20)
    
        buttonfin.clicked.connect(self.fileinslot)
        buttonfout.clicked.connect(self.fileoutslot)
        buttonstart.clicked.connect(self.startop)

        fileinlb = QtGui.QLabel('File in', self)
        fileoutlb = QtGui.QLabel('File out', self)
        progresslb = QtGui.QLabel('Progress', self)
        typelb = QtGui.QLabel('Type', parent = self)
        
        self.filein = QtGui.QLineEdit(self)
        self.filein.resize(235, 20)
        self.fileout = QtGui.QLineEdit(self)
        self.fileout.resize(235, 20)
        
        buttonfin.move(310, 65)
        buttonfout.move(310, 95)
        buttonstart.move(310, 35)
    
        self.filein.move(65, 65)
        self.fileout.move(65, 95)
        
        typelb.move(10, 30)
        fileinlb.move(10, 60)
        fileoutlb.move(10, 90)
        progresslb.move(10, 125)
    
        self.report.move(10, 160)
    
        self.combo.move(65, 35)
        
        aboutAction = QtGui.QAction('&About', self)
        aboutAction.setShortcut('Ctrl+A')
        aboutAction.setStatusTip('About the program')
        aboutAction.triggered.connect(self.showAbout)
        
        exitAction = QtGui.QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)
        
        self.statusBar()
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(aboutAction)
        fileMenu.addAction(exitAction)
        
        self.setGeometry(300, 300, 400, 250)
        self.setMinimumSize(400, 250)
        self.setMaximumSize(400, 250)
        self.setWindowTitle('Des Encryptor')
        
        self.show()
    
    def alertTrue(self):
        dialog = AlTrue(parent = self)
        dialog.exec_()
        dialog.destroy()
        
    def alertFalse(self):
        dialog = AlFalse(parent = self)
        dialog.exec_()
        dialog.destroy()

    def alertnofile(self):
        dialog = Alertname(parent = self)
        dialog.exec_()
        dialog.destroy()

    def showAbout(self):
        dialog = aboutDialog(parent = self)
        dialog.exec_()
        dialog.destroy()

    def fileinslot(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file')
        self.fileinstr = fname
        self.filein.setText(fname)
        
    def fileoutslot(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file')
        self.fileoutstr = fname
        self.fileout.setText(fname)

    def onActivated(self, text):
        self.typestr = text
    
    def startop(self):
        self.pbar.setValue(0)
        if(self.typestr == 'Encrypt'):
            self.startdes()
        if(self.typestr == 'Unencrypt'):
            self.startundes()
        if(self.typestr == 'Check'):
            self.startcheck()

    def startdes(self):
        if self.fileinstr != '':
            if self.fileoutstr == '':
                self.fileoutstr = self.fileinstr + '_DES'
                self.fileout.setText(self.fileoutstr)
            dodes = des.DES()
            dodes.input_encode(self, self.fileinstr, self.fileoutstr)
        else:
            self.alertnofile()
        
    def startundes(self):
        if self.fileinstr != '':
            if self.fileoutstr == '':
                self.fileoutstr = self.fileinstr + '_UNDES'
                self.fileout.setText(self.fileoutstr)
            dodes = des.DES()
            dodes.input_uncode(self, self.fileinstr, self.fileoutstr)
        else:
            self.alertnofile()
        
    def startcheck(self):
        if self.fileinstr != '' and self.fileoutstr != '':
            docheck = check.main()
            if docheck.check(self, self.fileinstr, self.fileoutstr) == True:
                self.alertTrue()
            else:
                self.alertFalse()
        else:
            self.alertnofile()

class aboutDialog(QtGui.QDialog):

    def __init__(self, parent = None):
        
        QtGui.QDialog.__init__(self, parent)
        
        self.resize(250, 100)
        self.setMinimumSize(250, 100)
        self.setMaximumSize(250, 100)
        buttonBox = QtGui.QDialogButtonBox(parent=self)
        buttonBox.setOrientation(QtCore.Qt.Horizontal)
        buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        buttonBox.accepted.connect(self.accept)
        buttonBox.move(75, 70)
        
        lb1 = QtGui.QLabel('A simple program to encryptor data', self)
        lb2 = QtGui.QLabel('Version 1.0', self)
        lb3 = QtGui.QLabel('Author: Brickgao', self)
        
        lb1.move(20, 15)
        lb2.move(80, 30)
        lb3.move(70, 45)
    
        self.setWindowTitle('About')
       
        self.show()

class Alertname(QtGui.QDialog):

    def __init__(self, parent = None):
        
        QtGui.QDialog.__init__(self, parent)

        grid = QtGui.QGridLayout()
        
        self.resize(200, 80)
        self.setMinimumSize(200, 80)
        self.setMaximumSize(200, 80)
        buttonBox = QtGui.QDialogButtonBox(parent=self)
        buttonBox.setOrientation(QtCore.Qt.Horizontal)
        buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        buttonBox.accepted.connect(self.accept)
        buttonBox.move(60, 50)
        
        lb = QtGui.QLabel('Please select the file', self)

        lb.move(30, 20)
    
        self.setWindowTitle('Alert')
       
        self.show()
    
class AlTrue(QtGui.QDialog):

    def __init__(self, parent = None):
        
        QtGui.QDialog.__init__(self, parent)

        grid = QtGui.QGridLayout()
        
        self.resize(200, 80)
        self.setMinimumSize(200, 80)
        self.setMaximumSize(200, 80)
        buttonBox = QtGui.QDialogButtonBox(parent=self)
        buttonBox.setOrientation(QtCore.Qt.Horizontal)
        buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        buttonBox.accepted.connect(self.accept)
        buttonBox.move(60, 50)
        
        lb = QtGui.QLabel('Two file is same', self)

        lb.move(50, 20)
    
        self.setWindowTitle('Alert')
       
        self.show()
    
class AlFalse(QtGui.QDialog):

    def __init__(self, parent = None):
        
        QtGui.QDialog.__init__(self, parent)

        grid = QtGui.QGridLayout()
        
        self.resize(200, 80)
        self.setMinimumSize(200, 80)
        self.setMaximumSize(200, 80)
        buttonBox = QtGui.QDialogButtonBox(parent=self)
        buttonBox.setOrientation(QtCore.Qt.Horizontal)
        buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        buttonBox.accepted.connect(self.accept)
        buttonBox.move(60, 50)
        
        lb = QtGui.QLabel('Two file is not same', self)

        lb.move(40, 20)
    
        self.setWindowTitle('Alert')
       
        self.show()

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = qtui()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
