# 1简单的窗口
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
# # 如果当前是主程序的意思？可以不用吧？c++来的概念？
# if __name__ == '__main__':
#     # 创建app
#     app = QApplication(sys.argv)
#     # 创建窗口
#     w = QWidget()
#     w.resize(250, 150)
#     w.move(300, 300)
#     w.setWindowTitle('simple')
#     w.show()
#
#     sys.exit(app.exec_())

# 2带窗口图标
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
# from PyQt5.QtGui import QIcon
#
#
# class Example(QWidget):
#     def __init__(self):
#         super(Example, self).__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         self.setGeometry(300, 300, 300, 220)
#         self.setWindowTitle('Icon')
#         self.setWindowIcon(QIcon('web.png'))
#         self.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# 3提示框
# import sys
# from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication
# from PyQt5.QtGui import QFont
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         QToolTip.setFont(QFont('SansSerif', 10))
#         self.setToolTip('This is a <b>QWidget</b> widget')
#         btn = QPushButton('Button', self)
#         btn.setToolTip('This is a <b>QPushButton</b> widget')
#         btn.resize(btn.sizeHint())
#         btn.move(50, 50)
#
#         self.setGeometry(300, 300, 300, 200)
#         self.setWindowTitle('ToolTips')
#         self.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# 4关闭窗口
# import sys
# from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
# from PyQt5.QtCore import QCoreApplication, QObject
#
#
# class Example(QWidget):
#     def __init__(self):
#         super(Example, self).__init__()
#         self.initUI()
#
#     def initUI(self):
#         qbtn = QPushButton('Quit', self)
#         qbtn.clicked.connect(QCoreApplication.instance().quit)
#         qbtn.resize(qbtn.sizeHint())
#         qbtn.move(50, 50)
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle('Quit button')
#         self.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# 5消息盒子
# import sys
# from PyQt5.QtWidgets import QWidget,QMessageBox,QApplication
#
# class Example(QWidget):
#     def __init__(self):
#         super(Example, self).__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setGeometry(300,300,250,150)
#         self.setWindowTitle('Message box')
#         self.show()
#
#     def closeEvent(self, event):
#         reply=QMessageBox.question(self,'Message','Are you sure to quit?',QMessageBox.Yes|QMessageBox.No,
#                                    QMessageBox.No)
#         if reply==QMessageBox.Yes:
#             event.accept()
#         else:
#             event.ignore()
#
# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     ex=Example()
#     sys.exit(app.exec_())

# 6窗口居中
# import sys
# from PyQt5.QtWidgets import QWidget,QDesktopWidget,QApplication
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.resize(250,150)
#         self.center()
#
#         self.setWindowTitle('Center')
#         self.show()
#
#     def center(self):
#         qr=self.frameGeometry()
#         cp=QDesktopWidget().availableGeometry().center()
#         qr.moveCenter(cp)
#         self.move(qr.topLeft())
#
# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     ex=Example()
#     sys.exit(app.exec_())

# 7状态栏
# import sys
# from PyQt5.QtWidgets import QMainWindow,QApplication
#
# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.statusBar().showMessage('Ready')
#         self.setGeometry(300,300,250,150)
#         self.setWindowTitle('Statusbar')
#         self.show()
#
# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     ex=Example()
#     sys.exit(app.exec_())

# 8菜单栏
# import sys
# from PyQt5.QtWidgets import QMainWindow,QAction,qApp,QApplication
# from PyQt5.QtGui import QIcon
#
# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         exitAction=QAction(QIcon('exit.png'),'&Exit',self)
#         exitAction.setShortcut('Ctrl+Q')
#         exitAction.setStatusTip('Exit application')
#         exitAction.triggered.connect(qApp.quit)
#         self.statusBar()
#         menubar=self.menuBar()
#         fileMenu=menubar.addMenu('&File')
#         fileMenu.addAction(exitAction)
#         self.setGeometry(300,300,300,200)
#         self.setWindowTitle('Menubar')
#         self.show()
#
# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     ex=Example()
#     sys.exit(app.exec_())

# 9工具栏
# import sys
# from PyQt5.QtWidgets import QMainWindow,QAction,qApp,QApplication
# from PyQt5.QtGui import QIcon
#
# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         exitAction=QAction(QIcon('exit24.png'),'Exit',self)
#         exitAction.setShortcut('Ctrl+Q')
#         exitAction.triggered.connect(qApp.quit)
#         self.toolbar=self.addToolBar('Exit')
#         self.toolbar.addAction(exitAction)
#         self.setGeometry(300,300,300,200)
#         self.setWindowTitle('Toolbar')
#         self.show()
#
# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     ex=Example()
#     sys.exit(app.exec_())

# 10主窗口
# import sys
# from PyQt5.QtWidgets import QMainWindow,QTextEdit,QAction,QApplication
# from PyQt5.QtGui import QIcon
#
#
# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         textEdit=QTextEdit()
#         self.setCentralWidget(textEdit)
#         exitAction=QAction(QIcon('exit24.png'),'Exit',self)
#         exitAction.setShortcut('Ctrl+Q')
#         exitAction.setStatusTip('Exit application')
#         exitAction.triggered.connect(self.close)
#         self.statusBar()
#         menubar=self.menuBar()
#         fileMenu=menubar.addMenu('&File')
#         fileMenu.addAction(exitAction)
#         toolbar=self.addToolBar('Exit')
#         toolbar.addAction(exitAction)
#         self.setGeometry(300,300,300,200)
#         self.setWindowTitle('Main window')
#         self.show()
#
# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     ex=Example()
#     sys.exit(app.exec_())

# 绝对定位,实际不会用的，不灵活
# import sys
# from PyQt5.QtWidgets import QWidget,QLabel,QApplication
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         lbl1=QLabel('Zetcode',self)
#         lbl1.move(15,10)
#         lbl2=QLabel('tutorials',self)
#         lbl2.move(35,40)
#         lbl3=QLabel('for programmer',self)
#         lbl3.move(55,70)
#         self.setGeometry(300,300,250,150)
#         self.setWindowTitle('Absolute')
#         self.show()
#
# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     ex=Example()
#     sys.exit(app.exec_())

# 盒布局
# import sys
# from PyQt5.QtWidgets import QWidget,QPushButton,QHBoxLayout,QVBoxLayout,QApplication
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         okButton=QPushButton('OK')
#         cancelButton=QPushButton('Cancle')
#         hbox=QHBoxLayout()
#         hbox.addStretch(1)
#         hbox.addWidget(okButton)
#         hbox.addWidget(cancelButton)
#         vbox=QVBoxLayout()
#         vbox.addStretch(1)
#         vbox.addLayout(hbox)
#         self.setLayout(vbox)
#         self.setGeometry(300,300,300,150)
#         self.setWindowTitle('Button')
#         self.show()
#
# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     ex=Example()
#     sys.exit(app.exec_())

# 格栅布局，最常用
# import sys
# from PyQt5.QtWidgets import QWidget,QGridLayout,QPushButton,QApplication
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         grid =QGridLayout()
#         self.setLayout(grid)
#         names=['Cls','Bck',',','Close','7','8','9','/','4','5','6','*','1','2','3','-'
#                ,'0','.','=','+']
#         positions=[(i,j)for i in range(5) for j in range(4)]
#         for positon, name in zip(positions,names):
#             if name =='':
#                 continue
#             button =QPushButton(name)
#             grid.addWidget(button,*positon)
#         self.move(300,150)
#         self.setWindowTitle('Calculator')
#         self.show()
#
# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     ex=Example()
#     sys.exit(app.exec_())

# 制作反馈信息提交布局
# import sys
# from PyQt5.QtWidgets import QWidget,QLabel,QLineEdit,QTextEdit,QGridLayout,QApplication
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.unitUI()
#
#     def unitUI(self):
#         title=QLabel('Title')
#         author=QLabel('Author')
#         review=QLabel('Review')
#         titleEdit=QLineEdit()
#         authorEdit=QLineEdit()
#         reviewEdit=QTextEdit()
#         grid=QGridLayout()
#         grid.setSpacing(10)
#         grid.addWidget(title,1,0)
#         grid.addWidget(titleEdit,1,1)
#         grid.addWidget(author,2,0)
#         grid.addWidget(authorEdit,2,1)
#         grid.addWidget(review,3,0)
#         grid.addWidget(reviewEdit,3,1,5,1)
#         self.setLayout(grid)
#         self.setGeometry(300,300,350,300)
#         self.setWindowTitle('Review')
#         self.show()
#
# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     ex=Example()
#     sys.exit(app.exec_())


# Signal&Slot
# import sys
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QWidget,QLCDNumber,QSlider,QVBoxLayout,QApplication
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.unitUI()
#
#     def unitUI(self):
#         lcd=QLCDNumber(self)
#         sld=QSlider(Qt.Horizontal,self)
#         vbox=QVBoxLayout()
#         vbox.addWidget(lcd)
#         vbox.addWidget(sld)
#         self.setLayout(vbox)
#         sld.valueChanged.connect(lcd.display)
#
#         self.setGeometry(300,300,250,150)
#         self.setWindowTitle('Signal&Slot')
#         self.show()
#
# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     ex=Example()
#     sys.exit(app.exec_())


# 重构事件处理器
# import sys
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QWidget,QApplication
#
#
# class Example(QWidget):
#     def __init__(self):
#         super(Example, self).__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setGeometry(300,300,250,150)
#         self.setWindowTitle('Event Handler')
#         self.show()
#
#     def keyPressEvent(self, e):
#         if e.key()==Qt.Key_Escape:
#             self.close()
#
# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     ex=Example()
#     sys.exit(app.exec_())

# 事件发送
# import sys
# from PyQt5.QtWidgets import QMainWindow,QPushButton,QApplication
#
# class Example(QMainWindow):
#     def __init__(self):
#         super(Example, self).__init__()
#         self.initUI()
#
#     def initUI(self):
#         btn1=QPushButton('Button 1',self)
#         btn1.move(30,50)
#         btn2=QPushButton('Button 2',self)
#         btn2.move(150,50)
#         btn1.clicked.connect(self.buttonClicked)
#         btn2.clicked.connect(self.buttonClicked)
#         self.statusBar()
#         self.setGeometry(300,300,290,150)
#         self.setWindowTitle('Event sender')
#         self.show()
#
#     def buttonClicked(self):
#         sender=self.sender()
#         self.statusBar().showMessage(sender.text()+'was pressed')
#
# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     ex=Example()
#     sys.exit(app.exec_())

# 信号发送
# import sys
# from PyQt5.QtCore import pyqtSignal,QObject
# from PyQt5.QtWidgets import QMainWindow,QApplication
#
#
# class Communicate(QObject):
#     closeApp=pyqtSignal()
#
# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.c=Communicate()
#         self.c.closeApp.connect(self.close)
#
#         self.setGeometry(300,300,290,150)
#         self.setWindowTitle('Emit signal')
#         self.show()
#
#     def mousePressEvent(self, event):
#         self.c.closeApp.emit()
#
# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     ex=Example()
#     sys.exit(app.exec_())

# 对话框

# import sys
# from PyQt5.QtWidgets import QWidget,QPushButton,QLineEdit,QInputDialog,QApplication
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.btn=QPushButton('Dialog',self)
#         self.btn.move(20,20)
#         self.btn.clicked.connect(self.showDialog)
#
#         self.le=QLineEdit(self)
#         self.le.move(130,22)
#
#         self.setGeometry(300,300,290,150)
#         self.setWindowTitle('Input Dialog')
#         self.show()
#
#     def showDialog(self):
#         text,ok=QInputDialog.getText(self,'Input dialog','Enter your name:')
#         if ok:
#             self.le.setText((text))
#
# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     ex=Example()
#     sys.exit(app.exec_())

# 提供颜色的选择的对话框
# import sys
# from PyQt5.QtWidgets import QWidget,QPushButton,QFrame,QColorDialog,QApplication
# from PyQt5.QtGui import QColor
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         col=QColor(0,0,0)
#         self.btn=QPushButton('Dialog',self)
#         self.btn.move(20,20)
#         self.btn.clicked.connect(self.showDialog)
#         self.frm=QFrame(self)
#         self.frm.setStyleSheet('QWidget { background-color:%s }'%col.name())
#         self.frm.setGeometry(130,22,100,100)
#
#         self.setGeometry(300,300,250,180)
#         self.setWindowTitle('Color Dialog')
#         self.show()
#
#     def showDialog(self):
#         col=QColorDialog.getColor()
#
#         if col.isValid():
#             self.frm.setStyleSheet('QWidget { background-color:%s }'%col.name())
#
# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     ex=Example()
#     sys.exit(app.exec_())

# 字体的选择
# import sys
# from PyQt5.QtWidgets import QWidget,QVBoxLayout,QPushButton,QSizePolicy,QLabel,QFontDialog,QApplication
#
# class Example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         vbox=QVBoxLayout()
#         btn=QPushButton('Dialog',self)
#         btn.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
#         btn.move(20,20)
#         vbox.addWidget(btn)
#         btn.clicked.connect(self.showDialog())
#
#         self.lbl=QLabel('knowledge only matters',self)
#         self.lbl.move(130,20)
#
#         vbox.addWidget(self.lbl)
#         self.setLayout(vbox)
#
#         self.setGeometry(300,300,250,180)
#         self.setWindowTitle('Font Dialog')
#         self.show()
#
#     def showDialog(self):
#         font,ok=QFontDialog.getFont()
#         if ok:
#             self.lbl.setFont(font)
#
# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     ex=Example()
#     sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import QMainWindow,QTextEdit,QAction,QFileDialog,QApplication
# from PyQt5.QtGui import QIcon
#
#
# class Example(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.textEdit=QTextEdit()
#         self.setCentralWidget(self.textEdit)
#         self.statusBar()
#
#         openFile=QAction(QIcon('open.png'),'Open',self)
#         openFile.setShortcut('Ctrl+O')
#         openFile.setStatusTip('Open new file')
#         openFile.triggered.connect(self.showDialog)
#
#         menubar=self.menuBar()
#         fileMenu=menubar.addMenu('&File')
#         fileMenu.addAction(openFile)
#
#         self.setGeometry(300,300,350,300)
#         self.setWindowTitle('Font Dialog')
#         self.show()
#
#     def showDialog(self):
#         frame=QFileDialog.getOpenFileName(self,'Open File','/home')
#         if frame[0]:
#             f=open(frame[0],'r')
#             with f:
#                 data=f.read()
#                 self.textEdit.setText(data)
#
#
# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     ex=Example()
#     sys.exit(app.exec_())

# 控件 QCheckBox
# import sys
# from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
# from PyQt5.QtCore import Qt
#
#
# class Example(QWidget):
#     def __init__(self):
#         super(Example, self).__init__()
#         self.initUI()
#
#     def initUI(self):
#         cb = QCheckBox('show title', self)
#         cb.move(20, 20)
#         cb.toggle()
#         cb.stateChanged.connect(self.changeTitle)
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle('QCheckBox')
#         self.show()
#
#     def changeTitle(self, state):
#         if state == Qt.checked:
#             self.setWindowTitle('QCheckBox')
#         else:
#             self.setWindowTitle('')
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# 切换按钮
# import sys
# from PyQt5.QtWidgets import QWidget,QPushButton,QFrame,QApplication
# from PyQt5.QtGui import QColor
#
#
# class Example(QWidget):
#     def __init__(self):
#         super(Example, self).__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.col=QColor(0,0,0)
#
#         redb=QPushButton('Red',self)
#         redb.setCheckable(True)
#         redb.move(10,10)
#         redb.clicked[bool].connect(self.setColor)
#
#         redb = QPushButton('Green', self)
#         redb.setCheckable(True)
#         redb.move(10, 60)
#         redb.clicked[bool].connect(self.setColor)
#
#         redb = QPushButton('Blue', self)
#         redb.setCheckable(True)
#         redb.move(10, 110)
#         redb.clicked[bool].connect(self.setColor)
#
#         self.square=QFrame(self)
#         self.square.setGeometry(150,20,100,100)
#         self.square.setStyleSheet('QWidget{ background-color: %s }' %self.col.name())
#
#         self.setGeometry(300,300,280,170)
#         self.setWindowTitle('Toggle button')
#         self.show()
#
#     def setColor(self,pressed):
#         source=self.sender()
#
#         if pressed:
#             val=255
#         else:
#             val=0
#
#         if source.text()=='Red':
#             self.col.setRed(val)
#         elif source.text()=='Green':
#             self.col.setGreen(val)
#         else:
#             self.col.setBlue(val)
#
#         self.square.setStyleSheet('QWidget{ background-color: %s }' %self.col.name())
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# QSlider
# import sys
# from PyQt5.QtWidgets import QWidget, QSlider, QLabel, QApplication
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QPixmap
#
#
# class Example(QWidget):
#     def __init__(self):
#         super(Example, self).__init__()
#         self.initUI()
#
#     def initUI(self):
#         sld = QSlider(Qt.Horizontal, self)
#         sld.setFocusPolicy(Qt.NoFocus)
#         sld.setGeometry(30, 40, 100, 30)
#         sld.valueChanged[int].connect(self.changeValue)
#
#         self.label = QLabel(self)
#         self.label.setPixmap(QPixmap('mute.png'))
#         self.label.setGeometry(160, 40, 80, 30)
#
#         self.setGeometry(300, 300, 280, 170)
#         self.setWindowTitle('QSlider')
#         self.show()
#
#     def changeValue(self, value):
#         if value == 0:
#             self.label.setPixmap(QPixmap('mute.png'))
#         elif value > 0 and value <= 30:
#             self.label.setPixmap(QPixmap('min.png'))
#         elif value > 30 and value < 80:
#             self.label.setPixmap(QPixmap('med.png'))
#         else:
#             self.label.setPixmap(QPixmap('max.png'))
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# QProgressBar
# import sys
# from PyQt5.QtWidgets import QWidget,QProgressBar,QPushButton,QApplication
# from PyQt5.QtCore import QBasicTimer
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.pbar=QProgressBar(self)
#         self.pbar.setGeometry(30,40,200,25)
#
#         self.btn=QPushButton('Start',self)
#         self.btn.move(40,80)
#         self.btn.clicked.connect(self.doAction)
#
#         self.timer=QBasicTimer()
#         self.step=0
#
#         self.setGeometry(300,300,280,170)
#         self.setWindowTitle('QProgressBar')
#         self.show()
#
#     def timerEvent(self, e):
#         if self.step>=100:
#             self.timer.stop()
#             self.btn.setText('finished')
#             return
#         self.step=self.step+1
#         self.pbar.setValue(self.step)
#
#     def doAction(self):
#         if self.timer.isActive():
#             self.timer.stop()
#             self.btn.setText('start')
#         else:
#             self.timer.start(100,self)
#             self.btn.setText('stop')
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# QCalendarWidget
# import sys
# from PyQt5.QtWidgets import QWidget,QCalendarWidget,QLabel,QApplication
# from PyQt5.QtCore import QDate
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         cal=QCalendarWidget(self)
#         cal.setGridVisible(True)
#         cal.move(20,20)
#         cal.clicked[QDate].connect(self.showDate)
#
#         self.lbl=QLabel(self)
#         date=cal.selectedDate()
#         self.lbl.setText(date.toString())
#         self.lbl.move(130,260)
#
#         self.setGeometry(300,300,350,300)
#         self.setWindowTitle('Calendar')
#         self.show()
#
#     def showDate(self,date):
#         self.lbl.setText(date.toString())
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# QPixmap
# import sys
# from PyQt5.QtWidgets import QWidget,QHBoxLayout,QLabel,QApplication
# from PyQt5.QtGui import QPixmap
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         hbox=QHBoxLayout(self)
#         pixmap=QPixmap('redrock.png')
#
#         lbl=QLabel(self)
#         lbl.setPixmap(pixmap)
#
#         hbox.addWidget(lbl)
#         self.setLayout(hbox)
#
#         self.move(300,200)
#         self.setWindowTitle('red rock')
#         self.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# QLineEdit
# import sys
# from PyQt5.QtWidgets import QWidget,QLineEdit,QLabel,QApplication
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.lbl=QLabel(self)
#         qle=QLineEdit(self)
#
#         qle.move(60,100)
#         self.lbl.move(60,40)
#
#         qle.textChanged[str].connect(self.onChanged)
#
#         self.setGeometry(300,300,280,170)
#         self.setWindowTitle('QLineEdit')
#         self.show()
#
#     def onChanged(self,text):
#         self.lbl.setText(text)
#         self.lbl.adjustSize()
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# QSplitter
# import sys
# from PyQt5.QtWidgets import QWidget,QHBoxLayout,QFrame,QSplitter,QStyleFactory,QApplication
# from PyQt5.QtCore import Qt
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         hbox=QHBoxLayout(self)
#         topleft=QFrame(self)
#         topleft.setFrameShape(QFrame.StyledPanel)
#         topright = QFrame(self)
#         topright.setFrameShape(QFrame.StyledPanel)
#         bottom = QFrame(self)
#         bottom.setFrameShape(QFrame.StyledPanel)
#
#         splitter1=QSplitter(Qt.Horizontal)
#         splitter1.addWidget(topleft)
#         splitter1.addWidget(topright)
#
#         splitter2 = QSplitter(Qt.Vertical)
#         splitter2.addWidget(splitter1)
#         splitter2.addWidget(bottom)
#
#         hbox.addWidget(splitter2)
#         self.setLayout(hbox)
#
#         self.setGeometry(300,300,300,200)
#         self.setWindowTitle('QSplitter')
#         self.show()
#
#     def onChanged(self,text):
#         self.lbl.setText(text)
#         self.lbl.adjustSize()
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# QComboBox
# import sys
# from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QApplication
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.lbl = QLabel('ubuntu', self)
#         combo = QComboBox(self)
#         combo.addItem('ubuntu')
#         combo.addItem('mandriva')
#         combo.addItem('fedora')
#         combo.addItem('arch')
#         combo.addItem('gentoo')
#
#         combo.move(50, 50)
#         self.lbl.move(50, 150)
#
#         combo.activated[str].connect(self.onActivated)
#
#         self.setGeometry(300, 300, 300, 200)
#         self.setWindowTitle('QComboBox')
#         self.show()
#
#     def onActivated(self, text):
#         self.lbl.setText(text)
#         self.lbl.adjustSize()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# 拖放：略

# 绘图:略
