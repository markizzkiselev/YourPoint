import sys, os
import csv
import sqlite3
from PIL import Image
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QFileDialog, QSpinBox
from PyQt5.QtGui import QFont
from class_basket import Basket
from class_qimageclasses import QImageButton, QImageText

con = sqlite3.connect("design.sqlite")
cur = con.cursor()

app = QApplication(sys.argv)


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.basket = Basket()
        self.initUI()

    def initUI(self):
        desktop = app.desktop()
        self.setWindowTitle('MFC designer')
        self.setGeometry(0, 0, desktop.availableGeometry().width(), desktop.availableGeometry().height())

        self.red_background = QImageText(self)
        self.red_background.setGeometry(0, 0, 300, self.height())
        self.red_background.setStyleSheet("background-color: blue; border: none;")

        self.logo = QImageButton(self)
        self.logo.setGeometry(50, 50, 200, 200)
        self.logo.setImage('images/logo.png')
        self.logo.newOption('border: none;')

        self.logo_font = QFont('Arial', 50)
        self.logo_font.setWeight(500)

        self.logo_text = QLabel(self)
        self.logo_text.setText('Установить изображение :')
        self.logo_text.setGeometry(400, 100, 1100, 200)
        self.logo_text.setFont(self.logo_font)

        self.set_logo_button = QImageButton(self)
        self.set_logo_button.setGeometry(1500, 50, 300, 300)
        self.set_logo_button.setImage('images/logo.png')
        self.set_logo_button.newOption('border : none;')
        self.set_logo_button.clicked.connect(self.set_new_logo)

        button_font = QFont('Arial', 24)
        button_font.setWeight(500)

        self.position_font = QFont('Arial', 30)
        self.position_font.setWeight(500)

        self.tub_button_1 = QImageButton(self)
        self.tub_button_1.setGeometry(-10, 300, 285, 100)
        self.tub_button_1.setStyleSheet("QPushButton"
                                        "{"
                                        "background-color : white; border-radius: 10px;"
                                        "border-top-left-radius: 0; border-bottom-left-radius: 0;"
                                        "text-align: left;"
                                        "}"
                                        )
        self.tub_button_1.setText('  Основное')
        self.tub_button_1.setFont(button_font)
        self.tub_button_1.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"), offset=QtCore.QPointF(10.0, 10.0)))
        self.tub_button_1.clicked.connect(self.state_1)

        self.tub_button_2 = QImageButton(self)
        self.tub_button_2.setGeometry(-10, 425, 285, 100)
        self.tub_button_2.setStyleSheet("QPushButton"
                                        "{"
                                        "background-color : white; border-radius: 10px;"
                                        "border-top-left-radius: 0; border-bottom-left-radius: 0;"
                                        "text-align: left;"
                                        "}"
                                        )
        self.tub_button_2.setText('  Разделы')
        self.tub_button_2.setFont(button_font)
        self.tub_button_2.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"), offset=QtCore.QPointF(10.0, 10.0)))
        self.tub_button_2.clicked.connect(self.state_2)

        self.tub_button_3 = QImageButton(self)
        self.tub_button_3.setGeometry(-10, 550, 285, 100)
        self.tub_button_3.setStyleSheet("QPushButton"
                                        "{"
                                        "background-color : white; border-radius: 10px;"
                                        "border-top-left-radius: 0; border-bottom-left-radius: 0;"
                                        "text-align: left;"
                                        "}"
                                        )
        self.tub_button_3.setText('  Позиции')
        self.tub_button_3.setFont(button_font)
        self.tub_button_3.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"), offset=QtCore.QPointF(10.0, 10.0)))
        self.tub_button_3.clicked.connect(self.state_3)

        self.tub_button_4 = QImageButton(self)
        self.tub_button_4.setGeometry(-10, 675, 285, 100)
        self.tub_button_4.setStyleSheet("QPushButton"
                                        "{"
                                        "background-color : white; border-radius: 10px;"
                                        "border-top-left-radius: 0; border-bottom-left-radius: 0;"
                                        "text-align: left;"
                                        "}"
                                        )
        self.tub_button_4.setText('  Коды')
        self.tub_button_4.setFont(button_font)
        self.tub_button_4.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"), offset=QtCore.QPointF(10.0, 10.0)))
        self.tub_button_4.clicked.connect(self.state_4)

        self.tub_buttons = [
            self.tub_button_1,
            self.tub_button_2,
            self.tub_button_3,
            self.tub_button_4
        ]

        self.title_font = QFont('Arial', 50)
        self.title_font.setWeight(500)

        self.files_up_button = QImageButton(self)
        self.files_up_button.setText('↑')
        self.files_up_button.setGeometry(350, 50, 50, 440)
        self.files_up_button.setFont(self.position_font)
        self.files_up_button.newOption("QPushButton"
                                       "{"
                                       "background-color : blue; border-radius: 10px;"
                                       "}"
                                       "QPushButton::pressed"
                                       "{"
                                       "background-color : cyan; border-radius: 10px;"
                                       "}"
                                       )
        self.files_up_button.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"), offset=QtCore.QPointF(10.0, 10.0)))
        self.files_up_button.clicked.connect(self.files_up)

        self.files_down_button = QImageButton(self)
        self.files_down_button.setText('↓')
        self.files_down_button.setGeometry(350, 515, 50, 440)
        self.files_down_button.setFont(self.position_font)
        self.files_down_button.newOption("QPushButton"
                                         "{"
                                         "background-color : blue; border-radius: 10px;"
                                         "}"
                                         "QPushButton::pressed"
                                         "{"
                                         "background-color : cyan; border-radius: 10px;"
                                         "}"
                                         )
        self.files_down_button.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"), offset=QtCore.QPointF(10.0, 10.0)))
        self.files_down_button.clicked.connect(self.files_down)

        self.files_moves_buttons = [
            self.files_up_button,
            self.files_down_button
        ]

        self.file_high = 0
        self.title_buttons = []
        self.title_arrows = []
        self.files = []
        self.filenames = []
        self.image_connecter = {}
        self.founder = []
        self.found_connecter = {}
        self.file_delete = []
        self.delete_connecter = {}
        self.all_file_buttons = [
            self.title_buttons,
            self.title_arrows,
            self.files,
            self.filenames,
            self.file_delete,
            self.founder
        ]
        y = 50
        for i in range(50):
            title = QLineEdit(self)
            title.setGeometry(425, y, 100, 100)
            title.setStyleSheet("QLineEdit"
                                "{"
                                "background-color : white; border-radius: 30px;"
                                "border-top-right-radius: 10; border-bottom-right-radius: 10;"
                                "}"
                                )
            title.setFont(self.title_font)
            title.setGraphicsEffect(
                QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"),
                                                    offset=QtCore.QPointF(10.0, 10.0)))
            title.setText(f'{i + 1}')
            title.setAlignment(QtCore.Qt.AlignCenter)
            title.setReadOnly(True)
            self.title_buttons.append(title)

            arrow = QImageButton(self)
            arrow.setGeometry(525, y, 100, 100)
            arrow.setImage('images/arrow.png')
            arrow.newOption('border: none;')
            arrow.setGraphicsEffect(
                QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"),
                                                    offset=QtCore.QPointF(0, 10.0)))
            self.title_arrows.append(arrow)

            file = QImageButton(self)
            file.setGeometry(650, y, 100, 100)
            file.setImage('images/file.png')
            file.newOption('border: none;')
            file.setGraphicsEffect(
                QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"),
                                                    offset=QtCore.QPointF(10.0, 10.0)))
            file.clicked.connect(self.found_file)
            self.files.append(file)

            delete = QImageButton(self)
            delete.setGeometry(775, y, 100, 100)
            delete.setImage('images/block.png')
            delete.newOption('border : none;')
            delete.clicked.connect(self.delete_file)
            delete.setGraphicsEffect(
                QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"),
                                                    offset=QtCore.QPointF(10.0, 10.0)))
            self.file_delete.append(delete)

            image = QImageButton(self)
            image.setGeometry(900, y, 100, 100)
            image.newOption('border : none;')
            image.setGraphicsEffect(
                QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"),
                                                    offset=QtCore.QPointF(10.0, 10.0)))
            self.founder.append(image)

            name = QImageButton(self)
            name.setGeometry(1025, y, 625, 100)
            name.setFont(self.title_font)
            name.newOption('border: none; text-align: left;')
            name.setText('')
            self.filenames.append(name)
            self.image_connecter[file] = [name, image]
            self.delete_connecter[delete] = name
            y += 150

        self.append_file_button = QImageButton(self)
        self.append_file_button.setGeometry(425, 50, 1000, 100)
        self.append_file_button.setText('+')
        self.append_file_button.setFont(self.position_font)
        self.append_file_button.newOption("QPushButton"
                                          "{"
                                          "background-color : blue; border-radius: 30px;"
                                          "}"
                                          "QPushButton::pressed"
                                          "{"
                                          "background-color : cyan; border-radius: 30px;"
                                          "}"
                                          )
        self.append_file_button.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"), offset=QtCore.QPointF(10.0, 10.0)))
        self.append_file_button.clicked.connect(self.show_new_file)

        self.file_save_button = QImageButton(self)
        self.file_save_button.setGeometry(self.width() - 250, self.height() - 250, 200, 200)
        self.file_save_button.setImage('images/save.png')
        self.file_save_button.newOption('border: none;')
        self.file_save_button.clicked.connect(self.save_files)

        self.section_buttons = []
        self.section_buttons_connecter = {}
        self.section_buttons_high = 0

        button = QImageButton(self)
        button.setGeometry(
            (desktop.availableGeometry().width() - button.width()) // 2 - 200,
            (desktop.availableGeometry().height() - button.height()) // 2 + 200,
            200,
            200)
        button.newOption('border-radius: 30px;')
        button.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"),
                                                offset=QtCore.QPointF(10.0, 10.0)))
        button.setFont(button_font)
        self.section_buttons_connecter[button] = 0
        self.section_buttons.append(button)

        button = QImageButton(self)
        button.setGeometry(
            (desktop.availableGeometry().width() - button.width()) // 2 + 50,
            (desktop.availableGeometry().height() - button.height()) // 2 + 150,
            300,
            300)
        button.newOption('border-radius: 30px;')
        button.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"),
                                                offset=QtCore.QPointF(10.0, 10.0)))
        button.setFont(button_font)
        self.section_buttons_connecter[button] = 1
        self.section_buttons.append(button)

        button = QImageButton(self)
        button.setGeometry(
            (desktop.availableGeometry().width() - button.width()) // 2 + 400,
            (desktop.availableGeometry().height() - button.height()) // 2 + 200,
            200,
            200)
        button.newOption('border-radius: 30px;')
        button.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"),
                                                offset=QtCore.QPointF(10.0, 10.0)))
        button.setFont(button_font)
        self.section_buttons_connecter[button] = 2
        self.section_buttons.append(button)

        arrow_font = QFont('Arial', 100)
        arrow_font.setWeight(500)

        self.section_arrow_up = QImageButton(self)
        self.section_arrow_up.setGeometry(
            (desktop.availableGeometry().width() - button.width()) // 2 - 350,
            (desktop.availableGeometry().height() - button.height()) // 2 + 280,
            200,
            200)
        self.section_arrow_up.setText('<')
        self.section_arrow_up.newOption('border: none;')
        self.section_arrow_up.setFont(arrow_font)
        self.section_arrow_up.clicked.connect(self.up_down_section_buttons)

        self.section_arrow_down = QImageButton(self)
        self.section_arrow_down.setGeometry(
            (desktop.availableGeometry().width() - button.width()) // 2 + 650,
            (desktop.availableGeometry().height() - button.height()) // 2 + 280,
            200,
            200)
        self.section_arrow_down.setText('>')
        self.section_arrow_down.newOption('border: none;')
        self.section_arrow_down.setFont(arrow_font)
        self.section_arrow_down.clicked.connect(self.up_down_section_buttons)

        two_font = QFont('Arial', 20)
        two_font.setWeight(500)

        self.position_images = []
        self.position_txt = []
        self.prices = []
        self.all_position_buttons = [
            self.position_images,
            self.position_txt,
            self.prices
        ]
        for i in range(3):
            position_image_button = QImageButton(self)
            position_image_button.setGeometry(375 + 525 * i, 225, 200, 200)
            position_image_button.newOption('border-radius: 30px;')
            position_image_button.setGraphicsEffect(
                QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"),
                                                    offset=QtCore.QPointF(10.0, 10.0)))
            position_image_button.setImage('images/burger.jpg')
            position_image_button.clicked.connect(self.set_img)
            self.position_images.append(position_image_button)

            position_text = QLineEdit(self)
            position_text.setGeometry(600 + 525 * i, 275, 200, 50)
            position_text.setFont(two_font)
            position_text.setStyleSheet("QLineEdit"
                                        "{"
                                        "background-color : white; border-radius: 10px;"
                                        "}"
                                        )
            self.position_txt.append(position_text)

            price = QSpinBox(self)
            price.setGeometry(600 + 525 * i, 350, 200, 50)
            price.setMaximum(99999)
            price.setFont(two_font)
            price.setStyleSheet("QSpinBox"
                                "{"
                                "background-color : white; border-radius: 10px;"
                                "}"
                                )
            self.prices.append(price)

        pos_font = QFont('Arial', 30)
        pos_font.setWeight(500)

        self.position_arrow_up = QImageButton(self)
        self.position_arrow_up.setGeometry(375, 50, 1475, 100)
        self.position_arrow_up.setText('˄')
        self.position_arrow_up.newOption("QPushButton"
                                         "{"
                                         "background-color : blue; border-radius: 10px;"
                                         "}"
                                         "QPushButton::pressed"
                                         "{"
                                         "background-color : cyan; border-radius: 10px;"
                                         "}"
                                         )
        self.position_arrow_up.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"), offset=QtCore.QPointF(10.0, 10.0)))
        self.position_arrow_up.setFont(pos_font)
        self.position_arrow_up.clicked.connect(self.poser)

        self.position_arrow_down = QImageButton(self)
        self.position_arrow_down.setGeometry(375, 500, 1475, 100)
        self.position_arrow_down.setText('˅')
        self.position_arrow_down.newOption("QPushButton"
                                           "{"
                                           "background-color : blue; border-radius: 10px;"
                                           "}"
                                           "QPushButton::pressed"
                                           "{"
                                           "background-color : cyan; border-radius: 10px;"
                                           "}"
                                           )
        self.position_arrow_down.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"), offset=QtCore.QPointF(10.0, 10.0)))
        self.position_arrow_down.setFont(pos_font)
        self.position_arrow_down.clicked.connect(self.poser)

        self.pos_high = 0

        self.button_plus = QImageButton(self)
        self.button_plus.setText('+')
        self.button_plus.setGeometry(350, 50, 425, 200)
        self.button_plus.setFont(self.position_font)
        self.button_plus.newOption("QPushButton"
                                   "{"
                                   "background-color : blue; border-radius: 30px;"
                                   "}"
                                   "QPushButton::pressed"
                                   "{"
                                   "background-color : cyan; border-radius: 30px;"
                                   "}"
                                   )
        self.button_plus.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"), offset=QtCore.QPointF(10.0, 10.0)))
        self.button_plus.clicked.connect(self.plus)

        self.pluser = 0

        self.save_itm_button = QImageButton(self)
        self.save_itm_button.setGeometry(self.width() - 250, self.height() - 250, 200, 200)
        self.save_itm_button.setImage('images/save.png')
        self.save_itm_button.newOption('border: none;')
        self.save_itm_button.clicked.connect(self.save_items)

        self.code_up_button = QImageButton(self)
        self.code_up_button.setText('↑')
        self.code_up_button.setGeometry(350, 50, 50, 440)
        self.code_up_button.setFont(self.position_font)
        self.code_up_button.newOption("QPushButton"
                                      "{"
                                      "background-color : blue; border-radius: 10px;"
                                      "}"
                                      "QPushButton::pressed"
                                      "{"
                                      "background-color : cyan; border-radius: 10px;"
                                      "}"
                                      )
        self.code_up_button.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"), offset=QtCore.QPointF(10.0, 10.0)))
        self.code_up_button.clicked.connect(self.codes_up)

        self.code_down_button = QImageButton(self)
        self.code_down_button.setText('↓')
        self.code_down_button.setGeometry(350, 515, 50, 440)
        self.code_down_button.setFont(self.position_font)
        self.code_down_button.newOption("QPushButton"
                                        "{"
                                        "background-color : blue; border-radius: 10px;"
                                        "}"
                                        "QPushButton::pressed"
                                        "{"
                                        "background-color : cyan; border-radius: 10px;"
                                        "}"
                                        )
        self.code_down_button.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"), offset=QtCore.QPointF(10.0, 10.0)))
        self.code_down_button.clicked.connect(self.codes_down)

        self.code_moves_buttons = [
            self.code_up_button,
            self.code_down_button
        ]

        self.codes_font = QFont('Arial', 46)
        self.codes_font.setWeight(500)

        self.code_buttons = []
        self.arrow_buttons = []
        self.promo_buttons = []
        self.use_code_buttons = []
        self.all_code_buttons = [
            self.code_buttons,
            self.arrow_buttons,
            self.promo_buttons,
            self.use_code_buttons,
            self.code_moves_buttons
        ]
        self.all_moved_buttons = [
            self.code_buttons,
            self.arrow_buttons,
            self.promo_buttons,
            self.use_code_buttons
        ]
        self.num_code = 1
        self.del_code_connecter = {}
        y = 50
        for i in range(50):
            code_label = QLineEdit(self)
            code_label.setGeometry(425, y, 300, 100)
            code_label.setFont(self.codes_font)
            code_label.setStyleSheet("QLineEdit"
                                     "{"
                                     "background-color : white; border-radius: 30px;"
                                     "border-top-right-radius: 10; border-bottom-right-radius: 10;"
                                     "}"
                                     )
            code_label.setGraphicsEffect(
                QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"),
                                                    offset=QtCore.QPointF(10.0, 10.0)))
            code_label.setText(f'MFC{self.num_code}')
            self.code_buttons.append(code_label)

            arrow = QImageButton(self)
            arrow.setGeometry(725, y, 100, 100)
            arrow.setImage('images/arrow.png')
            arrow.newOption('border: none;')
            arrow.setGraphicsEffect(
                QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"),
                                                    offset=QtCore.QPointF(0, 10.0)))
            self.arrow_buttons.append(arrow)

            promo = QLineEdit(self)
            promo.setGeometry(825, y, 500, 100)
            promo.setFont(self.codes_font)
            promo.setStyleSheet("QLineEdit"
                                "{"
                                "background-color : blue; border-radius: 10px;"
                                "border-top-right-radius: 0; border-bottom-right-radius: 0;"
                                "}"
                                )
            promo.setGraphicsEffect(
                QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"),
                                                    offset=QtCore.QPointF(10.0, 10.0)))
            promo.setText('Позиция')
            self.promo_buttons.append(promo)

            use_code_button = QImageButton(self)
            use_code_button.setGeometry(1325, y, 100, 100)
            use_code_button.setImage('images/codes.png')
            use_code_button.newOption('border: none;')
            use_code_button.setGraphicsEffect(
                QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"),
                                                    offset=QtCore.QPointF(10.0, 10.0)))
            use_code_button.clicked.connect(self.delete_code)
            self.del_code_connecter[use_code_button] = [code_label, promo]
            self.use_code_buttons.append(use_code_button)
            self.num_code += 1
            y += 150

        self.save_code_button = QImageButton(self)
        self.save_code_button.setGeometry(self.width() - 250, self.height() - 250, 200, 200)
        self.save_code_button.setImage('images/save.png')
        self.save_code_button.newOption('border: none;')
        self.save_code_button.clicked.connect(self.save_codes)

        self.append_code_button = QImageButton(self)
        self.append_code_button.setGeometry(425, 50, 1000, 100)
        self.append_code_button.setText('+')
        self.append_code_button.setFont(self.position_font)
        self.append_code_button.newOption("QPushButton"
                                          "{"
                                          "background-color : blue; border-radius: 30px;"
                                          "}"
                                          "QPushButton::pressed"
                                          "{"
                                          "background-color : cyan; border-radius: 30px;"
                                          "}"
                                          )
        self.append_code_button.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"), offset=QtCore.QPointF(10.0, 10.0)))
        self.append_code_button.clicked.connect(self.show_new)

        self.codes_mover = 0

        self.soon_font = QFont('Arial', 50)
        self.soon_font.setWeight(500)

        self.state_1()

    def state_1(self):
        self.logo_text.show()
        self.set_logo_button.show()
        self.save_itm_button.hide()
        self.position_arrow_up.hide()
        self.position_arrow_down.hide()
        self.button_plus.hide()
        self.append_file_button.hide()
        self.file_save_button.hide()
        self.append_code_button.hide()
        self.save_code_button.hide()
        for i in self.section_buttons:
            i.hide()
        self.section_arrow_up.hide()
        self.section_arrow_down.hide()
        for i in self.all_position_buttons:
            for j in i:
                j.hide()
        for i in self.all_file_buttons:
            for j in i:
                j.hide()
        for i in self.all_code_buttons:
            for j in i:
                j.hide()
        for i in self.files_moves_buttons:
            i.hide()
        for i in self.tub_buttons:
            i.setStyleSheet("QPushButton"
                            "{"
                            "background-color : white; border-radius: 10px;"
                            "border-top-left-radius: 0; border-bottom-left-radius: 0;"
                            "text-align: left;"
                            "}"
                            )
            i.resize(285, 100)
        self.tub_button_1.setStyleSheet("QPushButton"
                                        "{"
                                        "background-color : orange; border-radius: 10px;"
                                        "border-top-left-radius: 0; border-bottom-left-radius: 0;"
                                        "text-align: left;"
                                        "}"
                                        )
        self.tub_button_1.setGeometry(-10, 300, 335, 100)

    def set_new_logo(self):
        try:
            self.fname = QFileDialog.getOpenFileName(self, 'Выберите файл : ', '')[0]
            self.sender().setImage(self.fname)
            self.found_connecter[self.fname.split('/')[-1]] = self.fname
            self.sender().logo_found(self.fname)
            self.sender().setImage('images/logo.png')
            self.logo.setImage('images/logo.png')
        except Exception:
            pass

    def state_2(self):
        self.set_logo_button.hide()
        self.save_itm_button.hide()
        self.position_arrow_up.hide()
        self.position_arrow_down.hide()
        self.button_plus.hide()
        self.file_save_button.show()
        self.logo_text.hide()
        self.append_code_button.hide()
        self.save_code_button.hide()
        for i in self.section_buttons:
            i.hide()
        self.section_arrow_up.hide()
        self.section_arrow_down.hide()
        for i in self.all_position_buttons:
            for j in i:
                j.hide()
        for i in self.all_file_buttons:
            for j in i:
                j.hide()
        for i in self.all_code_buttons:
            for j in i:
                j.hide()
        for i in self.files_moves_buttons:
            i.show()
        for i in self.tub_buttons:
            i.setStyleSheet("QPushButton"
                            "{"
                            "background-color : white; border-radius: 10px;"
                            "border-top-left-radius: 0; border-bottom-left-radius: 0;"
                            "text-align: left;"
                            "}"
                            )
            i.resize(285, 100)
        self.tub_button_2.setStyleSheet("QPushButton"
                                        "{"
                                        "background-color : orange; border-radius: 10px;"
                                        "border-top-left-radius: 0; border-bottom-left-radius: 0;"
                                        "text-align: left;"
                                        "}"
                                        )
        self.tub_button_2.setGeometry(-10, 425, 335, 100)
        data_state = cur.execute("""SELECT * FROM Section""").fetchall()
        for i in range(len(data_state)):
            if data_state[i][1]:
                self.filenames[i].setText(data_state[i][1].split('/')[-1])
                self.founder[i].setImage(data_state[i][1])
                self.found_connecter[data_state[i][1].split('/')[-1]] = data_state[i][1]
                for j in self.all_file_buttons:
                    j[i].show()
        self.files_start()
        for i in range(len(self.title_buttons)):
            if self.title_buttons[i].isHidden():
                self.append_file_button.move(self.code_buttons[i].x(), self.code_buttons[i].y())
                self.append_file_button.show()
                break

    def found_file(self):
        try:
            self.fname = QFileDialog.getOpenFileName(self, 'Выберите файл : ', '')[0]
            self.image_connecter[self.sender()][1].setImage(self.fname)
            self.image_connecter[self.sender()][0].setText(self.fname.split('/')[-1])
            self.found_connecter[self.fname.split('/')[-1]] = self.fname
        except Exception:
            pass

    def save_files(self):
        for i in range(len(self.filenames)):
            if not self.filenames[i].isHidden() and self.filenames[i].text():
                data_state = cur.execute("""SELECT * FROM Section""").fetchall()
                if len(data_state) >= i + 1 and self.filenames[i].text():
                    cur.execute(f"UPDATE Section "
                                f"SET image = '{self.found_connecter[self.filenames[i].text()]}' "
                                f"WHERE id = '{i + 1}'")
                else:
                    cur.execute(
                        f"INSERT INTO Section(image) VALUES('{self.found_connecter[self.filenames[i].text()]}')")
                    cur.execute(f"INSERT INTO SectionBtn(name,image,price) VALUES('','','')")
            elif not self.filenames[i].isHidden():
                cur.execute(f"DELETE from Section "
                            f"WHERE id = '{i + 1}'")
                cur.execute(f"DELETE from SectionBtn "
                            f"WHERE id = '{i + 1}'")
            else:
                break
        self.state_2()
        con.commit()

    def show_new_file(self):
        for i in range(len(self.title_buttons)):
            if self.title_buttons[i].isHidden():
                self.append_file_button.move(self.title_buttons[i].x(), self.title_buttons[i].y() + 150)
                for j in self.all_file_buttons:
                    j[i].show()
                break

    def delete_file(self):
        for i in self.founder[self.filenames.index(self.delete_connecter[self.sender()]):-2]:
            if self.filenames[self.founder.index(i) + 1].text():
                i.setImage(self.found_connecter[self.filenames[self.founder.index(i) + 1].text()])
            else:
                i.setStyleSheet('border : none;')
        for i in self.filenames[self.filenames.index(self.delete_connecter[self.sender()]):-2]:
            i.setText(self.filenames[self.filenames.index(i) + 1].text())

    def files_up(self):
        if self.file_high < 0:
            for i in self.all_file_buttons:
                for j in i:
                    j.move(j.x(), j.y() + 150)
            self.append_file_button.move(self.append_file_button.x(), self.append_file_button.y() + 150)
            self.file_high += 1

    def files_down(self):
        a = 49
        for i in range(len(self.filenames)):
            if self.filenames[i].isHidden():
                a = i - 1
                break
        if a > abs(self.file_high) + 4:
            for i in self.all_file_buttons:
                for j in i:
                    j.move(j.x(), j.y() - 150)
            self.append_file_button.move(self.append_file_button.x(), self.append_file_button.y() - 150)
            self.file_high -= 1

    def files_start(self):
        if self.file_high == 0:
            pass
        elif self.file_high > 0:
            for i in range(self.file_high):
                self.files_down()
        else:
            for j in range(abs(self.file_high)):
                self.files_up()

    def state_3(self):
        self.set_logo_button.hide()
        self.save_itm_button.show()
        self.position_arrow_up.show()
        self.position_arrow_down.show()
        self.button_plus.hide()
        self.section_buttons_high = 0
        self.append_file_button.hide()
        self.file_save_button.hide()
        self.logo_text.hide()
        self.append_code_button.hide()
        self.save_code_button.hide()
        for i in self.section_buttons:
            i.show()
        self.section_arrow_up.show()
        self.section_arrow_down.show()
        for i in self.all_position_buttons:
            for j in i:
                j.hide()
        for i in self.all_file_buttons:
            for j in i:
                j.hide()
        for i in self.all_code_buttons:
            for j in i:
                j.hide()
        for i in self.files_moves_buttons:
            i.hide()
        for i in self.tub_buttons:
            i.setStyleSheet("QPushButton"
                            "{"
                            "background-color : white; border-radius: 10px;"
                            "border-top-left-radius: 0; border-bottom-left-radius: 0;"
                            "text-align: left;"
                            "}"
                            )
            i.resize(285, 100)
        self.tub_button_3.setStyleSheet("QPushButton"
                                        "{"
                                        "background-color : orange; border-radius: 10px;"
                                        "border-top-left-radius: 0; border-bottom-left-radius: 0;"
                                        "text-align: left;"
                                        "}"
                                        )
        self.tub_button_3.setGeometry(-10, 550, 335, 100)
        self.load_sections()

    def load_sections(self):
        data_section = cur.execute("""SELECT * FROM Section""").fetchall()
        if len(data_section) > 1:
            self.pos_high = 0
            if self.section_buttons_high == 0:
                self.section_buttons[0].hide()
                self.section_buttons[1].show()
                self.section_buttons[2].show()
                for i in data_section[0:2:1]:
                    self.section_buttons[i[0] - self.section_buttons_high].setImage(i[1])
                    self.section_buttons_connecter[self.section_buttons[i[0] - self.section_buttons_high]] = i[0]
            elif self.section_buttons_high == len(data_section) - 1:
                self.section_buttons[0].show()
                self.section_buttons[1].show()
                self.section_buttons[2].hide()
                self.section_buttons[data_section[-2][0] - self.section_buttons_high].setImage(data_section[-2][1])
                self.section_buttons_connecter[self.section_buttons[data_section[-2][0] - self.section_buttons_high]] = \
                    data_section[-2][0]
                self.section_buttons[data_section[-1][0] - self.section_buttons_high].setImage(data_section[-1][1])
                self.section_buttons_connecter[self.section_buttons[data_section[-1][0] - self.section_buttons_high]] = \
                    data_section[-1][0]
            else:
                self.section_buttons[0].show()
                self.section_buttons[1].show()
                self.section_buttons[2].show()
                for i in data_section[self.section_buttons_high - 1:self.section_buttons_high + 2:1]:
                    self.section_buttons[i[0] - self.section_buttons_high].setImage(i[1])
                    self.section_buttons_connecter[self.section_buttons[i[0] - self.section_buttons_high]] = i[0]
            self.load_items()
        elif len(data_section) == 1:
            self.section_buttons[0].hide()
            self.section_buttons[1].show()
            self.section_buttons[2].hide()
            self.section_buttons[1].setImage(data_section[0][1])
            self.section_buttons_connecter[self.section_buttons[1]] = data_section[0][0]
            self.load_items()
        else:
            self.state_2()

    def load_items(self):
        data_section = cur.execute("""SELECT * FROM SectionBtn""").fetchall()
        if data_section[self.section_buttons_high][1]:
            if len(data_section[self.section_buttons_high][1].split(';')) >= 3 + self.pos_high * 3:
                for i in range(0 + self.pos_high * 3, 3 + self.pos_high * 3):
                    self.position_txt[i - self.pos_high * 3].show()
                    self.position_images[i - self.pos_high * 3].show()
                    self.prices[i - self.pos_high * 3].show()
                    self.position_txt[i - self.pos_high * 3].setText(
                        data_section[self.section_buttons_high][1].split(';')[i])
                    self.position_images[i - self.pos_high * 3].setImage(
                        data_section[self.section_buttons_high][2].split(';')[i])
                    self.prices[i - self.pos_high * 3].setValue(
                        int(data_section[self.section_buttons_high][3].split(';')[i]))
                self.button_plus.hide()
            else:
                for i in range(0 + self.pos_high * 3,
                               len(data_section[self.section_buttons_high][1].split(';'))):
                    self.position_txt[i - self.pos_high * 3].show()
                    self.position_images[i - self.pos_high * 3].show()
                    self.prices[i - self.pos_high * 3].show()
                    self.position_txt[i - self.pos_high * 3].setText(
                        data_section[self.section_buttons_high][1].split(';')[i])
                    self.position_images[i - self.pos_high * 3].setImage(
                        data_section[self.section_buttons_high][2].split(';')[i])
                    self.prices[i - self.pos_high * 3].setValue(
                        int(data_section[self.section_buttons_high][3].split(';')[i]))
                for i in range(len(data_section[self.section_buttons_high][1].split(';')) - self.pos_high * 3, 3):
                    for j in self.all_position_buttons:
                        j[i].hide()
                self.button_plus.move(
                    self.all_position_buttons[0][
                        len(data_section[self.section_buttons_high][1].split(';')) - self.pos_high * 3].x(),
                    self.all_position_buttons[0][
                        len(data_section[self.section_buttons_high][1].split(';')) - self.pos_high * 3].y()
                )
                self.button_plus.show()
                self.pluser = len(data_section[self.section_buttons_high][1].split(';')) - self.pos_high * 3
        else:
            for i in range(3):
                for j in self.all_position_buttons:
                    j[i].hide()
            self.button_plus.move(
                self.all_position_buttons[0][0].x(),
                self.all_position_buttons[0][0].y()
            )
            self.button_plus.show()
            self.pluser = 0

    def poser(self):
        data_section = cur.execute("""SELECT * FROM SectionBtn""").fetchall()
        if self.sender() == self.position_arrow_down:
            if len(data_section[self.section_buttons_high][1].split(';')) >= (self.pos_high + 1) * 3:
                self.pos_high += 1
                self.load_items()
        else:
            if self.pos_high > 0:
                self.pos_high -= 1
                self.load_items()

    def plus(self):
        self.position_images[self.pluser].show()
        self.position_txt[self.pluser].show()
        self.prices[self.pluser].show()
        self.position_images[self.pluser].setImage('images/file.png')
        self.position_txt[self.pluser].setText('')
        self.prices[self.pluser].setValue(0)
        if self.pluser < 2:
            self.pluser += 1
            self.button_plus.move(self.button_plus.x() + 525, self.button_plus.y())
        else:
            self.button_plus.hide()

    def set_img(self):
        try:
            self.fname = QFileDialog.getOpenFileName(self, 'Выберите файл : ', '')[0]
            self.sender().setImage(self.fname)
        except Exception:
            pass

    def up_down_section_buttons(self):
        data_section = cur.execute("""SELECT * FROM SectionBtn""").fetchall()
        if self.sender() == self.section_arrow_down:
            if len(data_section) - 1 > self.section_buttons_high:
                self.section_buttons_high += 1
        else:
            if self.section_buttons_high > 0:
                self.section_buttons_high -= 1
        self.load_sections()

    def save_items(self):
        data_section = cur.execute(
            f"""SELECT * FROM SectionBtn WHERE id = {self.section_buttons_high + 1}""").fetchall()[0]
        sn = data_section[1].split(';')
        si = data_section[2].split(';')
        sc = data_section[3].split(';')
        for i in range(self.pos_high * 3, self.pos_high * 3 + 3):
            if not self.position_txt[i - self.pos_high * 3].isHidden() and\
                    self.position_txt[i - self.pos_high * 3].text():
                if i < len(sn):
                    sn[i] = self.position_txt[i - self.pos_high * 3].text()
                else:
                    sn.append(self.position_txt[i - self.pos_high * 3].text())
                if i < len(si):
                    si[i] = self.position_images[i - self.pos_high * 3].get_image()
                else:
                    si.append(self.position_images[i - self.pos_high * 3].get_image())
                if i < len(sc):
                    sc[i] = str(self.prices[i - self.pos_high * 3].value())
                else:
                    sc.append(str(self.prices[i - self.pos_high * 3].value()))
        a = ';'.join(sn)
        if a[0] == ';':
            a = a[1:]
        cur.execute(f"UPDATE SectionBtn "
                    f"SET name = '{a}' "
                    f"WHERE id = '{self.section_buttons_high + 1}'")
        b = ';'.join(si)
        if b[0] == ';':
            b = b[1:]
        cur.execute(f"UPDATE SectionBtn "
                    f"SET image = '{b}' "
                    f"WHERE id = '{self.section_buttons_high + 1}'")
        c = ';'.join(sc)
        if c[0] == ';':
            c = c[1:]
        cur.execute(f"UPDATE SectionBtn "
                    f"SET price = '{c}' "
                    f"WHERE id = '{self.section_buttons_high + 1}'")
        con.commit()


    def state_4(self):
        self.set_logo_button.hide()
        self.save_itm_button.hide()
        self.position_arrow_up.hide()
        self.position_arrow_down.hide()
        self.button_plus.hide()
        self.append_file_button.hide()
        self.file_save_button.hide()
        self.logo_text.hide()
        self.codes_start()
        self.save_code_button.show()
        for i in self.section_buttons:
            i.hide()
        self.section_arrow_up.hide()
        self.section_arrow_down.hide()
        for i in self.all_position_buttons:
            for j in i:
                j.hide()
        for i in self.all_file_buttons:
            for j in i:
                j.hide()
        for i in self.all_code_buttons:
            for j in i:
                j.hide()
        for i in self.files_moves_buttons:
            i.hide()
        for i in self.code_moves_buttons:
            i.show()
        for i in self.tub_buttons:
            i.setStyleSheet("QPushButton"
                            "{"
                            "background-color : white; border-radius: 10px;"
                            "border-top-left-radius: 0; border-bottom-left-radius: 0;"
                            "text-align: left;"
                            "}"
                            )
            i.resize(285, 100)
        self.tub_button_4.setStyleSheet("QPushButton"
                                        "{"
                                        "background-color : orange; border-radius: 10px;"
                                        "border-top-left-radius: 0; border-bottom-left-radius: 0;"
                                        "text-align: left;"
                                        "}"
                                        )
        self.tub_button_4.setGeometry(-10, 675, 335, 100)

        with open('promocodes.csv', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for index, row in enumerate(reader):
                self.code_buttons[index].setText(row[0])
                self.code_buttons[index].show()
                self.arrow_buttons[index].show()
                self.promo_buttons[index].setText(row[1])
                self.promo_buttons[index].show()
                self.use_code_buttons[index].show()

        for i in range(len(self.code_buttons)):
            if self.code_buttons[i].isHidden():
                self.append_code_button.move(self.code_buttons[i].x(), self.code_buttons[i].y())
                self.append_code_button.show()
                break

    def codes_start(self):
        if self.codes_mover == 0:
            pass
        elif self.codes_mover > 0:
            for i in range(self.codes_mover):
                self.codes_up()
        else:
            for j in range(abs(self.codes_mover)):
                self.codes_down()

    def delete_code(self):
        for i in self.del_code_connecter[self.sender()]:
            i.setText('')

    def codes_down(self):
        a = 0
        for i in range(len(self.code_buttons)):
            if self.code_buttons[i].isHidden():
                a = i
                break
        if a - self.codes_mover > 5:
            for i in self.all_moved_buttons:
                for j in i:
                    j.move(j.x(), j.y() - 150)
            self.append_code_button.move(self.append_code_button.x(), self.append_code_button.y() - 150)
            self.codes_mover += 1

    def codes_up(self):
        if self.codes_mover > 0:
            for i in self.all_moved_buttons:
                for j in i:
                    j.move(j.x(), j.y() + 150)
            self.append_code_button.move(self.append_code_button.x(), self.append_code_button.y() + 150)
            self.codes_mover -= 1

    def show_new(self):
        for i in range(len(self.code_buttons)):
            if self.code_buttons[i].isHidden():
                self.append_code_button.move(self.code_buttons[i].x(), self.code_buttons[i].y() + 150)
                self.code_buttons[i].setText(f'MFC{i + 1}')
                self.promo_buttons[i].setText('Позиция')
                self.code_buttons[i].show()
                self.arrow_buttons[i].show()
                self.promo_buttons[i].show()
                self.use_code_buttons[i].show()
                break

    def save_codes(self):
        with open('promocodes.csv', 'w', newline='', encoding="utf8") as csvfile:
            writer = csv.writer(
                csvfile, delimiter=';', quotechar="'", quoting=csv.QUOTE_MINIMAL)
            for i in range(len(self.code_buttons)):
                if self.code_buttons[i].text() and self.promo_buttons[i].text() and \
                        not self.code_buttons[i].isHidden():
                    writer.writerow([self.code_buttons[i].text(), self.promo_buttons[i].text()])
        self.state_4()
