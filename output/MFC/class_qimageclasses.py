import csv
from PIL import Image
from PyQt5.QtWidgets import QPushButton, QTextEdit

images = 0
used_images = {}
logo = 'logo.png'
with open('images.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar="'")
    for index, row in enumerate(reader):
        used_images[f'{row[0]}'] = f'{row[1]}'
        images = int(row[1])
with open('logotype.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar="'")
    for row in enumerate(reader):
        logo = row[1][0]
images += 1


class QImageButton(QPushButton):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._image = None
        self.options = ''
        self.image = None
        self.img = ''

    def newOption(self, option):
        self.options += option + ' '
        if self.image:
            self.setStyleSheet(f"{self.options}background-image : url({self.image});")
        else:
            self.setStyleSheet(f"{self.options}")

    def setColText(self, text):
        if int(text) < 100:
            self.setText(text)
        else:
            self.setText('99')

    def setColText_(self, text):
        if int(text) < 10000:
            self.setText(text)
        else:
            self.setText('9999')

    def get_image(self):
        return self.img

    def getOptions(self):
        return self.options

    def setImage(self, image):
        global images, used_images
        if image == 'logo.png':
            image = logo
        self.img = image
        img = Image.open(image)
        if f'{(f"""{self.width()}/{self.height()}""", image)}' not in used_images:
            new_image = img.resize((self.width(), self.height()))
            new_image.save(f'new_image_{images}.png')
            used_images[f'{(f"""{self.width()}/{self.height()}""", image)}'] = f'{images}'
            with open('images.csv', 'a', newline='', encoding="utf8") as csvfile:
                writer = csv.writer(
                    csvfile, delimiter=';', quotechar="'", quoting=csv.QUOTE_MINIMAL)
                writer.writerow([f'{(f"""{self.width()}/{self.height()}""", image)}', f'{images}'])
            self.image = f'new_image_{images}.png'
            self.setStyleSheet(f"{self.options}background-image : url(new_image_{images}.png);")
            images += 1
        else:
            self.image = f"""new_image_{used_images[f'{(f"{self.width()}/{self.height()}", image)}']}.png"""
            self.setStyleSheet(
                f"""{self.options}background-image : url(new_image_{used_images[f'{(f"{self.width()}/{self.height()}", image)}']}.png);""")

    def logo_found(self, imger):
        global logo
        logo = imger
        with open('logotype.csv', 'w', newline='', encoding="utf8") as csvfile:
            writer = csv.writer(
                csvfile, delimiter=';', quotechar="'", quoting=csv.QUOTE_MINIMAL)
            writer.writerow([imger])


class QImageText(QTextEdit):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._image = None
        self.setReadOnly(True)
        self.options = ''
        self.image = None

    def newOption(self, option):
        self.options += option + ' '
        if self.image:
            self.setStyleSheet(f"{self.options}background-image : url({self.image});")
        else:
            self.setStyleSheet(f"{self.options}")

    def setImage(self, image):
        global images, used_images
        img = Image.open(image)
        if f'{(f"""{self.width()}/{self.height()}""", image)}' not in used_images:
            new_image = img.resize((self.width(), self.height()))
            new_image.save(f'new_image_{images}.png')
            used_images[f'{(f"""{self.width()}/{self.height()}""", image)}'] = f'{images}'
            with open('images.csv', 'a', newline='', encoding="utf8") as csvfile:
                writer = csv.writer(
                    csvfile, delimiter=';', quotechar="'", quoting=csv.QUOTE_MINIMAL)
                writer.writerow([f'{(f"""{self.width()}/{self.height()}""", image)}', f'{images}'])
            self.image = f'new_image_{images}.png'
            self.setStyleSheet(f"{self.options}background-image : url(new_image_{images}.png);")
            images += 1
        else:
            self.image = f"""new_image_{used_images[f'{(f"{self.width()}/{self.height()}", image)}']}.png"""
            self.setStyleSheet(
                f"""{self.options}background-image : url(new_image_{used_images[f'{(f"{self.width()}/{self.height()}", image)}']}.png);""")
