from PyQt6.QtWidgets import QMainWindow
from ui.untitled3_ui import Ui_MainWindow2
from windows.window_manager import WindowManager
from utils.logger import logger


class SecondWindow(QMainWindow):
    def __init__(self, on_close_callback=None):
        super().__init__()
        self.on_close_callback = on_close_callback
        self.ui2 = Ui_MainWindow2()
        self.ui2.setupUi(self)

        # 连接关闭窗口的动作
        self.ui2.actionw.triggered.connect(self.close)

        # 使用与原始代码完全相同的方式连接按钮框
        self.ui2.buttonBox.accepted.connect(lambda: self._on_ok_clicked())
        self.ui2.buttonBox.rejected.connect(lambda: self._on_cancel_clicked())

        # 连接菜单项以切换到第一界面
        self.ui2.actionw.triggered.connect(self.show_main_window)

        # 连接菜单项以切换到第三界面
        self.ui2.action.triggered.connect(self.show_s4_window)

        logger.debug("Second window initialized")
        logger.debug(f"buttonBox type: {type(self.ui2.buttonBox)}")
        logger.debug(f"buttonBox buttons: {self.ui2.buttonBox.buttons()}")

    def _on_ok_clicked(self):
        try:
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
        except Exception as e:
            logger.error(f"Error in OK button: {e}")

    def _on_cancel_clicked(self):
        try:
            logger.debug("Cancel button clicked")
            print("Cancel按钮被点击了！")
            self.ui2.checkBox.setChecked(False)
            self.ui2.checkBox_2.setChecked(False)
            self.ui2.checkBox_3.setChecked(False)
            self.ui2.checkBox_4.setChecked(False)
            self.ui2.lineEdit_6.clear()
        except Exception as e:
            logger.error(f"Error in Cancel button: {e}")

    def _append_text(self, text):
        current = self.ui2.lineEdit_6.text()
        self.ui2.lineEdit_6.setText(current + text)

    def show_main_window(self):
        """显示第一界面"""
        try:
            self.close()
            WindowManager.show_main_window()
        except Exception as e:
            logger.error(f"Error showing main screen: {e}")

    def show_s4_window(self):
        """显示第三界面"""
        try:
            self.close()
            WindowManager.show_s4_window()
        except Exception as e:
            logger.error(f"Error showing third screen: {e}")

    def closeEvent(self, event):
        try:
            logger.debug("Second window is closing")
            if self.on_close_callback:
                self.on_close_callback()
            event.accept()
        except Exception as e:
            logger.error(f"Error in closeEvent: {e}")