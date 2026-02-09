import sys
from PyQt6.QtWidgets import QApplication
from windows.main_window import MyMainWindow

def main():
    try:
        app = QApplication(sys.argv)
        window = MyMainWindow()
        window.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()