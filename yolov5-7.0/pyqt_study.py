import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QPushButton, QDesktopWidget, QFileDialog, QLabel, QAction, QMenu
from PyQt5.QtGui import QPixmap,QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('植物病害识别系统')

        filemenu = self.menuBar().addMenu('File')

        # 获取屏幕尺寸
        screen = QDesktopWidget().screenGeometry()
        screen_width = screen.width()
        screen_height = screen.height()

        # 设置窗口尺寸和位置
        self.setGeometry(0, 0, int(screen_width/3), int(screen_height/3))
        self.center()

        # 添加一个按钮用于上传图片
        upload_btn = QPushButton('上传图片', self)
        btn_width = 300
        btn_height = 100
        upload_btn.setGeometry((self.width() - btn_width) // 2, self.height() - btn_height - 10, btn_width, btn_height)
        upload_btn.clicked.connect(self.upload_image)

        # 添加一个标签用于显示图片
        self.image_label = QLabel(self)
        self.image_label.setGeometry(10, 10, int(self.width() / 2) - 20, self.height() - 120)
        self.image_label.setScaledContents(True)

    def center(self):
        # 获取窗口尺寸
        qr = self.frameGeometry()
        # 获取屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 将窗口中心点移动到屏幕中心点
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def upload_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "选择图片", "", "图片文件 (*.png *.jpg *.jpeg *.bmp);;所有文件 (*)", options=options)
        if file_path:
            pixmap = QPixmap(file_path)
            self.image_label.setPixmap(pixmap)
            QMessageBox.information(self, '图片路径', file_path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())