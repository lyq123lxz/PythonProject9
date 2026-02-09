from utils.logger import logger


class WindowManager:
    _main_window = None
    _second_window = None
    _s4_window = None

    @classmethod
    def show_main_window(cls):
        from windows.main_window import MyMainWindow

        if cls._main_window is not None and cls._main_window.isVisible():
            cls._main_window.raise_()
            cls._main_window.activateWindow()
            logger.debug("Main window already exists, bringing to front")
            return

        if cls._main_window is not None:
            cls._main_window.close()

        cls._main_window = MyMainWindow()
        cls._main_window.show()
        logger.debug("Main window shown")

    @classmethod
    def show_second_window(cls):
        from windows.second_window import SecondWindow

        if cls._second_window is not None and cls._second_window.isVisible():
            cls._second_window.raise_()
            cls._second_window.activateWindow()
            logger.debug("Second window already exists, bringing to front")
            return

        if cls._second_window is not None:
            cls._second_window.close()

        cls._second_window = SecondWindow(on_close_callback=cls._on_second_window_closed)
        cls._second_window.show()
        logger.debug("Second window shown")

    @classmethod
    def _on_second_window_closed(cls):
        if cls._second_window is not None:
            cls._second_window.close()
            cls._second_window = None
            logger.debug("Second window reference cleared")

    @classmethod
    def show_s4_window(cls):
        from windows.s4_window import S4Window

        if cls._s4_window is not None and cls._s4_window.isVisible():
            cls._s4_window.raise_()
            cls._s4_window.activateWindow()
            logger.debug("S4 window already exists, bringing to front")
            return

        if cls._s4_window is not None:
            cls._s4_window.close()

        cls._s4_window = S4Window(on_close_callback=cls._on_s4_window_closed)
        cls._s4_window.show()
        logger.debug("Se4 window shown")

    @classmethod
    def _on_s4_window_closed(cls):
        if cls._s4_window is not None:
            cls._s4_window.close()
            cls._s4_window = None
            logger.debug("S4 window reference cleared")