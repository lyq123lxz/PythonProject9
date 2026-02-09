from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import QUrl
from ui.untitled4 import Ui_MainWindow4
from utils.logger import logger
import os

# 假设 MyMainWindow 和 SecondWindow 已经定义好
from windows.main_window import MyMainWindow
from windows.second_window import SecondWindow

class S4Window(QMainWindow):
    def __init__(self, on_close_callback=None):
        super().__init__()
        self.on_close_callback = on_close_callback
        self.ui4 = Ui_MainWindow4()
        self.ui4.setupUi(self)

        # 初始化播放器
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)

        # 设置音频文件路径
        music_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "music.mp3")
        logger.debug(f"Music path: {music_path}")
        self.player.setSource(QUrl.fromLocalFile(music_path))

        # 设置音量旋钮范围 (0-100)
        self.ui4.dial.setMinimum(0)
        self.ui4.dial.setMaximum(100)

        # 连接旋钮的值变化信号到音量设置方法
        self.ui4.dial.valueChanged.connect(self.set_volume)

        # 在窗口显示时开始播放音乐
        self.ui4.pushButton.clicked.connect(self.toggle_play_pause)

        # 连接菜单项的动作到相应的槽函数
        self.ui4.action.triggered.connect(self.show_first_screen)
        self.ui4.action_2.triggered.connect(self.show_second_screen)

    def set_volume(self, value):
        """根据旋钮的值设置音量"""
        self.audio_output.setVolume(value / 100.0)

    def toggle_play_pause(self):
        """切换播放/暂停状态"""
        try:
            if self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
                self.player.pause()
            else:
                self.player.play()
        except Exception as e:
            logger.error(f"Error in toggle_play_pause: {e}")

    def showEvent(self, event):
        """重写showEvent方法，在窗口显示时开始播放音乐"""
        try:
            super().showEvent(event)
            self.player.play()
        except Exception as e:
            logger.error(f"Error in showEvent: {e}")

    def show_first_screen(self):
        """显示第一个屏幕"""
        try:
            self.close()
            self.first_screen = MyMainWindow()
            self.first_screen.show()
        except Exception as e:
            logger.error(f"Error showing first screen: {e}")

    def show_second_screen(self):
        """显示第二个屏幕"""
        try:
            self.close()
            self.second_screen = SecondWindow(on_close_callback=self._on_second_window_closed)
            self.second_screen.show()
        except Exception as e:
            logger.error(f"Error showing second screen: {e}")

    def _on_second_window_closed(self):
        self.second_screen = None
        logger.debug("Second window reference cleared")

    def closeEvent(self, event):
        """重写closeEvent方法，确保资源被正确释放"""
        try:
            self.player.stop()
            self.player.deleteLater()
            self.audio_output.deleteLater()
            if self.on_close_callback:
                self.on_close_callback()
            event.accept()
        except Exception as e:
            logger.error(f"Error in closeEvent: {e}")