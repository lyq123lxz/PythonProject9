from PyQt6.QtWidgets import QMessageBox
from utils.logger import logger


class Calculator:
    @staticmethod
    def calculate(line_edit1, line_edit2, line_edit3, label, operation):
        """通用计算方法"""
        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b
        }
        try:
            num1 = float(line_edit1.text())
            num2 = float(line_edit2.text())
            label.setText(operation)

            if operation == '/' and num2 == 0:
                raise ZeroDivisionError()

            result = ops[operation](num1, num2)
            line_edit3.setText(str(result))
            logger.info(f"Result: {num1} {operation} {num2} = {result}")
        except ValueError:
            logger.error("Invalid input")
            QMessageBox.warning(None, "输入错误", "请输入有效的数字")
        except ZeroDivisionError:
            logger.error("Division by zero")
            QMessageBox.warning(None, "输入错误", "除数不能为零")
