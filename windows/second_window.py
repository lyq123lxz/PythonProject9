from PyQt6.QtWidgets import QMainWindow
from ui.untitled3_ui import Ui_MainWindow2
from utils.logger import logger


class SecondWindow(QMainWindow):
    def __init__(self, on_close_callback=None):
        super().__init__()
        self.on_close_callback = on_close_callback
        self.ui2 = Ui_MainWindow2()
        self.ui2.setupUi(self)

        self.ui2.actionw.triggered.connect(self.close)

        # 使用与原始代码完全相同的方式连接
        self.ui2.buttonBox.accepted.connect(lambda: self._on_ok_clicked())
        self.ui2.buttonBox.rejected.connect(lambda: self._on_cancel_clicked())

        logger.debug("Second window initialized")
        logger.debug(f"buttonBox type: {type(self.ui2.buttonBox)}")
        logger.debug(f"buttonBox buttons: {self.ui2.buttonBox.buttons()}")

    def _on_ok_clicked(self):
        logger.debug("OK button clicked")
        print("OK按钮被点击了！")
        self.ui2.lineEdit_6.clear()
        if self.ui2.checkBox.isChecked():
            print("+法被选中了。")
            self._append_text("+")
        if self.ui2.checkBox_2.isChecked():
            print("*法被选中了。")
            self._append_text("*")
        if self.ui2.checkBox_4.isChecked():
            print("-法被选中了。")
            self._append_text("-")
        if self.ui2.checkBox_3.isChecked():
            print("/法被选中了。")
            self._append_text("/")

    def _on_cancel_clicked(self):
        logger.debug("Cancel button clicked")
        print("Cancel按钮被点击了！")
        self.ui2.checkBox.setChecked(False)
        self.ui2.checkBox_2.setChecked(False)
        self.ui2.checkBox_3.setChecked(False)
        self.ui2.checkBox_4.setChecked(False)
        self.ui2.lineEdit_6.clear()

    def _append_text(self, text):
        current = self.ui2.lineEdit_6.text()
        self.ui2.lineEdit_6.setText(current + text)

    def closeEvent(self, event):
        logger.debug("Second window is closing")
        if self.on_close_callback:
            self.on_close_callback()
        event.accept()
