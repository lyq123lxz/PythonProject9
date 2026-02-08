# 应用配置
APP_NAME = "计算器"
LOG_FILE = "calculator.log"
LOG_LEVEL = "DEBUG"

# 老虎机配置
SLOT_MACHINE_INTERVAL = 500  # 图片切换间隔(毫秒)
SLOT_MACHINE_MIN_IMAGE = 1
SLOT_MACHINE_MAX_IMAGE = 12

# 中奖配置
WINNING_IMAGES = {
    3: {"name": "老虎", "prize": 100000},
    9: {"name": "猴子", "prize": 50000}
}

# 资源路径
DATA_DIR = "data"
