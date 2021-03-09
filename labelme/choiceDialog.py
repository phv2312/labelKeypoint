#
# Copyright (C) 2011 Michael Pitidis, Hussein Abdulwahid.
#
# This file is part of Labelme.
#
# Labelme is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Labelme is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Labelme.  If not, see <http://www.gnu.org/licenses/>.
#

try:
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
    PYQT5 = True
except ImportError:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
    PYQT5 = False

from .lib import newIcon, labelValidator
from constants import class_names, class_position
# TODO:
# - Calculate optimal position so as not to go out of screen area.

BB = QDialogButtonBox

"""
Click on cooridnate --> appear ChoiceDialog.
"""
from functools import partial
class ChoiceDialog(QDialog):

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.green, 3, Qt.SolidLine))
        painter.drawRect(185, 70, 135 ,140)
        painter.drawRect(135, 220, 235, 220)

        painter.setPen(QPen(Qt.red, 5, Qt.SolidLine))
        painter.drawText(120, 30, "Please select the right pose. THANK YOU !")

    def __init__(self, text="Choose object label", parent=None):
        super(ChoiceDialog, self).__init__(parent)
        self.edit = QLineEdit()
        self.edit.setText(text) #title hien len
        self.edit.setEnabled(False)
        self.edit.setValidator(labelValidator()) # kiem tra title nhap vao co dung dan
        self.edit.editingFinished.connect(self.postProcess)
        layout = QVBoxLayout()
        layout.addWidget(self.edit)

        # Tested. We can use this codes to build a background
        dialog_w = 500
        dialog_h = 500

        self.setGeometry(200, 200, dialog_w, dialog_h)
        customized_buttons = []
        for cls_name, ratio in class_position.items():
            print (cls_name, ratio)
            r_x, r_y = ratio

            _button = QPushButton(text=cls_name,parent=self)
            _button.setGeometry(int(r_x * dialog_w), int(r_y * dialog_h), 35, 35)
            _button.setStyleSheet("""
                    QPushButton {
                        border: 1px solid black;
                        border-radius: 16px;
                        background-color: rgb(255, 255, 255);
                        font-size: 10px;
                        color: black;
                        }
                    QPushButton:hover {
                        border: 1px solid blue;
                        border-radius: 16px;
                        background-color: rgb(220, 220, 220);
                        font-size: 11px;
                        color: blue;
                        }
                    """)

            click_func = partial(self.p, text=cls_name)
            _button.clicked.connect(click_func)

            customized_buttons += [_button]

    def p(self, text):
        self.edit.setText(text)
        self.accept()

    #
    # def p1(self):
    #     self.edit.setText(class_names[0])
    #     self.accept()
    #
    # def p2(self):
    #     self.edit.setText(class_names[1])
    #     self.accept()
    #
    # def p3(self):
    #     self.edit.setText(class_names[2])
    #     self.accept()
    #
    # def p4(self):
    #     self.edit.setText(class_names[3])
    #     self.accept()
    #
    # def p5(self):
    #     self.edit.setText(class_names[4])
    #     self.accept()
    #
    # def p6(self):
    #     self.edit.setText(class_names[5])
    #     self.accept()
    #
    # def p7(self):
    #     self.edit.setText(class_names[6])
    #     self.accept()
    #
    # def p8(self):
    #     self.edit.setText(class_names[7])
    #     self.accept()
    #
    # def p9(self):
    #     self.edit.setText(class_names[8])
    #     self.accept()
    #
    # def p10(self):
    #     self.edit.setText(class_names[9])
    #     self.accept()
    #
    # def p11(self):
    #     self.edit.setText(class_names[10])
    #     self.accept()
    #
    # def p12(self):
    #     self.edit.setText(class_names[11])
    #     self.accept()
    #
    # def p13(self):
    #     self.edit.setText(class_names[12])
    #     self.accept()
    #
    # def p14(self):
    #     self.edit.setText(class_names[13])
    #     self.accept()
    #
    # def p15(self):
    #     self.edit.setText(class_names[14])
    #     self.accept()
    #
    # def p16(self):
    #     self.edit.setText(class_names[15])
    #     self.accept()

    def validate(self):
        if PYQT5:
            if self.edit.text().strip():
                self.accept()
        else:
            if self.edit.text().trimmed():
                self.accept()

    def postProcess(self):
        if PYQT5:
            self.edit.setText(self.edit.text().strip())
        else:
            self.edit.setText(self.edit.text().trimmed())

    def popUp(self, text='', move=True):
        self.edit.setText(text)
        self.edit.setSelection(0, len(text))
        self.edit.setFocus(Qt.PopupFocusReason)
        if move:
            self.move(QCursor.pos())
        return self.edit.text() if self.exec_() else None
