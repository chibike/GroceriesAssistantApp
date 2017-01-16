from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindowObject(object):
    def setupUi(self, MainWindowObject, accountDict):
        MainWindowObject.setObjectName(_fromUtf8("MainWindowObject"))
        MainWindowObject.resize(333, 256)
        MainWindowObject.setMinimumSize(QtCore.QSize(333, 256))
        MainWindowObject.setMaximumSize(QtCore.QSize(333, 256))
        MainWindowObject.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("logo01.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindowObject.setWindowIcon(icon)
        MainWindowObject.setAutoFillBackground(True)
        self.windowReference = MainWindowObject
        self._accountDict = accountDict
        self._maxTrials = 5
        self._numOfTrials = 0
        self.verticalLayoutWidget = QtGui.QWidget(MainWindowObject)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 311, 151))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.nameLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.nameLabel.setMinimumSize(QtCore.QSize(299, 24))
        self.nameLabel.setMaximumSize(QtCore.QSize(299, 24))
        self.nameLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.nameLabel.setObjectName(_fromUtf8("nameLabel"))
        self.verticalLayout.addWidget(self.nameLabel)
        self.nameLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.nameLineEdit.setMinimumSize(QtCore.QSize(299, 27))
        self.nameLineEdit.setMaximumSize(QtCore.QSize(299, 27))
        self.nameLineEdit.setObjectName(_fromUtf8("nameLineEdit"))
        self.verticalLayout.addWidget(self.nameLineEdit)
        self.passwordLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.passwordLabel.setMinimumSize(QtCore.QSize(299, 25))
        self.passwordLabel.setMaximumSize(QtCore.QSize(299, 25))
        self.passwordLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.passwordLabel.setObjectName(_fromUtf8("passwordLabel"))
        self.verticalLayout.addWidget(self.passwordLabel)
        self.passwordLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.passwordLineEdit.setMinimumSize(QtCore.QSize(299, 27))
        self.passwordLineEdit.setMaximumSize(QtCore.QSize(299, 27))
        self.passwordLineEdit.setMaxLength(20)
        self.passwordLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordLineEdit.setObjectName(_fromUtf8("passwordLineEdit"))
        self.verticalLayout.addWidget(self.passwordLineEdit)
        self.rememberMeCheckBox = QtGui.QCheckBox(MainWindowObject)
        self.rememberMeCheckBox.setGeometry(QtCore.QRect(10, 180, 141, 25))
        self.rememberMeCheckBox.setMinimumSize(QtCore.QSize(141, 25))
        self.rememberMeCheckBox.setMaximumSize(QtCore.QSize(141, 25))
        self.rememberMeCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rememberMeCheckBox.setChecked(True)
        self.rememberMeCheckBox.setObjectName(_fromUtf8("rememberMeCheckBox"))
        self.cancelPushButton = QtGui.QPushButton(MainWindowObject)
        self.cancelPushButton.setGeometry(QtCore.QRect(10, 210, 81, 34))
        self.cancelPushButton.setMinimumSize(QtCore.QSize(81, 34))
        self.cancelPushButton.setMaximumSize(QtCore.QSize(81, 34))
        self.cancelPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancelPushButton.setObjectName(_fromUtf8("cancelPushButton"))
        self.registerPushButton = QtGui.QPushButton(MainWindowObject)
        self.registerPushButton.setGeometry(QtCore.QRect(100, 210, 81, 34))
        self.registerPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.registerPushButton.setObjectName(_fromUtf8("registerPushButton"))
        self.loginPushButton = QtGui.QPushButton(MainWindowObject)
        self.loginPushButton.setGeometry(QtCore.QRect(240, 210, 81, 34))
        self.loginPushButton.setMinimumSize(QtCore.QSize(81, 34))
        self.loginPushButton.setMaximumSize(QtCore.QSize(81, 34))
        self.loginPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginPushButton.setObjectName(_fromUtf8("loginPushButton"))

        self.setupValues()
        self.retranslateUi(MainWindowObject)
        QtCore.QMetaObject.connectSlotsByName(MainWindowObject)

    def retranslateUi(self, MainWindowObject):
        MainWindowObject.setWindowTitle(_translate("MainWindowObject", "Blink Groceries Assistant", None))
        MainWindowObject.setToolTip(_translate("MainWindowObject", "Created by Blink", None))
        MainWindowObject.setStatusTip(_translate("MainWindowObject", "Created by Blink", None))
        self.nameLabel.setText(_translate("MainWindowObject", "Name", None))
        self.nameLineEdit.setStatusTip(_translate("MainWindowObject", "Enter username", None))
        self.passwordLabel.setText(_translate("MainWindowObject", "Password", None))
        self.passwordLineEdit.setStatusTip(_translate("MainWindowObject", "Enter password", None))
        self.rememberMeCheckBox.setToolTip(_translate("MainWindowObject", "Click to automate login", None))
        self.rememberMeCheckBox.setStatusTip(_translate("MainWindowObject", "Click to automate login", None))
        self.rememberMeCheckBox.setText(_translate("MainWindowObject", "Remember me", None))
        self.cancelPushButton.setToolTip(_translate("MainWindowObject", "Click to cancel registration", None))
        self.cancelPushButton.setStatusTip(_translate("MainWindowObject", "Click to cancel registration", None))
        self.cancelPushButton.setText(_translate("MainWindowObject", "Cancel", None))
        self.cancelPushButton.pressed.connect(self.cancelButtonClicked) #connected cancel button click event to cancel button function
        self.registerPushButton.setToolTip(_translate("MainWindowObject", "Click to navigate to sign up page", None))
        self.registerPushButton.setStatusTip(_translate("MainWindowObject", "Click to navigate to sign up page", None))
        self.registerPushButton.setText(_translate("MainWindowObject", "Register", None))
        self.registerPushButton.pressed.connect(self.registerButtonClicked) #connected register button click event to register button function
        self.loginPushButton.setToolTip(_translate("MainWindowObject", "Click to login account", None))
        self.loginPushButton.setStatusTip(_translate("MainWindowObject", "Click to login account", None))
        self.loginPushButton.setText(_translate("MainWindowObject", "Create", None))
        self.loginPushButton.pressed.connect(self.loginButtonClicked) #connected login button click event to login button function

    def setupValues(self):
        '''Initializes all relevant values'''
        self.canceled = False
        self.hasNoAccount = False
        self.username = None
        self.password = None

    def cancelButtonClicked(self):
        '''When cancel button clicked return canceled signal'''
        self.canceled = True
        self.windowReference.close()

    def loginButtonClicked(self):
        '''When login button clicked return username and password'''
        self.canceled = False
        self.hasNoAccount = False
        self.username = hash(str(self.nameLineEdit.text()))
        self.password = hash(str(self.passwordLineEdit.text()))
        self._numOfTrials += 1
        try:
            if self._accountDict[self.username] == self.password:
                self.windowReference.close()
            else:
                QtGui.QMessageBox.information(self, "Warning", "Invalid Password")
        except:
            #print("Invalid password")
            QtGui.QMessageBox.information(self.windowReference, "Warning", "Invalid Password")

        if self._numOfTrials >= self._maxTrials:
            QtGui.QMessageBox.information(self.windowReference, "Warning", "Number of Trials Exceeded")
            self.cancelButtonClicked()

    def registerButtonClicked(self):
        '''If Have an account button clicked return has an account signal'''
        self.canceled = False
        self.hasNoAccount = True
        self.windowReference.close()

    def getValues(self):
        '''Return relevant values'''
        return [self.canceled, self.hasNoAccount, self.username, self.password]

class LoginDialogBox(QtGui.QDialog, Ui_MainWindowObject):
    def __init__(self, parent=None, rememberMeData=None, accountData=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_MainWindowObject()
        self.ui.setupUi(self, accountData)

    def getValues(self):
        return self.ui.getValues()

##if __name__ == "__main__":
##    import sys
##    acc_dict = {"username":"password"}
##    app = QtGui.QApplication(sys.argv)
##    MainWindowObject = QtGui.QWidget()
##    ui = Ui_MainWindowObject()
##    ui.setupUi(MainWindowObject, acc_dict)
##    MainWindowObject.show()
##    sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    rmd = [False, hash("username"), hash("password")]
    acd = {hash("username"):hash("password"),hash("username"):hash("password")}
    app = LoginDialogBox(rememberMeData=rmd, accountData=acd)
    app.exec_()
    val = app.getValues()
    if val[0] == False:
        print("Not Canceled")
    elif val[1] == True:
        print("Has an account")
    else:
        print("Username =", val[2])
        print("Password =", val[3])

        
