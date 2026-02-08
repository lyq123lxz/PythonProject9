import random
import time
import os
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QTimer
from utils.logger import logger
from utils.resource import resource_path
from config import WINNING_IMAGES

class SlotMachine:
    def __init__(self):
        self.timer = None
        self.start_time = None
        self.last_image = None
        self.is_running = False

    def start(self, line_edit, label):
        """开始老虎机"""
        if self.is_running:
            logger.warning("Slot machine is already running")
            return

        line_edit.clear()
        self.start_time = time.time()
        self.last_image = None
        self.is_running = True
        self.timer = QTimer()

        def update_image():
            random_num = random.randint(1, 12)
            image_path = resource_path(os.path.join('data', f"{random_num}.jpg"))
            self.last_image = random_num

            pixmap = QPixmap(image_path)
            if not pixmap.isNull():
                label.setPixmap(pixmap.scaled(label.size()))
                logger.debug(f"Displaying image: {image_path}")
            else:
                logger.error(f"Image not found: {image_path}")

        self.timer.timeout.connect(update_image)
        self.timer.start(500)
        logger.info("Slot machine started")

    def stop(self, line_edit, label):
        """停止老虎机"""
        if not self.is_running:
            QMessageBox.information(None, "提示", "老虎机未启动")
            return

        if self.timer:
            self.timer.stop()

        if self.last_image in WINNING_IMAGES:
            prize_info = WINNING_IMAGES[self.last_image]
            line_edit.setText(str(prize_info["prize"]))
            QMessageBox.information(None, "恭喜", f"您中奖了! {prize_info['name']}！获得{prize_info['prize']}元!")
        else:
            line_edit.setText("0")
            QMessageBox.information(None, "很遗憾", "未中奖，再来！")

        self.is_running = False
        self.timer = None
        logger.info(f"Slot machine stopped, result: {self.last_image}")
