import sys
import des
from PyQt4 import QtGui
from PyQt4 import QtCore

class qtui(QtGui.QMainWindow):
    
    def __init__(self):
        super(qtui, self).__init__()
        
        self.initUI()
    
    def initUI(self):

#button = QtGui.QPushButton(u'Open File', parent=self)

#        button.clicked.connect(self.add)

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
        self.setWindowTitle('Des Encryptor')
        self.show()

    def showAbout(self):
        dialog = aboutDialog(parent = self)
        dialog.exec_()
        dialog.destroy()
        
class aboutDialog(QtGui.QDialog):

    def __init__(self, parent = None):

        QtGui.QDialog.__init__(self, parent)

        grid = QtGui.QGridLayout()
        
        self.resize(200, 100)
        self.setMinimumSize(200, 100)
        self.setMaximumSize(200, 100)
        buttonBox = QtGui.QDialogButtonBox(parent=self)
        buttonBox.setOrientation(QtCore.Qt.Horizontal)
        buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        buttonBox.accepted.connect(self.accept)
        buttonBox.move(40, 70)
        
        grid.addWidget(QtGui.QLabel('A simple program to encryptor data'), 0, 0)
        grid.addWidget(QtGui.QLabel('Version 1.0'), 1, 0)
        grid.addWidget(QtGui.QLabel('Author: Brickgao'), 2, 0)
        grid.addWidget(QtGui.QLabel(''), 3, 0)
    
        self.setWindowTitle('About')
       
        self.setLayout(grid) 

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = qtui()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
