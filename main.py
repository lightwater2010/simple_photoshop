#создай тут фоторедактор Easy Editor!
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox, QRadioButton, QHBoxLayout,QGroupBox, QButtonGroup, QLineEdit,QTextEdit, QListWidget, QFileDialog
import os
from PIL import Image,ImageFilter, ImageEnhance
from PyQt5.QtGui import QPixmap
app = QApplication([])
win = QWidget()
win.setFixedSize(600,400)
win.setWindowTitle("Easy Editor")

katalog_bt = QPushButton("Папка")
katalog_bt.setFixedSize(100,20)
list_of_images = QListWidget()
list_of_images.setFixedSize(100,320)
left_bt = QPushButton("Лево")
right_bt = QPushButton("Право")
window_bt = QPushButton("Зеркало")
contrast_bt = QPushButton("Резкость")
black_white_bt = QPushButton("Ч/Б")
contour_bt = QPushButton("Карандаш")
img_label = QLabel("Картинка")
img_label.setFixedSize(400,400)

main_line = QHBoxLayout()
line_v1 = QVBoxLayout()
line_v2 = QVBoxLayout()
line_h1 = QHBoxLayout()

line_v1.addWidget(katalog_bt, alignment=Qt.AlignLeft)
line_v2.addWidget(img_label, alignment=Qt.AlignCenter)
line_v1.addWidget(list_of_images,alignment=Qt.AlignLeft)
line_h1.addWidget(left_bt, alignment=(Qt.AlignLeft | Qt.AlignBottom ))
line_h1.addWidget(right_bt,alignment=(Qt.AlignBottom | Qt.AlignLeft))
line_h1.addWidget(window_bt,alignment=(Qt.AlignBottom | Qt.AlignLeft))
line_h1.addWidget(contrast_bt,alignment=(Qt.AlignBottom | Qt.AlignLeft))
line_h1.addWidget(black_white_bt,alignment=(Qt.AlignBottom | Qt.AlignLeft))
line_h1.addWidget(contour_bt, alignment=(Qt.AlignBottom | Qt.AlignLeft))
work_dir = ''
extensions = [".jpg",".png",".jpeg",".svg"]
def chooseWorkDir():
     global work_dir
     work_dir = QFileDialog.getExistingDirectory()
     if work_dir:
          return work_dir
def filter_files(extensions):
     files = os.listdir(chooseWorkDir())
     right_files = []
     for file in files:
          for extension in extensions:
               if file.endswith(extension):
                    right_files.append(file)
     return right_files
def showfiles():
     list_of_images.addItems(filter_files(extensions))
class ImageProccessor():
     def __init__(self,katalog_of_changed_images):
          self.filename = None
          self.image = None
          self.katalog_of_changed_images = katalog_of_changed_images
          self.save_dir = "Modified/"
     def loadFile(self,filename):
          self.filename = filename
          if self.filename:
               path = os.path.join(work_dir, self.filename)
               self.image = Image.open(path)
          print(self.filename)
     def showImage(self,path):
          img_label.hide()
          pixmap = QPixmap(path)
          width, height = img_label.width(), img_label.height()
          pixmap = pixmap.scaled(width, height, Qt.KeepAspectRatio)
          img_label.setPixmap(pixmap)
          img_label.show()
     def do_black_white(self):
          self.image = self.image.convert("L")
          if work_dir.endswith(self.save_dir.replace("/", "")):
               img_path = os.path.join(work_dir, self.filename)
          else:
               img_path = os.path.join(work_dir, self.save_dir, self.filename)
          self.image.save(img_path)
          self.showImage(img_path)
     def do_contrast(self):
          self.image = self.image.filter(ImageFilter.SHARPEN)
          print(work_dir)
          if work_dir.endswith(self.save_dir.replace("/", "")):
               img_path = os.path.join(work_dir, self.filename)
          else:
               img_path = os.path.join(work_dir, self.save_dir, self.filename)
          self.image.save(img_path)
          self.showImage(img_path)
     def window_img(self):
          self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
          if work_dir.endswith(self.save_dir.replace("/", "")):
               img_path = os.path.join(work_dir, self.filename)
          else:
               img_path = os.path.join(work_dir, self.save_dir, self.filename)
          self.image.save(img_path)
          self.showImage(img_path)
     def rotate_left(self):
          self.image = self.image.transpose(Image.ROTATE_90)
          if work_dir.endswith(self.save_dir.replace("/", "")):
               img_path = os.path.join(work_dir, self.filename)
          else:
               img_path = os.path.join(work_dir, self.save_dir, self.filename)
          self.image.save(img_path)
          self.showImage(img_path)
     def create_katalog_for_changed_images(self,path):
          os.mkdir(path)
     def do_contour_photo(self):
          self.image = self.image.filter(ImageFilter.CONTOUR)
          if work_dir.endswith(self.save_dir.replace("/", "")):
               img_path = os.path.join(work_dir, self.filename)
          else:
               img_path = os.path.join(work_dir, self.save_dir, self.filename)
          self.image.save(img_path)
          self.showImage(img_path)
     def rotate_right(self):
          self.image = self.image.transpose(Image.ROTATE_270)
          if work_dir.endswith(self.save_dir.replace("/", "")):
               img_path = os.path.join(work_dir, self.filename)
          else:
               img_path = os.path.join(work_dir, self.save_dir, self.filename)
          self.image.save(img_path)
          self.showImage(img_path)
katalog_bt.clicked.connect(showfiles)
work_img = ImageProccessor('')

def help_to_ShowImage():
     if list_of_images.selectedItems():
          path_of_catalog = os.path.join(work_dir, "Modified/")
          if not os.path.exists(path_of_catalog):
               work_img.create_katalog_for_changed_images(path_of_catalog)
          image_name = list_of_images.selectedItems()[0].text()
          work_img.loadFile(image_name)
          path = os.path.join(work_dir, image_name)
          work_img.showImage(path)
list_of_images.itemClicked.connect(help_to_ShowImage)
black_white_bt.clicked.connect(work_img.do_black_white)
contrast_bt.clicked.connect(work_img.do_contrast)
window_bt.clicked.connect(work_img.window_img)
left_bt.clicked.connect(work_img.rotate_left)
contour_bt.clicked.connect(work_img.do_contour_photo)
right_bt.clicked.connect(work_img.rotate_right)
line_v2.addLayout(line_h1)
main_line.addLayout(line_v1)
main_line.addLayout(line_v2)
win.setLayout(main_line)

win.show()
app.exec()