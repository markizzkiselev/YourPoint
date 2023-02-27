import sys
import csv
import sqlite3
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel
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
        self.setWindowTitle('MFC')
        self.setGeometry(0, 0, desktop.availableGeometry().width(), desktop.availableGeometry().height())

        self.red_background = QImageText(self)
        self.red_background.setGeometry(0, 0, 400, self.height())
        self.red_background.setStyleSheet("background-color: red; border: none;")

        self.logo = QImageButton(self)
        self.logo.setGeometry(100, 50, 200, 200)
        self.logo.setImage('images/logo.png')
        self.logo.newOption('border: none;')

        button_font = QFont('Arial', 20)
        button_font.setWeight(500)

        arrow_font = QFont('Arial', 100)
        arrow_font.setWeight(500)

        self.section_arrow_up = QImageButton(self)
        self.section_arrow_up.setGeometry(10, 400, 130, 200)
        self.section_arrow_up.setText('↑')
        self.section_arrow_up.newOption('border: none;')
        self.section_arrow_up.setFont(arrow_font)
        self.section_arrow_up.clicked.connect(self.up_down_section_buttons)

        self.section_arrow_down = QImageButton(self)
        self.section_arrow_down.setGeometry(10, 625, 130, 200)
        self.section_arrow_down.setText('↓')
        self.section_arrow_down.newOption('border: none;')
        self.section_arrow_down.setFont(arrow_font)
        self.section_arrow_down.clicked.connect(self.up_down_section_buttons)

        self.section_buttons = []
        self.section_buttons_connecter = {}
        self.section_buttons_high = 0
        for i in range(3):
            button = QImageButton(self)
            button.setGeometry(150, 300 + 225 * i, 200, 200)
            button.newOption('border-radius: 30px;')
            button.setGraphicsEffect(
                QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"),
                                                    offset=QtCore.QPointF(10.0, 10.0)))
            button.setFont(button_font)
            button.clicked.connect(self.start_state)
            self.section_buttons_connecter[button] = i
            self.section_buttons.append(button)
        self.load_sections()

        self.basket_button = QImageButton(self)
        self.basket_button.setGeometry(self.width() - 250, self.height() - 250, 200, 200)
        self.basket_button.setImage('images/basketshop.png')
        self.basket_button.newOption('border: none;')
        self.basket_button.clicked.connect(self.state_basket)

        self.basket_col = QPushButton(self)
        self.basket_col.setGeometry(self.width() - 250, self.height() - 210, 200, 200)
        self.basket_col.setText('0')

        self.col_font = QFont('Arial', 35)
        self.col_font.setWeight(500)

        self.basket_col.setFont(self.col_font)
        self.basket_col.clicked.connect(self.state_basket)
        self.basket_col.setStyleSheet('color : white; border: none;')

        self.code_label = QLineEdit(self)
        self.code_label.setGeometry(1475, 50, 300, 100)

        self.codes_font = QFont('Arial', 46)
        self.codes_font.setWeight(500)

        self.code_label.setFont(self.codes_font)
        self.code_label.setStyleSheet("QLineEdit"
                                      "{"
                                      "background-color : white; border-radius: 30px;"
                                      "border-top-right-radius: 0; border-bottom-right-radius: 0;"
                                      "}"
                                      )
        self.code_label.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"), offset=QtCore.QPointF(10.0, 10.0)))

        self.use_code_button = QImageButton(self)
        self.use_code_button.setGeometry(1775, 50, 100, 100)
        self.use_code_button.setImage('images/codes.png')
        self.use_code_button.newOption('border: none;')
        self.use_code_button.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"), offset=QtCore.QPointF(10.0, 10.0)))
        self.use_code_button.clicked.connect(self.read_code)

        self.position_image_button_1 = QImageButton(self)
        self.position_image_button_1.setGeometry(500, 100, 400, 400)
        self.position_image_button_1.newOption('border-radius: 30px;')
        self.position_image_button_1.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"), offset=QtCore.QPointF(10.0, 10.0)))

        self.position_image_button_2 = QImageButton(self)
        self.position_image_button_2.setGeometry(950, 100, 400, 400)
        self.position_image_button_2.newOption('border-radius: 30px;')
        self.position_image_button_2.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"), offset=QtCore.QPointF(10.0, 10.0)))

        self.position_image_button_3 = QImageButton(self)
        self.position_image_button_3.setGeometry(1400, 100, 400, 400)
        self.position_image_button_3.newOption('border-radius: 30px;')
        self.position_image_button_3.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"), offset=QtCore.QPointF(10.0, 10.0)))

        self.position_font = QFont('Arial', 30)
        self.position_font.setWeight(500)

        self.position_text_button_1 = QImageButton(self)
        self.position_text_button_1.setGeometry(500, 525, 400, 100)
        self.position_text_button_1.setFont(self.position_font)
        self.position_text_button_1.newOption("QPushButton"
                                              "{"
                                              "background-color : red; border-radius: 30px;"
                                              "}"
                                              "QPushButton::pressed"
                                              "{"
                                              "background-color : orange; border-radius: 30px;"
                                              "}"
                                              )
        self.position_text_button_1.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"), offset=QtCore.QPointF(10.0, 10.0)))
        self.position_text_button_1.clicked.connect(self.append_to_basket)

        self.position_text_button_2 = QImageButton(self)
        self.position_text_button_2.setGeometry(950, 525, 400, 100)
        self.position_text_button_2.setFont(self.position_font)
        self.position_text_button_2.newOption("QPushButton"
                                              "{"
                                              "background-color : red; border-radius: 30px;"
                                              "}"
                                              "QPushButton::pressed"
                                              "{"
                                              "background-color : orange; border-radius: 30px;"
                                              "}"
                                              )
        self.position_text_button_2.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"), offset=QtCore.QPointF(10.0, 10.0)))
        self.position_text_button_2.clicked.connect(self.append_to_basket)

        self.position_text_button_3 = QImageButton(self)
        self.position_text_button_3.setGeometry(1400, 525, 400, 100)
        self.position_text_button_3.setFont(self.position_font)
        self.position_text_button_3.newOption("QPushButton"
                                              "{"
                                              "background-color : red; border-radius: 30px;"
                                              "}"
                                              "QPushButton::pressed"
                                              "{"
                                              "background-color : orange; border-radius: 30px;"
                                              "}"
                                              )
        self.position_text_button_3.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"), offset=QtCore.QPointF(10.0, 10.0)))
        self.position_text_button_3.clicked.connect(self.append_to_basket)

        self.price_button_1 = QImageButton(self)
        self.price_button_1.setGeometry(500, 625, 400, 100)
        self.price_button_1.setFont(self.position_font)
        self.price_button_1.newOption("border : none")

        self.price_button_2 = QImageButton(self)
        self.price_button_2.setGeometry(950, 625, 400, 100)
        self.price_button_2.setFont(self.position_font)
        self.price_button_2.newOption("border : none")

        self.price_button_3 = QImageButton(self)
        self.price_button_3.setGeometry(1400, 625, 400, 100)
        self.price_button_3.setFont(self.position_font)
        self.price_button_3.newOption("border : none")

        self.price_buttons = [
            self.price_button_1,
            self.price_button_2,
            self.price_button_3
        ]

        self.position_image_buttons = [
            self.position_image_button_1,
            self.position_image_button_2,
            self.position_image_button_3
        ]

        self.position_text_buttons = [
            self.position_text_button_1,
            self.position_text_button_2,
            self.position_text_button_3
        ]

        self.pr_con = {
            self.position_text_button_1: self.price_button_1,
            self.position_text_button_2: self.price_button_2,
            self.position_text_button_3: self.price_button_3
        }

        self.basket_buttons = []
        self.minus_buttons = []
        self.minus_buttons_connect = {}
        self.col_buttons = []
        self.col_buttons_connect = {}
        self.plus_buttons = []
        self.plus_buttons_connect = {}
        self.pricer = []
        self.price_con = {}
        y = 50
        for i in range(100):
            button = QImageButton(self)
            button.setGeometry(525, y, 425, 75)
            button.setFont(self.position_font)
            button.newOption("QPushButton"
                             "{"
                             "background-color : red; border-radius: 30px; text-align: left;"
                             "}"
                             )
            button.setGraphicsEffect(
                QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"),
                                                    offset=QtCore.QPointF(10.0, 10.0)))
            button.hide()
            self.basket_buttons.append(button)

            price = QImageButton(self)
            price.setGeometry(975, y, 150, 75)
            price.setFont(self.position_font)
            price.newOption("QPushButton"
                            "{"
                            "background-color : red; border-radius: 30px; text-align: left; text-align: center"
                            "}"
                            )
            price.setGraphicsEffect(
                QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"),
                                                    offset=QtCore.QPointF(10.0, 10.0)))
            price.hide()
            self.pricer.append(price)

            button_minus = QImageButton(self)
            button_minus.setText('-')
            button_minus.setGeometry(1150, y, 75, 75)
            button_minus.setFont(self.position_font)
            button_minus.newOption("QPushButton"
                                   "{"
                                   "background-color : red; border-radius: 30px;"
                                   "}"
                                   "QPushButton::pressed"
                                   "{"
                                   "background-color : orange; border-radius: 30px;"
                                   "}"
                                   )
            button_minus.setGraphicsEffect(
                QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"),
                                                    offset=QtCore.QPointF(10.0, 10.0)))
            self.minus_buttons.append(button_minus)
            self.minus_buttons_connect[button_minus] = button
            button_minus.hide()
            button_minus.clicked.connect(self.append_in_basket)

            button_col = QImageButton(self)
            button_col.setGeometry(1250, y, 75, 75)
            button_col.setFont(self.position_font)
            button_col.newOption("QPushButton"
                                 "{"
                                 "background-color : red; border-radius: 30px;"
                                 "}"
                                 )
            button_col.setGraphicsEffect(
                QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"),
                                                    offset=QtCore.QPointF(10.0, 10.0)))
            self.col_buttons.append(button_col)
            self.col_buttons_connect[button] = button_col
            button_col.hide()

            self.price_con[price] = button_col

            button_plus = QImageButton(self)
            button_plus.setText('+')
            button_plus.setGeometry(1350, y, 75, 75)
            button_plus.setFont(self.position_font)
            button_plus.newOption("QPushButton"
                                  "{"
                                  "background-color : red; border-radius: 30px;"
                                  "}"
                                  "QPushButton::pressed"
                                  "{"
                                  "background-color : orange; border-radius: 30px;"
                                  "}"
                                  )
            button_plus.setGraphicsEffect(
                QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"),
                                                    offset=QtCore.QPointF(10.0, 10.0)))
            self.plus_buttons.append(button_plus)
            self.plus_buttons_connect[button_plus] = button
            button_plus.hide()
            button_plus.clicked.connect(self.append_in_basket)
            y += 100

        self.basket_up_button = QImageButton(self)
        self.basket_up_button.setText('↑')
        self.basket_up_button.setGeometry(450, 50, 50, 440)
        self.basket_up_button.setFont(self.position_font)
        self.basket_up_button.newOption("QPushButton"
                                        "{"
                                        "background-color : red; border-radius: 10px;"
                                        "}"
                                        "QPushButton::pressed"
                                        "{"
                                        "background-color : orange; border-radius: 10px;"
                                        "}"
                                        )
        self.basket_up_button.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"), offset=QtCore.QPointF(10.0, 10.0)))
        self.basket_up_button.clicked.connect(self.basket_up)

        self.basket_down_button = QImageButton(self)
        self.basket_down_button.setText('↓')
        self.basket_down_button.setGeometry(450, 515, 50, 440)
        self.basket_down_button.setFont(self.position_font)
        self.basket_down_button.newOption("QPushButton"
                                          "{"
                                          "background-color : red; border-radius: 10px;"
                                          "}"
                                          "QPushButton::pressed"
                                          "{"
                                          "background-color : orange; border-radius: 10px;"
                                          "}"
                                          )
        self.basket_down_button.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(self, color=QtGui.QColor("black"), offset=QtCore.QPointF(10.0, 10.0)))
        self.basket_down_button.clicked.connect(self.basket_down)

        self.free_basket_button = QLabel(self)
        self.free_basket_button.resize(1000, 100)
        self.free_basket_button.setText('Корзина пуста.')

        self.free_font = QFont('Arial', 50)
        self.free_font.setWeight(500)

        self.free_basket_button.setFont(self.free_font)
        self.free_basket_button.move(
            (desktop.availableGeometry().width() - self.free_basket_button.width()) // 2 + 150,
            (desktop.availableGeometry().height() - self.free_basket_button.height()) // 2,
        )
        self.free_basket_button.setAlignment(QtCore.Qt.AlignCenter)

        self.right_button = QImageButton(self)
        self.right_button.setGeometry(500, 800, 200, 200)
        self.right_button.setImage('images/arrow_left.png')
        self.right_button.newOption('border: none;')
        self.right_button.clicked.connect(self.listed)

        self.left_button = QImageButton(self)
        self.left_button.setGeometry(750, 800, 200, 200)
        self.left_button.setImage('images/arrow.png')
        self.left_button.newOption('border: none;')
        self.left_button.clicked.connect(self.listed)

        self.lister = 0
        self.del_index = 0

        self.read_code_flag = False
        self.del_position_flag = False

        self.state = 0
        self.section_buttons[0].click()

    def center(self):
        desktop = app.desktop()
        x = (desktop.availableGeometry().width() - self.width()) // 2
        y = (desktop.availableGeometry().height() - self.height()) // 2
        self.move(x, y)

    def read_code(self):
        self.read_code_flag = True
        with open('promocodes.csv', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for index, row in enumerate(reader):
                if row[0] == self.code_label.text():
                    self.basket.append(row[1])
                    self.state_basket()
            self.code_label.setText('')

    def load_sections(self):
        data_section = cur.execute("""SELECT * FROM Section""").fetchall()
        for i in data_section[0 + self.section_buttons_high:3 + self.section_buttons_high]:
            self.section_buttons[i[0] - 1 - self.section_buttons_high].setImage(i[1])
            self.section_buttons_connecter[self.section_buttons[i[0] - 1 - self.section_buttons_high]] = i[0]

    def up_down_section_buttons(self):
        data_section = cur.execute("""SELECT * FROM Section""").fetchall()
        if self.sender() == self.section_arrow_down:
            if len(data_section) > self.section_buttons_high + 3:
                self.section_buttons_high += 1
        else:
            if self.section_buttons_high > 0:
                self.section_buttons_high -= 1
        self.load_sections()

    def listed(self):
        data_state = cur.execute("""SELECT * FROM SectionBtn""").fetchall()
        if self.sender() == self.right_button:
            if self.lister > 0:
                self.lister -= 1
        else:
            if len(data_state[self.state - 1][1].split(';')) - 3 > self.lister:
                self.lister += 1
        for i in data_state:
            if self.state == i[0]:
                for j in range(3):
                    if i[1] and i[2]:
                        if len(i[1].split(';')) > j:
                            self.position_image_buttons[j].setImage(i[2].split(';')[j + self.lister])
                            self.position_text_buttons[j].setText(i[1].split(';')[j + self.lister])
                            self.price_buttons[j].setText(i[3].split(';')[j + self.lister])

    def start_state(self):
        self.right_button.show()
        self.left_button.show()
        self.state = self.section_buttons_connecter[self.sender()]
        self.lister = 0
        self.code_label.hide()
        self.use_code_button.hide()
        self.free_basket_button.hide()
        self.basket_up_button.hide()
        self.basket_down_button.hide()
        if len(self.basket) < 100:
            self.basket_col.setText(f'{len(self.basket)}')
        else:
            self.basket_col.setText(f'99+')
        self.red_background.show()
        self.logo.show()
        for i in self.section_buttons:
            i.show()
        self.basket_button.show()
        self.basket_col.show()
        self.position_image_button_1.show()
        self.position_image_button_2.show()
        self.position_image_button_3.show()
        self.position_text_button_1.show()
        self.position_text_button_2.show()
        self.position_text_button_3.show()
        self.price_button_1.show()
        self.price_button_2.show()
        self.price_button_3.show()
        data_state = cur.execute("""SELECT * FROM SectionBtn""").fetchall()
        for i in data_state:
            if self.section_buttons_connecter[self.sender()] == i[0]:
                for j in range(3):
                    if i[2] and i[1]:
                        if len(i[1].split(';')) > j:
                            self.position_image_buttons[j].setImage(i[2].split(';')[j + self.lister])
                            self.position_text_buttons[j].setText(i[1].split(';')[j + self.lister])
                            self.price_buttons[j].setText(i[3].split(';')[j + self.lister])
                        else:
                            self.position_image_buttons[j].hide()
                            self.position_text_buttons[j].hide()
                            self.price_buttons[j].hide()
                    else:
                        self.position_image_buttons[j].hide()
                        self.position_text_buttons[j].hide()
                        self.price_buttons[j].hide()
                        self.right_button.hide()
                        self.left_button.hide()
        for i in self.basket_buttons:
            i.hide()
        for i in self.minus_buttons:
            i.hide()
        for i in self.col_buttons:
            i.hide()
        for i in self.plus_buttons:
            i.hide()
        for i in self.pricer:
            i.hide()

    def basket_start(self):
        if self.basket.get_height() == 0:
            pass
        elif self.basket.get_height() > 0:
            for i in range(self.basket.get_height()):
                self.basket_down()
        else:
            for j in range(abs(self.basket.get_height())):
                self.basket_up()

    def basket_up(self):
        if self.basket.get_height() < 0:
            for i in self.basket_buttons:
                i.move(i.x(), i.y() + 100)
            for j in self.minus_buttons:
                j.move(j.x(), j.y() + 100)
            for k in self.col_buttons:
                k.move(k.x(), k.y() + 100)
            for q in self.plus_buttons:
                q.move(q.x(), q.y() + 100)
            for v in self.pricer:
                v.move(v.x(), v.y() + 100)
            self.basket.up()

    def basket_down(self):
        if len(self.basket.give_basket()) > abs(self.basket.get_height()) + 9:
            for i in self.basket_buttons:
                i.move(i.x(), i.y() - 100)
            for j in self.minus_buttons:
                j.move(j.x(), j.y() - 100)
            for k in self.col_buttons:
                k.move(k.x(), k.y() - 100)
            for q in self.plus_buttons:
                q.move(q.x(), q.y() - 100)
            for v in self.pricer:
                v.move(v.x(), v.y() - 100)
            self.basket.down()

    def state_basket(self):
        self.price_button_1.hide()
        self.price_button_2.hide()
        self.price_button_3.hide()
        self.right_button.hide()
        self.left_button.hide()
        if len(self.basket) != 0:
            self.basket_up_button.show()
            self.basket_down_button.show()
            self.code_label.show()
            self.use_code_button.show()
        else:
            self.basket_up_button.hide()
            self.basket_down_button.hide()
            self.code_label.hide()
            self.use_code_button.hide()
            self.free_basket_button.show()
        if self.del_position_flag:
            self.basket_start()
            for i in range(self.del_index):
                self.basket_down()
            self.del_position_flag = False
        if not self.read_code_flag:
            self.basket_start()
        else:
            self.read_code_flag = False
        for i in self.basket_buttons:
            i.hide()
        for i in self.minus_buttons:
            i.hide()
        for i in self.col_buttons:
            i.hide()
        for i in self.plus_buttons:
            i.hide()
        for i in self.pricer:
            i.hide()
        self.red_background.show()
        self.logo.show()
        for i in self.section_buttons:
            i.show()
        self.basket_button.hide()
        self.basket_col.hide()
        self.position_image_button_1.hide()
        self.position_image_button_2.hide()
        self.position_image_button_3.hide()
        self.position_text_button_1.hide()
        self.position_text_button_2.hide()
        self.position_text_button_3.hide()
        n = 0
        for i in self.basket.give_basket():
            self.basket_buttons[n].show()
            self.basket_buttons[n].setText(f'  {i}')
            self.col_buttons[n].setColText(f'{self.basket.give_basket()[i]}')
            self.minus_buttons[n].show()
            self.col_buttons[n].show()
            self.plus_buttons[n].show()
            self.pricer[n].setColText_(str(int(self.basket.get_price(i)) * int(self.price_con[self.pricer[n]].text())))
            self.pricer[n].show()
            n += 1

    def append_in_basket(self):
        if self.sender() in self.minus_buttons:
            self.basket.give_basket()[self.minus_buttons_connect[self.sender()].text()[2:]] -= 1
            self.col_buttons_connect[self.minus_buttons_connect[self.sender()]].setColText(
                f'{self.basket.give_basket()[self.minus_buttons_connect[self.sender()].text()[2:]]}'
            )
        elif self.sender() in self.plus_buttons:
            self.basket.give_basket()[self.plus_buttons_connect[self.sender()].text()[2:]] += 1
            self.col_buttons_connect[self.plus_buttons_connect[self.sender()]].setColText(
                f'{self.basket.give_basket()[self.plus_buttons_connect[self.sender()].text()[2:]]}'
            )
        del_list = []
        for i in self.basket.give_basket():
            if self.basket.give_basket()[i] == 0:
                del_list.append(i)
                self.del_index = list(self.basket.give_basket().keys()).index(i) + 1
        for i in del_list:
            self.del_position_flag = True
            del self.basket.give_basket()[i]
        self.read_code_flag = True
        self.state_basket()

    def append_to_basket(self):
        self.basket.append(self.sender().text(), self.pr_con[self.sender()].text())
        if len(self.basket) < 100:
            self.basket_col.setText(f'{len(self.basket)}')
        else:
            self.basket_col.setText(f'99+')
