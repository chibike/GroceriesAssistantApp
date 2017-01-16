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
    def setupUi(self, MainWindowObject):
        MainWindowObject.setObjectName(_fromUtf8("MainWindowObject"))
        MainWindowObject.resize(363, 303)
        MainWindowObject.setMinimumSize(QtCore.QSize(363, 303))
        MainWindowObject.setMaximumSize(QtCore.QSize(363, 303))
        MainWindowObject.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("logo01.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindowObject.setWindowIcon(icon)
        MainWindowObject.setAutoFillBackground(True)
        self.windowRefernece = MainWindowObject
        self.verticalLayoutWidget = QtGui.QWidget(MainWindowObject)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 341, 201))
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
        self.confirmPasswordLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.confirmPasswordLabel.setMinimumSize(QtCore.QSize(299, 24))
        self.confirmPasswordLabel.setMaximumSize(QtCore.QSize(299, 24))
        self.confirmPasswordLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.confirmPasswordLabel.setObjectName(_fromUtf8("confirmPasswordLabel"))
        self.verticalLayout.addWidget(self.confirmPasswordLabel)
        self.confirmPasswordLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.confirmPasswordLineEdit.setMinimumSize(QtCore.QSize(299, 27))
        self.confirmPasswordLineEdit.setMaximumSize(QtCore.QSize(299, 27))
        self.confirmPasswordLineEdit.setMaxLength(20)
        self.confirmPasswordLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.confirmPasswordLineEdit.setObjectName(_fromUtf8("confirmPasswordLineEdit"))
        self.verticalLayout.addWidget(self.confirmPasswordLineEdit)
        self.rememberMeCheckBox = QtGui.QCheckBox(MainWindowObject)
        self.rememberMeCheckBox.setGeometry(QtCore.QRect(10, 220, 141, 25))
        self.rememberMeCheckBox.setMinimumSize(QtCore.QSize(141, 25))
        self.rememberMeCheckBox.setMaximumSize(QtCore.QSize(141, 25))
        self.rememberMeCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rememberMeCheckBox.setChecked(True)
        self.rememberMeCheckBox.setObjectName(_fromUtf8("rememberMeCheckBox"))
        self.cancelPushButton = QtGui.QPushButton(MainWindowObject)
        self.cancelPushButton.setGeometry(QtCore.QRect(10, 260, 81, 34))
        self.cancelPushButton.setMinimumSize(QtCore.QSize(81, 34))
        self.cancelPushButton.setMaximumSize(QtCore.QSize(81, 34))
        self.cancelPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancelPushButton.setObjectName(_fromUtf8("cancelPushButton"))
        self.hasAnAccountPushButton = QtGui.QPushButton(MainWindowObject)
        self.hasAnAccountPushButton.setGeometry(QtCore.QRect(100, 260, 161, 34))
        self.hasAnAccountPushButton.setMinimumSize(QtCore.QSize(161, 34))
        self.hasAnAccountPushButton.setMaximumSize(QtCore.QSize(161, 34))
        self.hasAnAccountPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.hasAnAccountPushButton.setObjectName(_fromUtf8("hasAnAccountPushButton"))
        self.createPushButton = QtGui.QPushButton(MainWindowObject)
        self.createPushButton.setGeometry(QtCore.QRect(270, 260, 81, 34))
        self.createPushButton.setMinimumSize(QtCore.QSize(81, 34))
        self.createPushButton.setMaximumSize(QtCore.QSize(81, 34))
        self.createPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.createPushButton.setObjectName(_fromUtf8("createPushButton"))

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
        self.confirmPasswordLabel.setText(_translate("MainWindowObject", "Confirm Password", None))
        self.confirmPasswordLineEdit.setStatusTip(_translate("MainWindowObject", "Repeat Password", None))
        self.rememberMeCheckBox.setToolTip(_translate("MainWindowObject", "Click to automate login", None))
        self.rememberMeCheckBox.setStatusTip(_translate("MainWindowObject", "Click to automate login", None))
        self.rememberMeCheckBox.setText(_translate("MainWindowObject", "Remember me", None))
        self.cancelPushButton.setToolTip(_translate("MainWindowObject", "Click to cancel registration", None))
        self.cancelPushButton.setStatusTip(_translate("MainWindowObject", "Click to cancel registration", None))
        self.cancelPushButton.setText(_translate("MainWindowObject", "Cancel", None))
        self.cancelPushButton.pressed.connect(self.cancelButtonClicked) #connected cancel button click event to cancel button function
        self.hasAnAccountPushButton.setToolTip(_translate("MainWindowObject", "Click to navigate to login page", None))
        self.hasAnAccountPushButton.setStatusTip(_translate("MainWindowObject", "Click to navigate to login page", None))
        self.hasAnAccountPushButton.setText(_translate("MainWindowObject", "Have an account", None))
        self.hasAnAccountPushButton.pressed.connect(self.hasAnAccountButtonClicked) #connected hasAnAccount button click event to hasAnAccount button function
        self.createPushButton.setToolTip(_translate("MainWindowObject", "Click to create account", None))
        self.createPushButton.setStatusTip(_translate("MainWindowObject", "Click to create account", None))
        self.createPushButton.setText(_translate("MainWindowObject", "Create", None))
        self.createPushButton.pressed.connect(self.createButtonClicked) #connected create button click event to create button function

    def cancelButtonClicked(self):
        self.canceled = True
        self.windowRefernece.close()

    def createButtonClicked(self):
        self.rememberMeCheckStateVariable = self.rememberMeCheckBox.checkState()
        self.username = hash( str(self.nameLineEdit.text()) )
        self.password = hash( str(self.passwordLineEdit.text()) )
        self.canceled = False
        self.hasAnAccount = False

        if self.password != hash(str(self.confirmPasswordLineEdit.text())):
            print ("Passwords don't match")
            QtGui.QMessageBox.information(self.windowReference, "Warning", "Passwords don't match")
        else:
            self.windowRefernece.close()

    def hasAnAccountButtonClicked(self):
        self.hasAnAccount = True
        self.canceled = False
        self.windowRefernece.close()

    def setupValues(self):
        self.rememberMeCheckStateVariable = self.rememberMeCheckBox.checkState()
        self.username = None
        self.password = None
        self.canceled = False
        self.hasAnAccount = False

    def getValues(self):
        return [self.canceled, self.hasAnAccount, self.rememberMeCheckStateVariable, self.username, self.password]

class CreateAccountDialogBox(QtGui.QDialog, Ui_MainWindowObject):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_MainWindowObject()
        self.ui.setupUi(self)

    def getValues(self):
        return self.ui.getValues()

##if __name__ == "__main__":
##    import sys
##    app = QtGui.QApplication(sys.argv)
##    MainWindowObject = QtGui.QWidget()
##    ui = Ui_MainWindowObject()
##    ui.setupUi(MainWindowObject)
##    MainWindowObject.show()
##    sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = CreateAccountDialogBox()
    app.exec_()
    val = app.getValues()
    if val[0] == False:
        print("Not Canceled")
    elif val[1] == True:
        print("Has an account")
    else:
        print("Username =", val[2])
        print("Password =", val[3])
