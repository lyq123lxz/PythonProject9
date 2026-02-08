from PyQt6.QtWidgets import QMainWindow
from ui.cal_window import Ui_MainWindow
from functions.calculator import Calculator
from functions.slot_machine import SlotMachine
from windows.window_manager import WindowManager
from utils.logger import logger

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.slot_machine = SlotMachine()
        self._connect_signals()

    def _connect_signals(self):
        # 计算器操作
        self.ui.action.triggered.connect(lambda: Calculator.calculate(
            self.ui.lineEdit, self.ui.lineEdit_2, self.ui.lineEdit_3, self.ui.label, '+'
        ))
        self.ui.action_2.triggered.connect(lambda: Calculator.calculate(
            self.ui.lineEdit, self.ui.lineEdit_2, self.ui.lineEdit_3, self.ui.label, '-'
        ))
        self.ui.action_3.triggered.connect(lambda: Calculator.calculate(
            self.ui.lineEdit, self.ui.lineEdit_2, self.ui.lineEdit_3, self.ui.label, '*'
        ))
        self.ui.action_4.triggered.connect(lambda: Calculator.calculate(
            self.ui.lineEdit, self.ui.lineEdit_2, self.ui.lineEdit_3, self.ui.label, '/'
        ))

        # 老虎机操作
        self.ui.pushButton.clicked.connect(
            lambda: self.slot_machine.start(self.ui.lineEdit_4, self.ui.label_3)
        )
        self.ui.pushButton_2.clicked.connect(
            lambda: self.slot_machine.stop(self.ui.lineEdit_4, self.ui.label_3)
        )
        # 第二窗口连接
        self.ui.action_5.triggered.connect(WindowManager.show_second_window)
        logger.debug("Main window initialized")