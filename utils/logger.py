import logging
import os
import sys


def get_log_path():
    """获取可写的日志文件路径"""
    if getattr(sys, 'frozen', False):
        # 打包后：日志放在 exe 同目录
        log_dir = os.path.dirname(sys.executable)
    else:
        # 开发环境：日志放在项目根目录
        log_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    return os.path.join(log_dir, 'calculator.log')


log_file_path = get_log_path()

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=log_file_path,
    filemode='w'
)

logger = logging.getLogger(__name__)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(console_handler)
