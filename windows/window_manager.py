from utils.logger import logger


class WindowManager:
    _second_window = None

    @classmethod
    def show_second_window(cls):
        from windows.second_window import SecondWindow

        if cls._second_window is not None and cls._second_window.isVisible():
            cls._second_window.raise_()
            cls._second_window.activateWindow()
            logger.debug("Second window already exists, bringing to front")
            return

        cls._second_window = SecondWindow(on_close_callback=cls._on_second_window_closed)
        cls._second_window.show()
        logger.debug("Second window shown")

    @classmethod
    def _on_second_window_closed(cls):
        cls._second_window = None
        logger.debug("Second window reference cleared")
