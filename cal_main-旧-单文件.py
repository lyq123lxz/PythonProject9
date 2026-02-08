import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QTimer
import os
import random
import time
import logging
from cal_window import Ui_MainWindow  # 导入 Ui_MainWindow 类
from untitled3_ui_ui import Ui_MainWindow2

# 全局定义第二屏幕状态
_second_window_instance = None

# 配置日志记录器
logging.basicConfig(
    level=logging.DEBUG,  # 设置日志级别为 DEBUG
    format='%(asctime)s - %(levelname)s - %(message)s',  # 设置日志格式
    filename='calculator.log',  # 将日志写入文件
    filemode='w'  # 覆盖之前的日志文件
)

# 创建一个日志记录器
logger = logging.getLogger(__name__)

# 添加 StreamHandler 以将日志信息输出到控制台
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(console_handler)

# 定义一个全局的加法子程序
def add_numbers(line_edit1, line_edit2, line_edit3, label):
    try:
        label.setText("+")

        # 从 QLineEdit 中获取输入值
        num1 = float(line_edit1.text())
        num2 = float(line_edit2.text())
        logger.debug(f"Input values: num1={num1}, num2={num2}")

        # 计算加法
        result = num1 + num2

        # 显示结果
        line_edit3.setText(str(result))
        # 记录计算结果
        logger.info(f"Addition result: {result}")
    except ValueError:
        # 如果输入不是有效的数字，显示错误消息
        logger.error("Invalid input: Please enter valid numbers")
        QMessageBox.warning(None, "输入错误", "请输入有效的数字")

# 定义一个全局的减法子程序
def subs_numbers(line_edit1, line_edit2, line_edit3, label):
    try:
        label.setText("-")

        # 从 QLineEdit 中获取输入值
        num1 = float(line_edit1.text())
        num2 = float(line_edit2.text())
        logger.debug(f"Input values: num1={num1}, num2={num2}")

        # 计算减法
        result = num1 - num2

        # 显示结果
        line_edit3.setText(str(result))
        # 记录计算结果
        logger.info(f"Subtraction result: {result}")
    except ValueError:
        # 如果输入不是有效的数字，显示错误消息
        logger.error("Invalid input: Please enter valid numbers")
        QMessageBox.warning(None, "输入错误", "请输入有效的数字")

# 定义一个全局的乘法子程序
def mult_numbers(line_edit1, line_edit2, line_edit3, label):
    try:
        label.setText("*")

        # 从 QLineEdit 中获取输入值
        num1 = float(line_edit1.text())
        num2 = float(line_edit2.text())
        logger.debug(f"Input values: num1={num1}, num2={num2}")

        # 计算乘法
        result = num1 * num2

        # 显示结果
        line_edit3.setText(str(result))
        # 记录计算结果
        logger.info(f"Multiplication result: {result}")
    except ValueError:
        # 如果输入不是有效的数字，显示错误消息
        logger.error("Invalid input: Please enter valid numbers")
        QMessageBox.warning(None, "输入错误", "请输入有效的数字")

# 定义一个全局的除法子程序
def divi_numbers(line_edit1, line_edit2, line_edit3, label):
    try:
        label.setText("/")

        # 从 QLineEdit 中获取输入值
        num1 = float(line_edit1.text())
        num2 = float(line_edit2.text())
        logger.debug(f"Input values: num1={num1}, num2={num2}")

        # 计算除法
        result = num1 / num2

        # 显示结果
        line_edit3.setText(str(result))
        # 记录计算结果
        logger.info(f"Division result: {result}")
    except ValueError:
        # 如果输入不是有效的数字，显示错误消息
        logger.error("Invalid input: Please enter valid numbers")
        QMessageBox.warning(None, "输入错误", "请输入有效的数字")
    except ZeroDivisionError:
        # 如果除数为零，显示错误消息
        logger.error("Division by zero")
        QMessageBox.warning(None, "输入错误", "除数不能为零")

#定义调用第二个窗口的全局子程序
def se2_windows():
    global _second_window_instance
    logger.debug("se2_windows function called")

    # 如果第二个窗口已经存在且可见,则不重复创建
    if _second_window_instance is not None and _second_window_instance.isVisible():
        _second_window_instance.raise_()  # 将窗口提到最前
        _second_window_instance.activateWindow()  # 激活窗口
        logger.debug("Second window already exists, bringing to front")
        return

    # 创建一个继承自 QMainWindow 的子类,用于第二个窗口
    class SecondWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            # 初始化界面
            self.ui2 = Ui_MainWindow2()
            self.ui2.setupUi(self)

            # 连接菜单项动作到关闭当前窗口的方法
            self.ui2.actionw.triggered.connect(self.close)
            self.ui2.buttonBox.accepted.connect(lambda: onOkClicked(self.ui2))
            self.ui2.buttonBox.rejected.connect(lambda: onCancelClicked(self.ui2))
            logger.debug("Second window initialized and connected to close action")

        def closeEvent(self, event):
            global _second_window_instance
            logger.debug("Second window is closing")
            _second_window_instance = None  # 窗口关闭时清空引用
            event.accept()

    # 将第二个窗口的引用保存到全局变量
    _second_window_instance = SecondWindow()
    _second_window_instance.show()
    logger.debug("Second window shown")

# 全局定义老虎机状态
_slot_machine_state = {
    'timer': None,
    'start_time': None,
    'last_image': None,
    'is_running': False
}

# 获取资源文件路径
def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# 全局定义老虎机开始子程序
def on_pushButton_start_clicked(line_Edit4, label_3):
    """开始按钮的处理函数"""
    try:
        # 如果已经在运行,不重复启动
        if _slot_machine_state['is_running']:
            logger.warning("Slot machine is already running")
            return

        # 清空之前的结果
        line_Edit4.clear()

        # 初始化状态
        _slot_machine_state['start_time'] = time.time()
        _slot_machine_state['last_image'] = None
        _slot_machine_state['is_running'] = True
        _slot_machine_state['timer'] = QTimer()

        # 更新图片的逻辑
        def update_image():
            # 随机选择并显示图片
            random_num = random.randint(1, 12)
            image_path = resource_path(os.path.join('data', f"{random_num}.jpg"))
            _slot_machine_state['last_image'] = random_num

            pixmap = QPixmap(image_path)
            if not pixmap.isNull():
                label_3.setPixmap(pixmap.scaled(label_3.size()))
                logger.debug(f"Displaying image: {image_path}")
            else:
                logger.error(f"Image not found: {image_path}")

        # 连接定时器并启动
        _slot_machine_state['timer'].timeout.connect(update_image)
        _slot_machine_state['timer'].start(500)  # 每100ms更新一次,速度更快

        logger.info("Slot machine started")

    except Exception as e:
        logger.error(f"Error starting slot machine: {e}")
        QMessageBox.warning(None, "错误", f"老虎机启动出错: {e}")

# 全局定义老虎机停止子程序
def on_pushButton_stop_clicked(line_Edit4, label_3):
    """停止按钮的处理函数"""
    try:
        # 检查是否在运行
        if not _slot_machine_state['is_running']:
            logger.warning("Slot machine is not running")
            QMessageBox.information(None, "提示", "老虎机未启动")
            return

        # 停止定时器
        if _slot_machine_state['timer']:
            _slot_machine_state['timer'].stop()

        # 判断结果
        if _slot_machine_state['last_image'] == 3:
            line_Edit4.setText("10")
            logger.info(f"Winner! Last image was 老虎 (3.jpg)")
            QMessageBox.information(None, "恭喜", "您中奖了! 老虎！！！获得10元!")
        elif _slot_machine_state['last_image'] == 9:
            line_Edit4.setText("5")
            logger.info(f"Winner! Last image was 猴子 (9.jpg)")
            QMessageBox.information(None, "恭喜", "您中奖了! 猴子！！！获得5元!")
        else:
            line_Edit4.setText("0")
            logger.info(f"Lost. Last image was {_slot_machine_state['last_image']}.jpg")
            QMessageBox.information(None, "很遗憾", "未中奖，再来！")

        # 重置状态
        _slot_machine_state['is_running'] = False
        _slot_machine_state['timer'] = None

    except Exception as e:
        logger.error(f"Error stopping slot machine: {e}")
        QMessageBox.warning(None, "错误", f"老虎机停止出错: {e}")

# 创建一个继承自 QMainWindow 的子类
class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 初始化界面
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 连接加法动作
        self.ui.action.triggered.connect(lambda: add_numbers(
            self.ui.lineEdit,
            self.ui.lineEdit_2,
            self.ui.lineEdit_3,
            self.ui.label
        ))

        # 连接减法动作
        self.ui.action_2.triggered.connect(lambda: subs_numbers(
            self.ui.lineEdit,
            self.ui.lineEdit_2,
            self.ui.lineEdit_3,
            self.ui.label
        ))

        # 连接乘法动作
        self.ui.action_3.triggered.connect(lambda: mult_numbers(
            self.ui.lineEdit,
            self.ui.lineEdit_2,
            self.ui.lineEdit_3,
            self.ui.label
        ))

        # 连接除法动作
        self.ui.action_4.triggered.connect(lambda: divi_numbers(
            self.ui.lineEdit,
            self.ui.lineEdit_2,
            self.ui.lineEdit_3,
            self.ui.label
        ))

        # 连接老虎机开始按钮
        self.ui.pushButton.clicked.connect(
            lambda: on_pushButton_start_clicked      (self.ui.lineEdit_4, self.ui.label_3)
        )

        # 连接老虎机停止按钮(假设第二个按钮是 pushButton_2)
        self.ui.pushButton_2.clicked.connect(
            lambda: on_pushButton_stop_clicked(self.ui.lineEdit_4, self.ui.label_3)
        )
        #连接第二个界面
        self.ui.action_5.triggered.connect(se2_windows)

# 定义全局的 OK 按钮点击处理函数
def onOkClicked(ui2):
        print("OK按钮被点击了！")
        # 如果你想在这里执行其他操作，比如验证表单数据或保存信息，可以在此处添加代码
        # 例如，你可以检查复选框的状态，或者读取文本框的内容等
        # 示例：获取复选框状态
        if ui2.checkBox.isChecked():
            print("+法被选中了。")
            current_text = ui2.lineEdit_6.text()  # 获取当前文本
            new_text = current_text + "+"  # 在现有文本基础上增加 "+"
            ui2.lineEdit_6.setText(new_text)  # 设置新文本

        if ui2.checkBox_2.isChecked():
            print("*法被选中了。")
            current_text = ui2.lineEdit_6.text()  # 获取当前文本
            new_text = current_text + "*"  # 在现有文本基础上增加 "*"
            ui2.lineEdit_6.setText(new_text)  # 设置新文本

        if ui2.checkBox_4.isChecked():
            print("-法被选中了。")
            current_text = ui2.lineEdit_6.text()  # 获取当前文本
            new_text = current_text + "-"  # 在现有文本基础上增加 "-"
            ui2.lineEdit_6.setText(new_text)  # 设置新文本

        if ui2.checkBox_3.isChecked():
            print("/法被选中了。")
            current_text = ui2.lineEdit_6.text()  # 获取当前文本
            new_text = current_text + "/"  # 在现有文本基础上增加 "/"
            ui2.lineEdit_6.setText(new_text)  # 设置新文本


# 定义全局的 Cancel 按钮点击处理函数
def onCancelClicked(ui2):
    print("Cancel按钮被点击了！")
    # 如果你想在这里执行其他操作，比如清除表单数据或显示提示信息，可以在此处添加代码
    # 示例：清除所有复选框的状态
    ui2.checkBox.setChecked(False)
    ui2.checkBox_2.setChecked(False)
    ui2.checkBox_3.setChecked(False)
    ui2.checkBox_4.setChecked(False)
    # 清空文本框
    ui2.lineEdit_6.clear()


# 主函数
def main():
    app = QApplication(sys.argv)
    # 创建 MyMainWindow 实例
    window = MyMainWindow()
    # 显示主窗口
    window.show()
    # 进入应用程序主循环
    sys.exit(app.exec())

if __name__ == "__main__":
    main()