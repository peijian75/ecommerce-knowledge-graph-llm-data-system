import os
from dotenv import load_dotenv  # 新增

# 加载 .env 文件
load_dotenv()

from pathlib import Path

# 1. 目录路径
ROOT_DIR = Path(__file__).parent.parent.parent

DATA_DIR = ROOT_DIR / 'data'
NER_DIR = 'ner'
RAW_DATA_DIR = DATA_DIR / NER_DIR / 'raw'
PROCESSED_DATA_DIR = DATA_DIR / NER_DIR / 'processed'

LOG_DIR = ROOT_DIR / 'logs'
CHECKPOINT_DIR = ROOT_DIR / 'checkpoints'

# web 静态目录
WEB_STATIC_DIR = ROOT_DIR / 'src' / 'web' / 'static'

# 2. 数据文件名 和 模型名称
RAW_DATA_FILE = str(RAW_DATA_DIR / 'data.json')
MODEL_NAME = 'google-bert/bert-base-chinese'

# 3. 超参数
BATCH_SIZE = 2
EPOCHS = 5
LEARNING_RATE = 5e-5

SAVE_STEPS = 20

# 4. NER任务分类标签
LABELS = ['B', 'I', 'O']

# 5. 数据库连接
MYSQL_CONFIG = {
    'host': os.getenv("MYSQL_HOST"),
    'port': int(os.getenv("MYSQL_PORT")),
    'user': os.getenv("MYSQL_USER"),
    'password': os.getenv("MYSQL_PASSWORD"),
    'database': os.getenv("MYSQL_DATABASE"),
}

NEO4J_CONFIG = {
    'uri': os.getenv("NEO4J_URI"),
    'auth': (
        os.getenv("NEO4J_USER"),
        os.getenv("NEO4J_PASSWORD")
    )
}

API_KEY = os.getenv("API_KEY")