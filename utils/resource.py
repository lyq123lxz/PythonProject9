import sys
import os
from config import DATA_DIR

def resource_path(relative_path):
    """获取资源文件的绝对路径"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def get_image_path(image_num):
    """获取图片文件路径"""
    return resource_path(os.path.join(DATA_DIR, f"{image_num}.jpg"))
